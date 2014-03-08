# Source code: (C) 2013-2014 Omar Metwally (omarmetwally.quora.com)
from flask import Flask, request, g, flash, redirect, render_template
from werkzeug import secure_filename
import glob, os

app = Flask(__name__)

PHOTOS_DIRECTORY = '/var/www/remedy/remedy/static'

@app.route('/')
@app.route('/index')
def startdd_index():
	return "Hello, World!"

@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
	if request.method == 'POST':
		f = request.files['uploadedfile']
		f.save('/var/www/remedy/remedy/static/' + secure_filename(f.filename))
	return "OK"

@app.route('/upload_text', methods=['POST'])
def upload_text():
	if not request.json or not 'text' in request.json:
		abort(400)
	
	print "Text: ", request.json['text']
	text = request.json['text']
	result = perform_query('insert into text values (?)', text)

	return "OK"
	

@app.route('/remedy_feed', methods=['GET', 'POST'])
def remedy_feed():
	photo_list = []
	video_list = []
	prefix = '/static/'
	os.chdir(PHOTOS_DIRECTORY)
	files = glob.glob("*.jpg")
	files.sort(key=lambda x: os.path.getmtime(x))
	files.reverse()

	for f in files:
		photo_list.append(prefix+f)
	
	files = glob.glob("*.mp4")
	files.sort(key=lambda x: os.path.getmtime(x))
	files.reverse()

	for f in files:
		video_list.append(prefix+f)
	
	return render_template('remedy_feed.html', photo_list=photo_list, video_list=video_list)

from test_view import *
from dbconfig import *

if __name__ == '__main__':
	app.run()


