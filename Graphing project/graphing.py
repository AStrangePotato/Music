# Import our modules that we are using
import matplotlib.pyplot as plt
import numpy as np
from playsound import playsound

import threading

import math

from soundtest import playNotes

quantity = 250

blues = [36,39,41,42,43,46,48,46,43,42,41,39,36]
bMinHar = [35,37,38,40,42,43,46,47,46,43,42,40,38,37,35]
penta = [35,37,39,42,44,47,44,42,39,37,35]
chromatic = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]
wholeTone = [35,37,39,41,43,45,47,45,43,41,39,37,35]
sus = [28,31,33,35,33,35,33,31,30,23,30,30,28,31,33,35,33,35,33,31,30,30,38,38,40,38,35,28,35,33,31,30,26,23,30,30,28,31,33,35,33,35,33,30,26,28]

# Create the vectors X and Y
def linear():
    return list(range(quantity))

def quadratic():
    a = list(range(quantity))
    for i in range(len(a)):
        a[i] = a[i] ** 2
    '''for i in range(len(a)):
        a[i] = a[i] % 40'''
    return a

def triangular():
    a = []
    for i in range(quantity):
        a.append(i * (i+1) / 2)
    return a

def sine():
    a = []
    for i in range(quantity):
        a.append(10 *math.sin(0.2 * i))
    return a

def fibonacci():
    a = [1,1]
    for i in range(quantity - 2):
        a.append(a[i+1]+a[i])
    return a

pitch_formula = int(input("Enter pitch formula\n1: linear, 2: quadratic, 3: triangular, 4: sine, 5: fibonacci\n"))
tempo_formula = int(input("Enter tempo formula\n1: linear, 2: quadratic, 3: triangular, 4: sine, 5: fibonacci\n"))

if pitch_formula == 1: #linear
    x_pitch = linear()
    y_pitch = linear()
elif pitch_formula == 2: #quadratic
    x_pitch = linear()
    y_pitch = quadratic()
elif pitch_formula == 3: #triangular
    x_pitch = linear()
    y_pitch = triangular()
elif pitch_formula == 4: #sine
    x_pitch = linear()
    y_pitch = sine()
elif pitch_formula == 5: #fibonacci
    x_pitch = linear()
    y_pitch = fibonacci()
    
if tempo_formula == 1: #linear
    x_tempo = linear()
    y_tempo = linear()
elif tempo_formula == 2: #quadratic
    x_tempo = linear()
    y_tempo = quadratic()
elif tempo_formula == 3: #triangular
    x_tempo = linear()
    y_tempo = triangular()
elif tempo_formula == 4: #sine
    x_tempo = linear()
    y_tempo = sine()
elif tempo_formula == 5: #fibonacci
    x_tempo = linear()
    y_tempo = fibonacci()



# Add a title
plt.title('Graphing Music Project')

#grid
plt.grid(alpha=.4,linestyle='--')

# Create the plot
plt.plot(x_pitch, y_pitch, label='Pitch')
plt.plot(x_tempo, y_tempo, label='Tempo')

plt.xlabel('x axis')
plt.ylabel('y axis' )

#show legend
plt.legend()
#plt.arrow()

# Show the plot

def lostAgain():
    playNotes(y_pitch)
    
threading.Thread(target=lostAgain).start()
plt.show()


