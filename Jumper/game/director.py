from game.word import words_list
from game.terminal_service import display
from game.guesser import guess


class director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        word: gives a random word
        is_playing (boolean): Whether or not to keep playing.
        guesser: The game's guesser. 
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """The class constructor.
     
        Args:
        self (Director): an instance of Director.
        """
        self.is_playing = True
        self.word_list = words_list()
        self.display = display()
        self.guesser = guess()


    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
                self.get_inputs()
                self.do_updates()
                self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means Dealing the card.
        Args:
        self (Director): An instance of Director.
        """
        self.display.guy()
        self.display.parachute()
        choice = self.guesser.user_input()
        self.display.check_guess(choice)



    def do_updates(self):
        self.is_playing = self.display.not_dead()


    def do_outputs(self):
        """Outputs game information. 
        Here it outputs the parachute and 
        Args:
        self (Director): An instance of Director.
        """
        if self.is_playing == False:
            self.display.parachute()

        if self.display.check_win():
            print("You landed safely! ")
            self.is_playing = False