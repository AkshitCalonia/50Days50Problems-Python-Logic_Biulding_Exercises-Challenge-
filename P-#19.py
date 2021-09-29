'''Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []
'''

def setsminus(ls, st):
    lsstr = []
    lsstr[:0] = st
    return list(set(lsstr) - set(ls)) if len(lsstr)>len(ls) else list(set(ls) - set(lsstr))

print(setsminus(["s", "t", "r", "i", "n", "g", "w"], "string"))


# import keyboard
# import turtle
# import time

# # using module keyboard
# while True:  # making a loop
#     t = turtle.Pen()
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('w'):  # if key 'q' is pressed
#             print('forward')
#             t.forward(100)
#         if keyboard.is_pressed('a'):  # if key 'q' is pressed
            
#             print('left')
#             t.tilt(90)
#             t.forward(100)
#         if keyboard.is_pressed('d'):  # if key 'q' is pressed
#             print('right')
#             t.tilt(180)
#             t.forward(100)
#         if keyboard.is_pressed('s'):  # if key 'q' is pressed
#             print('back')
#             t.tilt(360)
#             t.forward(100)
            
#     except:
#         break  # if user pressed a key other than the given key the loop will break

# time.sleep(1)

# time.sleep(1)

# time.sleep(1)
