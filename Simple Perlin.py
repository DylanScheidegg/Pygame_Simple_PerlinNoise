from noise import snoise2
import pygame

width = 1280
height = 720
window = pygame.display.set_mode((width, height))


class GameMap(object):
    def __init__(self, map_width, map_height):
        self.block_size = 8
        self.map_width = map_width // self.block_size
        self.map_height = map_height // self.block_size
        self.scl = 0.1

    def create(self):
        f = open('game.txt', 'w')

        arrx = []
        xcor = 0
        for x in range(self.map_width):
            ycor = 0
            arry = []
            for y in range(self.map_height):
                val = int(abs(snoise2(x * self.scl, y * self.scl) * 255))
                f.write(str(val) + ',')
                print(val)
                arry.append(val)
                ycor += self.block_size
            f.write('\n')
            arrx.append(arry)
            xcor += self.block_size
        return arrx

    def draw(self, garr):
        xcor = 0
        for x in garr:
            ycor = 0
            for y in x:
                pygame.draw.rect(window, (y, y, y), (xcor, ycor, self.block_size, self.block_size))
                ycor += self.block_size
            xcor += self.block_size


game_map = GameMap(width, height)
gmap = game_map.create()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
            quit()

    game_map.draw(gmap)
    pygame.display.update()
