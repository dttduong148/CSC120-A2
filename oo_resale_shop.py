from typing import Dict, Union
from computer import Computer
class ResaleShop:
        
    # What attributes will it need?
    inventory: list
    # Dict[int, Dict[str, Union[str, int, bool]]] = {}

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    
    def buy(self, 
            description, 
            processor_type, 
            hard_drive_capacity, 
            memory, 
            operating_system,
            year_made,
            price) -> None:
        
        computer = Computer(description, 
            processor_type, 
            hard_drive_capacity, 
            memory, 
            operating_system,
            year_made,
            price)
        # self.itemID += 1
        self.inventory.append(computer)
        print (f"Item added: {computer.description}, {computer.processor_type}, {computer.hard_drive_capacity}, {computer.memory}, {computer.operating_system}, {computer.year_made}, {computer.price}")
    def sell(self, itemID) -> None:
        if itemID in range(len(self.inventory)): 
            computer = self.inventory[itemID]
            self.inventory.pop(itemID)
            print(f"Item {itemID} is sold! Details: {computer.description}, {computer.processor_type}, {computer.hard_drive_capacity}, {computer.memory}, {computer.operating_system}, {computer.year_made}, {computer.price}")
        else: 
            print("Item", itemID, "not found. Please select another item to sell.")

    def print_inventory(self) -> str:
        print("-" * 21)
        print("MY INVENTORY")
        print("-" * 21)
        for itemID in range(len(self.inventory)):
            computer = self.inventory[itemID]
            print("Item", itemID, ":", computer.description, 
                  computer.processor_type,
                  computer.hard_drive_capacity,
                  computer.memory,
                  computer.operating_system,
                  computer.year_made,
                  computer.price )

def main():
    my_shop = ResaleShop()
    my_shop.buy("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    my_shop.buy("Mac Air (2020)",
        "M1",
        1024, 64,
        "macOS Monterey", 2020, 1800)
    
    my_shop.sell(1)
    
    my_shop.print_inventory()


    
main()



