#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# build_json.py - Wednesday, May 14, 2025
""" DocString goes here. """
__version__ = "0.1.0-dev4"

import json
import jsons
import os
import sys
import time
from datetime import datetime, timedelta
from glob import glob
from os.path import exists, getmtime, join, lexists, realpath
from pathlib import Path

__module__ = Path(__file__).resolve().stem
_basedir = Path(__file__).resolve().parent


def main():
	filename = "all_components.json"
	json_include_dir = _basedir / "components" / "json"
	resume_dict = { "$schema": "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json" }
	sections = "basics work volunteer education awards publications skills languages interests references projects meta".split()
	with open(filename, "wt") as outfile:
		# outfile.write(first_line + "\n")
		for s in sections:
			component = json_include_dir / f"{s}.json"
			print(component)
			with open(component, "rt") as infile:
				# outfile.writelines(infile.readlines())
				# data = json.load(infile)
				data = json.loads(infile.read())
				resume_dict.update(data)
		print(resume_dict)
		json.dump(resume_dict, outfile, indent=2)
	return


def init():
	started = time.strftime(_iso_datefmt, _run_localtime)
	print(f"Run Start: {__module__} v{__version__} {started}")
	return


def eoj():
	stop_ts = time.time()
	stop_localtime = time.localtime(stop_ts)
	stop_gmtime = time.gmtime(stop_ts)
	duration = timedelta(seconds=(stop_ts - _run_ts))
	print(f"Run Stop : {time.strftime(_iso_datefmt, stop_localtime)}  Duration: {duration}")
	return


def do_nothing():
	pass


if __name__ == '__main__':
	_run_ts = time.time()
	_run_dt = datetime.fromtimestamp(_run_ts).astimezone()
	_run_localtime = time.localtime(_run_ts)
	_run_gmtime = time.gmtime(_run_ts)
	_run_ymd = time.strftime("%Y%m%d", _run_localtime)
	_run_hms = time.strftime("%H%M%S", _run_localtime)
	_run_ymdhms = f"{_run_ymd}_{_run_hms}"
	_iso_datefmt = "%Y-%m-%d %H:%M:%S%z"

	init()
	main()
	eoj()
