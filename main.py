import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
HEART_INTERVAL = 30

class heart:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def update(self):
        if self.y < SCREEN_HEIGHT:
            self.y += 1

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8, pyxel.COLOR_BLACK)


class GameWindow:
    def __init__(self):
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="BOmBs")
        pyxel.mouse(True)
        pyxel.load("my_resource.pyxres")
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT *4//5
        self.hearts = []
        self.isCollision = False
        pyxel.run(self.update,self.draw)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH -12:
            self.player_x += 1
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
            self.player_x -= 1
        if pyxel.frame_count % HEART_INTERVAL == 0:
            self.hearts.append(heart(pyxel.rndi(0,SCREEN_WIDTH -8),0))

        for Heart in self.hearts.copy():
            Heart.update()

            if (self.player_x <= Heart.x <= self.player_x + 8 and
                    self.player_y <= Heart.y <= self.player_y + 8):
                self.isCollision = True

            if Heart.y >= SCREEN_HEIGHT:
                self.hearts.remove(Heart)


    def draw(self):
        pyxel.cls(pyxel.COLOR_GREEN)
        for Heart in self.hearts:
            Heart.draw()

        pyxel.blt(self.player_x, self.player_y,0,16,0,16,16,pyxel.COLOR_BLACK)

        if self.isCollision:
            pyxel.text(SCREEN_WIDTH //2 - 15,SCREEN_HEIGHT//2,"GAME OVER",pyxel.COLOR_ORANGE)

game = GameWindow()