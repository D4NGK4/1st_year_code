print("Submitted by: Dan Joshua M. Tagaan ")

usernames = ["John", "Peter", "David"]
passwords = ["abc123", "123abc", "a1b2c3"]

curr_username = str(input("Username: "))
curr_password = str(input("Password: "))

correct = False

index = 0
for x in usernames:
    if curr_username == usernames and passwords == passwords[index]:
        correct: True
        break
    index = index + 1


if correct == True:
    print("Welcome, " + curr_username)
else:
    print("Account not found.")