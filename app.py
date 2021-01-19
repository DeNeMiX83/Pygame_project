from data.config import *
from menu.game_over import game_over
from game_things import info
from menu.game_pause import game_pause
from sprites.config import all_sprites, player_sprites
from sprites.funk.game import create_meteor, get_space_ship
from menu.start_menu import start_screen


def check_event():
    global running, player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_pause():
                    player = get_space_ship(info['ship_type'])
        player_sprites.update(event)
    all_sprites.update()


if __name__ == '__main__':
    size = width, height = size
    start_screen()
    pygame.mouse.set_visible(False)
    player = get_space_ship(info['ship_type'])
    running = True
    clock = pygame.time.Clock()
    create_meteor()
    while running:
        check_event()
        screen.fill((0, 0, 0))
        if not player.alive():
            game_over()
            player = get_space_ship(info['ship_type'])
        all_sprites.draw(screen)
        create_meteor()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
