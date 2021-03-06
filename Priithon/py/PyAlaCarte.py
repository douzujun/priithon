"""PyAlaCarte is a simple programmer's editor."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: PyAlaCarte.py,v 1.6 2004/03/15 13:42:37 PKO Exp $"
__revision__ = "$Revision: 1.6 $"[11:-2]

import wx
#seb from wx import py
import editor #seb

import os
import sys

class App(wx.App):
    """PyAlaCarte standalone application."""

    def __init__(self, filename=None):
        self.filename = filename
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        wx.InitAllImageHandlers()
        #seb self.frame = py.editor.EditorFrame(filename=self.filename)
        self.frame = editor.EditorFrame(filename=self.filename)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main(filename=None):
    if not filename and len(sys.argv) > 1:
        filename = sys.argv[1]
    if filename:
        filename = os.path.realpath(filename)
    app = App(filename)
    app.MainLoop()

if __name__ == '__main__':
    main()
