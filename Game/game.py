import sys  
import pygame
pygame.init()
pygame.display.set_caption(str(sys.argv))

W = 480 ; H = 640

scr = pygame.display.set_mode((W,H))

exitGame = False
X = W/2 ; dX = 0
Y = H/2 ; dY = 0

BACK = (0x12, 0x34, 0x56)
FORE = (0x98, 0x87, 0x76)

PAD_W = 110
PAD_H = PAD_W/5

while not exitGame:
    scr.fill(BACK)
    scr.fill(FORE, rect=[X, Y, PAD_W, PAD_H])
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exitGame = true
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: exitGame = True
            elif e.key == pygame.K_LEFT : dX = -1
            elif e.key == pygame.K_RIGHT: dX = +1
    X += dX
    if X < 0: X = 0
    elif X > W - PAD_W: X = W - PAD_W
        
pygame.quit()

# # win = wx.Window(form) ; form.display = win
# # os.environ['SDL_WINDOWID'] = str(win.GetHandle())
# 
# # def onPaint(e):
# #     scr.fill((0,0,0))
# #     pygame.display.update()
# # win.Bind(wx.EVT_PAINT, onPaint)
# #  
# # print pygame.display.Info()
# # 
# # print pygame.display.set_mode(size)
# # 
# # menu = wx.MenuBar() ; form.SetMenuBar(menu)
# # 
# # file = wx.Menu() ; menu.Append(file,'&File')
# # quit = file.Append(wx.ID_EXIT,'&Quit')
# # form.Bind(wx.EVT_MENU,lambda e:form.Close(),quit)
# # # 
# # # # panel = wx.Panel(form)
# # #  
# # # hwnd = form.GetHandle() ; print hwnd
# # #  
# # # os.environ['SDL_WINDOWID'] = str(hwnd)
# # #  
# # avi = pygame.movie.Movie('drop.avi')
# # if avi.has_video(): w,h=avi.get_size()
# # 
# # display = pygame.display.set_mode((w,h))
# # # display = pygame.display.set_mode((w,h))
# # 
# # avi.set_display(display)
# # avi.play()
# # 
# # import pygame
# # pygame.display.init()
# #   
# # # avi = pygame.movie.Movie('drop.avi') ; print avi
# # # if avi.has_video(): w,h=avi.get_size() ; print w,h
# #  
# # display = pygame.display.set_mode(form.GetSizeTuple())
# #   
# # # avi.set_display(display)
# # # avi.play()
