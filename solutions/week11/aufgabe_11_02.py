'''
Aufgabe 11.2

Eine Gerade wird durch die Funktionsgleichung

 y = m * x + b

mit der Steigung m und dem y-Achsenabschnitt b beschrieben. Schreiben Sie eine Funktion, die eine Gerade im
Intervall [-5,5] zeichnet und bei der die y-Achse stets zwischen -10 und 10 anzeigt. Eine Benutzerin oder ein
Benutzer soll die Steigung im Bereich m in [-3,3] mit der Schrittweite 0.1 und den y-Achsenabschnitt
b in [-7.5, 7.5] mit der Schrittweite 0.5 wählen können.
'''
from __future__ import print_function
from ipywidgets import interact
import ipywidgets as widgets
from matplotlib.pylab import *
from numpy import *


def zeichne_gerade(m, b):
    x = linspace(-5, 5)
    y = m * x + b
    plot(x, y)
    xlim(-5, 5)
    ylim(-10, 10)


interact(zeichne_gerade,
         m = widgets.FloatSlider(min=-3, max=3, steps=0.1, value=1),
         b = widgets.FloatSlider(min=-7.5, max=7.5, steps=0.5, value=0));