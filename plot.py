import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


terms = ['frontal lobe', 'temporal lobe', 'parietal lobe', 'occipital lobe']
counts1 = [0, 1842, 808, 521]
counts2 = [1842, 0, 751, 627]
counts3 = [808, 751, 0, 444]
counts4 = [521, 627, 444, 0]

x = np.arange(len(terms))  # the label locations
width = 0.35  # the width of the bars


fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, counts1, width, label='Term List 1')
rects2 = ax.bar(x + width/2, counts2, width, label='Term List 2')
rects1 = ax.bar(x - width/2, counts3, width, label='Term List 3')
rects2 = ax.bar(x + width/2, counts4, width, label='Term list 4')

ax.set_ylabel('Counts')
ax.set_title('Counts for each Term List')
ax.set_xticks(x)
ax.set_xticklabels(terms)
ax.legend()


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)


plt.show()
plt.savefig('counts.png')
