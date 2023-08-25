import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
 
x = np.linspace(0, 3, 300)
y = np.sin(5 * np.pi * x)
 
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
l, = ax.plot(x, y)
 
def onChange(value):
    l.set_ydata(np.sin(value * np.pi * x))
    fig.canvas.draw_idle()
 
slideraxis = fig.add_axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(slideraxis, label='Frequency [Hz]',
                valmin=0, valmax=10, valinit=5)
slider.on_changed(onChange)
plt.show()