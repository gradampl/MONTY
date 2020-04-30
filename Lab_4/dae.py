def isPalindrom(string):
    reversed = string[::-1]
    if string.lower() == reversed.lower():
        return True
    else:
        return False

print(str(isPalindrom("Mononom")))
print(str(isPalindrom("Pononom")))

# Result:
#
# True
# False
#
# Process finished with exit code 0