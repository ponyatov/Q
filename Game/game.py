import sys  
import pygame
pygame.init()
pygame.display.set_caption(str(sys.argv))

scr = pygame.display.set_mode((480,640))

exitGame = False
X = 480/2
Y = 640/2

BACK = (0x12, 0x34, 0x56)
FORE = (0x98, 0x76, 0x54)

while not exitGame:
    scr.fill(BACK)
    scr.fill(FORE, rect=[X,Y,111,111])
    pygame.display.update()
    for e in pygame.event.get():
        if e.type == pygame.QUIT: exitGame = true
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE: exitGame = True
            elif e.key == pygame.K_LEFT : X -= 11
            elif e.key == pygame.K_RIGHT: X += 11
        
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
