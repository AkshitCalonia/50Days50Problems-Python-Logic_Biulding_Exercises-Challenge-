# Create a function that takes three arguments (first dictionary, second dictionary, key) in order to:

# Return the boolean True if both dictionaries have the same values for the same keys.
# If the dictionaries don't match, return the string "Not the same", or the string "One's empty" if only one of the dictionaries contains the given key.

dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }

def check(dict1, dict2, ky):
    if ky in dict1 and ky in dict2 and dict1.get(ky) == dict2.get(ky):
        return True
    elif ky in dict1 or ky in dict2:
        return "One's empty"
    else:
        return "Not the same"

print(check(dict_first, dict_second, "sun"))
