import string


def clean_string(instring):
    """
    clean up a string to make it easier to match
    """

    outstring = instring.replace('_', ' ').strip()
    outstring = outstring.lower()
    outstrings = outstring.split(' ')
    outstrings = [word.translate(None, string.punctuation) for word in outstrings]
    outstring = ' '.join(outstrings)
    return outstring


def phrase_masher(str1, str2):
    """
    Mash two phrases together
    """
    
    

def punmaker(strings):
    """
    Generate puns

    Parameters
    ----------
    strings : list of strings
    """

    # let's find the unique words, and make a dictionary to keep track
    uwords_dict = {}
    all_words = []
    for title in strings:
        all_words.extend(title.split(' '))
    # Make them unique
    all_words = list(set(all_words))
    for word in all_words:
        uwords_dict[word] = []

    for i, title in enumerate(strings):
        words = strings.split(' ')
        for word in words:
            uwords_dict[word].append(i)

    # Now to loop through each key and see what combinations can be made.


def read_wikipedia(filename, title_length=2):
    """
    Read in the wikipedia list of article names
    """

    # Read in each line
    with open(filename) as f:
        lines = f.readlines()

    # Make all lower case and strip punctuation
    lines = [clean_string(line) for line in lines]

    if title_length is not None:
        lines = [line for line in lines if (len(line.split(' ')) <= title_length) & (len(line.split(' ')) > 1)]

    return lines

