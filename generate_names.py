from punmaker import *

titles = read_wikipedia('data/enwiki-latest-all-titles-in-ns0')
print("read in %i titles" % len(titles))


#puns = punmaker(titles[500000:600000], outfile='puns.txt')
puns = punmaker(titles, outfile='puns.txt')
