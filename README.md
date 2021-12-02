# BubbleTea-Class
The BubbleTea class models the real life object of a cup of bubble tea. It's inspired by a customers ability to make adjustments to their  drink at a boba shop. The user can input variables to customize the size, tea type, sweetness level, ice level, and topping of the bubble tea.  The contents in the drink can be fully customizeable through the five input variables. The user is given the creative liberty to create their very own cup of bubble tea. 

Description of Classes and Data Variables: -------------------------------------------------------------------------------------------------

class BubbleTea: The BubbleTea class is a single class meant to represent a cup of bubble tea. It takes in user input and its methods 
store information about the drink and can make adjustments to it. 

variables:
size: Represents the size of the drink. Users can decide whether they want a small or a large.  
tea:  Represents the tea of the drink. Users can choose whatever tea type they desire. 
sweetness: Represents the sweetness level of the drink and is entered in as a percentage. The percentages they choose can be 100%, 75%, 50%, 25%, or 0%
ice: Represent the ice level of the drink and is also entered in as a percentage. The ice levels should be 100%, 75%, 50%, 30%, or 0%
topping:  The user can enter any topping of choice - boba, lychee jelly, pudding, grass jelly, etc. This will be the topping portion of the cup of boba.

order: This variable is created within the class __init__ method. It's meant to call the receipt method and make its dictionary accessable throughout the class.

Description of Methods:--------------------------------------------------------------------------------------------------------------------

__init__(self, size, tea, sweetness, ice, topping): 
Takes in inputs of the drinks size, tea type, sweetness level, ice level, and topping from the main method and stores the inputs as private
data variables used throughout the class. Also creates a variable receipt which calls the receipt() method in the class to access its dictionary.

receipt(self): Method takes in self argument and organizes contents of drink into a dictionary - the dictionary acting as a description/receipt.
The keys of the dictionary are size, tea type, sweetness, ice, and topping, the values are the private variables in that order. The method 
returning the dictionary

get_size(self): Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It searches through the dictionary to obtain the key and value of the drinks size and returns a string containing its size.

get_tea(self):  Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It searches through the dictionary to obtain the key and value of the tea type and returns a string describing the drinks percentage 
of sweetness.

get_sweetness(self): Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It searches through the dictionary to obtain the key and value of the sweetness level and returns a string describing the drinks percentage 
of sweetness.

get_ice(self): Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It searches through the dictionary to obtain the key and value of the ice level and returns a string describing the drinks percentage 
of ice.

get_topping(self): Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It searches through the dictionary to obtain the key and value of the drinks topping and returns a string describing the drinks topping.

size_upgrade(self): Method takes in the self argument and uses it to call the receipt variable to obtain the drinks dictionary of contents. 
It calls the dictionary (receipt) key "size" to replace its previous size with a large. It will return the updated dictionary. 

main(): The main method greets user with a welcome message and asks them to input variables for their drink. The variables will be entered
into the class to create the cup of bubble tea. It will then ask them questions and depending on the users response, it'll call the get and 
additional methods.

DEMO PROGRAM DOCUMENTATION:

Demo Program Description: 

Demo and Instructions: 
The demo program will act as a cashier in a boba shop. They will ask the user questions regarding what they want in their drink and have them 
input the information into the class to build the drink. This will be the users first interaction with the BubbleTea class.
The demo program will then ask the a user questions regarding the information they want to access about their drink. This is how the 
user will interect with the get classes. If the size of their drink is a "small", the user will be asked if they want an upgrade to a "large". 
If they respond "yes", changes will be made to the size of their final order. They will then be asked if they would like to review specific 
contents of their order. If they respond with "yes" it will ask them what they would like to review. For example if they type in tea, it will
give them the tea type in a string. If they respond "no", they will just be given a receipt. The inputs they can enter are tea, size, ice level, 
sweetness level, and topping. Once done with reviewing their order, they will be given a receipt of their finalized cup of boba. 

Where to Run Program:
The user can run the program on their console. If running through the terminal it should start running when opened, if being run through code
editor - the program should start running after run is pressed. 
