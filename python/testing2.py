#!/usr/bin/env python3

usernames = set()
passwords = dict()


def newusers():
    global usernames
    global passwords

    name = input("Enter a name: ")
    while name in usernames:
        name = input("Name taken, pick another name: ")

    usernames.add(name)
    passwords[name] = input('Password: ')

def oldusers():
    global usernames
    global passwords

    name = input("Input your name: ")
    pw = input("Input your password: ")

    if pw == passwords.get(name):
        print("%s, welcome back" % name )
    else:
        print('login failed')


def login():
    option = """
    (N)ew User Login
    (O)ld User Login
    (E)xit
    """

    i = ""
    while i != "E":

        i = input(option)
        if i == "N":
            newusers()
            continue

        if i == "O":
            oldusers()
            continue


if __name__ == '__main__':
    login()
