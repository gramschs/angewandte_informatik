'''
Aufgabe 11.1

Schreiben Sie eine Funktion, die die Funktion f(x) = sin(k * x) im Intervall [-2 * pi, 2 * pi] zeichnet.
Definieren Sie anschließend für k einen Slider mit Startwert k = 2. Bewegen Sie anschließend den Slider.
'''

# %%
from __future__ import print_function
from ipywidgets import interact
from matplotlib.pylab import *


# %%
def sinus_funktion(k):
    x = linspace(-2 * pi, 2 * pi, 200)
    y = sin(k * x)
    plot(x, y)


interact(sinus_funktion, k=2)
