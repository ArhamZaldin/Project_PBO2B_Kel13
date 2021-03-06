import wx
import wxFilePy
import database as DB
from datetime import datetime

class MainGui(wxFilePy.MainFrame):
    def __init__(self, parent):
        wxFilePy.MainFrame.__init__(self, parent)
        now = datetime.now()
        date = now.strftime("%A, %d %B %Y")
        self.tanggal.SetLabel(date)
        self.dashboard = DashboardGui(parent=self)
        self.dataKeluarga = DataKeluargaGui(parent=self)
        self.rekomDana = RekomDanaGui(parent=self)
        self.rekapData = RekapDataGui(parent=self)
        self.dashboard.Show()
        self.dataKeluarga.Hide()
        self.rekomDana.Hide()
        self.rekapData.Hide()

    def btn_dashboard_click( self, event ):
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.titleMenu.SetLabel("Dashboard")
        self.dashboard.Show()
        self.dataKeluarga.Hide()
        self.rekomDana.Hide()
        self.rekapData.Hide()

        if self.dashboard.keluargaRendah.GetNumberRows() > 0:
            self.dashboard.keluargaRendah.DeleteRows(pos=0, numRows=self.dashboard.keluargaRendah.GetNumberRows())

        lowData = DB.dataKeluarga().lowerTotal()
        count = 0
        for row in lowData:
            self.dashboard.keluargaRendah.AppendRows(1)
            self.dashboard.keluargaRendah.SetRowSize(count, 30)
            self.dashboard.keluargaRendah.SetColSize(0, 280)
            self.dashboard.keluargaRendah.SetColSize(1, 100)
            self.dashboard.keluargaRendah.SetCellAlignment(count, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
            self.dashboard.keluargaRendah.SetCellValue(count, 0, row[1])
            self.dashboard.keluargaRendah.SetCellValue(count, 1, f"Rp{row[3]}")
            count += 1

        if self.dashboard.bantuanBaru.GetNumberRows() > 0:
            self.dashboard.bantuanBaru.DeleteRows(pos=0, numRows=self.dashboard.bantuanBaru.GetNumberRows())

        data = DB.rekap().newestData()
        count = 0
        for row in range(len(data[0])):
            self.dashboard.bantuanBaru.AppendRows(1)
            self.dashboard.bantuanBaru.SetRowSize(count, 30)
            self.dashboard.bantuanBaru.SetColSize(0, 280)
            self.dashboard.bantuanBaru.SetColSize(1, 100)
            self.dashboard.bantuanBaru.SetCellAlignment(count, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
            self.dashboard.bantuanBaru.SetCellValue(count, 0, data[0][row][0][0])
            self.dashboard.bantuanBaru.SetCellValue(count, 1, f"Rp{data[1][row][2]}")
            count += 1

    def btn_keluarga_click( self, event ):
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_keluarga.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.titleMenu.SetLabel("Data Keluarga")
        self.dataKeluarga.Show()
        self.dataKeluarga.filterSatu.SetSelection(0)
        self.dataKeluarga.filterDua.Hide()
        self.dataKeluarga.filterDua.SetSelection(0)
        self.dataKeluarga.filterValue.Hide()
        self.dataKeluarga.filterValue.SetValue("")
        self.dashboard.Hide()
        self.rekomDana.Hide()
        self.rekapData.Hide()

        lenCols = self.dataKeluarga.dataKeluargaGrid.GetNumberCols()

        if self.dataKeluarga.dataKeluargaGrid.GetNumberRows() > 0:
            self.dataKeluarga.dataKeluargaGrid.DeleteRows(pos=0, numRows=self.dataKeluarga.dataKeluargaGrid.GetNumberRows())
        data = DB.dataKeluarga().showKeluarga()
        count = 0
        for row in data:
            noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
            self.dataKeluarga.dataKeluargaGrid.AppendRows(1)
            self.dataKeluarga.dataKeluargaGrid.SetRowSize(count, 30)
            for col in range(lenCols):
                self.dataKeluarga.dataKeluargaGrid.SetColSize(col, 162)
                self.dataKeluarga.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
            self.dataKeluarga.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
            self.dataKeluarga.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
            self.dataKeluarga.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
            self.dataKeluarga.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{totalPendapatan}")
            self.dataKeluarga.dataKeluargaGrid.SetCellValue(count, 4, alamat)
            count += 1

    def btn_rekom_click( self, event ):
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_rekomen.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_rekap.png"))
        self.titleMenu.SetLabel("Rekomendasi Dana")
        self.rekomDana.Show()
        self.rekomDana.umrInput.SetValue("")
        self.rekomDana.rekomGrid.Hide()
        self.dashboard.Hide()
        self.dataKeluarga.Hide()
        self.rekapData.Hide()

    def btn_rekap_click( self, event ):
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_rekap.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        self.titleMenu.SetLabel("Rekap Bantuan")
        self.rekapData.Show()
        self.dashboard.Hide()
        self.dataKeluarga.Hide()
        self.rekomDana.Hide()
        self.rekapData.rekapOption.Show()
        self.rekapData.riwayatBantuan.Hide()

    def searchEnter( self, event ):
        noKK = self.searchEngine.GetValue()
        if DB.dataKeluarga().searchDetailKeluarga(noKK):
            searchModal(parent=self, noKK=noKK).Show()
        else:
            wx.MessageBox("Data yang Anda Masukkan Tidak Ada!", "KESALAHAN")

class DashboardGui(wxFilePy.dashboardPanel):
    def __init__(self, parent):
        wxFilePy.dashboardPanel.__init__(self, parent)

        lowData = DB.dataKeluarga().lowerTotal()
        count = 0
        for row in lowData:
            self.keluargaRendah.AppendRows(1)
            self.keluargaRendah.SetRowSize(count, 30)
            self.keluargaRendah.SetColSize(0, 280)
            self.keluargaRendah.SetColSize(1, 100)
            self.keluargaRendah.SetCellAlignment(count, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
            self.keluargaRendah.SetCellValue(count, 0, row[1])
            self.keluargaRendah.SetCellValue(count, 1, f"Rp{row[3]}")
            count += 1

        data = DB.rekap().newestData()
        count = 0
        for row in range(len(data[0])):
            self.bantuanBaru.AppendRows(1)
            self.bantuanBaru.SetRowSize(count, 30)
            self.bantuanBaru.SetColSize(0, 280)
            self.bantuanBaru.SetColSize(1, 100)
            self.bantuanBaru.SetCellAlignment(count, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
            self.bantuanBaru.SetCellValue(count, 0, data[0][row][0][0])
            self.bantuanBaru.SetCellValue(count, 1, f"Rp{data[1][row][2]}")
            count += 1

class DataKeluargaGui(wxFilePy.dataKeluargaPanel):
    def __init__(self, parent):
        wxFilePy.dataKeluargaPanel.__init__(self, parent)
        self.lenCols = self.dataKeluargaGrid.GetNumberCols()

    def filterOneSelected( self, event ):
        self.filterValue.SetValue("")
        value = self.filterSatu.GetSelection()
        if value == 0:
            self.filterDua.Hide()
            self.filterValue.Hide()
            if self.dataKeluargaGrid.GetNumberRows() > 0:
                self.dataKeluargaGrid.DeleteRows(pos=0, numRows=self.dataKeluargaGrid.GetNumberRows())
            data = DB.dataKeluarga().showKeluarga()
            count = 0
            for row in data:
                noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                self.dataKeluargaGrid.AppendRows(1)
                self.dataKeluargaGrid.SetRowSize(count, 30)
                for col in range(self.lenCols):
                    self.dataKeluargaGrid.SetColSize(col, 162)
                    self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                self.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
                self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                self.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
                self.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{totalPendapatan}")
                self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                count += 1

        else:
            self.filterDua.Show()
            self.filterDua.SetSelection(0)
            self.filterValue.Show()

    def filterValueChange( self, event ):
        if self.filterValue.GetValue():
            if self.dataKeluargaGrid.GetNumberRows() > 0:
                self.dataKeluargaGrid.DeleteRows(pos=0, numRows=self.dataKeluargaGrid.GetNumberRows())

        value = self.filterSatu.GetSelection()
        if value == 1 and self.filterValue.GetValue():
            if self.filterDua.GetSelection() == 0:
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByTotalAbove(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 162)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
                    self.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{totalPendapatan}")
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

            elif self.filterDua.GetSelection() == 1:
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByTotalBelow(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 162)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, str(noKK))
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, str(anggotaKeluarga))
                    self.dataKeluargaGrid.SetCellValue(count, 3, str(totalPendapatan))
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

        elif value == 2 and self.filterValue.GetValue():
            if self.filterDua.GetSelection() == 0:
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByAnggotaAbove(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 162)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, str(noKK))
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, str(anggotaKeluarga))
                    self.dataKeluargaGrid.SetCellValue(count, 3, str(totalPendapatan))
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

            elif self.filterDua.GetSelection() == 1:
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByAnggotaBelow(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 162)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, str(noKK))
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, str(anggotaKeluarga))
                    self.dataKeluargaGrid.SetCellValue(count, 3, str(totalPendapatan))
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

    def btn_tambahData( self, event ):
        addModal(parent=self).ShowModal()

    def btn_ubahData( self, event ):
        changeModal(parent=self).ShowModal()

    def btn_hapusData( self, event ):
        delModal(parent=self).ShowModal()

class addModal(wxFilePy.addData):
    def __init__(self, parent):
        wxFilePy.addData.__init__(self, parent)

    def btn_addKeluarga( self, event ):
        noKK = self.nomorKK.GetValue()
        kepalaKeluarga = self.kepKeluarga.GetValue()
        anggota = self.jumAnggota.GetValue()
        total = self.totalPendapatan.GetValue()
        alamat = self.alamatBaru.GetValue()
        nikKep = self.nikKepala.GetValue()
        insert = DB.anggotaKeluarga().addKeluarga(noKK, kepalaKeluarga, anggota, total, alamat, nikKep)
        if insert:
            wx.MessageBox("Data Berhasil Ditambahkan!", "INFORMASI")
        else:
            wx.MessageBox("Data yang Anda Masukkan Sudah Ada atau \n Form Tidak Boleh Kosong", "KESALAHAN")

class changeModal(wxFilePy.changeData):
    def __init__(self, parent):
        wxFilePy.changeData.__init__(self, parent)
        self.ubahNotebook.SetPageText(0, "Anggota Keluarga")
        self.ubahNotebook.SetPageText(1, "Total Pendapatan")
        self.ubahNotebook.SetPageText(2, "Alamat")

    def btn_ubahAnggota( self, event ):
        noKK = self.nomorKK_anggota.GetValue()
        nama = self.namaAnggota.GetValue()
        nik = self.nikAnggota.GetValue()
        insert = DB.anggotaKeluarga().setAnggota(nik, nama, noKK)
        if insert:
            DB.anggotaKeluarga().updateAnggota(noKK)
            wx.MessageBox("Data Berhasil Ditambahkan!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK Tidak Ditemukan atau \n NIK Sudah Ada atau \n Form Tidak Boleh Kosong", "KESALAHAN")

    def btn_ubahTotal( self, event ):
        noKK = self.nomorKK_total.GetValue()
        total = self.totalBaru.GetValue()
        insert = DB.dataKeluarga().updateTotalPendapatan(noKK, total)
        if insert:
            wx.MessageBox("Data Berhasil Diubah!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK Tidak Ditemukan atau \n Form Tidak Boleh Kosong", "KESALAHAN")

    def btn_ubahAlamat( self, event ):
        noKK = self.nomorKK_alamat.GetValue()
        alamat = self.alamatBaru.GetValue()
        insert = DB.dataKeluarga().updateAlamat(noKK, alamat)
        if insert:
            wx.MessageBox("Data Berhasil Diubah!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK Tidak Ditemukan atau \n Form Tidak Boleh Kosong", "KESALAHAN")

class delModal(wxFilePy.delData):
    def __init__(self, parent):
        wxFilePy.delData.__init__(self, parent)
        self.delNotebook.SetPageText(0, "Data Keluarga")
        self.delNotebook.SetPageText(1, "Anggota Keluarga")

    def btn_delKeluarga( self, event ):
        noKK = self.nomorKK_keluarga.GetValue()
        insert = DB.dataKeluarga().delKeluarga(noKK)
        if insert:
            wx.MessageBox("Data Berhasil Dihapus!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK Tidak Ditemukan atau \n Form Tidak Boleh Kosong", "KESALAHAN")

    def btn_delAnggota( self, event ):
        noKK = self.nomorKK_anggota.GetValue()
        nik = self.nikAnggota.GetValue()
        insert = DB.anggotaKeluarga().delAnggota(noKK, nik)
        if insert:
            wx.MessageBox("Data Berhasil Dihapus!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK atau NIK Tidak Ditemukan atau \n Form Tidak Boleh Kosong", "KESALAHAN")

class RekomDanaGui(wxFilePy.rekomDanaPanel):
    def __init__(self, parent):
        wxFilePy.rekomDanaPanel.__init__(self, parent)

    def umrChange( self, event ):
        if self.rekomGrid.GetNumberRows() > 0:
            self.rekomGrid.DeleteRows(pos=0, numRows=self.rekomGrid.GetNumberRows())
        lenCols = self.rekomGrid.GetNumberCols()
        umrValue = self.umrInput.GetValue()
        data = DB.bantuan().analyze(umrValue)
        if data:
            self.rekomGrid.Show()
            count = 0
            for row in range(len(data[0])):
                self.rekomGrid.AppendRows(1)
                self.rekomGrid.SetRowSize(count, 30)
                for col in range(lenCols):
                    self.rekomGrid.SetColSize(col, 205)
                    self.rekomGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                self.rekomGrid.SetCellValue(count, 0, f"{data[0][row][0]}")
                self.rekomGrid.SetCellValue(count, 1, data[0][row][1])
                self.rekomGrid.SetCellValue(count, 2, data[0][row][4])
                self.rekomGrid.SetCellValue(count, 3, f"Rp{data[1][row]}")
                self.rekomGrid.SetCellFont(count, 3, wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Roboto"))
                count += 1

class RekapDataGui(wxFilePy.rekapDataPanel):
    def __init__(self, parent):
        wxFilePy.rekapDataPanel.__init__(self, parent)

    def catatBantuan_btn( self, event ):
        catatModal(parent=self).ShowModal()

    def riwayatBantuan_btn( self, event ):
        self.riwayatBantuan.Show()
        self.riwayatBantuan.Enable()
        self.rekapOption.Hide()
        lenCols = self.rekapGrid.GetNumberCols()
        if self.rekapGrid.GetNumberRows() > 0:
            self.rekapGrid.DeleteRows(pos=0, numRows=self.rekapGrid.GetNumberRows())
        data = DB.rekap().riwayatBantuan()
        if data:
            count = 0
            for row in range(len(data[0])):
                self.rekapGrid.AppendRows(1)
                self.rekapGrid.SetRowSize(count, 30)
                for col in range(lenCols):
                    self.rekapGrid.SetColSize(col, 205)
                    self.rekapGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                self.rekapGrid.SetCellValue(count, 0, f"{data[1][row][1]}")
                self.rekapGrid.SetCellValue(count, 1, data[0][row][0][0])
                self.rekapGrid.SetCellValue(count, 2, f"Rp{data[1][row][2]}")
                self.rekapGrid.SetCellValue(count, 3, data[1][row][3])
                count += 1

class catatModal(wxFilePy.catatData):
    def __init__(self, parent):
        wxFilePy.catatData.__init__(self, parent)

    def addCatat_btn( self, event ):
        noKK = self.nomorKK.GetValue()
        dana = self.danaBeri.GetValue()
        insert = DB.rekap().catatBantuan(noKK, dana)
        if insert:
            wx.MessageBox("Data Berhasil Ditambahkan!", "INFORMASI")
        else:
            wx.MessageBox("Nomor KK Tidak Ditemukan atau \n Form Tidak Boleh Kosong", "KESALAHAN")

class searchModal(wxFilePy.searchData):
    def __init__(self, parent, noKK):
        wxFilePy.searchData.__init__(self, parent)
        data = DB.dataKeluarga().searchDetailKeluarga(noKK)
        for x in data[0]:
            nomorKK, kepala, anggota, total, alamat = x
            self.nomorKK.SetLabel(f"{nomorKK}")
            self.kepKeluarga.SetLabel(kepala)
            self.anggota.SetLabel(f"{anggota}")
            self.total.SetLabel(f"Rp{total}")
            self.alamat.SetLabel(alamat)

        if self.searchGrid.GetNumberRows() > 0:
            self.searchGrid.DeleteRows(pos=0, numRows=self.searchGrid.GetNumberRows())

        lenCols = self.searchGrid.GetNumberCols()

        count = 0
        for y in data[1]:
            nik, nama, nokk = y
            self.searchGrid.AppendRows(1)
            self.searchGrid.SetRowSize(count, 30)
            for col in range(lenCols):
                self.searchGrid.SetColSize(col, 320)
                self.searchGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
            self.searchGrid.SetCellValue(count, 0, f"{nik}")
            self.searchGrid.SetCellValue(count, 1, nama)
            count += 1

app = wx.App()
frame = MainGui(parent=None)
frame.Show()
app.MainLoop()
DB.Database().close()