import wx
import wx.html2
import requests

app = wx.App()

#ugly web browser


class mainWindow(wx.Frame):
    def __init__(self,*args,**kw):
        super(mainWindow,self).__init__(*args,**kw)
        #urlbar = wx.TextCtrl(panel)
        web = wx.html2.WebView.New(self,size=(900,700))
        web.LoadURL("https://www.google.com")
        web.Show()

        google = wx.Button(self,label="Google",pos=(900,100))
        ddg = wx.Button(self,label="DuckDuckGo",pos=(900,120))
        yt = wx.Button(self,label="Youtube",pos=(900,140))


        def g(self): # Google
            web.LoadURL("https://www.google.com")

        def dg(self): #DuckDuckGo
            web.LoadURL("https://start.duckduckgo.com")
            

        def ytt(self): #Youtube
            web.LoadURL("https://www.youtube.com")

        google.Bind(wx.EVT_BUTTON,g)
        ddg.Bind(wx.EVT_BUTTON,dg)
        yt.Bind(wx.EVT_BUTTON,ytt)

fr = mainWindow(None,title="hi lol")
fr.Show()
app.MainLoop()
