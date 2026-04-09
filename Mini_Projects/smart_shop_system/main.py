import config as c


# Step 1: Input
username = input("enter username : ")
password = input("enter password : ")
age = int(input("enter your age : "))


# Step 2: Membership check
if username in c.USERS:
    print("username found")    
else:
    print("username not found")


#  Step 3 : Login Validation
if username == c.ADMIN_USER and password == c.ADMIN_PASSWORD:
    print ("login successfull")
else:
    print("login failed")


# Step 4: Age validation
if age >=18 and age <=60:
    print("access allowed")
else:
    print("access restricted")


# Step 5: Shopping system
total = 0

price1 = int(input("enter price of item 1 : "))
price2 = int(input("enter price of item 2 : "))
price3 = int(input("enter price of item 3 : "))

total += price1
total += price2
total += price3

print("total price for all 3 item : ", total)


# Step 6: Discount logic (comparison + logical)
if total > 500 :
    total -= 50
    print("Discount applied of 50 as bill is more than 500 ")


# Step 7: Even/Odd check (arithmetic + comparison)
if total % 2 == 0:
    print("final amount is even ")
else:
    print("final amount is odd ")


# Step 8: Identity check (concept demo)
a = total
b = total
print("same memory check : ", a is b)


# Final output
print("Final bill:", total)