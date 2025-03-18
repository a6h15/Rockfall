import pyxel

SCREEN_WIDTH = 160
SCREEN_HEIGHT = 120
HEART_INTERVAL = 10
START_SCENE = "start"
PLAY_SCENE = "play"
GAME_OVER_DISPLAY_TIME = 60

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
        pyxel.init(SCREEN_WIDTH,SCREEN_HEIGHT,title="RockFall")
        pyxel.mouse(True)
        self.current_screen = START_SCENE
        pyxel.load("my_resource.pyxres")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update,self.draw)

    def reset_play_scene(self):
        self.player_x = SCREEN_WIDTH // 2
        self.player_y = SCREEN_HEIGHT * 4 // 5
        self.hearts = []
        self.isCollision = False
        self.game_over_display_timer = GAME_OVER_DISPLAY_TIME

    def update_start_scene(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.reset_play_scene()
            self.current_screen = PLAY_SCENE

    def update_play_scene(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.player_x < SCREEN_WIDTH -12:
            self.player_x += 1
        elif pyxel.btn(pyxel.KEY_LEFT) and self.player_x > -4:
            self.player_x -= 1
        if pyxel.frame_count % HEART_INTERVAL == 0:
            self.hearts.append(heart(pyxel.rndi(0,SCREEN_WIDTH -8),0))

        if self.isCollision:
            if self.game_over_display_timer >0:
                self.game_over_display_timer -= 1
            else:
                self.current_screen= START_SCENE
            return

        for Heart in self.hearts.copy():
            Heart.update()

            if (self.player_x <= Heart.x <= self.player_x + 8 and
                    self.player_y <= Heart.y <= self.player_y + 8):
                self.isCollision = True

            if Heart.y >= SCREEN_HEIGHT:
                self.hearts.remove(Heart)


    def update(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

        if self.current_screen == START_SCENE:
            self.update_start_scene()
        elif self.current_screen == PLAY_SCENE:
            self.update_play_scene()

    def draw_play_scene(self):
        pyxel.blt(0,0,0,32,120,160,120)
        for Heart in self.hearts:
            Heart.draw()

        pyxel.blt(self.player_x, self.player_y, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)

        if self.isCollision:
            pyxel.text(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2, "GAME OVER", pyxel.COLOR_ORANGE)

    def draw_start_screen(self):
        pyxel.blt(0,0,1,16,0,160,120)
        pyxel.text(SCREEN_WIDTH//2-20,SCREEN_HEIGHT//2,f"Start",pyxel.COLOR_BLACK)

    def draw(self):
        if self.current_screen == START_SCENE:
            self.draw_start_screen()
        elif self.current_screen == PLAY_SCENE:
            self.draw_play_scene()

game = GameWindow()
