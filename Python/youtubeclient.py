import wx
import random
import subprocess

#Youtube mp3 downloader

app = wx.App()


class MyWindow(wx.Frame):
    def __init__(self,*args,**kw):
        super(MyWindow,self).__init__(*args,**kw)


        dlButton = wx.Button(self,label="Download mp3",pos=(150,180))
        linkBox = wx.TextCtrl(self,pos=(300/2,300/2))

        def dl(self):
            subprocess.call("youtube-dl -x --audio-format mp3 "+linkBox.GetValue(),shell=True)

        dlButton.Bind(wx.EVT_BUTTON,dl)




window = MyWindow(None,title="Tball's youtube downloader")
window.Show()

app.MainLoop()
