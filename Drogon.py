#importando o pygame
import pygame
from pygame import event
from pygame.constants import WINDOWHITTEST
from pygame.display import set_caption
pygame.init()

pygame.display.set_caption('dracarys')

#colocando o tamanho da janela do game
tamanho = (700,500)
tela = pygame.display.set_mode(tamanho)
dragao = pygame.image.load("imagens/newdrag.png")
cenario = pygame.image.load("imagens/cenario.png")
caixatxt = pygame.image.load("imagens/caixatxt.png")
seta = pygame.image.load("imagens/setapixel.png")
fonte = pygame.font.Font(None, 30)
fonte_dev = pygame.font.Font(None, 40)
fonte_placar = pygame.font.Font(None, 60)
fonte_press = pygame.font.Font(None, 40)
fonte_fim = pygame.font.Font(None, 80)
texto = fonte.render("Drogon Dracaryssssssss", True, (0,0,0))

# # music-------------------------------------------------------------------------------------------
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.load('trilha sonora/menu drag 8bits.wav')
pygame.mixer.music.play()
pygame.event.wait(-1)

# criando variavel de musica ao matar o drag
kick = pygame.mixer.Sound("trilha sonora/dragao_flechado1.wav")
kick.set_volume(0.3)
tiro = pygame.mixer.Sound("trilha sonora/fecha_atirando.wav")
tiro.set_volume(0.1)

# colocando o menu--------------------------------------------------------------------------------------------------------------------------------------
menupic = pygame.image.load("imagens/menu 2.png")
# menu.convert()

# criando as vareaveis
executando = False
acertei = False
x = -260
y_dragao = 50
y = 380
velocidade = 0
pontos = 0
x_seta = 353




# colocando relogio para controlar o FPS-------------------------------------------------
relogio = pygame.time.Clock()
# variavel criada para os While---------------------------------------------------------------
menu = True
executando = True
fim = True
# pygame.display.update()
while menu:
    tela.fill((125,125,125))
    tela.blit(menupic,(0,0))
    press = fonte_press.render("PRESSIONE PARA INICIAR",True,(150,150,150))
    tela.blit(press, (300,450))
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            menu = False
            executando = False
        if evento.type == pygame.KEYDOWN:
            menu = False


#fazendo o loop para abrir janela do game----------------------------------------------------------------------
while executando:
    # aqui temos os FPS, nesse caso será 24 FPS
    relogio.tick(30)
    #pintando o cenario de branco
    tela.fill((125,125,125))
    # tudo que for ser exibido na tela do jogo tem que colocar a tela.blit
    tela.blit(cenario,(0,0))
    tela.blit(caixatxt,(2,2))
    tela.blit(texto, (25,45))
    # Criando o placar                                                  
    placar = fonte_placar.render(str(pontos),True,(0,0,0))
    tela.blit(placar, (615,35))

    tela.blit(seta,(x_seta,y))
    tela.blit(dragao,(x,y_dragao))
    # colocando movimento constante nos dragao e na seta (para qualquer coisa se tornar constante é necessario ficar fora dos "if")
    x = x+10
    y = y-velocidade
    # a queda do dragao ao ser acertado
    if acertei:
        y_dragao = y_dragao + 10

    # o momento que o dragao volta ao inicio------------------------------------------
    if y_dragao == 360:
        x = -300
        y_dragao = 50
        dragao = pygame.transform.flip(dragao,False,True)
        acertei = False
        
        
    # fazendo o dragao começar a descer
    if x > 700:
        x = -220
        y_dragao = y_dragao + 50
        pontos = pontos-5
    # fazendo a seta voltar a posição inicial
    if y < -100:
        y = 380
        velocidade = 0
    # fazendo a colisão do dragao e sa seta
    if y == 100:
        if x >= 220 and x <=360:        
            pontos = pontos+5 
            print("matou")
            dragao = pygame.transform.flip(dragao,False,True)
            acertei = True
            y = 380
            velocidade = 0

            kick.play()

    # criando o fechamento de jogo e as frases motivadoras              
    if pontos == -25:
        executando = False 
    if pontos == -20:
        texto = fonte.render("Nãoooooooooooooooooooooooooooooooooooo!!!!!!", True, (0,0,0))
    if pontos == -15:
        texto = fonte.render("Cuidado, você está quase perdendo a cidade!!", True, (0,0,0))
    if pontos == -5:
        texto = fonte.render("Força guerreiro, você consegue!", True, (0,0,0))
    if pontos == 0:
        texto = fonte.render("Mate o dragão antes que ele destrua a cidade", True, (0,0,0))
    if pontos == 25:
        texto = fonte.render("Força, você está quase lá!", True, (0,0,0))
    if pontos == 30:
        executando = False


    pygame.display.flip()
#colocando o executando false para assim poder fechar o jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
            fim = False
        if evento.type ==pygame.KEYDOWN:
            velocidade = 20
            tiro.play()



while fim:
    tela.fill((125,125,125))
    tela.blit(menupic ,(0,0))
    devs = fonte_dev.render('criadores: LCDomingos & IPaulino',True,(125,125,125))
    tela.blit(devs, (130,450))
    reiniciar = fonte_fim.render("FIM",True,(125,125,125))
    tela.blit(reiniciar, (300,350))
    pygame.display.flip()
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim = False

#mostrando todos os eventos-------------------------
        # print(evento)
        # print(pontos)