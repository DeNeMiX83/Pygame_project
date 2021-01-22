from data.config import *
from game import game_things
from game.menu.game_over import game_over
from game.game_things import info
from game.menu.game_pause import game_pause
from sprites.config import all_sprites, player_sprites
from game.funk.game import create_meteor, get_space_ship, view_koins, view_score
from game.menu.start_menu import start_screen


def check_event():
    global running, player
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_pause():
                    player = get_space_ship(info['ship_type'])
        if event.type == chek_score_event:
            game_things.game_score += 1
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
    game_things.game_score = 0
    while running:
        check_event()
        screen.fill((0, 0, 0))
        if not player.alive():
            game_over()
            start_screen()
            game_things.game_score = 0
            player = get_space_ship(info['ship_type'])
        all_sprites.draw(screen)
        view_koins(0.008, 0.95, font_size=30, x_center=False)
        view_score(0.008, 0.90, font_size=30, x_center=False)
        create_meteor()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
