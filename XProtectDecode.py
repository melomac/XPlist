#!/usr/bin/env python

# BBEdit Text Filter
# 
# Parse and Decode Identities and Patterns
# for a quicker, but no so accurate, overview.

import re
from sys import stdin, stdout

# ---------------------------------------------------------------------------

def filter(text):
	lines = text.splitlines()

	i = 0
	for line in lines:
		
		if line.find("<key>Identity</key>") != -1:
			# SHA1 hex digest			
			
			if lines[i+1].find("<data>") != -1:
				lines[i+1] = process_identity(lines[i+1])
			
		elif line.find("<key>Pattern</key>") != -1:
			# Regular expression
			lines[i+1] = process_pattern(lines[i+1])

		i += 1

	return "\n".join(lines)

def process_identity(line):
	r = re.compile("([\t]+)<data>(.+)</data>")
	p = r.findall(line)

	return "{pad}<data>{sha}</data>".format(
		pad = p[0][0],
		sha = p[0][1].decode("base64").encode("hex")
		)

def process_pattern(line):
	r = re.compile("([\t]+)<string>(.+)</string>")
	p = r.findall(line)

	return "{pad}<string>\n{pattern}\n{pad}</string>".format(
		pad = p[0][0],
		pattern = _process_pattern(p[0][1], p[0][0])
		)

def _process_pattern(pattern, pad):
	result = []

	for p in pattern.split("*"):
		try:
			result.append("{pad}STR: {str}".format(
				pad = pad,
				str = p.decode("hex"))
			)
		
		except:
			result.append("{pad}HEX: {hex}".format(
				pad = pad,
				hex = p)
			)

	return "\n".join(result)

# ---------------------------------------------------------------------------

if __name__ == "__main__":
	text = stdin.read()
	stdout.write(filter(text))
