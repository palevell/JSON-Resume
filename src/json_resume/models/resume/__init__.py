# models/resume/__init__.py

from .personal import Personal
from .skills import Skills
from .experience import Experience


class Resume(object):
	name = Personal.name
	location = Personal.location
	email = Personal.email
	web = Personal.web
	linkedin = Personal.linkedin

	skills = Skills()
	# programming = skills.programming

	def programming(self):
		return self.skills.programming


__all__ = [Resume,]
