# Write a Python program to accept the user's first and last name and then getting
# them printed in the the reverse order with a space between first name and last name.
def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::]))

print(reverse_string_words("ineuron"))
