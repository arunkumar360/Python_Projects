email = input("Enter your email address:")

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]  

print(f"Your username is {username} and domain name is {domain}")