"""
        Filename: computer.py
        Description: An OOP code for the class Computer 
        Author: Ivy Li
        Date: 19 September 2024
       
"""

"""
    class ResaleShop does all the action that associates withe the computer itself
"""
class Computer:

    """
    attributes
    """
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year: int
    price: int

    """
    Contructor
    It takes in all the attributes, which are the details of a computer. 
    """
    def __init__(self, description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year: int,
                    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year = year
        self.price = price

    

def main():
    
    #make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    print(computer.description)


if __name__ == "__main__":
    main()