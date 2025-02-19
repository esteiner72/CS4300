import os

def task6_1(file_name):
    with open(file_name, "r") as file:
        text = file.read()
    return len(text.split())

