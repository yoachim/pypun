from punmaker import *

titles = read_wikipedia('data/enwiki-latest-all-titles-in-ns0')
print("read in %i titles" % len(titles))


# puns = punmaker(titles[500000:600000])
puns = punmaker(titles)

print("generated %i puns." % len(puns))

myfile = open("puns.txt", "w", encoding='utf-8')

for pun in puns:
    print(pun, file=myfile)

myfile.close()
