# Import function to collect data, and helper functions to analyze co-occurrence data
import lisc
from lisc.collect import collect_counts
from lisc.analysis.counts import compute_normalization, compute_association_index

# Set some terms to search for
terms_a = [['Salmonella enterica'], ['Escherichia coli'],['Sus scrofa'],['Homo sapiens'],['Mus musculus']]

# Collect 'counts' (co-occurrence data) - across a single list of terms
coocs, term_counts, meta_dat = collect_counts(terms_a, db='nucleotide', verbose=True)

# Check how many articles were found for each combination
print(coocs)

# Print out how many articles found for each term
for term, count in zip(terms_a, term_counts):
    print('{:12} : {}'.format(term[0], count))
