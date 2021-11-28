#Words With Duplicate Letters
'''
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.

Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True
no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".
no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".

Notes
Letter matches are case-insensitive.
'''

def no_duplicate_letters(st):
    st = st.split(" ")
    ans = True
    for i in st:
        for l in i:
            if i.count(l) >= 2:
                ans = False
    return ans

print(no_duplicate_letters("An apple a day keeps the doctor away."))