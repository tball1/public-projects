import wx
import requests
import random
import string
import subprocess
import sys

app = wx.App()

#bgpath = "bg.jpg"

def generateString(len):
    ns = ""
    for i in range(0,len):
        ns = ns + random.choice(string.ascii_letters)
    return ns



class mainFrame(wx.Frame):

        

    def __init__(self,*args,**kw):
        super(mainFrame,self).__init__(*args,**kw)
        
        
        link = wx.TextCtrl(self,value="Enter link..")
        fname = wx.TextCtrl(self,value = "File name",pos=(0,30))
        
        
        
        getbutton = wx.Button(self,-1,"get",pos=(120,0))
        
        
        exitt = wx.Button(self,-1,"Exit",pos=(310,0))
        
        #bg = wx.StaticBitmap(self)
        #bg.SetBitmap(wx.Bitmap(bgpath))
        
        random = wx.CheckBox(self,label="Randomized file names",pos=(0,60))
        openonready = wx.CheckBox(self,label="Open on download",pos=(0,80))
        
        wx.StaticText(self,label="Made by Tball",pos=(0,100))
        
        
        def Clicked(self):
            url = link.GetValue()
            
            if url.startswith("https://") or url.startswith("http://"):
                imagedata = requests.get(url,stream=True)
                filename = fname.GetValue()
                
                if ".jpg" in url:
                    filename = filename+".jpg"
                    
                if ".png" in url:
                    filename = filename+".png"
                        
                if ".gif" in url:
                    filename = filename+".gif"
                
                
                
                if random.GetValue():
                    if ".jpg" in url:
                        filename = generateString(7)+".jpg"
                    
                    if ".png" in url:
                        filename = generateString(7)+".png"
                        
                    if ".gif" in url:
                        filename = generateString(7)+".gif"
                
                open(filename,"a+").close()
                img = open(filename,"wb+")
                for chunk in imagedata.iter_content(chunk_size=512):
                    if chunk:
                        img.write(chunk)
                img.flush()
                img.close()
                
                if openonready.GetValue():
                    subprocess.call("start "+filename,shell=True)
        
        getbutton.Bind(wx.EVT_BUTTON,Clicked)
        exitt.Bind(wx.EVT_BUTTON,sys.exit)



frame = mainFrame(None,title="image dl (by tball)",style=wx.STAY_ON_TOP)

frame.Show()

app.MainLoop()