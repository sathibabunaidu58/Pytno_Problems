a = input('enter a word : ')
b=("Palindrome" if a==a[::-1] else 'Not Palindrom')
print(b)