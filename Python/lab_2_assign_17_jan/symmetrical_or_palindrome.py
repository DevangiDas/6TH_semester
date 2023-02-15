#Python program to check whether the string is Symmetrical or Palindrome
a_random_string = input("Enter your string here\n")
length_of_string = len(a_random_string)
def symmetrical_or_palindrome(string):
    new_string=''.join(reversed(string))
    if(new_string==string):
        return True
    else: 
        return False
catch = symmetrical_or_palindrome(a_random_string)
if (catch==True):
    print("The string is symmetrical or palindrome")
else:
    print("The string is not symmetrical or palindrome")