from lisc.objects.base import Base
# Initialize a base object
base = Base()
# Set some terms
terms = [['chemistry'], ['biology']]
# Add terms to the object
base.add_terms(terms)
# Check the terms added to the base object
base.check_terms()
# Set up a list of multiple terms, each with synonyms
terms = [['gene', 'genetic'], ['cortex', 'cortical']]
# Set up inclusions and exclusions
#   Each is a list, that should be the same length as the number of terms
inclusions = [['brain'], ['body']]
exclusions = [['protein'], ['subcortical']]
# Add the inclusion and exclusions
base.add_terms(inclusions, 'inclusions')
base.add_terms(exclusions, 'exclusions')
# Check the loaded terms
base.check_terms()
# Check inclusion & exclusion words
base.check_terms('inclusions')
print('\n')
base.check_terms('exclusions')
# Check the label for the current terms
base.labels