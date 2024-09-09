#initialize
import random

floodPrem = 90
floodDed = 2000

cost1 = 6439
cost2 = 3081  
cost3 = 160632
cost4 = 10000
gain5 = 200
gain6 = 2000
gain7 = 20
gain8 = 200

premium1 = 80
deductible1 = 3000
premium2 = 100
deductible2 = 2000
premium3 = 120
deductible3 = 1000

insurancePaid = 0
youPaid = 0
amountLeft = 15000


#####USER'S RANDOMLY GENERATED SCENARIOS#####
scenariosList = []
#SCENARIO 1
scenariosList.append("Oh no! You found out that your property had caught on fire. Thank goodness you have landlord insurance though! Since the fire didn't spread too far, the total cost of all the damages is around $6,439.")
#SCENARIO 2
scenariosList.append("There was a huge hailstorm that was so intense that it broke a majority of the windows in your property. Your landlord insurance can help cover for that though! After assessing the damage, the total cost of the damages comes to $3,081.")
#SCENARIO 3
scenariosList.append("Aw man, your property got completely flooded from the recent flood. Unfortunately, your landlord insurance doesn't cover for floods, but if you purchased flood insurance, then it can cover for your damages. The total cost of all the damages is $160,632.")
#SCENARIO 4
scenariosList.append("One of your tenants decided to sue you for $10,000 because they fell down the stairs and broke their back because of a broken handrail. You agreed to pay for their medical expenses.")
#SCENARIO 5
scenariosList.append("While you were out for a walk, you found 2 crisp $100 bills on the ground. How lucky!")
#SCENARIO 6
scenariosList.append("Congratulations, you won $2,000 from a mini jackpot!")
#SCENARIO 7
scenariosList.append("You helped a kind old lady cross the street, and she gave you $20 for your kindness.")
#SCENARIO 8
scenariosList.append("Your parents gave you $200 because you are their favorite successful child. Shh.... don't tell your siblings!")


######THE USER'S LANDLORD INSURANCE PLANS######
insurancePlans = []
insurancePlans.append("$80 premium and $3000 deductible")
insurancePlans.append("$100 premium and $2000 deductible")
insurancePlans.append("$120 premium and $1000 deductible")


#functions
def scenarios():
  return random.choice(scenariosList)
  
    
#main
print("*"*33)
print("THE LANDLORD INSURANCE SIMULATION")
print("*"*33)
name = input("\nHello! What is your name? ")
print(f"\nWelcome, {name}, to the landlord insurance simulation! Today, you, the landlord, will be choosing an insurance plan to secure your property in case of an emergency! Currently, you only have $15k in your bank account to spend on insurance. You will be stuck in scenarios that can harm the state of your property (or not!), so be sure to choose your plan wisely! This program will end after you experience a randomly selected scenario that occurs once each round. There will be 10 rounds in total. Make sure you keep your property safe and bank account stable after the last round :)")

enter = input("\nPress the ENTER key to continue. ")
if enter == "":
  print("\nHere is the current list of landlord insurance plans...")
print("\nLandlord Insurance Plans:")
print("Plan 1:", insurancePlans[0])
print("Plan 2:", insurancePlans[1])
print("Plan 3:", insurancePlans[2])
print("\n***All of these plans have a $200,000 landlord property coverage***")

insurancePlan = int(input("\nWhich insurance plan would you like? Please type in a number: "))

#INSURANCE PLAN 1
if insurancePlan == 1:
  print("\nOkay, you have selected the", insurancePlans[0], "plan!")
  floodPurchase = input("\nWould you also like to purchase flood insurance ($90 premium and $2,000 deductible with a $250,000 building coverage) for your property as well? Your property is located in an area that may experience floods. Type in yes or no: ")
  #PLAN 1 WITH FLOOD INSURANCE
  if floodPurchase == "yes":
    print("\nGreat! You have purchased flood insurance. Now, may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      #PLAN 1 WITH FLOOD INSURANCE ROUNDS 1-10
      for x in range(10):
        print()
        print()
        print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
        choice = scenarios()
        print(choice)
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 1
        if choice == scenariosList[0]:
          youPaid = youPaid + premium1 + floodPrem + deductible1
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 2
        elif choice == scenariosList[1]:
            youPaid = youPaid + premium1 + floodPrem + deductible1
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 3
        elif choice == scenariosList[2]:
          print("\nYou purchased flood insurance, so your damages will be covered!")
          youPaid = youPaid + premium1 + floodPrem + floodDed
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 4
        elif choice == scenariosList[3]:
            youPaid = youPaid + premium1 + floodPrem + deductible1
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 5
        elif choice == scenariosList[4]:
          youPaid += premium1 + floodPrem
          amountLeft = amountLeft - youPaid + gain5
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 6
        elif choice == scenariosList[5]:
          youPaid += premium1 + floodPrem
          amountLeft = amountLeft - youPaid + gain6
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 7
        elif choice == scenariosList[6]:
          youPaid += premium1 + floodPrem
          amountLeft = amountLeft - youPaid + gain7
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 1 WITH FLOOD INSURANCE IN SCENARIO 8
        else:
          youPaid += premium1 + floodPrem
          amountLeft = amountLeft - youPaid + gain8
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
  #PLAN 1 WITHOUT FLOOD INSURANCE
  else:
    print("\nOkay, now may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      for x in range(10):
          print()
          print()
          print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
          choice = scenarios()
          print(choice)
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 1
          if choice == scenariosList[0]:
            youPaid = youPaid + premium1  + deductible1
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 2
          elif choice == scenariosList[1]:
            youPaid = youPaid + premium1  + deductible1
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 3
          elif choice == scenariosList[2]:
            print("\nUnfortunately, you didn't purchase flood insurance, so the damages won't be covered by insurance :(")
            youPaid = youPaid + cost3 + premium1
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print("***YOU ARE IN MAJOR DEBT***")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 4
          elif choice == scenariosList[3]:
            youPaid = youPaid + premium1 + deductible1
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 5
          elif choice == scenariosList[4]:
            youPaid += premium1 
            amountLeft = amountLeft - youPaid + gain5
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 6
          elif choice == scenariosList[5]:
            youPaid += premium1 
            amountLeft = amountLeft - youPaid + gain6
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 7
          elif choice == scenariosList[6]:
            youPaid += premium1 
            amountLeft = amountLeft - youPaid + gain7
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 1 WITHOUT FLOOD INSURANCE IN SCENARIO 8
          else:
            youPaid += premium1 
            amountLeft = amountLeft - youPaid + gain8
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")  
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
            
#INSURANCE PLAN 2
elif insurancePlan == 2:
  print("\nOkay, you have selected the", insurancePlans[1], "plan!")
  floodPurchase = input("\nWould you also like to purchase flood insurance ($90 premium and $2,000 deductible with a $250,000 building coverage) for your property as well? Your property is located in an area that may experience floods. Type in yes or no: ")
  #PLAN 2 WITH FLOOD INSURANCE
  if floodPurchase == "yes":
    print("\nGreat! You have purchased flood insurance. Now, may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      for x in range(10):
        print()
        print()
        print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
        choice = scenarios()
        print(choice)
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 1
        if choice == scenariosList[0]:
          youPaid = youPaid + premium2 + floodPrem + deductible2
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 2
        elif choice == scenariosList[1]:
            youPaid = youPaid + premium2 + floodPrem + deductible2
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 3
        elif choice == scenariosList[2]:
          print("\nYou purchased flood insurance, so your damages will be covered!")
          youPaid = youPaid + premium2 + floodPrem + floodDed
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 4
        elif choice == scenariosList[3]:
            youPaid = youPaid + premium2 + floodPrem + deductible2
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 5
        elif choice == scenariosList[4]:
          youPaid += premium2 + floodPrem
          amountLeft = amountLeft - youPaid + gain5
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 6
        elif choice == scenariosList[5]:
          youPaid += premium2 + floodPrem
          amountLeft = amountLeft - youPaid + gain6
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 7
        elif choice == scenariosList[6]:
          youPaid += premium2 + floodPrem
          amountLeft = amountLeft - youPaid + gain7
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 2 WITH FLOOD INSURANCE IN SCENARIO 8
        else:
          youPaid += premium2 + floodPrem
          amountLeft = amountLeft - youPaid + gain8
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
  #PLAN 2 WITHOUT FLOOD INSURANCE
  else:
    print("\nOkay, now may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      #PLAN 2 WITHOUT FLOOD INSURANCE ROUNDS 1-10
      for x in range(10):
          print()
          print()
          print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
          choice = scenarios()
          print(choice)
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 1
          if choice == scenariosList[0]:
            youPaid = youPaid + premium2 + deductible2
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 2
          elif choice == scenariosList[1]:
            youPaid = youPaid + premium2 + deductible2
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 3
          elif choice == scenariosList[2]:
            print("\nUnfortunately, you didn't purchase flood insurance, so the damages won't be covered by insurance :(")
            youPaid = youPaid + cost3 + premium2 
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            print("***YOU ARE IN MAJOR DEBT***")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 4
          elif choice == scenariosList[3]:
            youPaid = youPaid + premium2 + deductible2 
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 5
          elif choice == scenariosList[4]:
            youPaid += premium2 
            amountLeft = amountLeft - youPaid + gain5
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 6
          elif choice == scenariosList[5]:
            youPaid += premium2 
            amountLeft = amountLeft - youPaid + gain6
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 7
          elif choice == scenariosList[6]:
            youPaid += premium2 
            amountLeft = amountLeft - youPaid + gain7
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 2 WITHOUT FLOOD INSURANCE IN SCENARIO 8
          else:
            youPaid += premium2 
            amountLeft = amountLeft - youPaid + gain8
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
 
else:
  #INSURANCE PLAN 3
  print("\nOkay, you have selected the", insurancePlans[2], "plan!")
  floodPurchase = input("\nWould you also like to purchase flood insurance ($90 premium and $2,000 deductible with a $250,000 building coverage) for your property as well? Your property is located in an area that may experience floods. Type in yes or no: ")
  #PLAN 3 WITH FLOOD INSURANCE
  if floodPurchase == "yes":
    print("\nGreat! You have purchased flood insurance. Now, may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      #PLAN 3 WITH FLOOD INSURANCE ROUNDS 1-10
      for x in range(10):
        print()
        print()
        print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
        choice = scenarios()
        print(choice)
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 1
        if choice == scenariosList[0]:
          youPaid = youPaid + premium3 + floodPrem + deductible3
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 2
        elif choice == scenariosList[1]:
            youPaid = youPaid + premium3 + floodPrem + deductible3
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
      #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 3
        elif choice == scenariosList[2]:
          print("\nYou purchased flood insurance, so your damages will be covered!")
          youPaid = youPaid + premium3 + floodPrem + floodDed
          amountLeft = amountLeft - youPaid
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 4
        elif choice == scenariosList[3]:
            youPaid = youPaid + premium3 + floodPrem + deductible3
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 5
        elif choice == scenariosList[4]:
          youPaid += premium3 + floodPrem
          amountLeft = amountLeft - youPaid + gain5
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 6
        elif choice == scenariosList[5]:
          youPaid += premium3 + floodPrem
          amountLeft = amountLeft - youPaid + gain6
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 7
        elif choice == scenariosList[6]:
          youPaid += premium3 + floodPrem
          amountLeft = amountLeft - youPaid + gain7
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
        #PLAN 3 WITH FLOOD INSURANCE IN SCENARIO 8
        else:
          youPaid += premium3 + floodPrem
          amountLeft = amountLeft - youPaid + gain8
          print(f"\nRemaining balance: ${amountLeft}")
          print(f"You paid: ${youPaid}")
          youPaid = 0
          enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
  #PLAN 3 WITHOUT FLOOD INSURANCE
  else:
    print("\nOkay, now may let the scenarios begin!")
    enter2 = input("\nPress the ENTER key to continue. ")
    if enter2 == "":
      print()
      #PLAN 3 WITH FLOOD INSURANCE ROUNDS 1-10
      for x in range(10):
          print()
          print()
          print(f"\nROUND {x+1} (or AKA MONTH {x+1})")
          choice = scenarios()
          print(choice)
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 1
          if choice == scenariosList[0]:
            youPaid = youPaid + premium3 + deductible3
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 2
          elif choice == scenariosList[1]:
            youPaid = youPaid + premium3 + deductible3
            amountLeft = amountLeft - youPaid  
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0            
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 3
          elif choice == scenariosList[2]:
            print("\nUnfortunately, you didn't purchase flood insurance, so the damages won't be covered by insurance :(")
            youPaid = youPaid + cost3 + premium3
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print("***YOU ARE IN MAJOR DEBT***")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 4
          elif choice == scenariosList[3]:
            youPaid = youPaid + premium3 + deductible3
            amountLeft = amountLeft - youPaid
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 5
          elif choice == scenariosList[4]:
            youPaid += premium3 
            amountLeft = amountLeft - youPaid + gain5
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 6
          elif choice == scenariosList[5]:
            youPaid += premium3 
            amountLeft = amountLeft - youPaid + gain6
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 7
          elif choice == scenariosList[6]:
            youPaid += premium3 
            amountLeft = amountLeft - youPaid + gain7
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
          #PLAN 3 WITHOUT FLOOD INSURANCE IN SCENARIO 8
          else:
            youPaid += premium3 
            amountLeft = amountLeft - youPaid + gain8
            print(f"\nRemaining balance: ${amountLeft}")
            print(f"You paid: ${youPaid}")
            youPaid = 0
            enter3 = input("\nPress the ENTER key to continue. ")
      print(f"\nFINAL BALANCE: ${amountLeft}")
      if amountLeft > 0:
        print("\nGreat job! You kept your bank account stable!")
      else:
        print("\nUnfortunately, you did not keep your bank account stable :(")
