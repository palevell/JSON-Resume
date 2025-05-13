# models/__main__.py

import os

from os.path import getsize, splitext

def setup():
	for entry in os.scandir():
		if getsize(entry.name) > 0:
			continue
		model_name = splitext(entry.name)[0].capitalize()
		print(f"{entry.name} {model_name}")
		header = "\n".join([
			f"# models/{entry.name}",
			"",
			f"class {model_name}(object):",
			f'	name = "{model_name} Model"',
			"\n",
		])
		with open(entry.name, "wt") as fp:
			fp.write(header)


if __name__ == "__main__":
	setup()
