#!/usr/bin/python3
def element_at(my_list, idx):
    listlen = len(my_list)
    idx_len = listlen - 1
    if idx < 0:
        return None
    elif idx > idx_len:
        return None
    else:
        return my_list[idx]
