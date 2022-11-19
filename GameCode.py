import tkinter
import random
import time

class TicTacToe(tkinter.Canvas):
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.nullify_state()
        self.game_field = {0:(0,0), 1:(1,0), 2:(2,0), 3:(0,1), 4:(1,1), 5:(2,1), 6:(0,2), 7:(1,2), 8:(2,2)}
        self.pack()
        self.draw_lines()
        self.bind('<Button-1>', self.click)    
   
    def nullify_state(self):
        self.state = [None,None,None,None,None,None,None,None,None]
        
    #processing of clicking on canvas method
    def click(self, event):
        x = event.x  
        y = event.y 
        column = x // 100
        row = y // 100 
        i = column + row*3 
        
        if self.state[i] != None:
            return 
        self.state[i] = 'x'
        self.draw_x(column, row)
        result = self.get_winner()
        if result == None:
            self.bot_move()
            result = self.get_winner()
        if result != None:
            self.create_text(150, 150, text=result, fill='blue')
            time.sleep(2)
            self.delete('all') 
            self.restart_game()            
    
    def restart_game(self):
        self.nullify_state()
        self.create_text(150,150,text='restarting game...',fill='blue')
        time.sleep(2)
        self.delete('all')
        self.update()
        self.draw_lines()        
       
    def get_empty_cells_indexes(self):
        list_of_indexes = []
        for index, i in enumerate(self.state):
            if i == None:e
                list_of_indexes.append(index)
        return list_of_indexes        
    
    def bot_move(self): 
        list_of_indexes = self.get_empty_cells_indexes()
        random_index = random.choice(list_of_indexes) 
        self.state[random_index] = 'o' 
        column, row = self.game_field[random_index]
        self.draw_o(column, row) 
        
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
            if conditions == ['x', 'x', 'x']:
                return 'x_win'
            elif conditions == ['o', 'o', 'o']:
                return 'o_win'
        for i in self.state:
            if i == None:
                return None 
        return 'draw'        
            
            
tk_window = tkinter.Tk()
game = TicTacToe(tk_window)


game.mainloop()
