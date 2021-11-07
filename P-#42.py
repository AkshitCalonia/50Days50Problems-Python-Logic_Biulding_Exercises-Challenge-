#Word to Bitstring to Boolean List
'''
Create a function that converts a word to a bitstring and then to a boolean list based on the following criteria:

Locate the position of the letter in the English alphabet (from 1 to 26).
Odd positions will be represented as 1 and even positions will be represented as 0.
Convert the represented positions to boolean values, 1 for True and 0 for False.
Store the conversions into an array.
Examples
to_boolean_list("deep") ➞ [False, True, True, False]
# deep converts to 0110
# d is the 4th alphabet - 0
# e is the 5th alphabet - 1
# e is the 5th alphabet - 1
# p is the 16th alphabet - 0

to_boolean_list("loves") ➞ [False, True, False, True, True]

to_boolean_list("tesh") ➞ [False, True, True, False]
Notes
The letter A is at position 1 and Z at 26.
All input strings are in lowercase letters of the English alphabet.
'''

alp_dict = {
        'a' : '1', 
        'b' : '2', 
        'c' : '3', 
        'd' : '4', 
        'e' : '5', 
        'f' : '6', 
        'g' : '7', 
        'h' : '8', 
        'i' : '9', 
        'j' : '10', 
        'k' : '11', 
        'l' : '12', 
        'm' : '13', 
        'n' : '14', 
        'o' : '15', 
        'p' : '16', 
        'q' : '17', 
        'r' : '18', 
        's' : '19', 
        't' : '20', 
        'u' : '21', 
        'v' : '22', 
        'w' : '23', 
        'x' : '24', 
        'y' : '25', 
        'z' : '26'
}


def to_boolean_list(wrd):
    recs = []
    for i in wrd:
        if int(alp_dict[i]) % 2 == 0:
            wrd = wrd.replace(i, "0")
        else:
            wrd = wrd.replace(i, "1")
    
    for k in wrd:
        if k == "0":
            recs.append(False)
        else:
            recs.append(True)
    
    return recs


print(to_boolean_list("loves"))
