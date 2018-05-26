MODULE  = 'Q'
TITLE   = 'Qbject system'
GITHUB  = 'https://github.com/ponyatov/Q'
AUTHOR  = 'Dmitry Ponyatov'
EMAIL   = 'dponyatov@gmail.com'
LICENSE = 'All rights reserved'

README  = '''
# %s
## %s

(c) %s <<%s>>, %s

github: %s
'''%(MODULE,TITLE,AUTHOR,EMAIL,LICENSE,GITHUB)

import sys

# use wxPython
import wx
# and Scintilla editor
import wx.stc

# wxApplication
app = wx.App()

# main window
main = wx.Frame(None,title='%s'%sys.argv) ; main.Show()

# menu
menu = wx.MenuBar() ; main.SetMenuBar(menu)

# editor
editor = wx.stc.StyledTextCtrl(main) ; editor.SetValue(README)

# start GUI
app.MainLoop()
