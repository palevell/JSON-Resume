# json2toml.py - Thursday, May 15, 2025
# -*- coding: utf-8 -*-
__version__ = "0.1.0-dev7"

import json
import os
import sys
import toml
from pathlib import Path

_basedir = Path(__file__).resolve().parent


def usage():
	print("Usage: json2toml.py FILE")
	return


def main(filename: str | Path):
	print(f"Args: {filename}")
	src = str(filename)
	dst = src.rstrip("json") + "toml"
	with open(src, "rt") as infile, open(dst, "wt") as outfile:
		data = infile.read()
		print(data)
		jdata = json.loads(data)
		# json.load(data)
		print(jdata)
		toml.dump(jdata, outfile)
		do_nothing()
	return


def do_nothing():
	pass


if __name__ == "__main__":
	_refdir = _basedir.parent.parent / "ref"
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		# usage()
		filename = _refdir / "resume-sample.json"
		main(filename)
