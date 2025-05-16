#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if search in my_list:
        new = my_list.copy()
        for i in range(len(new)):
            if new[i] == search:
                new[i] = replace
        return new
    else:
        return my_list
