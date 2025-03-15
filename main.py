import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120

class GameWindow:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="BOmBs")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT *4//5
        self.heart_x = SCREEN_WIDTH //2
        self.heart_y = 0
        self.isCollision = False
        pyxel.run(self.update,self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH -12:
            self.player_x += 1
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
            self.player_x -= 1

        if self.heart_y < SCREEN_HEIGHT:
            self.heart_y += 1
        if (self.player_x <= self.heart_x <= self.player_x + 8 and
            self.player_y <= self.heart_y <= self.player_y +8):
            self.isCollision = True

    def draw(self):
        pyxel.cls(pyxel.COLOR_GREEN)
        pyxel.blt(self.heart_x,self.heart_y,0,8,0,8,8,pyxel.COLOR_BLACK)
        pyxel.blt(self.player_x, self.player_y,0,16,0,16,16,pyxel.COLOR_BLACK)

        if self.isCollision:
            pyxel.text(SCREEN_WIDTH //2 - 15,SCREEN_HEIGHT//2,"GAME OVER",pyxel.COLOR_ORANGE)

game = GameWindow()