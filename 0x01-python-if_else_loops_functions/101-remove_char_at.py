#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return (str)
    else:
        cutstr = str[:n] + str[n:]
        return (cutstr)
