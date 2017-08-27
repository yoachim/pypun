import string
import itertools


def clean_string(instring):
    """
    clean up a string to make it easier to match
    """

    outstring = instring.replace('_', ' ').strip()
    outstring = outstring.lower()
    outstrings = outstring.split(' ')
    translator = str.maketrans('', '', string.punctuation)
    outstrings = [word.translate(translator) for word in outstrings]
    outstring = ' '.join(outstrings)
    return outstring


def phrase_masher(str1, str2):
    """
    Mash two phrases together
    """
    l1 = str1.split(' ')
    l2 = str2.split(' ')
    if l1[0] == l2[-1]:
        result = l2[0:-1]
        result.extend(l1)
    elif l2[0] == l1[-1]:
        result = l1[0:-1]
        result.extend(l2)
    else:
        result = None
    if result is not None:
        result = ' '.join(result)
    return result


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
        words = title.split(' ')
        for word in words:
            uwords_dict[word].append(i)

    # Now to loop through each key and see what combinations can be made.
    results = []
    for key in uwords_dict:
        if len(uwords_dict[key]) > 1:
            combos = itertools.combinations(uwords_dict[key], 2)
            for combo in combos:
                mashup = phrase_masher(strings[combo[0]], strings[combo[1]])
                if mashup is not None:
                    results.append(mashup)
    return results


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

