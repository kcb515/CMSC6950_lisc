import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

terms = ['frontal lobe', 'temporal lobe', 'parietal lobe', 'occipital lobe']
plt.bar(terms, [14496, 28219, 5099, 3822])
plt.xlabel('Term')
plt.ylabel('Documents')
plt.title('The number of documents found for each search term')
plt.show()
plt.savefig('document.png')
