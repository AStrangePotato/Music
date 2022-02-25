from pydub import AudioSegment
from pydub.playback import play
import pydub
from pydub import *

AudioSegment.converter = r"C:\FFmpeg\bin\FFmpeg.exe"
AudioSegment.ffmpeg = r"C:\bin\FFmpeg.exe"
AudioSegment.ffprobe = r"C:\FFmpeg\bin\ffprobe.exe"
notes = {
    '0':'C1',
    '1':'Db1',
    '2':'D1',
    '3':'Eb1',
    '4':'E1',
    '5':'F1',
    '6':'Gb1',
    '7':'G1',
    '8':'Ab1',
    '9':'A1',
    '10':'Bb1',
    '11':'B1',


    '12':'C2',
    '13':'Db2',
    '14':'D2',
    '15':'Eb2',
    '16':'E2',
    '17':'F2',
    '18':'Gb2',
    '19':'G2',
    '20':'Ab2',
    '21':'A2',
    '22':'Bb2',
    '23':'B2',


    '24':'C3',
    '25':'Db3',
    '26':'D3',
    '27':'Eb3',
    '28':'E3',
    '29':'F3',
    '30':'Gb3',
    '31':'G3',
    '32':'Ab3',
    '33':'A3',
    '34':'Bb3',
    '35':'B3',


    '36':'C4',
    '37':'Db4',
    '38':'D4',
    '39':'Eb4',
    '40':'E4',
    '41':'F4',
    '42':'Gb4',
    '43':'G4',
    '44':'Ab4',
    '45':'A4',
    '46':'Bb4',
    '47':'B4',


    '48':'C5',
    '49':'Db5',
    '50':'D5',
    '51':'Eb5',
    '52':'E5',
    '53':'F5',
    '54':'Gb5',
    '55':'G5',
    '56':'Ab5',
    '57':'A5',
    '58':'Bb5',
    '59':'B5',


    '60':'C6',
    '61':'Db6',
    '62':'D6',
    '63':'Eb6',
    '64':'E6',
    '65':'F6',
    '66':'Gb6',
    '67':'G6',
    '68':'Ab6',
    '69':'A6',
    '70':'Bb6',
    '71':'B6',


    '72':'C7',
    '73':'Db7',
    '74':'D7',
    '75':'Eb7',
    '76':'E7',
    '77':'F7',
    '78':'Gb7',
    '79':'G7',
    '80':'Ab7',
    '81':'A7',
    '82':'Bb7',
    '83':'B7',
    '84':'C8'
}

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    altFR = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return altFR.set_frame_rate(sound.frame_rate)

a = [35,37,38,40,42,43,46]
b = [47,46,43,42,40,38,37,35]

def playNotes(keyList, tempoList):
    i=0
    try:
        for pitch in keyList:
            pitch = str(round(int(pitch)))
            if pitch in notes:
                
                file = "notes/" + notes[pitch] + ".wav"
                sound = AudioSegment.from_file(file)
                print(file) # debug purposes leave for now
                play(speed_change(sound, tempoList[i] / 12))
                i+=1
                
            else:
                print(f"Note {pitch} not found.")
                
    except Exception as e:
        print(e)
