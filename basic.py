#print("bittu")

'''x = 'awesome'
def myfunc():
  global x
  x = 'fantastic'
myfunc()
print('Python is ' + x)'''

"""print("He is called 'Johnny'")
print('He is called "Johnny"')"""


balance = 5000

print("1. Check balance")
print("2. Withdraw balance")
print("3. Deposit")
print("4. Exit")

while True:
    n = int(input("Enter your choice: "))

    if n == 1:
        print("Current balance:", balance)

    elif n == 2:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Current balance:", balance)

    elif n == 3:
        deposit = int(input("Enter amount to deposit: "))
        balance += deposit
        print("Deposit successful")
        print("Current balance:", balance)

    elif n == 4:
        print("Thank you!")
        break

    else:
        print("Madharchod jyada mat daal")