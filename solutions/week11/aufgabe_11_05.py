'''
Aufgabe 11.5

Schreiben Sie ein Programm, bei dem der Benutzer über eine Drop-Down-Liste zwischen den Funktionen Sinus und Kosinus
wählen darf. Anschließend wird die ausgewählte Funktion im Intervall [-2 * pi, 2 * pi] gezeichnet. Über eine Checkbox darf
der Benutzer entscheiden, ob die Gitterlinien eingeblendet werden sollen oder nicht.
'''

from ipywidgets import interact
import ipywidgets as widgets
from numpy import linspace, sin, cos, pi
from matplotlib.pylab import plot, grid

def plotte_sin_cos(funktion, mit_gitter):
    x = linspace(-2*pi, 2*pi)
    if funktion == 'Sinus':
        y = sin(x)
    else:
        y = cos(x)
    plot(x,y)
    grid(mit_gitter)

funktion_dropdown = widgets.Dropdown(
    options = ['Sinus', 'Kosinus'],
    value = 'Sinus',
    description = 'Funktion: '
)

gitter_checkbox = widgets.Checkbox(
    value = False,
    description = 'Gitterlinien ein ',
    indent = False
)

interact(plotte_sin_cos, funktion = funktion_dropdown, mit_gitter = gitter_checkbox);