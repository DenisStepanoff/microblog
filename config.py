import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'Sfe2yr4k7ht4F9s'
