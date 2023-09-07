message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch == ' ':
        encoded_message = encoded_message + ' '
    elif ch == '!':
        encoded_message = encoded_message + '!'
    elif ch == ch.upper():
        pos = ord(ch.upper()) - ord('A')  # find difference
        pos = (pos + offset) % 26
        new_ch = chr(pos + ord('A'))  # find replacement
        encoded_message = encoded_message + new_ch
    else:
        pos = ord(ch) - ord('a')  # find difference
        pos = (pos + offset) % 26
        new_ch = chr(pos + ord('a'))  # find replacement
        encoded_message = encoded_message + new_ch

print(encoded_message)

# Julius Caesar code