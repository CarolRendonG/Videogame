from pygame import *
import sys
import random

init()
screen = display.set_mode((800,600))
clock = time.Clock()
guardado= (255,255,255)
a2= (0,0,0)
k1=0
z1, z2, z3, z4, z5,z6, z7, z8, z9, z10, z11, z12, z13 = (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)
j1= (0,0,0)
c = 1
d = 1
p=1
a=1
b=1
o=1
f=1
g=1
h=1
i=1
j=1
k=1
l=1
contador= 0

def Bienvenida():
    fondo = image.load("bienvenidajuego.png")
    fondo = transform.scale(fondo, (800,600))
    character = image.load("niña2.png")
    character = transform.scale(character, (200,400))
    calibriFont = font.SysFont("Arial", 50)
    boton= image.load("botonazul.png")
    boton= transform.scale(boton,(130,130))
    botongrande= transform.scale(boton,(150,150))
    botonRect= Rect(340,330,120,140)
    x = 0
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                 if botonRect.collidepoint(mouse.get_pos()):
                     return 1    
            if e.type == KEYDOWN and e.key == K_a:    #Si presiona la tecla a
                return 1
        screen.blit(fondo, (0,0))
        screen.blit(boton, (340,330))
        if botonRect.collidepoint(mouse.get_pos()):
            screen.blit(botongrande, (330,320))
        else:
            screen.blit(boton, (340,330))    
        draw.rect(screen, (90,180,120), (80,50,250,50), 0)
        hello = calibriFont.render("Bienvenido", True, (0,0,0))
        screen.blit(character, (x,200))
        screen.blit(hello, (100, 50))
        x = x + 1
        if x>800: x=-200
        display.flip()
def Seleccion():
    fondo = image.load("selecciondedibujo.png")
    fondo = transform.scale(fondo, (800,600))
    character = image.load("niño.png")
    character = transform.scale(character, (200,400))
    #dibujo1= image.load("dibujo1.png")
    dibujo2= image.load("dibujo11.png")
    dibujo2= transform.scale(dibujo2,(350,300))
    #dibujo1Rect= Rect(250,100,300,200)
    dibujo2Rect= Rect(200,170,310,230)
    #dibujo1grande= transform.scale(dibujo1,(300,200))
    dibujo2grande= transform.scale(dibujo2,(390,320))
    x=0
    
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 0
            if e.type == KEYDOWN and e.key == K_m: return 2
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                 #if dibujo1Rect.collidepoint(mouse.get_pos()):
                     #return 2
                 if dibujo2Rect.collidepoint(mouse.get_pos()):
                     return 3
        
        screen.blit(fondo, (0,0))
       # screen.blit(dibujo1, (250,100))
        #if dibujo1Rect.collidepoint(mouse.get_pos()):
            #screen.blit(dibujo1grande, (250,90))
        #else:
            #screen.blit(dibujo1, (250,100))
        
        #screen.blit(dibujo2, (200,170))
        if dibujo2Rect.collidepoint(mouse.get_pos()):
            screen.blit(dibujo2grande, (200,170))
        else:
            screen.blit(dibujo2, (200,170))
            
        screen.blit(character, (x,220))
        x = x + 1
        if x>800: x=-200
        display.flip()
            
    
        
def Juego():
    fondo = image.load("escena2.png")
    fondo = transform.scale(fondo, (800,600))
    calibriFont = font.SysFont("Arial", 50)
    corte= time.get_ticks() +2000
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 1
        mili= time.get_ticks()
        hello= calibriFont.render(str(mili/1000), True, (50,100,150))
        screen.blit(fondo, (0,0))
        screen.blit(hello, (100,0))
        #print(mili)
        if mili>corte:
            mili=0
            return 3   
        clock.tick(30)
        
        display.flip()
        
def Juego2():
    global guardado
    fondo = image.load("eligecolor.png")
    fondo = transform.scale(fondo, (800,600))
    calibriFont = font.SysFont("Algerian", 50)
    corte= time.get_ticks() + 15000
    azul1= image.load("btnazul.png")
    verde1= image.load("btnverde.png")
    amarillo1= image.load("btnamarillo.png")
    rosa1= image.load("btnrosa.png")
    azul= transform.scale(azul1,(200,100))
    rosa= transform.scale(rosa1,(460,240))
    verde= transform.scale(verde1,(465,230))
    amarillo= transform.scale(amarillo1,(480,220))
    AzulRect= Rect(200,220,200,80)
    VerdeRect= Rect(400,310,200,80)
    RosaRect= Rect(200,320,200,60)
    AmarilloRect= Rect(415,230,180,80)
    x=510   #longitud de la barra de tiempo
    palabra= ["AMARILLO", "VERDE", "ROSA", "AZUL"]
    color = [(255,255,0), (0,255,0), (255,0,255), (0,255,255)] #amarillo,verde,rosa,azul cielo
    n= random.randint(0,3)  #palabra y color aleatorio
    m= random.randint(0,3)
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 1
            if e.type == KEYDOWN and e.key == K_k: guardado=color[n]
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if AmarilloRect.collidepoint(mouse.get_pos()):
                    guardado=color[0]
                    if "AMARILLO" in palabra[n]:
                        return 5
                    else:
                        return 4
                if AzulRect.collidepoint(mouse.get_pos()):
                    guardado=color[3]
                    if "AZUL" in palabra[n]:
                        return 5
                    else:
                        return 4
                if VerdeRect.collidepoint(mouse.get_pos()):
                    guardado=color[1]
                    if "VERDE" in palabra[n]:
                        return 5
                    else:
                        return 4
                if RosaRect.collidepoint(mouse.get_pos()):
                    guardado=color[2]
                    if "ROSA" in palabra[n]:
                        return 5
                    else:
                        return 4
        mili= time.get_ticks()
        hello= calibriFont.render(str(mili/1000), True, (50,100,150))   
        screen.blit(fondo, (0,0))
        screen.blit(hello, (100,0))
        screen.blit(azul, (200,220))
        screen.blit(verde, (270,250))
        screen.blit(rosa, (70,240))
        screen.blit(amarillo, (280,160))
        hello = calibriFont.render(palabra[n], True, color[m])  #color de la palabra
        screen.blit(hello, (270, 105))
        draw.rect(screen, (128,128,128), (195,500,x,30), 0) #x,y,ancho,alto
        x = x -6
        if mili>corte:
            mili=0
            return 4
        clock.tick(30)
        display.flip()

def Juego3():
    global guardado, z1, c, z2, d, z3, z4, z5, z6, z7, z8, z9, z10, z11, z12, z13, a, b, f, g, h, i, j, k, l, p, o, contador
    
    fondo = image.load("fondoblanco.jpg")
    fondo = transform.scale(fondo, (800,600))
    x,y,hu,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10= (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0)
    #a,b,c,d,e= 1, 1, 1, 1, 1
    print(guardado)
    CieloRect= Rect(0,0,800,400)
    Hojaarbol1= Rect(555,75,90,90)
    Hojaarbol2= Rect(500,150,100,100)
    Hojaarbol3= Rect(600,150,100,100)
    v1= Rect(40,70,130,50)
    v2= Rect(210,70,130,50)
    v3= Rect(40,150,130,50)
    v4= Rect(210,150,130,50)
    v5= Rect(40,230,130,50)
    v6= Rect(210,230,130,50)
    pasto= Rect(0,400,800,200)
    tronco= Rect(560,250,80,150)
    edificio= Rect(20,50,350,350)
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 0
            if e.type == KEYDOWN and e.key == K_k: a1 = color[n]
            if e.type == MOUSEBUTTONDOWN and e.button==1:
                if Hojaarbol1.collidepoint(mouse.get_pos()):
                    y= guardado
                    z1 = y ###
                    c=0
                    contador= contador +1
                    return 3
                elif Hojaarbol2.collidepoint(mouse.get_pos()):
                    hu = guardado
                    z2= hu
                    d=0
                    contador= contador +1
                    return 3
                elif Hojaarbol3.collidepoint(mouse.get_pos()):
                    a1= guardado
                    z3=a1
                    o=0
                    contador= contador +1
                    return 3
                elif v1.collidepoint(mouse.get_pos()):
                    a2= guardado
                    z4=a2
                    g=0
                    contador= contador +1
                    return 3
                elif v2.collidepoint(mouse.get_pos()):
                    a3= guardado
                    z5=a3
                    h=0
                    contador= contador +1
                    return 3
                elif v3.collidepoint(mouse.get_pos()):
                    a4= guardado
                    z6=a4
                    i=0
                    contador= contador +1
                    return 3
                elif v4.collidepoint(mouse.get_pos()):
                    a5= guardado
                    z7=a5
                    j=0
                    contador= contador +1
                    return 3
                elif v5.collidepoint(mouse.get_pos()):
                    a6= guardado
                    z8=a6
                    k=0
                    contador= contador +1
                    return 3
                elif v6.collidepoint(mouse.get_pos()):
                    a7= guardado
                    z9=a7
                    l=0
                    contador= contador +1
                    return 3
                elif pasto.collidepoint(mouse.get_pos()):
                    a8= guardado
                    z10=a8
                    a=0
                    contador= contador +1
                    return 3
                elif tronco.collidepoint(mouse.get_pos()):
                    a9= guardado
                    z11= a9
                    b=0
                    contador= contador +1
                    return 3
                elif edificio.collidepoint(mouse.get_pos()):
                    a10= guardado
                    z12= a10
                    f=0
                    contador= contador +1
                    return 3
                elif CieloRect.collidepoint(mouse.get_pos()):
                    x= guardado
                    z13=x
                    p=0
                    contador= contador +1
                    return 3
                
        if contador == 10:
            return 6
        screen.blit(fondo, (0,0))
        k1=draw.rect(screen, z13, (0,0,800,400), p)#cielo
        k2=draw.rect(screen, z10, (0,400,800,200), a)#pasto
        k3=draw.rect(screen, z11, (560,250,80,150), b) #tronco
        k4=draw.circle(screen, z1, (600,120), 45, c) #hojarbol1 ####
        k5=draw.circle(screen, z2, (550,200), 50, d) #hojaarbol2
        k6=draw.circle(screen, z3, (650,200), 50, o) #hojaarbol3
        k7=draw.rect(screen, z12, (20,50,350,350), f)#edificio
        k8=draw.rect(screen, z4, (40,70,130,50), g) #v1
        k9=draw.rect(screen, z5, (210,70,130,50), h)#v2
        k10=draw.rect(screen, z6, (40,150,130,50), i)#v3
        k11=draw.rect(screen, z7, (210,150,130,50), j)#v4
        k12=draw.rect(screen, z8, (40,230,130,50), k)#v5
        k13=draw.rect(screen, z9, (210,230,130,50), l) #v6
        draw.rect(screen, (0,0,0), (560,250,80,150), 1) 
        
        
        
        display.flip()

def Perdiste():
    fondo = image.load("perdistee.png")
    fondo = transform.scale(fondo, (800,600))
    
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 0
        
        screen.blit(fondo, (0,0))
        display.flip()
def Ganaste():
    fondo = image.load("ganaste.png")
    fondo = transform.scale(fondo, (800,600))
    
    while True:
        screen.fill((200,200,200))
        for e in event.get():
            if e.type == QUIT: sys.exit()
            if e.type == KEYDOWN and e.key == K_ESCAPE: return 0
        
        screen.blit(fondo, (0,0))
        display.flip()
    
escena = 0
while True:
    if escena==0: escena = Bienvenida()
    if escena==1: escena = Seleccion()
    if escena==2: escena = Juego()
    if escena==3: escena = Juego2()
    if escena==4: escena = Perdiste()
    if escena==5: escena = Juego3()
    if escena==6: escena = Ganaste()
    
    #palabra= amarillo, verde, rosa, azul
    #color = (255,255,0), (0,0,255), (255,0,255), (0,255,255)
    