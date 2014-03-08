#from flask import g, session, url_for, request, render_template
from __init__ import app
#from werkzeug import secure_filename
#import glob, os

PHOTOS_DIRECTORY = '/var/www/insight/insight/static'

'''
@app.route('/this')
def this_func():
	return "OK"

@app.route('/upload_photo', methods=['GET', 'POST'])
def upload_photo():
	if request.method == 'POST':
		f = request.files['uploadedfile']
		f.save('/var/www/remedy/remedy/static/' + secure_filename(f.filename))
	return "OK"
	
@app.route('/remedy_feed', methods=['GET', 'POST'])
def remedy_feed():
	photo_list = []
	video_list = []
	prefix = '/static/'
	os.chdir(PHOTOS_DIRECTORY)
	for files in glob.glob("*.jpg"):
		photo_list.append(prefix+files)
	
	for files in glob.glob("*.mp4"):
		video_list.append(prefix+files)
	
	return render_template('remedy_feed.html', photo_list=photo_list, video_list=video_list)
'''
