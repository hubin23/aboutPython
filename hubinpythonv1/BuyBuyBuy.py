import wx
import requests
from bs4 import BeautifulSoup

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "BuyBuyBuy",size = (800,500))
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, "商品链接：",(10, 15))
        wx.StaticText(panel,-1,"商品名称：",(10,55))
        self.urlText = wx.TextCtrl(panel,-1,'',pos=(70,15),size=(600,20))
        self.goodsNameText = wx.TextCtrl(panel, -1, '', pos=(70, 55),style=wx.TE_READONLY, size=(600, 20))
        self.button = wx.Button(panel,-1,'确定',pos=(680,15),size=(60,20))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
    def OnClick(self,event):
        inputText = self.urlText.Value
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
        response= requests.request('get',url=inputText,headers=headers)
        soup = BeautifulSoup(response.text)
        goodsTitle = soup.title.string
        self.goodsNameText.SetValue(goodsTitle)
        print(soup.title.string)
app = wx.PySimpleApp()
TestFrame().Show()
app.MainLoop()