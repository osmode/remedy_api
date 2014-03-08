#!/usr/bin/python
import sys, logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/remedy")

from remedy import app as application
application.secret_key = 'Your secret key'

