print("Submitted by: Dan Joshua M. Tagaan ")

usernames = ["John", "Peter", "David"]
passwords = ["abc123", "123abc", "a1b2c3"]

curr_username = str(input("Username: "))
curr_password = str(input("Password: "))

correct = False

index = 0
for username in usernames:
    if curr_username == username and curr_password == passwords[index]:
        correct = True
    index = index + 1

if correct == True:
    print("Welcome, " + curr_username)
else:
    print("Account not found.")