import string

fd = open("cap.txt", 'r')
text = fd.read()
text = text.upper()
new_text = str()
for letter in text:
    if letter in string.ascii_uppercase or letter in ['\n', ' ']:
        new_text += letter

open("test_file.txt", 'w').write(new_text)
