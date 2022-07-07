class guess:
    def __init__(self):
        self.user_guess = ""
        
    def user_input(self):
        self.user_guess = False
        while self.user_guess is False:
            letter = input("Pick a letter [a-z]: ")
            self.user_guess = letter.isalpha()
            if self.user_guess is True:
                return letter
            
        
        
        