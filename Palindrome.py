def Palindrome():
    word = str(input())
    if word[::-1].startswith(word):
        print(True)
    else:
        print(False)

Palindrome()