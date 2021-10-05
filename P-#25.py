# Key - Mouse (Logic)
'''A keyboard and a mouse cost in total x, knowing that the keyboard costs y more than the mouse, calculate the price of the mouse. Round the price of the mouse.

Examples
KM({"Total": "10.00$", "Difference": "0.40$", "Mouse": "?"})
➞ {"Total": "10.00$", "Difference":"0.40$", "Mouse": "4.8$"}

KM({"Total": "90.00$", "Difference": "5.40$", "Mouse": "?"})
➞ {"Total": "90.00$", "Difference": "5.40$", "Mouse": "42.3$"}

KM({"Total": "1.30$", "Difference": "0.80$", "Mouse": "?"})
➞ {"Total": "1.30$", "Difference": "0.80$", "Mouse": "0.25$"}
'''
import numpy as np

def mouseocst(mydict):

    ttl = float(mydict["Total"].rstrip(mydict["Total"][-1]))
    dif = float(mydict["Difference"].rstrip(mydict["Difference"][-1]))

    A = [[1, 1], [1, -1]]
    B = [ttl, dif]

    ans = np.linalg.solve(A, B)
    # ans =  [x, y] = [Cost of Keyboard, cost of mouse]
    # Hence, ans[1], i.e. the cost of mouse 

    mydict["Mouse"] = str(ans[1])+"$"

    return mydict

print(mouseocst({"Total": "1.30$", "Difference": "0.80$", "Mouse": "?"}))
