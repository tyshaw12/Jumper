from game.word import words_list

class display:
    def __init__(self) -> None:
        self.misses = 0
        self.progress = []
        self.word = words_list.get_word()
        

    def guy(self):
        while len(self.progress) < len(self.word):
            self.progress.append('_')
        print(self.progress)

    def parachute(self):
        if self.misses < 1:
            print( "  ___")
        if self.misses < 2:
            print(' /___\ ')
        if self.misses < 3:
            print(' \   /')
        if self.misses < 4:
            print('  \ /')
            print('   O')
            print('  /|\ ')
            print('  / \ ')
            print()
            print('^^^^^^^')
        else:
            print('   x')
            print('  /|\ ')
            print('^^^^^^^')
            print('You died')
            print(f'The word was "{self.word}". ')

    def check_guess(self, letter):
        correct = False
        for i in range(len(self.word)):
            if letter == self.word[i]:
                self.progress[i] = letter
                correct = True
        if correct != True:
            self.misses += 1

    def not_dead(self):
        if self.misses > 3:
            return False
        else:
            return True

    def check_win(self):
        if '_' not in self.progress:
            print(' \ O /')
            print('   | ')
            print('  / \   ')
            return True
        else:
            return False