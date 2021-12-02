#Jasmine Liang
#11/29/21
#Assignment 10.1 Custom Class
#File: Boba_Class.py
#Purpose: Create class modeling a real world object. This class will model a bubble tea drink and its characteristics. 

#Class variable
#Class will represent a cup of bubble tea
class BubbleTea: 
    #data variables
    #takes in input from main method
    def __init__(self, size, tea, sweetness, ice, topping):
        #data variables
        #size of the drink
        self.size = size 
        #type of tea
        self.tea = tea
        #level of sweetness
        self.sweetness = sweetness
        #ice level
        self.ice = ice 
        #typf of topping
        self.topping = topping
        #call the receipt class to make dictionary that is accessible throughout class
        self.order = self.receipt()

    #organizes contents of drink into a dictionary to create a receipt
    def receipt(self):
        #sets each content to a dictionary key and user input as a value
        drink_contents = {"size": self.size, "tea": self.tea, "sweetness": self.sweetness, "ice": self.ice, "topping": self.topping}
        return drink_contents

    #function searches through dictionary and returns string of the size of the drink
    def get_size(self):
        #calls key to return value 
        drink_size = self.order["size"]
        #return in string form
        size_string = (f"Your drink is a size {drink_size}.")
        return size_string


    #function searches through dictionary and returns a string describing the drinks tea type 
    def get_tea(self):
        #calls key to return value
        drink_tea = self.order["tea"]
        #return in string form
        tea_string = (f"You ordered a {drink_tea}.")
        return tea_string
    
    #function searches through dictionary and returns a string describing the drinks percentage of sweetness
    def get_sweetness(self):
        #calls key to return value
        drink_sweetness = self.order["sweetness"]
        #return in string form
        sweetness_string = (f"Your drink has {drink_sweetness} sweetness.")
        return sweetness_string 

    #function searches through dictionary and returns a string describing the drinks percentage of ice
    def get_ice(self):
        #calls key to return value 
        ice_percentage = self.order["ice"]
        #return in string form 
        ice_string = (f"Your drink has {ice_percentage} ice.")
        return ice_string 

    #function searches through dictionary and returns a string of drinks topping
    def get_topping(self):
        #calls key to return value 
        drink_topping = self.order["topping"]
        #return in string form
        topping_string = (f"Your drink contains {drink_topping}")
        return topping_string 
      
    #calls the dictionary key "size" to replace its previous size with a large
    def size_upgrade(self):
       return self.order["size"]["large"]
      

#main method------------------------------------------------------------------------------------------------------------------

def main():
    #Greets user with a welcome message and asks them to enter in what they want in their drink
    print("Hello! Welcome to the Boba Shop!\nPlease enter in the drink size, tea type, sweetness level, ice level, and topping to create your drink.")
    #all input should be lowercase
    #sizes avaible are small or large
    size = input("size: ")
    #user can enter any tea of their choice
    tea = input("tea: ")
    #sweetness level can be 100%, 75%, 50%, 25%, or 0%
    sweetness = input("sweetness level: ")
    #ice level be 100%, 75%, 50%, 30%, or 0%
    ice = input("ice level: ")
    #user can enter any topping of choice - boba, lychee jelly, pudding, grass jelly, etc.
    topping = input("topping: ")

    #call class to create the new cup of boba with the users input
    cup_of_boba = BubbleTea(size, tea, sweetness, ice, topping)

    #if the size is small, ask the user for an upgrade 
    if size == "small":
        question = input("Would you like to upgrade to a large for $0.50? ")
        #if answer is yes, enter in the updated information
        if question == "yes":
            size = "large"
            cup_of_boba = BubbleTea(size, tea, sweetness, ice, topping)

    #ask user if they want to review their order to access the get methods
    review_order = input("Would you like to review your order? ")
    #use a while loop until response is "no"
    #ask user what they would like to review and call methods to access information inside the drink dictionary
    while( review_order != "no"):
        what = input("What would you like to review? ")
        if what == "size":
            print(cup_of_boba.get_size())
        elif what == "tea":
            print(cup_of_boba.get_tea())
        elif what == "sweetness level":
            print(cup_of_boba.get_sweetness())
        elif what == "ice level":
            print(cup_of_boba.get_ice())
        else: 
            print(cup_of_boba.get_topping())
        review_order = input("Is there anything else you'd like to review? ")
    
    #call receipt method from class to print the receipt of the boba drink describing its contents
    print("Great! Here's a receipt of your order.")
    print(cup_of_boba.receipt())

    #depending on size return exit message and price
    if size == "small":
        print("Your order will be $5.00. Thank you and enjoy!")
    else: 
        print("Your order will be $5.50. Thank you and enjoy!")

if __name__ == "__main__":
    main()

