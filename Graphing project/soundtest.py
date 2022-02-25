from playsound import playsound

notes = {
    "1":"C4",
    "2":"D4",
    "3":"E4",
    "4":"F4",
    "5":"G4",
    "6":"A4",
    "7":"B4",
    "8":"C5"

}

def playNotes(keyList):
    try:
        for pitch in keyList:
            if pitch in notes.values():
                pitch = str(round(int(pitch)))
                file = notes[pitch] + ".mp3"
                print(file)
                playsound(file)
            else:
                print(f"Note {pitch} not found.")
    except exception as e:
        print(e)

