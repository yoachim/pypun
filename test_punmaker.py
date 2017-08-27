from punmaker import clean_string, punmaker


# Should make this a true test class, whatever.

# Some phrases to try and mash
start_phrases = ['heavy petting', 'Petting Zoo', 'zoo party', 'daisy chain', 'chain link', 'ack ack'
                 'blah blah', 'petting park', 'taco time', 'time_cop']
# Clean them
start_phrases = [clean_string(phrase) for phrase in start_phrases]

result = punmaker(start_phrases)
print(result)
