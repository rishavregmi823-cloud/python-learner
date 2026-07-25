# ATM Login

correct_username = "Rishav"
correct_password = "1234"
balance = 5000

attempt = 0

while attempt < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("\n✅ Login Successful!!")
        print(f"Welcome {correct_username}")

        wish = input("Do you want to check your balance? (yes/no): ")

        if wish.lower() == "yes":
            print(f"Your current balance is Rs {balance}")

        print("Thanks for visiting!! See you again.")
        break

    else:
        attempt += 1
        print("\n Invalid Username or Password")
        print(f"Attempts left: {3 - attempt}")

if attempt == 3:
    print("\n Your 3 attempts are over!")
    print("You cannot login.")