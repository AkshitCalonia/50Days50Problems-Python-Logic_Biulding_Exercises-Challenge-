# Check if the given string consists of only letters and spaces and if every letter is in lower case.

def lettersonly(sen):
    return sen.islower and sen.replace(" ", "").isalpha()

lettersonly("PYTHON")