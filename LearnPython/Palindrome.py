promt: str = "Enter string to text or 'exit': "
mess = "Palindrome test: "
string: str = input(promt)

while string and string != "exit":
    strLen: int = len(string)

    range: int = strLen // 2
    finalIndex = strLen - 1

    i: int = 0
    while i < range and string[i] == string[finalIndex - i]:

        i += 1

    if i == range:
        print(mess, True)

    else:
        print(mess, False)
    string = input(promt)

del mess
del promt
del string