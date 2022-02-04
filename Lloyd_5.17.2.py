#Lloyd_5.17.2.py
"""Display the results of rolling a six-sided die in a bar graph. (Dietel Intro to Python)"""

import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns

rolls = [random.randrange(1, 7) for i in range(600)]

values, frequencies = np.unique(rolls, return_counts=True)
title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('darkgrid')
axes = sns.barplot(x=values, y=frequencies, palette='colorblind')
axes.set_title(title)
axes.set(xlabel='Die Value', ylabel='Frequency')
axes.set_ylim(top=max(frequencies) * 1.10) #Makes room for text above bar.
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0 #Calculates the center x-coordinate where the text will appear
    text_y = bar.get_height() #Gets the y-coordinate where the text will appear
    text = f'{frequency:,}\n{frequency / len(rolls):.3%}' #Creates a two-line string 
    axes.text(text_x, text_y, text, fontsize=11, ha='center', va='bottom') #Calls the axes objects text method to dipslay the text

plt.show()