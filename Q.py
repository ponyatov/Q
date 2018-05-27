MODULE  = 'Q'
TITLE   = 'Qbject system'
GITHUB  = 'https://github.com/ponyatov/Q'
AUTHOR  = 'Dmitry Ponyatov'
EMAIL   = 'dponyatov@gmail.com'
LICENSE = 'All rights reserved'

ABOUT   = '''
* OS IDE CAD/CAM/CAE RAD CAL (computer assisted learning)
* script languages: Python FORTH SmallTalk
* DB: (hyper)graph object knowledge database
* AI: Mynsky frames semantic hypergraph inference system
* metaprogramming and managed compilation:
'''

README = '''
# %s
## %s
### ask for lessons how to reimplement it to know deep in use

(c) %s <<%s>>, %s

github: %s

%s
''' % (MODULE, TITLE, AUTHOR, EMAIL, LICENSE, GITHUB, ABOUT)

# need for sys.argv command line parameters
import sys

# use wxPython
import wx
# and Scintilla editor
import wx.stc

# wxApplication
app = wx.App()

# main window
main = wx.Frame(None, title='%s' % sys.argv) ; main.Show()

# menu
menu = wx.MenuBar() ; main.SetMenuBar(menu)
# file
file = wx.Menu() ; menu.Append(file, '&File')
# file/save
save = file.Append(wx.ID_SAVE, '&Save')
# file/quit
quit = file.Append(wx.ID_EXIT, '&Quit')
main.Bind(wx.EVT_MENU, lambda e:main.Close(), quit)
# help
help = wx.Menu() ; menu.Append(help, '&Help')
# help/about
about = help.Append(wx.ID_ABOUT, '&About\tF1')
main.Bind(wx.EVT_MENU, lambda e:wx.MessageBox(README), about)

# editor
editor = wx.stc.StyledTextCtrl(main) ; editor.SetValue(README)

# large monospace font adopted for screen size
## fetch screen height as base for font scale
displaY = wx.GetDisplaySizeMM()[1]
## fetch available font from system
font = wx.Font(displaY / 11,
               wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
## set default styling in editor
editor.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,
                    'face:%s,size:%s' % (font.FaceName, font.PointSize))

# start GUI
app.MainLoop()
