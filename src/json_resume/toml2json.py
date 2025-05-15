#!/usr/bin/env python3
# toml2json.py - Thursday, May 15, 2025
# -*- coding: utf-8 -*-
__version__ = "0.1.0-dev12"

import json
import os
import sys
import toml
from pathlib import Path

_basedir = Path(__file__).resolve().parent


def usage():
	print("Usage: toml2json.py FILE")
	return


def main(filename: str | Path):
	src = str(filename)
	# dst = src.rstrip("toml") + "json"
	dst = src.replace("toml", "json")
	with open(src, "rt") as infile, open(dst, "wt") as outfile:
		# data = infile.read()
		# print(data)
		ydata = toml.load(infile)
		json.dump(ydata, outfile, indent=True, sort_keys=False)
		do_nothing()
	print(dst)
	return


def do_nothing():
	pass


if __name__ == "__main__":
	_refdir = _basedir.parent.parent / "ref"
	_jsondir = _basedir / "components" / "json"
	_tomldir = _basedir / "components" / "toml"
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		# usage()
		filename = _refdir / "resume-sample.toml"
		# filename = _tomldir / "basics.toml"
		# filename = _tomldir / "skills.toml"
		main(filename)
