#!/usr/bin/python

import sys
from bs4 import BeautifulSoup
import urllib2
import subprocess
import wave
from pydub import AudioSegment

url = sys.argv[1]
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")
content = soup.find('div', class_='post-content')
all_ps = content.find_all("p")

person_one = "Craig"
person_two = all_ps[0].string.split(" ")[3]

speaker_mapping = {person_one : "Victoria", person_two: "Daniel"}

current_speaker = ""
conversation = []
for p in all_ps:
    if current_speaker == "" and p.span == None: # Looking for first speaker
        continue
    elif p.span != None: # Speaker changed
        current_speaker = p.span.text[0:p.span.text.find(" ")]
        speech = p.text[p.text.find(" ") + 3:]
        conversation.append((current_speaker, speech))
    else: # New paragraph same speaker
        conversation.append((current_speaker, p.text))

# Create individual wav files
audio_files = []
for idx, (speaker, speech) in enumerate(conversation):
    audio_file = '{}.wav'.format(idx)
    audio_files.append(audio_file)
    subprocess.call(['say', '-v', speaker_mapping[speaker], '-o', audio_file, '--data-format', 'LEF32@8000', speech])

pause = AudioSegment.silent(duration=1000)

# Create interview file
full_interview = pause
for af in audio_files:
    sound = AudioSegment.from_file(af)
    full_interview += sound
    full_interview += pause
    subprocess.call(["rm", af]) # cleanup
full_interview.export("full_interview.wav", format='wav')
