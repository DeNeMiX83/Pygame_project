from data.config import *
from game import game_things
from game.menu.game_over import game_over
from game.game_things import info
from game.menu.game_pause import game_pause
from sprites.config import all_sprites, player_sprites, meteors_sprites
from game.funk.game import get_space_ship, view_koins, view_score
from game.menu.start_menu import start_screen
from sprites.environment.generate_meteors import GenerateMeteors


def check_event():
    global running, meteors_generate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                meteors_generate.pause()
                game_pause()
                meteors_generate.start()
        if event.type == chek_score_event:
            game_things.game_score += 1
        player_sprites.update(event)
    all_sprites.update()


def new_game():
    global meteors_generate
    start_screen()
    pygame.mouse.set_visible(False)
    game_things.game_score = 0
    game_things.player = get_space_ship(info['ship_type'])
    meteors_generate.new_data()


if __name__ == '__main__':
    size = width, height = size
    running = True
    clock = pygame.time.Clock()
    meteors_generate = GenerateMeteors()
    new_game()
    while running:
        check_event()
        screen.fill((0, 0, 0))
        if not game_things.player.alive():
            game_over()
            new_game()
        meteors_generate.generate()
        all_sprites.draw(screen)
        view_koins(0.008, 0.95, font_size=30, x_center=False)
        view_score(0.008, 0.90, font_size=30, x_center=False)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
