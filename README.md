<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=170&section=header&text=Text%20Encoding%20Audit&fontColor=ffffff&fontSize=38&animation=fadeIn" alt="Text Encoding Audit banner" width="100%"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=19&duration=3000&pause=900&color=14B8A6&center=true&vCenter=true&width=820&lines=Find%20BOMs%2C%20invalid%20UTF-8%2C%20and%20mixed%20line%20endings%20before%20they%20break%20builds" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/text-encoding-audit)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/text-encoding-audit)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/text-encoding-audit?style=flat)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/text-encoding-audit)

<img src="assets/illustration.svg" alt="Text Encoding Audit illustration" width="92%"/>
</div>

## :compass: Overview

A dependency-free Python scanner for text-file encoding markers and line-ending consistency. It reports UTF-8 validity, BOMs, and mixed CRLF/LF/CR files without modifying anything.

## :sparkles: Features

- :white_check_mark: Detects UTF-8 and UTF-16 byte-order marks
- :white_check_mark: Flags invalid UTF-8 and likely binary files
- :white_check_mark: Reports LF, CRLF, CR, and mixed line endings
- :white_check_mark: Scans selected files or directory trees read-only

## :clapper: Demo

```bash
python main.py . --extensions .py,.js,.ts,.md,.json
```

The example runs locally; no hosted service or upload is required.

## :rocket: Quick Start

```bash
python -m pip install -r requirements.txt
python main.py . --extensions .py,.js,.ts,.md,.json
```

Run `python main.py --help` to see all supported options.

## :toolbox: Tech Stack

- Python 3.10+ standard library
- Automated tests: unittest
- Local-first processing

## :file_folder: Folder Structure

```text
text-encoding-audit/
├── main.py
├── requirements.txt
├── tests/test_core.py
├── examples/README.md
└── assets/illustration.svg
```

## :world_map: Roadmap

- [x] Core workflow and CLI
- [x] Example input and tests
- [ ] Additional report formats
- [ ] Continuous integration on supported platforms

## :handshake: Contributing

Issues and pull requests are welcome. Keep changes focused, document behavior changes, and add tests for new features.

## :page_facing_up: License

MIT - see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated wave footer" width="100%"/></div>
