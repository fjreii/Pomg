import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle and Ball properties
paddle_width, paddle_height = 10, 100
ball_size = 10
paddle_speed = 10
ball_speed = 7

# Paddle positions
left_paddle = pygame.Rect(30, (height - paddle_height) // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 40, (height - paddle_height) // 2, paddle_width, paddle_height)

# Ball position and direction
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_dx, ball_dy = ball_speed * random.choice([1, -1]), ball_speed * random.choice([1, -1])

# Score
left_score, right_score = 0, 0

# Font
font = pygame.font.SysFont('comicsansms', 50)

def draw():
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))
    
    left_text = font.render(str(left_score), True, white)
    right_text = font.render(str(right_score), True, white)
    screen.blit(left_text, (width // 4 - left_text.get_width() // 2, 20))
    screen.blit(right_text, (width * 3 // 4 - right_text.get_width() // 2, 20))
    
    pygame.display.flip()

def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

def move_ball():
    global ball_dx, ball_dy, left_score, right_score
    
    ball.x += ball_dx
    ball.y += ball_dy
    
    if ball.top <= 0 or ball.bottom >= height:
        ball_dy = -ball_dy
        
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx
        
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= width:
        left_score += 1
        reset_ball()

def reset_ball():
    global ball_dx, ball_dy
    ball.x = width // 2 - ball_size // 2
    ball.y = height // 2 - ball_size // 2
    ball_dx, ball_dy = ball_speed * random.choice([1, -1]), ball_speed * random.choice([1, -1])

def main():
    clock = pygame.time.Clock()
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        move_paddles()
        move_ball()
        draw()
        clock.tick(60)
    
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()
