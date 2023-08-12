#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    
    for i in range(length):
        if i == idx:
            del my_list[i]
            break
    
    retur(my_list)
