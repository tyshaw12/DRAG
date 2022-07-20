import constants
screen = constants.screen
# Class to draw text and pictures 
class Draw():
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    def draw_pic(file, x, y):
        img = file
        screen.blit(img, (x,y))