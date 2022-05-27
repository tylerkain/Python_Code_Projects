#!/bin/bash

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_type = input(
    "Welcome to the PyPassword Generator! \n What Kind of Password would you like Easy or Advanced \n Type E for Easy or Adv for Advanced: ").lower()


def easy_password():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password = ""
    for char in range(nr_letters):
        password += random.choice(letters)

    for char in range(nr_numbers):
        password += random.choice(numbers)

    for char in range(nr_symbols):
        password += random.choice(symbols)
    print(password)


def advanced_password():
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))
    password_list = []
    password = ""
    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    for char in password_list:
        password += char
    print(password)


if password_type == 'e':
    print(easy_password())

else:
    print(advanced_password())






