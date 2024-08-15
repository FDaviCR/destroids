import pygame;
import sys;

# Inicializa o Pygame
pygame.init()

# Definir as dimensões da tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Definir a cor de fundo (RGB)
background_color = (0, 0, 0)

# Definir o título da janela
pygame.display.set_caption('Tela Inicial')

# Loop principal do jogo
running = True
while (running):
    # Preenche a tela com a cor de fundo
    screen.fill(background_color)

    # Lidar com eventos (como fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualizar a tela
    pygame.display.flip()

# Sair do Pygame
pygame.quit()
sys.exit()