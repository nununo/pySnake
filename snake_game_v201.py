""" Snake game!
    Originally by udemy course and adapted by Vasco Mora
"""

import random
import time
import sys
import pygame



# colors
BLACK = pygame.Color(0, 0, 0)       # background
GREEN = pygame.Color(0, 255, 0)     # snake
RED = pygame.Color(255, 0, 0)       # game over title
WHITE = pygame.Color(255, 255, 255) # score title


#  initialize pygame surface / canvas
BLOCK_SIZE_PX = 10
WIDTH_BLOCKS = 72
HEIGHT_BLOCKS = 43
WIDTH_PX = WIDTH_BLOCKS * BLOCK_SIZE_PX
HEIGHT_PX = HEIGHT_BLOCKS * BLOCK_SIZE_PX


# snake movement constants
DIRECTION_UP = 'UP'
DIRECTION_DOWN = 'DOWN'
DIRECTION_LEFT = 'LEFT'
DIRECTION_RIGHT = 'RIGHT'
DIRECTIONS = [
    DIRECTION_UP,
    DIRECTION_RIGHT,
    DIRECTION_DOWN,
    DIRECTION_LEFT,
]

OPPOSITE_DIRECTION = {
    DIRECTION_UP: DIRECTION_DOWN,
    DIRECTION_DOWN: DIRECTION_UP,
    DIRECTION_LEFT: DIRECTION_RIGHT,
    DIRECTION_RIGHT: DIRECTION_LEFT,
}
DELTA_MOVEMENT_PX = {
    DIRECTION_UP: [0, -BLOCK_SIZE_PX],
    DIRECTION_RIGHT: [BLOCK_SIZE_PX, 0],
    DIRECTION_DOWN: [0, BLOCK_SIZE_PX],
    DIRECTION_LEFT: [-BLOCK_SIZE_PX, 0],
}

# pygame event keys to movement
EVENT_KEY_DIRECTIONS = {
    pygame.K_UP: DIRECTION_UP,
    pygame.K_DOWN: DIRECTION_DOWN,
    pygame.K_LEFT: DIRECTION_LEFT,
    pygame.K_RIGHT: DIRECTION_RIGHT,
    ord('w'): DIRECTION_UP,
    ord('s'): DIRECTION_DOWN,
    ord('a'): DIRECTION_LEFT,
    ord('d'): DIRECTION_RIGHT,

}


class Food:
    """ defines the type of food and its location in the board
    """

    # food colors
    BROWN = pygame.Color(165, 42, 42)       
    CHOCOLATE = pygame.Color(210, 105, 30)
    
    # food value / volume
    value = 1


    def __init__(self):
        """ return a new position for food and its volume / value
        """

        self.x_pos = random.randrange(0, WIDTH_BLOCKS-1) * BLOCK_SIZE_PX
        self.y_pos = random.randrange(0, HEIGHT_BLOCKS-1) * BLOCK_SIZE_PX
        self.color = random.choice([self.BROWN, self.CHOCOLATE])

        return #[self.x_pos, self.y_pos, self.value]

    
    def position(self):
        
        return [self.x_pos, self.y_pos] 

    
    def draw(self, surface):
        """ draw the food
        """
        pygame.draw.rect(
            surface, 
            self.color,
            pygame.Rect(
                self.x_pos, self.y_pos, 
                BLOCK_SIZE_PX, BLOCK_SIZE_PX),
        )




def initialize_pygame():
    """ Check if pygame initializes without errors
    """

    numpass, numfail = pygame.init()
    if numfail > 0:
        print("(!) Had {} initialization errors, existing...".format(numfail))
        sys.exit(-1)
    else:
        print("(+) Pygame successfully initialized!")


def initial_snake_head_and_body(direction):
    """ determine initial snake position based on direction
    so it doesn't start to close to the limits
    """

    margin = 8
    min_x = min_y = margin
    max_x = WIDTH_BLOCKS - margin
    max_y = HEIGHT_BLOCKS - margin

    x_pos = random.randint(min_x, max_x) * BLOCK_SIZE_PX
    y_pos = random.randint(min_y, max_y) * BLOCK_SIZE_PX
    snake_head = [x_pos, y_pos]

    body_size = 3
    snake_body = []
    back_direction = DELTA_MOVEMENT_PX[OPPOSITE_DIRECTION[direction]]
    for body_block in range(body_size):
        body_x = snake_head[0] + body_block + back_direction[0]
        body_y = snake_head[1] + body_block + back_direction[1]
        snake_body.append([body_x, body_y])

    return snake_head, snake_body


def validate_direction(requested_direction, current_direction):
    """ validation of direction
    """

    if requested_direction == OPPOSITE_DIRECTION[current_direction]:
        # can't turn back over itself, keep current direction
        result = current_direction
    else:
        result = requested_direction

    return result


def update_snake_head(snake_head, direction):
    """ update snake position based on direction / heading
    """

    snake_head[0] += DELTA_MOVEMENT_PX[direction][0] # x coordinate
    snake_head[1] += DELTA_MOVEMENT_PX[direction][1] # y coordinate



def show_score(surface, score, game_over=False):
    """ show score
    """

    score_font = pygame.font.SysFont('Arial', 24)
    score_surface = score_font.render('Score: {}'.format(score), True, WHITE)
    score_rectangle = score_surface.get_rect()

    if not game_over:
        score_rectangle.midtop = (80, 10)
    else:
        score_rectangle.midtop = (WIDTH_PX // 2, 120)

    surface.blit(score_surface, score_rectangle)


def game_over(surface, score):
    """ game over function
    """

    my_font = pygame.font.SysFont('Arial', 72)
    go_surf = my_font.render('Game over!', True, RED)
    go_rect = go_surf.get_rect()
    go_rect.midtop = (WIDTH_PX // 2, 15)

    surface.blit(go_surf, go_rect)

    show_score(surface, score, game_over=True)

    pygame.display.flip()
    time.sleep(2)

    pygame.quit()
    sys.exit()


def draw_snake(surface, snake_body):
    """ draw the snake body in the given surface
    """
    for block in snake_body:
        pygame.draw.rect(
            surface, GREEN,
            pygame.Rect(block[0], block[1], BLOCK_SIZE_PX, BLOCK_SIZE_PX),
        )


def main():
    """ This is the actual snake code
    """

    initialize_pygame()

    pygame.display.set_caption('Snake game!')
    play_surface = pygame.display.set_mode((WIDTH_PX, HEIGHT_PX))

    # helps us set the pace
    fps_controller = pygame.time.Clock()

    # start game
    score = 0
    direction = random.choice(DIRECTIONS)
    change_to = direction

    # position variables
    snake_head, snake_body = initial_snake_head_and_body(direction)

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
