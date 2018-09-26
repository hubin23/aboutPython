import wx
import ContractTempRefresher


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "合同模板文件生成器", size=(500, 280))

        panel = wx.Panel(self)

        wx.StaticText(panel, -1, "选择Word文件：", pos=(15, 15))
        self.button1 = wx.Button(panel, -1, '打开', pos=(108, 15), size=(60, 20))
        self.button1.SetDefault()

        wx.StaticText(panel, -1, "数据源文件路径：", pos=(15, 45))
        self.sourcefileNameText = wx.TextCtrl(panel, -1, '此处为数据源文件路径', pos=(120, 45), style=wx.TE_READONLY,
                                              size=(300, 20))

        wx.StaticText(panel, -1, "选择存放路径：", pos=(15, 75))
        self.button3 = wx.Button(panel, -1, '选择', pos=(105, 75), size=(60, 20))

        wx.StaticText(panel, -1, "文件存放路径：", pos=(15, 105))
        self.finalFileSavePath = wx.TextCtrl(panel, -1, '此处为生成文件存放路径', pos=(110, 105), style=wx.TE_READONLY, size=(300, 20))

        wx.StaticText(panel, -1, "合同文件命名：", pos=(15, 135))
        self.generateFileName = wx.TextCtrl(panel, -1, '', pos=(110, 135),size=(120, 20))

        wx.StaticText(panel, -1, "合同文件类型（企业，个人）：", pos=(15, 165))
        self.contractType = wx.TextCtrl(panel, -1, '', pos=(190, 165), size=(50, 20))

        self.confirmButton = wx.Button(panel, -1, '确认生成', pos=(200, 200), size=(80, 30))

        self.Bind(wx.EVT_BUTTON, self.ChooseWordDoc, self.button1)
        self.Bind(wx.EVT_BUTTON, self.ChooseSavePath, self.button3)
        self.Bind(wx.EVT_BUTTON, self.ConfirmGenerate, self.confirmButton)

    def ChooseWordDoc(self, event):
        dlg = wx.FileDialog(self, u"选择文件", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.sourcefileNameText.SetValue(dlg.GetPath())
        dlg.Destroy()

    def ChooseSavePath(self,event):
        dlg = wx.DirDialog(self,u"选择存放目录", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.finalFileSavePath.SetValue(dlg.GetPath())
        dlg.Destroy()

    def ConfirmGenerate(self, event):
        if ContractTempRefresher.execute(self.sourcefileNameText.Value,
                                         self.finalFileSavePath.Value,
                                         self.generateFileName.Value,
                                         self.contractType.Value):
            dlg = wx.MessageDialog(None, u"生成文件成功！", u"生成结果", wx.OK | wx.ICON_INFORMATION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()


app = wx.PySimpleApp()
MainFrame().Show()
app.MainLoop()
