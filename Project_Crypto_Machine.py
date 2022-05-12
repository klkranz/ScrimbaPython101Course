import string

def enigma_light():
    # create keys string
    keys = string.printable
    # autogenerate the values string by offsetting original string
    values = keys[-3:] + keys[0:-3]
    # print(keys)
    # print(values)
    # create two dictionaries
    dict_e = {key: value for key, value in zip(keys, values)}
    dict_d = {value: key for value, key in zip(values, keys)}
    # print(dict_e)
    # print(dict_d)    
    #user input 'the message' and mode
    msg = input('Enter your message: ')
    mode = input('Enter mode: encode (e) OR decode (d): ')
    # run encode or decode
    if mode.lower() == 'e':
        msg_e = ''.join([dict_e[letter] for letter in msg])
        print('The encoded message is: ', msg_e)
    elif mode.lower() == 'd':
        msg_d = ''.join([dict_d[letter] for letter in msg])
        print('The decoded message is: ', msg_d)
    else:
        print('You entered an invalid mode, please try again.')
# clean and beautify the code
# forced mode into lower case, didn't force the message into lower case as he did because sometimes capital letters 
# are important for meaning. And because I didn't do that, I didn't need to capitalize the first letter of the final 
# output. Imported strings to generate the printable character (letters, numbers, punctuation and whitespace. 
# I also didn't return a string and have to print the function because the function printed so I could specify that 
# the output was either encoded or decoded. Still deciding if I want to make decode the default mode as he did.

enigma_light()

# His way
#def enigma_light():
#    # create keys string
#    keys = 'abcdefghijklmnopqrstuvwxyz !'
#    # autogenerate the values string by offsetting original string
#    values = keys[-1] + keys[0:-1]
#    # print(keys)
#    # print(values)
#    # create two dictionaries
#    dict_e = dict(zip(keys, values))
#    dict_d = dict(zip(values, keys))
#    # OR create 1 and then flip
#    # dict_e = dict(zip(keys,values))
#    # dict_d = {value:key for key, value in dict_e.items()}
#    # user input 'the message' and mode
#    msg = input('Enter your secret message quietly: ')
#    mode = input('Crypto mode: encode (e) OR decrypt as default: ')
#    # run encode or decode
#    if mode.lower() == 'e':
#        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
#    else:
#        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])
#
#    return new_msg.capitalize()
#
#
## return result
## clean and beautify the code
#
#print(enigma_light())
