import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

terms = ['Salmonella enterica','Escherichia coli','Sus scrofa','Homo sapiens','Mus musculus']
plt.bar(terms, [2940420,11455876,3751565,47509715,11515320])
plt.xlabel('Organism')
plt.ylabel('Number of Articles')
plt.title('The number of Articles found for each Organism')
plt.show()
plt.savefig('organism.png')
