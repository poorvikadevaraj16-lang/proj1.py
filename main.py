name=input("enter you name :")

def income():
    try:
      income=int(input("enter your monthly income: "))
      return income
    except ValueError:
      print("enter valid valid")
      return income()

income = income()

def category():
 expence_category ={}

 while True:
        category=input("enter the expence category:")
        try:
            expence2=int(input("enter the expence"))
        
        except ValueError:
            print("enter the valid expence")
            continue
        expence_category[category]=[expence2]
        choice = input("Do you want to add another expense? yes/no: ")
        if choice=="no":
            break
 return expence_category

expence_category = category()

def cat(expence_category):
    expence = 0

    for expenses in expence_category.values():
        for amount in expenses:
            expence += amount

    return expence

total = cat(expence_category)
print("Total expense:", total)

for category,expence2 in expence_category.items():
    print("the expence_category is",category,expence2)
    

def balance( income,expence):
    remaining_balance=income-expence
    if remaining_balance<0:
     print("exceeds the limit")

remaining=balance(income, total)
    

highest_expence=0
for category,expence2 in expence_category.items():
    for amount in expence2:
     if amount> highest_expence:
        highest_expence=amount

print(" the highest expence is ",highest_expence)

import ast

# ---------------- SAVE EXPENSES ----------------

with open("expence.txt", "a") as file:
    for category, expence2 in expence_category.items():
        file.write(category + ": " + str(expence2) + "\n")


# ---------------- READ FILE ----------------
try:
    with open("expence.txt", "r") as file:
        data = file.read()
    print(data)
except FileNotFoundError:
    print("the file not found")




# ---------------- LOAD EXPENSES INTO DICTIONARY ----------------

expence = {}

with open("expence.txt", "r") as file:
    for line in file:
        category, expence2 = line.split(":")

        expence2 = ast.literal_eval(expence2)

        if category in expence:
            expence[category].append(expence2)
        else:
            expence[category] =expence2

print(expence)
expence3=0

with open("expence.txt", "r") as file:
        for line in file:
            category,expence2=line.split(":")
            expence2=ast.literal_eval(expence2)
            for  amount in expence2:
                expence3+=amount

print(expence3)
print(type(expence2))
remain=income-expence3
print(remain)
highest_expence=0
with open("expence.txt","r") as file:
   for line in file :
      category,expence2=line.split(":")
      expence2=ast.literal_eval(expence2)
      for amount in expence2:
          if amount>highest_expence:
                highest_expence=amount

print(highest_expence)
         






