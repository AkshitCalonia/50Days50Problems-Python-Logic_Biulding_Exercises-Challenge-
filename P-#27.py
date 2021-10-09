#Remove The Word!
'''Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
'''

def remove_letters(ls, strz):
    if len(ls) > len(strz):
        return list(set(ls) - set(strz))
    else:
        return list(set(strz) - set(ls))

print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))