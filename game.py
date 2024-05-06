import pygame
import pytmx
import pyscroll

from player import Player


class Game:

    def __init__(self):

        # game window
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Wiredcore")

        # loading map (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generate player
        self.player = Player(30, 0)

        # drawing group
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):

        # game loop
        running = True

        while running:

            self.group.update()
            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()