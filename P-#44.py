#Secret Function 4.0
'''
Create a function based on the input and output. Look at the examples, there is a pattern.

Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"
secret("p.one") ➞ "<p class='one'></p>"
secret("p.four.five") ➞ "<p class='four five'></p>"

Notes
Input is a string.
'''

def secret(st):
    rec = st.split(".")
    rec2 = " ".join(list(j for j in rec if rec.index(j) != 0))
    return f"<{rec[0]} class='{rec2}'></{rec[0]}>"
print(secret("p.one.two.three"))