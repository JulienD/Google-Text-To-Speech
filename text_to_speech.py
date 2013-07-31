# example: sudo python text_to_speech.py fr "TEXT"
# encoding: utf-8
import urllib2
import urllib
import sys
import subprocess
import os
import hashlib

# Constructs the url to Google translate service.
TRANSLATE_URL = "http://translate.google.com/translate_tts?ie=UTF-8"
FILE_DIRECTORY = "audio"

def unicode_urlencode(params):
    if isinstance(params, dict):
        params = params.items()
    return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params])


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def getUniqueFileName(text, language):
	stripped = strip_non_ascii(text)
	md5 = hashlib.md5(stripped).hexdigest()	
	return md5


def getAudioFile(text, language):
	# Gets a unique file name for this request.
	filename = getUniqueFileName(text, language) + '.mp3'
	filepath = FILE_DIRECTORY + '/' + filename
	
	print "filepath > %s"  % (filepath)

	if os.path.isfile(filepath):
		# Checks if the request has already been saved.
		return filepath
	else:
		# Download the request.		
		if (audioFile == downloadAudioFile(text, language)) :
			# Stores the mp3.
			saveAudiofile(audioFile, filepath)
			return filepath	
		else:
			return {}


def downloadAudioFile(text, language):
    query_params = {"q": text, "tl": language}
    url = TRANSLATE_URL + "&" + unicode_urlencode(query_params)
    try:
        return make_request(url).read()
    except:
        return {}


def saveAudiofile(audioFile, filepath):
    try:
		output = open(filepath,'wb')
		output.write(audioFile)
		output.close()
		return True    
    except:
        return False


def make_request(url):
	req = urllib2.Request(url)
	req.add_header('User-agent', 'Mozilla 5.10')
	res = urllib2.urlopen(req)
	return res


def play(filename):
	# Plays the mp3 depending on the system.
	from sys import platform as _platform
	if _platform == "linux" or _platform == "linux2":
	    # linux
	    subprocess.call(["play", filename])
	elif _platform == "darwin":
	    # OS X
	    subprocess.call(["afplay", filename])


if __name__ == '__main__':
	# Gets the string from the command args 1.
	language = str(sys.argv[1])

	# Gets the string from the command args 2.
	text = str(sys.argv[2])

	# Gets the name of the file.
	audioFile = getAudioFile(text, language)

	# Plays the mp3.
	if audioFile :
		play(audioFile)

