## @file
## @brief Qbject Virtual Machine (Python implementation)

## @defgroup meta Metainformation
## @brief Project info
## @{

## module name
MODULE  = 'Q'
## short info
TITLE   = 'Qbject system'
## repository location
GITHUB  = 'https://github.com/ponyatov/Q'
## author
AUTHOR  = 'Dmitry Ponyatov'
## contact emain
EMAIL   = 'dponyatov@gmail.com'
## license
LICENSE = 'All rights reserved'

## longer project about 
ABOUT   = '''
* OS IDE CAD/CAM/CAE RAD CAL (computer assisted learning)
* script languages: Python FORTH SmallTalk
* DB: (hyper)graph object knowledge database
* AI: Mynsky frames semantic hypergraph inference system
* metaprogramming and managed compilation:
'''

## README.md
README = '''
# %s
## %s
### ask for lessons how to reimplement it to know deep in use

(c) %s <<%s>>, %s

github: %s

%s
''' % (MODULE, TITLE, AUTHOR, EMAIL, LICENSE, GITHUB, ABOUT)

## @}

## @defgroup qbject Qbject class tree
## @brief Generic types class system (metaprogramming and symbolic computations)
## @{

## generic Object class (the name was chosen not to interfere with Python3)
class Qbject:
    ## construct with given value
    def __init__(self, V):
        ## <type:value> must be compatible with PLY library token objects
        self.type = self.__class__.__name__.lower()
        ## single value
        self.value = V
    ## text dump (tree form)
    def __repr__(self): return self.dump()
    ## dump any object in tree form
    def dump(self, depth=0):
        S = self.head()
        return S
    ## dump object in short form (header only)
    def head(self,prefix=''):
        return '%s<%s:%s>' % (prefix,self.type, self.value)

## data stack
class Stack(Qbject): pass

## associative array (vocabulary)
class Voc(Qbject): pass
    
## @}

## @defgroup forth oFORTH
## @brief object FORTH interpreter
## @{

## data stack
S = Stack('DATA')

## system vocabulary
W = Voc('FORTH')

## @}

# need for sys.argv command line parameters
import sys

## @defgroup gui GUI
## wxPython wrappers and microIDE
## @{

# use wxPython
import wx
# and Scintilla editor
import wx.stc

# need 

## wxApplication
app = wx.App()

# large monospace font adopted for screen size
## fetch screen height as base for font scale
displaY = wx.GetDisplaySizeMM()[1]
## fetch available font from system
font = wx.Font(displaY / 11,
               wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

## @defgroup editor IDE/Text editor
## @{

## text editor window
class Editor(wx.Frame):
    ## construct text editor
    ## @param[in] parent window
    ## @param[in] title window title
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.initMenu()
        self.initEditor()
    ## initialize menu
    def initMenu(self):
        ## menu
        self.menu = wx.MenuBar() ; self.SetMenuBar(self.menu)
        
        ## file
        self.file = wx.Menu() ; self.menu.Append(self.file, '&File')
        ## file/save
        self.save = self.file.Append(wx.ID_SAVE, '&Save')
        ## file/quit
        self.quit = self.file.Append(wx.ID_EXIT, '&Quit')
        self.Bind(wx.EVT_MENU, self.onClose, self.quit)
        
        ## debug
        self.debug = wx.Menu() ; self.menu.Append(self.debug,'&Debug')
        ## debug/refresh
        self.refresh = self.debug.Append(wx.ID_REFRESH,'&Refresh\tF12')
        self.Bind(wx.EVT_MENU, self.onRefresh, self.refresh)
        ## debug/vocabulary
        self.words = self.debug.Append(wx.ID_ANY,'&Vocabulary\tF9',kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.toggleWords, self.words)
        ## debug/stack
        self.stack = self.debug.Append(wx.ID_ANY,'&Stack\tF8',kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.toggleStack, self.stack)

        ## help
        self.help = wx.Menu() ; self.menu.Append(self.help, '&Help')
        ## help/about
        self.about = self.help.Append(wx.ID_ABOUT, '&About\tF1')
        self.Bind(wx.EVT_MENU, lambda e:wx.MessageBox(README), self.about)
    ## initialize editor
    def initEditor(self):
        ## editor
        self.editor = wx.stc.StyledTextCtrl(self)
        ## set default styling in editor
        self.editor.StyleSetSpec(wx.stc.STC_STYLE_DEFAULT,
                        'face:%s,size:%s' % (font.FaceName, font.PointSize))
    ## toggle words window
    def toggleWords(self,e):
        if words.IsShown(): words.Hide()
        else:               words.Show() ; self.onRefresh(None)
    ## toggle stack window
    def toggleStack(self,e):
        if stack.IsShown(): stack.Hide()
        else:               stack.Show() ; self.onRefresh(None)
    ## update debug windows
    def onRefresh(self,e):
        if words.IsShown(): words.editor.SetValue(W.dump())
        if stack.IsShown(): stack.editor.SetValue(S.dump())
    ## close GUI
    def onClose(self,e):
        main.Close() ; stack.Close() ; words.Close() 

## main window
main = Editor(None, title = sys.argv[0] + '.src') ; main.Show()
main.editor.SetValue(README)

## stack window
stack = Editor(main, title = sys.argv[0] + '.stack')

## vocabulary window
words = Editor(main, title = sys.argv[0] + '.words')

## @}

# start GUI
app.MainLoop()

## @}

