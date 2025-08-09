from src.process import draw_process
from src.process import init_game
from src.process import destroy_game
from src.process import input_process
from lifecycle import game_state
from lib.render import render
from lib.prompt import action

if __name__ == "__main__":
    init_game()
    
    while game_state.is_running:
        draw_process()
        render()
        input_process(action())
        
    destroy_game()
