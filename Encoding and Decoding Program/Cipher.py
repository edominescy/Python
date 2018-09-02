'''
Erin Dominescy
1/12/2016
'''

'''
confirm function returns the input from the user if to know whether or not the program will 
    be encoding or decoding a message.
'''
def confirm():
    print("Would you like to encrypt or decrypt a message?\n Enter 'e' for encrypt or 'd' for decrypt. \n")
    get_answer = input().lower()
    return get_answer

'''
message function returns the input from the user containing the message to be encoded or 
    decoded.
'''
def message():
    return input("Please enter your message. \n")

'''
ciphkey function returns the integer variable between 1 and 26 that determines how the message 
    will be encrypted or decrypted.
'''
def ciphkey():
    key = 0
    while True:
        keyin = int(input("Please enter a key between 1 and 26. \n"))
        if 1 <= keyin <= 26:
            return keyin

'''
translate function returns the translated message by taking in the parameters of mode (encoded or decoded),
    message (the message to be translated), and keyret (keyin from the ciphkey function) and goes through 
    each letter of the message converting them to ordinal values while checking for uppercase and lowercase.
    Then the message is converted back to alphabet values from ordinal values and added to the empty string
    that was created at the beginning of the function.
'''
def translate(mode, message, keyret):
    if mode == 'd':
        keyret = -keyret
    emptys = ""
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num += keyret
            if letter.isupper():
                if num > ord('Z'):
                    num -= 26
                if num < ord('A'):
                    num += 26
            elif letter.islower():
                if num > ord('z'):
                    num -= 26
                if num < ord('a'):
                    num += 26
            emptys += chr(num)
        else:
            emptys += letter
    return emptys

'''
mode variable is now the confirm function
'''
mode = confirm()

'''
message variable is now the message function
'''
message = message()

'''
keyret variable is now the ciphkey function
'''
keyret = ciphkey()


'''
print statements for displaying the translated message and initializing the program.
'''
print("Your translated message is: \n")
print(translate(mode, message, keyret))
