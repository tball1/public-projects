import wx
import random

#Simple magic 8-ball program

app = wx.App()

picks = ["Go ahead","Maybe later","If you want","I dont think so..","No","Not a good idea","Sure","Yes","Try again later","Absolutely","Not Clear"]

class MyWindow(wx.Frame):
    def __init__(self,*args,**kw):
        super(MyWindow,self).__init__(*args,**kw)


        ask = wx.Button(self,label="Ask 8-ball",pos=(150,180))
        answer = wx.StaticText(self,label="Awaiting..",pos=(300/2,300/3))
        question = wx.TextCtrl(self,pos=(300/2,300/2))

        def GetRandomAnswer(self):
            pick = random.choice(picks)
            answer.SetLabel(pick)
            return pick

        ask.Bind(wx.EVT_BUTTON,GetRandomAnswer)




window = MyWindow(None,title="The magic 8 ball")
window.Show()

app.MainLoop()
