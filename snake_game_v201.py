from game import Game

def main():
    game = Game()
    game.run()

#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------
#----------------------------------------------------------------



def main_old():

    # start game
    score = 0
    direction = random.choice(DIRECTIONS)
    change_to = direction

    # start with no food on the field
    food = None
    food2 = None

    # main loop of the game:
    while True:
        if not food:
            food = Food() # create a new food object

        if not food2:
            food2 = Food()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                else:
                    change_to = EVENT_KEY_DIRECTIONS.get(event.key, change_to)

        direction = validate_direction(change_to, direction)
        update_snake_head(snake_head, direction)

        # snake body mechanism
        snake_body.insert(0, list(snake_head))
        if snake_head == food.position():
            score += 1
            food = None    # new food_postion generated next time
        elif snake_head == food2.position():
            score += 1
            food2 = None    # new food_postion generated next time
        else:
            snake_body.pop()

        # draw background
        play_surface.fill(BLACK)

        draw_snake(play_surface, snake_body)
        if food:
            food.draw(play_surface)
        if food2:
            food2.draw(play_surface)

        # check out of boundaries
        if snake_head[0] < 0 or snake_head[0] > WIDTH_PX - BLOCK_SIZE_PX:
            break
        if snake_head[1] < 0 or snake_head[1] > HEIGHT_PX - BLOCK_SIZE_PX:
            break

        # hit self body?
        self_hit = False
        for block in snake_body[1:]:
            if snake_head == block:
                self_hit = True
                break
        if self_hit:
            break

        # update surface
        show_score(play_surface, score)
        pygame.display.flip()
        fps_controller.tick(20)

    # exit
    game_over(play_surface, score)


if __name__ == '__main__':

    main()
