#!/usr/bin/env python3
"""Audit text-file BOMs, UTF-8 validity, and line-ending styles."""
import argparse
import json
from pathlib import Path
import sys

def analyze_bytes(data):
    if data.startswith(b"\xef\xbb\xbf"):
        encoding, body, bom = "utf-8", data[3:], True
    elif data.startswith(b"\xff\xfe"):
        encoding, body, bom = "utf-16-le", data[2:], True
    elif data.startswith(b"\xfe\xff"):
        encoding, body, bom = "utf-16-be", data[2:], True
    else:
        encoding, body, bom = "utf-8", data, False
    if b"\x00" in body and not encoding.startswith("utf-16"):
        return {"encoding":"binary-or-unknown","bom":bom,"line_endings":[],"mixed":False,"valid_text":False}
    try:
        body.decode(encoding)
        valid = True
    except UnicodeDecodeError:
        valid = False
    if not valid:
        return {"encoding":"invalid-utf8","bom":bom,"line_endings":[],"mixed":False,"valid_text":False}
    without_crlf = body.replace(b"\r\n", b"")
    counts = {"CRLF":body.count(b"\r\n"),"LF":without_crlf.count(b"\n"),"CR":without_crlf.count(b"\r")}
    styles = [name for name,count in counts.items() if count]
    return {"encoding":encoding,"bom":bom,"line_endings":styles,"counts":counts,
            "mixed":len(styles)>1,"valid_text":True}

def collect_files(paths, extensions):
    found=[]
    allowed={x.lower() if x.startswith(".") else "."+x.lower() for x in extensions}
    for raw in paths:
        path=Path(raw)
        if path.is_file():
            if not allowed or path.suffix.lower() in allowed: found.append(path)
        elif path.is_dir():
            for item in path.rglob("*"):
                if item.is_file() and ".git" not in item.parts and "node_modules" not in item.parts:
                    if not allowed or item.suffix.lower() in allowed: found.append(item)
    return sorted(set(found))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths",nargs="+")
    parser.add_argument("--extensions",default="",help="Comma-separated extensions, e.g. .py,.md")
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    files=collect_files(args.paths,[x.strip() for x in args.extensions.split(",") if x.strip()])
    results=[]
    for path in files:
        try: results.append({"path":str(path),"audit":analyze_bytes(path.read_bytes())})
        except OSError as exc: results.append({"path":str(path),"error":str(exc)})
    if args.json: print(json.dumps(results,indent=2))
    else:
        for item in results:
            audit=item.get("audit",{})
            flags=[]
            if item.get("error"): flags.append("read-error")
            if audit.get("bom"): flags.append("BOM")
            if not audit.get("valid_text",True): flags.append(audit.get("encoding","invalid"))
            if audit.get("mixed"): flags.append("mixed-line-endings")
            if flags: print(f"{item['path']}: {', '.join(flags)}")
        print(f"Scanned {len(results)} file(s).")
    return 1 if any(x.get("error") or not x.get("audit",{}).get("valid_text",True) or x.get("audit",{}).get("mixed") for x in results) else 0

if __name__=="__main__": raise SystemExit(main())
