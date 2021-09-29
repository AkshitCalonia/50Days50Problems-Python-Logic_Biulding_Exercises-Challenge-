# A night club will give you a word. For entrance, you need to provide the right number according to the provided word.

# Every given word will have a doubled letter, like "dd" in addiction. To answer the right number you need to find the doubled letter's position in the alphabets and multiply this number with 4.

# Create a function that takes the argument of word and returns the right number.

alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# func to find the duplicate letter

def dup(strin):
    j = []
    for k in range(len(strin)):
        if strin[k] == strin[-1]:
            j.append(strin[k])
            break
        elif strin[k] == strin[k+1]:
            j.append(strin[k])
        else:
            continue
        return print(alphabet_list.index(j[0]) * 4)

dup("hello")
