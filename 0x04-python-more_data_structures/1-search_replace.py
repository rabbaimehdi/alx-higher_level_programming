#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def f_search(element):
        return element if element != search else replace
    return list(map(f_search, my_list))
