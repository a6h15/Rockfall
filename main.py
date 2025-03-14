import pyxel

class GameWindow:
    def __init__(self):
        pyxel.init(160,120,title="BOmBs")
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_GRAY)
        pyxel.text(70,60,"Start",pyxel.COLOR_BLACK)


game = GameWindow()