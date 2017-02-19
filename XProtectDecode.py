#!/usr/bin/env python

# BBEdit Text Filter
# 
# Parse and Decode Identities and Patterns
# for a quicker, but no so accurate, overview.

import re
from sys import stdin, stdout

# ---------------------------------------------------------------------------

def filter(text):
	return decode_patterns(decode_identities(text))

def decode_identities(text):
	r = re.compile(r"(<key>Identity</key>.*?<data>)(.*?)(</data>)", flags=re.DOTALL)

	return re.sub(r, decode_identity, text)

def decode_identity(m):
	return m.group(1) + m.group(2).decode("base64").encode("hex") + m.group(3)

def decode_patterns(text):
	r = re.compile(r"(<key>Pattern</key>.*?<string>)(.*?)(</string>)", flags=re.DOTALL)

	return re.sub(r, decode_pattern, text)

def decode_pattern(m):
	r = re.compile(r"([\dA-F][\dA-F]+)")

	return m.group(1) + re.sub(r, decode_hex, m.group(2)) + m.group(3)

def decode_hex(m):
	return m.group().decode("hex")

# ---------------------------------------------------------------------------

if __name__ == "__main__":
	text = stdin.read()
	stdout.write(filter(text))
