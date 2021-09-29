# Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:

def TpofG(ls):
    nwls1 = []
    nwls2 = []
    final_list = []
    for i in range(len(ls)):
        j = ls[i]

        q = j.get("quantity")
        pr = j.get("price")

        nwls1.append(q)
        nwls2.append(pr)

    for i in range(len(nwls1)):
        k = nwls1[i] * nwls2[i]
        final_list.append(k)

    jsd = sum(final_list)

    return print(round(jsd, 1))


TpofG([
    {"product": "Milk", "quantity": 1, "price": 1.50},
    {"product": "Eggs", "quantity": 12, "price": 0.10},
    {"product": "Bread", "quantity": 2, "price": 1.60},
    {"product": "Cheese", "quantity": 1, "price": 4.50}
])
