#!/usr/bin/python
# encoding: utf-8

import argparse
import sys
import re
import urllib, urllib2
import time
import subprocess
import os


def main():
	if len(sys.argv)==1:
		# Display the help if no argument is setted.
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()

	if args.file:
		text = args.file.read()
	if args.string:
		text = ' '.join(map(str,args.string))

	text_lines = convertTextAsLinesOfText(text)

	downloadAudioFile(text_lines, args.language, args.output)

	if args.play == True:
		play(args.output.name)



def convertTextAsLinesOfText(text):
	''' This convert a word, a short text, a long text into several parts to 
		smaller than 100 characters. 
	'''	
	
	# Sanitizes the text.
	text = text.replace('\n','')
	text_list = re.split('(\,|\.|\;|\:)', text)	

	# Splits a text into chunks of texts.
	text_lines = []
	for idx, val in enumerate(text_list):

		if (idx % 2 == 0):
			text_lines.append(val)
		else :
			# Combines the string + the punctuation.
			joined_text = ''.join((text_lines.pop(),val))

			# Checks if the chunk need to be splitted again.
			if len(joined_text) < 100:
				text_lines.append(joined_text)
			else:
				subparts = re.split('( )', joined_text)
				temp_string = ""
				temp_array = []
				for part in subparts:
					temp_string = temp_string + part
					if len(temp_string) > 80:
						temp_array.append(temp_string)
						temp_string = ""
				#append final part
				temp_array.append(temp_string)
				text_lines.extend(temp_array)

	return text_lines

def downloadAudioFile(text_lines, language, audio_file):
	'''
		Donwloads a MP3 from Google Translatea mp3 based on a text and a 
		language code.
	'''
	for idx, line in enumerate(text_lines):
		query_params = {"tl": language, "q": line, "total": len(text_lines), "idx": idx}
		url = "http://translate.google.com/translate_tts?ie=UTF-8" + "&" + unicode_urlencode(query_params)
		headers = {"Host":"translate.google.com", "User-Agent":"Mozilla 5.10"}
		req = urllib2.Request(url, '', headers)
		sys.stdout.write('.')
		sys.stdout.flush()
		if len(line) > 0:
			try:
				response = urllib2.urlopen(req)
				audio_file.write(response.read())
				time.sleep(.5)
			except urllib2.HTTPError as e:
				print ('%s' % e)

	print 'Saved MP3 to %s' % (audio_file.name)
	audio_file.close()


def unicode_urlencode(params):
	'''
		Encodes params to be injected in an url.
	'''
	if isinstance(params, dict):
		params = params.items()
	return urllib.urlencode([(k, isinstance(v, unicode) and v.encode('utf-8') or v) for k, v in params])


def play(filename):
	''' 
		Plays the mp3 depending on the system.
	'''	
	if sys.platform == "linux" or sys.platform == "linux2":
		# linux
		subprocess.call(["play", filename])
	
	elif sys.platform == "darwin":
		# OS X
		subprocess.call(["afplay", filename])


if __name__ == '__main__':

	description="Google Text To Speech."
	parser = argparse.ArgumentParser(prog='GoogleTextToSpeech', description=description,
									 epilog='Have fun')

	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('-f', '--file', type=argparse.FileType('r'), help='File to read text from.')
	group.add_argument('-s', '--string', action='store', nargs='+', help='A string of text to convert to speech.')

	parser.add_argument('-o','--output', action='store', nargs='?',
						help='Filename to output audio to',
						type=argparse.FileType('w'), 
						default='out.mp3')
	parser.add_argument('-l','--language', action='store', nargs='?', help='Language to output text to.', default='en')
	
	parser.add_argument('-p','--play', action='store_true', help='Play the speech if your computer allows it.')
	#parser.add_argument('-c','--cache', action='store_true', help='Cache the result of the file for a later use.')

	main()
