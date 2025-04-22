import pygame
import random
from game_config import *

# 初始化Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("贪吃蛇游戏 - COMP2116 Final Project")

# 定义颜色（新增蛇和苹果的颜色）
SNAKE_COLOR = (0, 255, 0)  # 绿色
APPLE_COLOR = (255, 0, 0)  # 红色

# 蛇的初始位置和速度
snake = [(100, 100), (90, 100), (80, 100)]
direction = "RIGHT"
score = 0


# 生成食物
def spawn_apple():
    return (random.randint(0, SCREEN_WIDTH // 10 - 1) * 10,
            random.randint(0, SCREEN_HEIGHT // 10 - 1) * 10)


apple = spawn_apple()

# 游戏主循环
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # 处理键盘事件（保持不变）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # 移动蛇头（保持不变）
    head_x, head_y = snake[0]
    new_head = snake[0]  # 默认值防止未定义
    if direction == "UP":
        new_head = (head_x, head_y - 10)
    elif direction == "DOWN":
        new_head = (head_x, head_y + 10)
    elif direction == "LEFT":
        new_head = (head_x - 10, head_y)
    elif direction == "RIGHT":
        new_head = (head_x + 10, head_y)
    snake.insert(0, new_head)

    # 碰撞检测（保持不变）
    if (head_x < 0 or head_x >= SCREEN_WIDTH or
            head_y < 0 or head_y >= SCREEN_HEIGHT):
        running = False

    # 吃到食物逻辑（保持不变）
    if snake[0] == apple:
        score += 1
        apple = spawn_apple()
    else:
        snake.pop()

    # 绘制蛇和苹果（修改为纯色绘制）
    for pos in snake:
        pygame.draw.rect(screen, SNAKE_COLOR, (pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, APPLE_COLOR, (apple[0], apple[1], 10, 10))

    # 显示分数（保持不变）
    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()