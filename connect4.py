class Board:

    def __init__(self, height, width):
        '''constructs a new board object by initializing the following three attributes'''

        self.height = height

        self.width = width

        self.slots = [[' '] * width for row in range(self.height)]

#2

    def __str__(self):

        """ Returns a string representation for a Board object.

        """

        s = ''         # begin with an empty string



    

        for row in range(self.height):

            s += '|'   # one vertical bar at the start of the row



            for col in range(self.width):

                s += self.slots[row][col] + '|'



            s += '\n'  # newline at the end of the row

        for row in range(1):

            for col in range(self.width):

                s += '--'

            s+= '-'

            s+= '\n'

        for row in range(1):

            for col in range(self.width):

                s += ' ' + str(col)

           

            s+= '\n'

    # Add code here for the hyphens at the bottom of the board

    # and the numbers underneath it.





        return s

#3

    def __repr__(self):

        """ returns string representing the called Board object  """

        return str(self)       # calls our __str__



#4

    def add_checker(self, checker, col):

        """ adds a checker x or o to specified column on the board

        """

        assert(checker == 'X' or checker == 'O')

        assert(col >= 0 and col < self.width)



        if self.slots[0][col] == ' ':

            for i in range(self.height):

                

                if self.slots[i][col] =='X' or self.slots[i][col]== 'O':

                    self.slots[i-1][col] = checker

                    break

            if self.slots[-1][col] == ' ':

                self.slots[-1][col] = checker

            

#5

    def clear(self):
        '''clears the board'''

        for r in range(self.height):

            for c in range(self.width):

                 self.slots[r][c] = ' '





#6



    def add_checkers(self, colnums):

        """ takes in a string of column numbers and places alternating

        checkers in those columns of the called Board object, 

        starting with 'X'.

        """

        checker = 'X'   # start by playing 'X'



        for col_str in colnums:

            col = int(col_str)

            if 0 <= col < self.width:

                self.add_checker(checker, col)



        # switch to the other checker

            if checker == 'X':

                checker = 'O'

            else:

                checker = 'X'



#7

    def can_add_to(self, col):
        '''returns true if it is valid to place a checker in column col on calling board object
    
        or it will return false'''
        if col not in range(self.width):

            return False


        elif self.slots[0][col] != ' ':

            return False
        

        else:

            return True



#8

    def is_full(self):
        '''returns True if the called Board object is completely full of checkers,
        and returns False otherwise'''
        

        for c in range(self.width):

             if self.can_add_to(c)==True:

                 return False

        return True

#9

    def remove_checker(self, col):
        '''removers top checker from column col of called Board object'''
        for i in range(self.height):
            if self.slots[i][col] =='X' or self.slots[i][col]== 'O':
                self.slots[i][col]=' '
                break

#10
    #helper function
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        for row in range(self.height):
            for col in range(self.width - 3):
            # Check if the next four columns in this row
            # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    
    # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self,checker):
        '''Checks for a vertical win for the specified checker.'''

        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col] == checker and \
                   self.slots[row+2][col] == checker and \
                   self.slots[row+3][col] == checker:
                    return True
        return False

    
    def is_up_diagonal_win(self, checker):
        '''Accepts a parameter checker that is either X or O and returns True if there
        there are four consecutive slots containing checkers on the board going up diagonally'''
        for row in range(self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True
        return False        

 
    
    def is_down_diagonal_win(self, checker):
        '''Accepts a parameter checker that is either X or O and returns True if there
        there are four consecutive slots containing checkers on the board going down diagonally'''
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True
        return False

    def is_win_for(self,checker):
        '''accepts a parameter checker that is either x or o and returns True
        if there are four consecutive slots containing checker on the board'''
        assert(checker == 'X' or checker == 'O')
        if self.is_horizontal_win(checker)==True:
            return True
        elif self.is_vertical_win(checker)==True:
            return True
        elif self.is_up_diagonal_win(checker)==True:
            return True
        elif self.is_down_diagonal_win(checker)==True:
            return True
        else:
            return False




    # Write your Player class below.

#1
class Player:
    def __init__(self,checker):
        '''constructs a new Player object by initializing the following attributes'''
        assert(checker == 'X' or checker == 'O')
        self.checker= checker
        self.num_moves=0

#2
    def __str__(self):
        '''returns a string representing a Player object'''
        s='Player'+' '+(self.checker)
        return s

#3
    def __repr__(self):
        '''returns a string representing a Player object'''
        return str(self) 
#4
    def opponent_checker(self):
        '''returns one_character string representing the checker'''
        if self.checker=='X':
            return 'O'
        else:
            return 'X'

#5
    def next_move(self,board):
        '''accepts a Board object as a parameter and returns the column
        where the player wants to make the next move'''
        self.num_moves += 1
        while True:
             col = int(input('Enter a column: '))
             if board.can_add_to(col):
                 return col
             else:
                 print('Try again!')
             
 # if valid column index, return that integer
 # else, print 'Try again!' and keep looping
