import string, sys
import itertools


def clean_string(instring):
    """
    clean up a string to make it easier to match
    """

    # XXX--strip out anything in parantheses.

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


def isEnglish(s):
    try:
        str(s).encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True


def punmaker(strings, outfile=None, block=1e5, verbose=True):
    """
    Generate puns

    Parameters
    ----------
    strings : list of strings
    """

    if outfile is not None:
        outfile = open(outfile, "w", encoding='utf-8')

    # clean out the unicode crazy strings
    strings = [string for string in strings if isEnglish(string)]

    # remove any duplicates
    strings = list(set(strings))

    starting_words = set([title.split(' ')[0] for title in strings])
    ending_words = set([title.split(' ')[-1] for title in strings])
    possible_pun_words = starting_words.intersection(ending_words)

    strings = [string for string in strings if len(possible_pun_words.intersection(string.split(' '))) > 0]

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

    max_length = len(uwords_dict)
    # Now to loop through each key and see what combinations can be made.
    results = []
    for i, key in enumerate(uwords_dict):
        if len(uwords_dict[key]) > 1:
            combos = itertools.combinations(uwords_dict[key], 2)
            for combo in combos:
                mashup = phrase_masher(strings[combo[0]], strings[combo[1]])
                if mashup is not None:
                    results.append(mashup)
                    # dump the output to a file
                    if outfile is not None and len(results) > block:
                        for pun in results:
                            print(pun, file=outfile)
                        results = []
        if verbose:
            progress = i/max_length*100
            text = "\rprogress=%.1f%%" % progress
            sys.stdout.write(text)
            sys.stdout.flush()

    if verbose:
        print("")
    # Get any straglers
    if outfile is not None:
        for pun in results:
            print(pun, file=outfile)
            results = []
        outfile.close()

    return results


def read_wikipedia(filename, title_length=2):
    """
    Read in the wikipedia list of article names
    """

    # Read in each line
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()

    # Make all lower case and strip punctuation
    lines = [clean_string(line) for line in lines]

    if title_length is not None:
        lines = [line for line in lines if (len(line.split(' ')) <= title_length) & (len(line.split(' ')) > 1)]

    return lines

