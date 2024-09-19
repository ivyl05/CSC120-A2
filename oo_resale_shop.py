"""
        Filename: oo_resale_shop.py
        Description: An OOP code to run a small computer resale shop. 
        Author: Ivy Li
        Date: 19 September 2024
       
"""

from computer import * 

"""
    class ResaleShop does all the action that associates withe the shop
"""
class ResaleShop:
    
    """
        Attributes
        inventory is a dictionary that stores int and dict
        itemID is a int, representing the computer ID
    """
    from typing import Dict, Optional
    from computer import Computer
    inventory : Dict[int, Dict] = {}
    itemID = int

    """
        Contructor (does not take in anything)
    """ 
    def __init__(self):
         self.inventory= {}
         self.itemID = 0

    """
        Method
        It takes in a computer and add the computer to the Shop's inventory.
    """
    def buy(self, computer: Computer): 
        self.itemID += 1
        self.inventory [self.itemID] = computer


    """
        Method
        It takes in an itemID and a new price and updates the price of the computer. 
        If the computer is not found, it prints a error message. 
    """
    def update_price(self, item_id: int, new_price: Optional[int]=None): 
        self.new_price = new_price
        if self.itemID is not None:
            self.inventory [self.itemID].price = new_price
        else:
            print("Item", self.itemID, "not found. Cannot update price")
            

    """
        Method
        It takes in an itemID and sells that computer and removes it from the inventory. 
        If the computer is not found, it prints a error message. 
    """    
    def sell(self, item_id: int):
         if self.itemID is not None:
          print("Item", self.itemID, "sold!")
          del self.inventory [self.itemID]
         else:
             print("Item", self.itemID, "not found. Please select another item to sell.")
            
   
    """
        Method
        It takes in an itemID, a new os, and set the price base on how old the computer is. 
        It updates the computer to the new os if a new os is entered, or else it prints error message. 
    """    
    def refurbish (self, itemID: int, new_os: Optional[str] = None):

        self.itemID = itemID
        self.new_os = new_os
        item = self.inventory[self.itemID]
        if item.year < 2000:
             item.price =0
        elif item.year <2012:
            item.price =250
        elif item.year <2018:
            item.price =550
        else:
            item.price =1000
    
        if self.new_os is not None:
            item.operating_system = new_os
        else:
            print("Item", self.itemID, "not found. Please select another item to refurbish.")
            


def main():

    # Banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
         "macOS Big Sur", 2013, 1500)
    
    Shop=ResaleShop()
    
    # Buy a computer
    print("Buying", computer.description)
    print("Adding to inventory...")
    Shop.buy(computer)
    print("Done.\n")

    # Checking inventory
    print("Checking inventory...")
    print (Shop.itemID)
    print("{description:", computer.description, "processor_type:",computer.processor_type, "hard_drive_capacity:", computer.hard_drive_capacity, "memory:", computer.memory, "operating_system:", computer.operating_system, "year_made:", computer.year, "price:", computer.price, "}")
    print("Done.\n")

    # Upadate price 
    new_price = 1000
    Shop.update_price(Shop.itemID, new_price)
    print("Update price Item ID:", Shop.itemID, ", updating price to", new_price)
    print("Done.\n")

    # Checking inventory
    print("Checking inventory...")
    print("{description:", computer.description, "price:", computer.price, "}")
    print("Done.\n")
    

    # Refurbish
    new_OS = "MacOS Monterey"
    #new_OS = None
    print("Refurbishing Item ID:", Shop.itemID, ", updating OS to", new_OS)
    Shop.refurbish(Shop.itemID, new_OS)
    print("Done.\n")

    # Checking inventory
    print("Checking inventory...")
    print("{description:", computer.description,  "operating_system:", computer.operating_system, "price:", computer.price, "}")
    print("Done.\n")
    
    # Sell the computer
    print("Selling Item ID:", computer.description)
    Shop.sell(computer)
    
    # Checking inventory
    print("Checking inventory...")
    print (Shop.inventory)
    print("Done.\n")

if __name__ == "__main__":
    main()