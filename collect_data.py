#!/usr/bin/python3


def  collect_name():
    first_name = input("input your first name ")
    last_name = input("input your last name ")
    middle_name = input("input your middle name ")

    if not last_name or not first_name:
        return ''
    return first_name + " " + middle_name + " " + last_name
