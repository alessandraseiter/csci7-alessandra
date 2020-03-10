"""Module to print fasta digram dictionary as a 4x4 table"""


from typing import Dict
# make digram dictionary available for formatting
import problem2_test


# format digram dictionary into 4x4 table
def printDigrams(pairsCount: Dict[str,int]):
    """Print the digrams"""

    bases = ['A', 'G', 'C', 'T']

    # Print the column headings
    print(' ', end=' ')
    for ch in bases:
        print(ch.rjust(7), end=' ')
    print()

    # Print the body of the table
    for ch1 in bases:
        print(ch1, end=' ')

        # Print a row of the table
        for ch2 in bases:
            digram = ch1 + ch2
            if (digram in pairsCount):
                count = pairsCount[digram]
            else:
                count = 0

            # Print count, with formatting
            print(repr(count).rjust(7), end=' ')
        print()

# define empty dictionary
# pass ecoli.fasta through digram dictionary
# pass ecoli.fasta dictionary through formatting script
digrams = {}
digrams_dictionary = problem2_test.digram('ecoli.fasta')
printDigrams(digrams_dictionary)