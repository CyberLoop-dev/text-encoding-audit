import unittest
from main import analyze_bytes

class EncodingAuditTests(unittest.TestCase):
    def test_detects_utf8_bom(self):
        result=analyze_bytes(b"\\xef\\xbb\\xbfhello\\n")
        self.assertTrue(result["bom"])
        self.assertTrue(result["valid_text"])
    def test_detects_mixed_endings(self):
        result=analyze_bytes(b"one\\r\\ntwo\\n")
        self.assertTrue(result["mixed"])
    def test_detects_invalid_utf8(self):
        self.assertFalse(analyze_bytes(b"\\xff")["valid_text"])

if __name__=="__main__": unittest.main()
