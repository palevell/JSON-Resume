#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# build_resume.py - Tuesday, May 13, 2025
""" Build JSON file for my resume """
__version__ = "0.1.0-dev3"

import json
import jsons
import os
import sys
import time
from datetime import datetime, timedelta
from glob import glob
from os.path import exists, getmtime, join, lexists, realpath
from pathlib import Path

import toml

__module__ = Path(__file__).resolve().stem
_basedir = Path(__file__).resolve().parent


def build_resume():
	toml_filename = "all_components.toml"
	json_filename = "resume.json"
	schema = "https://raw.githubusercontent.com/jsonresume/resume-schema/v1.0.0/schema.json"
	build_toml(toml_filename)
	toml2json(toml_filename, json_filename, schema=schema)


def build_toml(filename: str):
	toml_include_dir = _basedir / "components" / "toml"
	sections = "basics work volunteer education awards publications skills languages interests references projects meta".split()
	with open(filename, "wt") as outfile:
		for s in sections:
			component = toml_include_dir / f"{s}.toml"
			print(component)
			with open(component, "rt") as infile:
				lines = infile.readlines()
				outfile.writelines(lines)
	print(filename)
	return


def toml2json(src: str | Path, dst: str | Path, schema=None):
	src = str(src)
	dst = str(dst)
	# dst = src.replace("toml", "json")
	resume_dict = {}
	if schema:
		resume_dict = {"$schema": schema }
	with open(src, "rt") as infile, open(dst, "wt") as outfile:
		# ydata = toml.load(infile)
		resume_dict.update(toml.load(infile))
		json.dump(resume_dict, outfile, indent=2, sort_keys=False)
		outfile.write("\n")
	print(dst)
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


def dump_json_old(filename, dataset, append: bool=False, overwrite: bool=False) -> int:
	item_count = -1
	if type(dataset) == dict:
		dataset = [dataset,]
	else:
		try:
			iterator = iter(dataset)
		except TypeError:
			# Not iterable
			dataset = [dataset, ]
		else:
			# Iterable
			pass
	try:
		if append:
			mode = "at"
		elif overwrite:
			mode = "wt"
		else:
			mode = "xt"
		with open(filename, mode) as jfile:
			for item in dataset:
				jfile.write(json.dumps(item, default=str) + "\n")
	except Exception as e:
		print(e, filename, file=sys.stderr)
	else:
		item_count = len(dataset)
	return item_count


def dump_jsons_old(filename, dataset, append: bool=False, overwrite: bool=False) -> int:
	item_count = -1
	if type(dataset) == dict:
		dataset = [dataset,]
	else:
		try:
			iterator = iter(dataset)
		except TypeError:
			# Not iterable
			dataset = [dataset, ]
		else:
			# Iterable
			pass
	try:
		if append:
			mode = "at"
		elif overwrite:
			mode = "wt"
		else:
			mode = "xt"
		with open(filename, mode) as jfile:
			for item in dataset:
				jfile.write(jsons.dumps(item, default=str) + "\n")
	except Exception as e:
		print(e, filename, file=sys.stderr)
	else:
		item_count = len(dataset)
	return item_count


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
	build_resume()
	eoj()
