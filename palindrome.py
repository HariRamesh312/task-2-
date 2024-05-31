def palindrome(string):
    return string == string[::-1]
string = "madam"
ans = palindrome(string)
if ans:
    print("True")
else:
    print("False")
