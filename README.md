# Text To Speech

This script allow you to convert a text to a speech based on Google Translate.

Each time you'll try to convert a text to a speech the script will download a mp3 file and store it in an audio directory. This will allow to reuse some speech without redownloading them.

## How to use it

    $ python text_to_speech LANGUAGE_CODE "TEXT"

example :

    $ python text_to_speech en "hello world"
