# import os
# 
# import wx
# 
# app = wx.App()
# 
# form = wx.Frame(None) ; form.Show()
# 
# win = wx.Window(form) ; form.display = win
# os.environ['SDL_WINDOWID'] = str(win.GetHandle())

import random,math
 
import pygame
pygame.display.init()
 
scr = pygame.display.set_mode((640,480))
print scr

r = g = b = 0

while True:
    r0 = r ; g0 = g ; b0 = b 
    r = random.randint(0x00,0xFF)
    g = random.randint(0x00,0xFF)
    b = random.randint(0x00,0xFF)
    dr = (r-r0)/100
    dg = (g-g0)/100
    db = (b-b0)/100
    for i in range(100):
        r += dr ; g += dg ; b += db
        scr.fill((r,g,b))
        pygame.display.update()

raw_input()
 
 
# def onPaint(e):
#     scr.fill((0,0,0))
#     pygame.display.update()
# win.Bind(wx.EVT_PAINT, onPaint)
#  
# app.MainLoop()
# 
# # import os,sys
# #  
# # # size = [320,240]
# # # 
# # # # print pygame.display.Info()
# # # # 
# # # # print pygame.display.set_mode(size)
# # # # 
# # # # raw_input()
# #  
# # import wx
# #  
# # app = wx.App()
# #  
# # form = wx.Frame(None) ; form.Show()
# #  
# # # menu = wx.MenuBar() ; form.SetMenuBar(menu)
# # # 
# # # file = wx.Menu() ; menu.Append(file,'&File')
# # # quit = file.Append(wx.ID_EXIT,'&Quit')
# # # form.Bind(wx.EVT_MENU,lambda e:form.Close(),quit)
# # 
# # # panel = wx.Panel(form)
# #  
# # hwnd = form.GetHandle() ; print hwnd
# #  
# # os.environ['SDL_WINDOWID'] = str(hwnd)
# #  
# # # avi = pygame.movie.Movie('drop.avi')
# # # if avi.has_video(): w,h=avi.get_size()
# # # 
# # # display = pygame.display.set_mode((w,h))
# # # # display = pygame.display.set_mode((w,h))
# # # 
# # # avi.set_display(display)
# # # avi.play()
# # # 
# # # # app.MainLoop()
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
# # 
# # raw_input()
