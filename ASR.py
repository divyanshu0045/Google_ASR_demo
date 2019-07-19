#!/usr/bin/env python

import speech_recognition as sr 
import librosa
import os
import soundfile as sf
import sys

def recog(path):
    for root, dirs, files in os.walk(path,topdown=True):  
        for name in files:
            AUDIO_FILE = (os.path.join(root, name)) 
            _tmp = 'tmp.wav'
            try:
                f,s = librosa.load(AUDIO_FILE)
            except:
                continue
            sf.write(_tmp, f, s, subtype='PCM_24')
              
            r = sr.Recognizer() 
              
            with sr.AudioFile(_tmp) as source: 
                audio = r.record(source)   
            try:
                text = r.recognize_google(audio) 
                print(os.path.basename(AUDIO_FILE).split('.')[0] + '|' + text)
                with(open('ASR_OUT.csv','a')) as f:
                    f.write(os.path.basename(AUDIO_FILE).split('.')[0] + '|' + text + '\n')
              
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
              
            except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
            finally:
                pass
                os.remove(_tmp)

if __name__ == "__main__":
    recog(sys.argv[1])

