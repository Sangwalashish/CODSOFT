import secrets
import string

password_len = int(input("Enter the desired length of your password (in Numbers): "))

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
spcl_char = string.punctuation

pss = uppercase + lowercase + digits + spcl_char

pswrd = ''
for i in range(password_len):
    pswrd += secrets.choice(pss)

print("Generated Password: ", pswrd)