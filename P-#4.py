# Jay and Silent Bob have been given a fraction of an ounce but they only understand grams. 
# Given an ounce weighs 28.3495 grams, convert the amount of ounces to grams. 
# Round the number of grams to one decimal place.

def conv(ou):
    j = ou * 28.3495
    return print(round(j, 1), end = ' gram')

conv(1)