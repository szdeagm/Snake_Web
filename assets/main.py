from pygame import *
from pygame.locals import *
from cobra import *
from pygame import time, font
import random, asyncio



async def main():
    init()

    cobra = Cobra()
    tela = display.set_mode((600,600))
    display.set_caption("Snake")
    fps = time.Clock()
    rodando = True
    fruta = Fruta()
    placar = 0
    fonte = font.SysFont('Courrier', 33)
    while rodando:
        await asyncio.sleep(0)
        if placar < 10:
            fps.tick(10)
        if placar >= 10:
            fps.tick(20) 
        for eventos in event.get():
            if eventos.type == QUIT:
                rodando = False
            elif eventos.type == KEYDOWN:
                if eventos.key == K_UP:
                    cobra.change_to = "UP"
                if eventos.key == K_DOWN:
                    cobra.change_to = "DOWN"
                if eventos.key == K_LEFT:
                    cobra.change_to = "LEFT"
                if eventos.key == K_RIGHT:
                    cobra.change_to = "RIGHT"
            
        if cobra.change_to == 'UP' and cobra.direction != 'DOWN':
            cobra.direction = 'UP'
        if cobra.change_to == 'DOWN' and cobra.direction != 'UP':
            cobra.direction = 'DOWN'
        if cobra.change_to == 'LEFT' and cobra.direction != 'RIGHT':
            cobra.direction = 'LEFT'
        if cobra.change_to == 'RIGHT' and cobra.direction != 'LEFT':
            cobra.direction = 'RIGHT'

        for i in range(len(cobra.cobra) - 1):
            cobra.cobra[i] = cobra.cobra[i + 1]

        
        tela.fill((0,0,0))

        if cobra.direction == "UP":
            cobra.cobra[-1][1] -= 10
            for cobra_pos in cobra.cobra:
                tela.blit(cobra.skin, cobra_pos)
                tela.blit(cobra.rayquaza_cima, (cobra_pos[0]-45, cobra_pos[1]-5))
        if cobra.direction == "DOWN":
            cobra.cobra[-1][1] += 10
            for cobra_pos in cobra.cobra:
                tela.blit(cobra.skin, cobra_pos)
                tela.blit(cobra.rayquaza, (cobra_pos[0]-35, cobra_pos[1]-70))
        if cobra.direction == "LEFT":
            cobra.cobra[-1][0] -= 10
            for cobra_pos in cobra.cobra:
                tela.blit(cobra.skin, cobra_pos)
                tela.blit(cobra.rayquaza_esquerda, (cobra_pos[0]-6, cobra_pos[1]-80))
        if cobra.direction == "RIGHT":
            cobra.cobra[-1][0] += 10
            for cobra_pos in cobra.cobra:
                tela.blit(cobra.skin, cobra_pos)
                tela.blit(cobra.rayquaza_direita, (cobra_pos[0]-115, cobra_pos[1]-76))
        if cobra.direction == "Right":
            for cobra_pos in cobra.cobra:
                tela.blit(cobra.skin, cobra_pos)
                tela.blit(cobra.rayquaza_parado, (cobra_pos[0]-50, cobra_pos[1]-50))

        if cobra.cobra[-1] == fruta.fruta:
            placar = placar + 1 
            fruta.reposicionar()


        tela.blit(fruta.fskin, fruta.fruta)
        tela.blit(fruta.frutafoto, (fruta.fruta[0] - 5, fruta.fruta[1] - 10))
        texto = fonte.render(f'Placar: {placar}', True, (255, 255, 255))
        tela.blit(texto, (20, 20))
        display.update()
        
    quit()

asyncio.run(main())

