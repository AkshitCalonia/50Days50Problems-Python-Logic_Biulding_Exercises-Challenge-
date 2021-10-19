#Pluralize!
'''
Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }
'''

def pluralize_the_list(ls):
    nondups = []    #not made the list as a set instead because it wont allow me to remove elemn from the list
    recs = []
    for i in ls:
        if i not in nondups:
            nondups.append(i)

    for i in nondups:
        if ls.count(i) > 1:
            nondups.remove(i)
            recs.append(i+"s")
    
    return set(nondups+recs)


print(pluralize_the_list(["cow", "pig", "cow", "cow"]))
