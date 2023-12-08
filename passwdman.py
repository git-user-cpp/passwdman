# MIT License
#
# Copyright (c) 2023 Andrew Kushyk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import hashlib

file_name = "pass.txt"


def create_account():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest()

    with open(file_name, "w") as database:
        database.write(username + "|" + hashed_password)
    print("Account created successfully!")


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest()

    with open(file_name, "r") as database:
        pass_man = database.read()

    if username in pass_man and hashed_password in pass_man:
        print("Login successful!")
    else:
        print("Invalid username or password")


def main():
    while True:
        choice = int(input("Enter 1 to create an account, 2 to login or 0 to exit: "))
        if choice == 0:
            break
        elif choice == 1:
            create_account()
        elif choice == 2:
            login()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
