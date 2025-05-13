#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# build_resume.py - Tuesday, May 13, 2025
""" Build JSON file for my resume """
__version__ = "0.1.0-dev0"

import json
import jsons
import os
import sys
import time
from datetime import datetime, timedelta
from glob import glob
from os.path import exists, getmtime, join, lexists, realpath
from pathlib import Path

from models import Resume

__module__ = Path(__file__).resolve().stem
_basedir = Path(__file__).resolve().parent


def main():
	resume = Resume()
	print(f"Resume: {resume.name}")
	print(f"Email: {resume.email}")
	print("Skills")
	print(resume.skills.programming)
	# programming = resume.programming
	# print(programming)


def main_old():
	sections = "awards basics education interests languages meta projects publications references skills volunteer work".split()
	about_dict = {
		"profile": "Profile"
	}
	awards_dict = {}
	certificates_dict = {}
	contact_dict = {}
	education_dict = {}
	employers_dict = {}
	experience_dict = {}
	meta_dict = {}
	projects_dict = {}
	publications_dict = {}
	references_dict = {}
	skills_dict = {}
	volunteer_dict = {}

	resume_dict = [
		contact_dict,
		about_dict,
		skills_dict,
		experience_dict,
		volunteer_dict,
		employers_dict,
		education_dict,
		projects_dict,
		publications_dict,
		awards_dict,
		certificates_dict,
		references_dict,
		meta_dict,
	]

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


def dump_json(filename, dataset, append: bool=False, overwrite: bool=False) -> int:
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


def dump_jsons(filename, dataset, append: bool=False, overwrite: bool=False) -> int:
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
	main()
	eoj()
