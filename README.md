Google-Text-To-Speech
=====================

A python script for using Google's text to speech feature to save text to an MP3 file.

```
usage: GoogleTextToSpeech.py [-h] [-o [OUTPUT]] [-l [LANGUAGE]]
                    (-f FILE | -s STRING [STRING ...])

Google Text To Speech.

optional arguments:
  -h, --help            show this help message and exit
  -o [OUTPUT], --output [OUTPUT]
                        Filename to output audio to
  -l [LANGUAGE], --language [LANGUAGE]
                        Language to output text to.
  -f FILE, --file FILE  File to read text from.
  -s STRING [STRING ...], --string STRING [STRING ...]
                        A string of text to convert to speech.
  -p, --play            Play the speech if your computer allows it.
```


Examples
=====================

To convert text from a file:

```
$ python GoogleTextToSpeech.py -f text.txt
```

To convert text from the commandline:

```
$ python GoogleTextToSpeech.py -l en -o audio.mp3 -s "hello world"
```

To convert text and play the mp3 audio

```
$ python GoogleTextToSpeech.py -l en -s "hello world" -p
```


Requierments
=====================

Audio
---------------------

To play the mp3 you need to have some packages installed on your system.

### Linux

For Linux, the script is using the play command included in the sox package. 

In case the sox package is not installed on your system:

```
$ sudo aptitude install sox
```

You may also need to install extra packages to gain support for MP3 

```
$ sudo aptitude install libsox-fmt-mp3
```


### Mac

For Mac, the script is using the afplay command which should already been installed on your system.


Thanks
=====================

Many thanks to Hung Truong (http://www.hung-truong.com/blog/) who helped me to build this Python script. First for given me the clue to send more than 100 characters for a mp3 and secondly for the Pyhton lessons I learned from his own scripts.