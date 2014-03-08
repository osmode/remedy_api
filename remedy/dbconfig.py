from flask import g, flash, redirect, request
from __init__ import app
import sqlite3

DATABASE = '/var/www/remedy/tmp/database.db'

def connect_db():
        return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
	g.db = connect_db()

@app.after_request
def after_request(response):
	g.db.close()
	return response

def query_db(query, args=(), one=False):
	cur = g.db.execute(query, args)
	rv = [dict((cur.description[idx][0], value)
		for idx, value in enumerate(row)) for row in cur.fetchall()]
	return (rv[0] if rv else None) if one else rv

def perform_query(query, args=()):
	cur = g.db.execute(query, args)
	g.db.commit()


