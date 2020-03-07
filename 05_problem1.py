"""Module to test whether a file is a fasta then count number of As, Cs, Gs, and Ts in it"""


def fasta(n):
    # create empty lists for each character we want to count
    a = []
    c = []
    g = []
    t = []

    try:
        with open(n, 'r') as input_file:
            # skip first (metadata) line of .fasta
            line = input_file.readline().strip()
            for line in input_file:
                # count each character in each line
                characters_a = line.count('A')
                characters_c = line.count('C')
                characters_g = line.count('G')
                characters_t = line.count('T')
                # add the character counts to each previously defined list
                a.append(characters_a)
                c.append(characters_c)
                g.append(characters_g)
                t.append(characters_t)
        # sum the totals of appended character counts
        total_a = sum(a)
        total_c = sum(c)
        total_g = sum(g)
        total_t = sum(t)
        # print character count totals
        print("A", total_a)
        print("C", total_c)
        print("G", total_g)
        print("T", total_t)
    # throws errors for missing files or files that are not in .fasta format
    except FileNotFoundError:
        print("Sorry, I can't find the file", n)
    except n.ext != '.fasta':
        print("Sorry, the file type of", n, "is invalid")
