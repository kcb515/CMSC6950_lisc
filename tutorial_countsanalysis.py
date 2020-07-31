from lisc.utils.db import SCDB
from lisc.utils.io import load_object

from lisc.plts.counts import plot_matrix, plot_clustermap, plot_dendrogram

# Reload the counts object from the last tutorial
counts = load_object('tutorial_counts', SCDB('lisc_db'))

# Look at the collected counts data for the first set of terms
counts.check_data(data_type='counts', dim='A')

# Look at the collected counts data for the second set of terms
counts.check_data(data_type='counts', dim='B')

# Compute a normalization of the co-occurrence data
counts.compute_score('normalize', dim='A')

# Check out the computed normalization
print(counts.score)

# Compute the association index
counts.compute_score('association')

# Check out the computed score
print(counts.score)
# Plot a matrix of the association index data
plot_matrix(counts.score, counts.terms['B'].labels, counts.terms['A'].labels)

# Plot a dendrogram, to cluster the terms
plot_dendrogram(counts.score, counts.terms['B'].labels)

