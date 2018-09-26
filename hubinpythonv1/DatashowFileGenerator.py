import wx
import os
import DatashowFileRefresher
import configparser


def ConfirmSetting(dict):
    print('dcece')


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "数据展示页面文件生成器", size=(500, 350))

        panel = wx.Panel(self)

        wx.StaticText(panel, -1, "选择Excel文件：", pos=(15, 15))
        self.button1 = wx.Button(panel, -1, '打开', pos=(105, 15), size=(60, 20))
        self.button1.SetDefault()

        wx.StaticText(panel, -1, "数据源文件路径：", pos=(15, 45))
        self.sourcefileNameText = wx.TextCtrl(panel, -1, '此处为数据源文件路径', pos=(120, 45), style=wx.TE_READONLY,
                                              size=(300, 20))

        wx.StaticText(panel, -1, "选择模板文件：", pos=(15, 90))
        self.button2 = wx.Button(panel, -1, '打开', pos=(105, 90), size=(60, 20))

        wx.StaticText(panel, -1, "模板页面文件路径：", pos=(15, 120))
        self.templateFileNameText = wx.TextCtrl(panel, -1, '此处为模板页面文件路径', pos=(130, 120), style=wx.TE_READONLY,
                                                size=(300, 20))

        wx.StaticText(panel, -1, "选择存放路径：", pos=(15, 165))
        self.button3 = wx.Button(panel, -1, '选择', pos=(105, 165), size=(60, 20))

        wx.StaticText(panel, -1, "文件存放路径：", pos=(15, 195))
        self.finalFileSavePath = wx.TextCtrl(panel, -1, '此处为生成文件存放路径', pos=(110, 195), style=wx.TE_READONLY,
                                                size=(300, 20))

        self.settingButton = wx.Button(panel, -1, '数据源设置', pos=(100, 240), size=(100, 40))
        self.confirmButton = wx.Button(panel, -1, '确认生成', pos=(260, 240), size=(100, 40))

        self.Bind(wx.EVT_BUTTON, self.ChooseExcel, self.button1)
        self.Bind(wx.EVT_BUTTON, self.ChooseTemplate, self.button2)
        self.Bind(wx.EVT_BUTTON, self.ChooseSavePath, self.button3)
        self.Bind(wx.EVT_BUTTON, self.SettingDataSource, self.settingButton)
        self.Bind(wx.EVT_BUTTON, self.ConfirmGenerate, self.confirmButton)

    def ChooseExcel(self, event):
        dlg = wx.FileDialog(self, u"选择文件", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.sourcefileNameText.SetValue(dlg.GetPath())
        dlg.Destroy()

    def ChooseTemplate(self, event):
        dlg = wx.FileDialog(self, u"选择文件", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.templateFileNameText.SetValue(dlg.GetPath())
        dlg.Destroy()

    def ChooseSavePath(self,event):
        dlg = wx.DirDialog(self,u"选择存放目录", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.finalFileSavePath.SetValue(dlg.GetPath())
        dlg.Destroy()

    def showSettingDiag(self,event):
        dialog = wx.Dialog(self, title='数据源设置', size=(750, 350))

        settingDialogInfo = {}

        modifyDataSourceInfo = {}

        # 第一列

        wx.StaticText(dialog, -1, "数据截止时间:", pos=(15, 5))
        self.newDataDeadLine = wx.TextCtrl(dialog, -1, '', pos=(100, 5), size=(40, 20))
        if self.newDataDeadLine.Value != '':
            modifyDataSourceInfo['newDataDeadLine'] = self.newDataDeadLine.Value

        wx.StaticText(dialog, -1, "统计起止时间:", pos=(15, 35))
        self.newValidDuringTime = wx.TextCtrl(dialog, -1, '', pos=(100, 35), size=(40, 20))
        if self.newValidDuringTime.Value != '':
            modifyDataSourceInfo['newValidDuringTime'] = self.newValidDuringTime.Value

        wx.StaticText(dialog, -1, "总交易金额:", pos=(15, 65))
        self.newTotalAmount = wx.TextCtrl(dialog, -1, '', pos=(100, 65), size=(40, 20))
        if self.newTotalAmount.Value != '':
            modifyDataSourceInfo['newTotalAmount'] = self.newTotalAmount.Value

        wx.StaticText(dialog, -1, "总交易笔数:", pos=(15, 95))
        self.newTotalTradeCount = wx.TextCtrl(dialog, -1, '', pos=(100, 95), size=(40, 20))
        if self.newTotalTradeCount.Value != '':
            modifyDataSourceInfo['newTotalTradeCount'] = self.newTotalTradeCount.Value

        wx.StaticText(dialog, -1, "总用户数:", pos=(15, 125))
        self.newTotalUser = wx.TextCtrl(dialog, -1, '', pos=(100, 125), size=(40, 20))
        if self.newTotalUser.Value != '':
            modifyDataSourceInfo['newTotalUser'] = self.newTotalUser.Value

        wx.StaticText(dialog, -1, "总收益:", pos=(15, 155))
        self.newTotalIncome = wx.TextCtrl(dialog, -1, '', pos=(100, 155), size=(40, 20))
        if self.newTotalIncome.Value != '':
            modifyDataSourceInfo['newTotalIncome'] = self.newTotalIncome.Value

        wx.StaticText(dialog, -1, "本周兑付数:", pos=(15, 185))
        self.newWeekReturnProjectCount = wx.TextCtrl(dialog, -1, '', pos=(100, 185), size=(40, 20))
        if self.newWeekReturnProjectCount.Value != '':
            modifyDataSourceInfo['newWeekReturnProjectCount'] = self.newWeekReturnProjectCount.Value

        wx.StaticText(dialog, -1, "本周兑付金额:", pos=(15, 215))
        self.newWeekReturnAmount = wx.TextCtrl(dialog, -1, '', pos=(100, 215), size=(40, 20))
        if self.newWeekReturnAmount.Value != '':
            modifyDataSourceInfo['newWeekReturnAmount'] = self.newWeekReturnAmount.Value

        # 第二列

        wx.StaticText(dialog, -1, "60前用户数:", pos=(180, 5))
        self.newEarly60Count = wx.TextCtrl(dialog, -1, '', pos=(255, 5), size=(40, 20))
        if self.newEarly60Count.Value != '':
            modifyDataSourceInfo['newEarly60Count'] = self.newEarly60Count.Value

        wx.StaticText(dialog, -1, "60后用户数:", pos=(180, 35))
        self.newAfter60Count = wx.TextCtrl(dialog, -1, '', pos=(255, 35), size=(40, 20))
        if self.newAfter60Count.Value != '':
            modifyDataSourceInfo['newAfter60Count'] = self.newAfter60Count.Value

        wx.StaticText(dialog, -1, "70后用户数:", pos=(180, 65))
        self.newAfter70Count = wx.TextCtrl(dialog, -1, '', pos=(255, 65), size=(40, 20))
        if self.newAfter70Count.Value != '':
            modifyDataSourceInfo['newAfter70Count'] = self.newAfter70Count.Value

        wx.StaticText(dialog, -1, "80后用户数:", pos=(180, 95))
        self.newAfter80Count = wx.TextCtrl(dialog, -1, '', pos=(255, 95), size=(40, 20))
        if self.newAfter80Count.Value != '':
            modifyDataSourceInfo['newAfter80Count'] = self.newAfter80Count.Value

        wx.StaticText(dialog, -1, "90后用户数:", pos=(180, 125))
        self.newAfter90Count = wx.TextCtrl(dialog, -1, '', pos=(255, 125), size=(40, 20))
        if self.newAfter90Count.Value != '':
            modifyDataSourceInfo['newAfter90Count'] = self.newAfter90Count.Value

        # 第三列

        wx.StaticText(dialog, -1, "15天产品数:", pos=(335, 5))
        self.new15ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 5), size=(40, 20))
        if self.new15ProductCount.Value != '':
            modifyDataSourceInfo['new15ProductCount'] = self.new15ProductCount.Value

        wx.StaticText(dialog, -1, "30天产品数:", pos=(335, 35))
        self.new30ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 35), size=(40, 20))
        if self.new30ProductCount.Value != '':
            modifyDataSourceInfo['new30ProductCount'] = self.new30ProductCount.Value

        wx.StaticText(dialog, -1, "60天产品数:", pos=(335, 65))
        self.new60ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 65), size=(40, 20))
        if self.new60ProductCount.Value != '':
            modifyDataSourceInfo['new60ProductCount'] = self.new60ProductCount.Value

        wx.StaticText(dialog, -1, "90天产品数:", pos=(335, 95))
        self.new90ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 95), size=(40, 20))
        if self.new90ProductCount.Value != '':
            modifyDataSourceInfo['new90ProductCount'] = self.new90ProductCount.Value

        wx.StaticText(dialog, -1, "180天产品数:", pos=(335, 125))
        self.new180ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 125), size=(40, 20))
        if self.new180ProductCount.Value != '':
            modifyDataSourceInfo['new180ProductCount'] = self.new180ProductCount.Value

        wx.StaticText(dialog, -1, "360天产品数:", pos=(335, 155))
        self.new360ProductCount = wx.TextCtrl(dialog, -1, '', pos=(415, 155), size=(40, 20))
        if self.new360ProductCount.Value != '':
            modifyDataSourceInfo['new360ProductCount'] = self.new360ProductCount.Value

        # 第四列

        wx.StaticText(dialog, -1, "年化<7%产品数:", pos=(500, 5))
        self.productSmallerThan7Count = wx.TextCtrl(dialog, -1, '', pos=(635, 5), size=(40, 20))
        if self.productSmallerThan7Count.Value != '':
            modifyDataSourceInfo['productSmallerThan7Count'] = self.productSmallerThan7Count.Value

        wx.StaticText(dialog, -1, "7%<年化<8%产品数:", pos=(500, 35))
        self.product7to8Count = wx.TextCtrl(dialog, -1, '', pos=(635, 35), size=(40, 20))
        if self.product7to8Count.Value != '':
            modifyDataSourceInfo['product7to8Count'] = self.product7to8Count.Value

        wx.StaticText(dialog, -1, "8%<年化<10%产品数:", pos=(500, 65))
        self.product8to10Count = wx.TextCtrl(dialog, -1, '', pos=(635, 65), size=(40, 20))
        if self.product8to10Count.Value != '':
            modifyDataSourceInfo['product8to10Count'] = self.product8to10Count.Value

        wx.StaticText(dialog, -1, "年化>10%产品数:", pos=(500, 95))
        self.productBiggerThan10Count = wx.TextCtrl(dialog, -1, '', pos=(635, 95), size=(40, 20))
        if self.productBiggerThan10Count.Value != '':
            modifyDataSourceInfo['productBiggerThan10Count'] = self.productBiggerThan10Count.Value

        wx.StaticText(dialog, -1, "*注意：", pos=(500, 133))
        wx.StaticText(dialog, -1, "1、填入项为需修改的单元格", pos=(505, 150))

        wx.settingConfirmButton = wx.Button(dialog, -1, '确认', pos=(550, 220), size=(100, 40))

        settingDialogInfo['dialog'] = dialog
        settingDialogInfo['modifyDataSourceInfo'] = modifyDataSourceInfo

        # dialog.ShowModal()

        self.Bind(wx.EVT_BUTTON, ConfirmSetting(dict=modifyDataSourceInfo), wx.settingConfirmButton)

        return settingDialogInfo

    def SettingDataSource(self,event):
        settingDialogInfo = self.showSettingDiag(self)
        dialog = settingDialogInfo['dialog']

        dialog.ShowModal()

    def ConfirmGenerate(self, event):
        if DatashowFileRefresher.execute(self.sourcefileNameText.Value, self.templateFileNameText.Value, self.finalFileSavePath.Value):
            dlg = wx.MessageDialog(None, u"生成文件成功！", u"生成结果", wx.OK | wx.ICON_INFORMATION)
            if dlg.ShowModal() == wx.ID_YES:
                self.Close(True)
            dlg.Destroy()


app = wx.PySimpleApp()
MainFrame().Show()
app.MainLoop()
