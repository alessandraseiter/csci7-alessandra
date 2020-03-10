"""Module to count how many of each digram there are in a fasta file then define a dictionary from that count"""


def digram(n):
    # create empty lists for each character that will be counted
    aa = []
    ag = []
    ac = []
    at = []
    ga = []
    gg = []
    gc = []
    gt = []
    ca = []
    cg = []
    cc = []
    ct = []
    ta = []
    tg = []
    tc = []
    tt = []

    try:
        with open(n, 'r') as input_file:
            # skip first (metadata) line of .fasta
            input_file.readline()
            for line in input_file:
                # count each character in each line
                string_aa = line.count('AA')
                string_ag = line.count('AG')
                string_ac = line.count('AC')
                string_at = line.count('AT')
                string_ga = line.count('GA')
                string_gg = line.count('GG')
                string_gc = line.count('GC')
                string_gt = line.count('GT')
                string_ca = line.count('CA')
                string_cg = line.count('CG')
                string_cc = line.count('CC')
                string_ct = line.count('CT')
                string_ta = line.count('TA')
                string_tg = line.count('TG')
                string_tc = line.count('TC')
                string_tt = line.count('TT')
                # add the character counts to each previously defined list
                aa.append(string_aa)
                ag.append(string_ag)
                ac.append(string_ac)
                at.append(string_at)
                ga.append(string_ga)
                gg.append(string_gg)
                gc.append(string_gc)
                gt.append(string_gt)
                ca.append(string_ca)
                cg.append(string_cg)
                cc.append(string_cc)
                ct.append(string_ct)
                ta.append(string_ta)
                tg.append(string_tg)
                tc.append(string_tc)
                tt.append(string_tt)
        # sum the totals of appended character counts
        total_aa = sum(aa)
        total_ag = sum(ag)
        total_ac = sum(ac)
        total_at = sum(at)
        total_ga = sum(ga)
        total_gg = sum(gg)
        total_gc = sum(gc)
        total_gt = sum(gt)
        total_ca = sum(ca)
        total_cg = sum(cg)
        total_cc = sum(cc)
        total_ct = sum(ct)
        total_ta = sum(ta)
        total_tg = sum(tg)
        total_tc = sum(tc)
        total_tt = sum(tt)
        # create dictionary of digram values
        digram_dict = {
            "AA": total_aa,
            "AG": total_ag,
            "AC": total_ac,
            "AT": total_at,
            "GA": total_ga,
            "GG": total_gg,
            "GC": total_gc,
            "GT": total_gt,
            "CA": total_ca,
            "CG": total_cg,
            "CC": total_cc,
            "CT": total_ct,
            "TA": total_ta,
            "TG": total_tg,
            "TC": total_tc,
            "TT": total_tt
        }
        return digram_dict
    # throws errors for missing files or files that are not in .fasta format
    except FileNotFoundError:
        print("Sorry, I can't find the file", n)
    except n.ext != '.fasta':
        print("Sorry, the file type of", n, "is invalid")
