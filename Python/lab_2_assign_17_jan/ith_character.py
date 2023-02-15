#Ways to remove i’th character from string in Python
string_input = input("enter your string:\n")
index_of_char_to_remove = int(input("enter the ith character index here:\n"))
new_string=""
for i in range(len(string_input)):
    if(i != index_of_char_to_remove):
        new_string = new_string+string_input[i]
print("The new string is:\t",new_string)