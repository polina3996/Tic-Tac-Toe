import tkinter
import random


class TicTacToeCanvas(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.nullify_state()
        self.game_field = {0:(0,0), 1:(1,0), 2:(2,0), 3:(0,1), 4:(1,1), 5:(2,1), 6:(0,2), 7:(1,2), 8:(2,2)}
        self.pack()  
        self.start_game()        
           
    def nullify_state(self):
        self.state = [None,None,None,None,None,None,None,None,None]
        
    #processing of clicking on canvas method
    def click(self, event):
        if not self.is_game_started:
            self.handle_select_symbol(event)
            return
        if (self.get_winner()):
            self.delete('all') 
            self.start_game()
            return
        x = event.x  
        y = event.y 
        column = x // 100
        row = y // 100 
        i = column + row*3 
        if self.state[i] != None:
            return 
        self.state[i] = self.player_symbol
        self.draw_player_symbol(column, row)
        result = self.get_winner()
        if result == None:
            self.bot_move()
            result = self.get_winner()
        if result != None:
            self.create_text(150, 150, text=f"{result}. Click anywhere on the field to start a new game", fill='blue')
            return
    
    def start_game(self):
        self.nullify_state()     
        self.delete('all')
        self.update()
        self.draw_x(0, 1)
        self.draw_o(2, 1)
        self.draw_lines()
        self.bind('<Button-1>', self.click) 
        self.is_game_started = False
        self.create_text(150, 150, text=f"Please select X or O", fill='blue')      
       
    def get_empty_cells_indexes(self):
        list_of_indexes = []
        for index, i in enumerate(self.state):
            if i == None:
                list_of_indexes.append(index)
        return list_of_indexes        
    
    def bot_move(self): 
        list_of_indexes = self.get_empty_cells_indexes()
        random_index = random.choice(list_of_indexes) 
        self.state[random_index] = self.bot_symbol
        column, row = self.game_field[random_index]
        self.draw_bot_symbol(column, row) 
    
    def handle_select_symbol(self, event):
        x = event.x  
        y = event.y 
        column = x // 100
        row = y // 100
        if column == 0 and row == 1:
            self.draw_player_symbol = self.draw_x 
            self.draw_bot_symbol = self.draw_o
            self.player_symbol = 'X'
            self.bot_symbol = 'O'
            self.is_game_started = True
            self.delete('all')
            self.update()                
            self.draw_lines()
        elif column == 2 and row == 1:
            self.draw_player_symbol = self.draw_o
            self.draw_bot_symbol = self.draw_x
            self.player_symbol = 'O'
            self.bot_symbol = 'X'
            self.is_game_started = True
            self.delete('all')                
            self.update()                
            self.draw_lines()
        
    #drawing the lines dividing the field into cells
    def draw_lines(self):
        self.create_line(100, 0, 100, 300, fill='grey')
        self.create_line(200, 0, 200, 300, fill='grey')
        self.create_line(0, 100, 300, 100, fill='grey')
        self.create_line(0, 200, 300, 200, fill='grey')   
     
    def draw_x(self, column, row): 
        self.create_line(column*100, row*100,column*100 + 100,row*100 + 100, width=5, fill='green')
        self.create_line(column*100,row*100 + 100,column*100 + 100,row*100,width=5, fill='green')    
      
    def draw_o(self, column, row): 
        self.create_oval(column*100,row*100,(column*100) + 100,(row*100) + 100, width=5, outline='red')    
   
    def get_winner(self):
        winner_combinations = [
        {0,1,2},
        {3,4,5},
        {0,3,6},
        {6,7,8},
        {1,4,7},
        {2,5,8},
        {0,4,8},
        {2,4,6}]
        for winner_combination in winner_combinations:
            conditions = []
            for i in winner_combination:
                condition = self.state[i]
                conditions.append(condition)
            if conditions == ['X', 'X', 'X']:
                return 'X wins!'
            elif conditions == ['O', 'O', 'O']:
                return 'O wins!'
        for i in self.state:
            if i == None:
                return None 
        return 'draw'        
     