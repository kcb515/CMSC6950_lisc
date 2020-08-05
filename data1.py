from lisc import Counts
from lisc.utils.db import SCDB
from lisc.utils.io import save_object
from lisc.plts.counts import plot_matrix, plot_clustermap, plot_dendrogram

# Set up some terms to search for
terms = [['frontal lobe'], ['temporal lobe'], ['parietal lobe'], ['occipital lobe']]

# Initialize counts object & add the terms that we want to collect co-occurrences for
counts = Counts()
counts.add_terms(terms)

# Collect co-occurrence data
counts.run_collection(verbose=True)

# Check out the raw count data
print(counts.counts)

# Check how many articles were found for each search term
counts.check_counts()

# Check the most studied term
counts.check_top()

# Set some new terms
terms_a = [['frontal lobe'], ['temporal lobe'], ['parietal lobe'], ['occipital lobe']]
terms_b = [['vision'], ['audition', 'auditory'], ['somatosensory'], ['olfaction', 'smell'],
           ['gustation', 'taste'], ['proprioception'], ['nociception', 'pain']]

# Set terms lists
#  Different terms lists are indexed by the 'A' and 'B' labels
counts.add_terms(terms_a, dim='A')
counts.add_terms(terms_b, dim='B')

# Collect co-occurrence data
counts.run_collection()

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
