#!/usr/bin/python3
import ctypes


class IntStruct(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("ob_size", ctypes.c_long),
        ("ob_digit", ctypes.c_int),
    ]


int42 = IntStruct.from_address(id(42))

#print(42)

int42.ob_digit = 80

#print(42)

#print("42 + 10 =", 42 + 10)
# IDK why it's 52, but in interactive mode it will be 90
# You can try import this file in interactive mode and type "42 + 10"

#print("42 == 80 =", 42 == 80)
