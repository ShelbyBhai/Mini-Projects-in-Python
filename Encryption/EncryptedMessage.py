print("Enter the Given Text & Shift Value : ")
_input_string = input()
_shift_Value = int(input())
print(_input_string, _shift_Value)

encrypted_input_string = ""

for char in _input_string:
    if char.isupper():
        encrypted_input_string += chr((ord(char)+_shift_Value-65)%26+65)
    elif char.islower():
        encrypted_input_string += chr((ord(char)+_shift_Value-97)%26+97)

print("The encrypted message is now : " + encrypted_input_string)




