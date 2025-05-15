#!/usr/bin/env python3
# yaml2toml.py - Thursday, May 15, 2025
# -*- coding: utf-8 -*-
__version__ = "0.1.0-dev11"

import toml
import os
import sys
import yaml
from pathlib import Path

_basedir = Path(__file__).resolve().parent


def usage():
	print("Usage: yaml2toml.py FILE")
	return


def main(filename: str | Path):
	src = str(filename)
	# dst = src.rstrip("yaml") + "toml"
	dst = src.replace("yaml", "toml")
	with open(src, "rt") as infile, open(dst, "wt") as outfile:
		# data = infile.read()
		# print(data)
		ydata = yaml.safe_load(infile)
		toml.dump(ydata, outfile)
		do_nothing()
	print(dst)
	return


def do_nothing():
	pass


if __name__ == "__main__":
	_refdir = _basedir.parent.parent / "ref"
	_tomldir = _basedir / "components" / "toml"
	_yamldir = _basedir / "components" / "yaml"
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		# usage()
		# filename = _yamldir / "basics.yaml"
		filename = _yamldir / "skills.yaml"
		main(filename)
