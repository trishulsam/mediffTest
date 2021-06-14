def checkpalindrome(word):
    str1= word[::-1].lower()
    str2 = word.lower()
    if(str1==str2):
        return True
    else:
        return False

word = input("enter the word needs to be checked: ")
print(checkpalindrome(word))