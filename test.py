dictionary = {    

    
}

notes = ["C","D","E","F","G","A","B"]


i=0

for octave in range(1,8):
    print("\n")
    for note in notes:
        hasFlat = note != "C" and note != "F"
        if hasFlat:
            print("'" + str(i) + "'" + f":'{note}b{octave}',")
            print("'" + str(i+1) + "'" + f":'{note}{octave}',")
            i+=2
            
        elif not hasFlat:
            print("'" + str(i) + "'" + f":'{note}{octave}',")
            i+=1
        
