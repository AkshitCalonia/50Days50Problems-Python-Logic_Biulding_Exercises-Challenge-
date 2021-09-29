'''Create a function that calculates what percentage of the box is filled in. Give your answer as a string percentage rounded to the nearest integer.

Examples
percent_filled([
  "####",
  "#  #",
  "#o #",
  "####"
]) ➞ "25%"

# One element out of four spaces.

percent_filled([
  "#######",
  "#o oo #",
  "#######"
]) ➞ "60%"

# Three elements out of five spaces.
'''

def per_fill(ls):
    strz = "".join(ls)
    ans =  round((strz.count("o")*100)/(strz.count("o")+strz.count(" ")))
    return f"{ans}%"
    

print(per_fill([
  "######",
  "#ooo #",
  "#oo  #",
  "#    #",
  "#    #",
  "######"
  ]))