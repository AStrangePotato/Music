# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
from playsound import playsound

notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"]
# Create the vectors X and Y

quantity = 10


imSoLost = []

x_pitch = np.array(range(quantity))
temp = input("Enter a formula for pitch graphing: *USE 'x'* \n")
if temp not None:
    y_pitch_formula = temp
else:
    y_pitch_formula = x_pitch * (x_pitch+1) / 2

y_pitch = y_pitch_formula



x_tempo = np.array(range(quantity))

x_pitch_formula = x_tempo ** 2

y_tempo = x_pitch_formula


for x in range(quantity):
    imSoLost.append(x * (x+1) / 2)

print(imSoLost)   



'''
round to nearest note on piano
play that note
1 = c
2= c#
etc
make list with y values for specified x increment

'''

# Add a title
plt.title('Graphing Music Project')

#grid
plt.grid(alpha=.4,linestyle='--')

# Create the plot
plt.plot(x_pitch, y_pitch, label='Pitch: x * (x+1) / 2')
plt.plot(x_tempo, y_tempo, label='Tempo: x ** 2')

plt.xlabel('x axis')
plt.ylabel('y axis' )

#show legend
plt.legend()
#plt.arrow()

# Show the plot
plt.show()



