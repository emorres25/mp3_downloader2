#!/usr/bin/env python

import youtube_dl
import pyperclip
import os


url = str(pyperclip.paste())
#os.system('cd ~/Downloads')
#os.system('youtube-dl --extract-audio --audio-format mp3 %s' % url)
os.system('youtube-dl -x --audio-format mp3 --prefer-ffmpeg %s' % url)
raw_input("")
