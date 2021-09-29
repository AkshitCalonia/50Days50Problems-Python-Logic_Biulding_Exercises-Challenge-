'''Some characters do not change after a rotation of 180 degrees. They can be read, although sometimes in a different way. For example, uppercase letters "H", "I", "N", "O", "S", "X", "Z" after rotation are not changed, the letter "M" becomes a "W", and vice versa.

So, the word "WOW" turns into the word "MOM". On the other hand, the word "HOME" cannot be rotated.

Find the number of unique readable Rotated Words in the input string txt (without duplicates).
'''

def txt(striz):
    unqlters = ["H", "I", "N", "O", "S", "X", "Z", "M"]
    caps = striz.upper()
    ns = caps.split(" ")

    for i in ns:
        for alpha in i:
            if alpha not in unqlters:
                ns[ns.index(i)] = ""
                break 
            else:
                continue
    j = ns.count("")
    for item in range(j):
        ns.remove("")

    return len(ns)
                

print(txt("MUBASHIR"))