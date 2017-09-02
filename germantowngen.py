import random

"""
Written by uristjack.
"""

def germantown():
    """Creates random town names in a rather Germanic flavour.
    """

    #List of German town prefixes.
    prefixlist = ["Birken", "Blau", "Blumen", "Bronze", "Buchen", "Drei",
                  "Eber", "Efeu", "Eichen", "Eisen", "Elfen", "Erken",
                  "Eschen", "Falken", "Feuer", "Fuchs", "Gold", "Grafen",
                  "Grau", "Greifen", "Hammer", "Herz", "Holz", "Kaiser",
                  "Keiler", "Koenigs", "Kohle", "Kupfer", "Nagel", "Neu",
                  "Nord", "Ober", "Ochsen", "Ost", "Raben", "Rinds",
                  "Ritter", "Rosen", "Rot", "Schatten", "Schlangen", "Schwarz",
                  "Silber", "Sonnen", "Stein", "Sued", "Ulmen", "Unter",
                  "Vier", "Wagen", "Wald", "Wehr", "Weiden", "Wein",
                  "Weiss", "West", "Wiesen", "Zwergen", "Uhlen", "Dunkel",
                  "Hell"]
    
    #List of German town suffixes.
    suffixlist = ["acker", "ad", "anger", "au", "auen", "bach",
                  "bad", "bar", "baum", "berg", "bergen", "brecht",
                  "bruch", "brueck", "brunn", "burg", "dorf", "drop",
                  "duene", "eck", "eich", "fall", "feld", "fels",
                  "forst", "furt", "gau", "grab", "grund", "grunden",
                  "hafen", "hag", "hain", "hall", "ham", "haus",
                  "hausen", "haven", "heim", "holm", "holt", "horst",
                  "huegel", "hus", "husen", "ingen", "kam", "kirchen",
                  "klamm", "mark", "marsch", "meer", "moor", "mund",
                  "pforten", "port", "quell", "rast", "ried", "roden",
                  "sand", "see", "sel", "stadt", "steg", "stein",
                  "stolz", "strand", "tal", "tannen", "turm", "unk",
                  "vell", "wacht", "wald", "wall", "weg", "weiher",
                  "weiler", "wein", "hofen", "hang", "hoeh", "wasser",
                  "wehr"]
    
    #Randomly chooses a prefix and suffix
    prefix = random.choice(prefixlist)
    suffix = random.choice(suffixlist)

    #Stitches prefix and suffix together into town name, and returns it
    return(prefix + suffix)
