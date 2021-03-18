from direct.stdpy import threading
from direct.showbase.ShowBase import ShowBase
from panda3d.core import VirtualFileSystem
import __builtin__, wx, os

__builtin__.__dict__.update(__import__('panda3d.core', fromlist=['*']).__dict__)

loadPrcFile('dependencies/config/guieditor.prc')
loadPrcFile('dependencies/config/general.prc')

defaultText = """from direct.gui.DirectGui import *

"""

def inject(_):
    code = textbox.GetValue()
    exec(code, globals())

app = wx.App(redirect=False)
frame = wx.Frame(None, title="Injector", size=(640, 400), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
panel = wx.Panel(frame)
button = wx.Button(parent=panel, id=-1, label="Inject", size=(50, 20), pos=(295, 0))
textbox = wx.TextCtrl(parent=panel, id=-1, pos=(20, 22), size=(600, 340), style=wx.TE_MULTILINE)

frame.Bind(wx.EVT_BUTTON, inject, button)
frame.Show()
app.SetTopWindow(frame)
textbox.AppendText(defaultText)
threading.Thread(target=app.MainLoop).start()

__builtin__.base = ShowBase()
base.run()