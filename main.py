MENU = {
  "espresso": {
      "ingredients": {
          "water": 50,
          "milk" : 0,
          "coffee": 18,
      },
      "cost": 1.5,
  },
  "latte": {
      "ingredients": {
          "water": 200,
          "milk": 150,
          "coffee": 24,
      },
      "cost": 2.5,
  },
  "cappuccino": {
      "ingredients": {
          "water": 250,
          "milk": 100,
          "coffee": 24,
      },
      "cost": 3.0,
  }
}

resources = {
  "water": 300,
  "milk": 200,
  "coffee": 100,
}

def start_machine():
    new_resources=resources
    #print(f"current resource in the coffee machine are ={new_resources}")
    while new_resources["water"] >= 0 and new_resources["milk"] >= 0 and new_resources["coffee"]>=0:
    
    
        # Ask the user what they want to drink
        
        print("What do you want to get?")
        print("espresso, latte, cappuccino, or do you like to get a machine report?")
    
        # Save the user input in a variable
        
        userchoice = input()
    
        if userchoice == "report" or userchoice== "off":
            break
    
        
        # Check if there are enough resources for the user request
        def check_resources(userchoice):
                water_consumption=int(MENU[userchoice]["ingredients"]["water"])
                milk_consumption=int((MENU[userchoice]["ingredients"]["milk"]))
                coffee_consumption=int((MENU[userchoice]["ingredients"]["coffee"]))
                beverage_cost=float((MENU[userchoice]["cost"]))
                return [water_consumption, milk_consumption, coffee_consumption, beverage_cost]
            
        
        # Define the remaining resources after the user has selected a drink
        
        def remaining_resources(userchoice):
            beverage_consumption=check_resources(userchoice)
            new_resources["water"]=new_resources["water"]-beverage_consumption[0]
            new_resources["milk"]=new_resources["milk"]-beverage_consumption[1]
            new_resources["coffee"]=new_resources["coffee"]-beverage_consumption[2]
            return new_resources
    
    
        #Get the user coins and calculate the total deposited amount
    
        def input_coin():
            print("Please insert coins")
            quarters=int(input("How many quarters?: "))
            dimes=int(input("How many dimes?: "))
            nickles=int(input("How many nickles?: "))
            pennies=int(input("How many pennies?: "))
            total_dollar_amount=quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
            return total_dollar_amount
    
        # Check if the user has enough money to purchase the drink and if not, refund the money
        # If the user has enough money, calculate the change and make the drink
    
        def check_price(coffeechoice):
            if user_dollar_input<MENU[userchoice]["cost"]:
                print(f"You do not have enough money and your ${user_dollar_input} is refunded")
            elif user_dollar_input>MENU[userchoice]["cost"]:
                refunded_amount= user_dollar_input - MENU[coffeechoice]["cost"] 
                print(f"Your refund is {refunded_amount}")
    
        # Compare the resources available in the machine against the user request
        # Calculate remaining resources after the purchase
        # Print the remaining resources after the purchase
        
        user_drink=check_resources(userchoice)
        if user_drink[0] > new_resources["water"]:
            print("Sorry there is not enough water")
        if user_drink[1] > new_resources["milk"]:
            print("Sorry there is not enough milk")
        if user_drink[2] > new_resources["coffee"]:
            print("Sorry there is not enough coffee")
        if user_drink[0] <= new_resources["water"] and user_drink[1] <= new_resources["milk"] and user_drink[2] <= new_resources["coffee"]:
            print(f"The water, milk, coffee, and price needed for this drink are : {user_drink}")
            
            if new_resources["water"]==0:
                print("Machine doesn't have any more water")
                break
            elif new_resources["milk"]==0:
                print("Machine doesn't have any more milk")
                break
            elif new_resources["coffee"]==0:
                print("Machine doesn't have any more coffee")
                break
            user_dollar_input=input_coin()
            if user_dollar_input>int(MENU[userchoice]["cost"]):
                new_resources=remaining_resources(userchoice)
                print(f"The user input to the coffee machine is, {user_dollar_input}")
                print(f"The remaining resources after your purchase are {new_resources}")
            else:
                check_price(userchoice)
    
    # Print a message to the user that the machine is out of resources when he makes a selection
    
    
    # Print a report of the remaining resources in the machine if the user asks for it
    if userchoice=='report':
        print(f"The water,milk, and coffee resources remaining in the machine are: {new_resources}")
    
    # Print a message telling the user that the machine is off
    
    if userchoice=='off':
        print("The machine is now off")

    start_machine()

 
            
        
        
 
    
    


start_machine()
