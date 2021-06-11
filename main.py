import wx
import wxFilePy

class Gui(wxFilePy.MainFrame):
    def __init__(self, parent):
        wxFilePy.MainFrame.__init__(self, parent)
        self.dashboard = wxFilePy.dashboardPanel(parent=self)
        self.dataKeluarga = wxFilePy.dataKeluargaPanel(parent=self)
        self.dashboard.Show()
        self.dataKeluarga.Hide()

    def btn_dashboard_click( self, event ):
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.dashboard.Show()
        self.dataKeluarga.Hide()

    def btn_keluarga_click( self, event ):
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_keluarga.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.dataKeluarga.Show()
        self.dashboard.Hide()

    def btn_rekom_click( self, event ):
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_rekomen.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.dashboard.Hide()
        self.dataKeluarga.Hide()

    def btn_rekap_click( self, event ):
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_rekap.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.dashboard.Hide()
        self.dataKeluarga.Hide()

app = wx.App()
frame = Gui(parent=None)
frame.Show()
app.MainLoop()