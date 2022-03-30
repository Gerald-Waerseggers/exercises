import re
from turtle import title
import urllib.request
import json
import sys

def to_url(string):
    '''
    URLs cannot contain spaces. Replaces each space by %20.
    '''
    return re.sub(' ', '%20', string)

'''
Returns the URL of the lyrics page of the song.
'''
artist = sys.argv[1]
title = sys.argv[2]
url = 'https://api.lyrics.ovh/v1/'
url += to_url(artist) + '/' + to_url(title)
html = urllib.request.urlopen(url).read().decode('utf-8')
output = json.loads(html)
print(output['lyrics'])
