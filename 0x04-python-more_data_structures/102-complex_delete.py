#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keystodel = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keystodel.append(key)
    for key in keystodel:
        del a_dictionary[key]
    return a_dictionary
