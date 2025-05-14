class Player:
    def __init__(self):
        self.name = " "
        self.symbol = " "
    def choose_name(self):
        while  True:
           name = input("Enter your name (leetr onle: ")
           if name.isalpha():
               self.name = name
               break
           print("Name must contain only letters")
    def choose_symbol(self):
        while True:
            symbol = input("Enter your symbol (x or o): ")
            if symbol.isalpha() and  len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Symbol must be a single letter (x or o)")




