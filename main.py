import wx
import wxFilePy
import database as DB

class MainGui(wxFilePy.MainFrame):
    def __init__(self, parent):
        wxFilePy.MainFrame.__init__(self, parent)
        self.dashboard = DashboardGui(parent=self)
        self.dataKeluarga = DataKeluargaGui(parent=self)
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
        rekomModal(parent=self).ShowModal()

    def btn_rekap_click( self, event ):
        self.rekap_btn.SetBitmap(wx.Bitmap("picture/btn_pressed_rekap.png"))
        self.dashboard_btn.SetBitmap(wx.Bitmap("picture/btn_dashboard.png"))
        self.keluarga_btn.SetBitmap(wx.Bitmap("picture/btn_keluarga.png"))
        self.rekom_btn.SetBitmap(wx.Bitmap("picture/btn_rekomen.png"))
        rekapModal(parent=self).ShowModal()

    def searchEnter( self, event ):
        noKK = self.search.GetValue()
        if DB.dataKeluarga().isAvailable(noKK):
            searchModal(parent=self, noKK=noKK).Show()

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
            self.keluargaRendah.SetCellValue(count, 1, f"Rp{int(row[3])}")
            count+=1

        data = DB.rekap().showHistory()
        count = 0
        for row in range(len(data[0])):
            self.bantuanBaru.AppendRows(1)
            self.bantuanBaru.SetRowSize(count, 30)
            self.bantuanBaru.SetColSize(0, 280)
            self.bantuanBaru.SetColSize(1, 100)
            self.bantuanBaru.SetCellAlignment(count, 1, wx.ALIGN_RIGHT, wx.ALIGN_CENTER)
            self.bantuanBaru.SetCellValue(count, 0, data[0][row][0][0])
            self.bantuanBaru.SetCellValue(count, 1, f"Rp{int(data[1][row][2])}")
            count+=1

class DataKeluargaGui(wxFilePy.dataKeluargaPanel):
    def __init__(self, parent):
        wxFilePy.dataKeluargaPanel.__init__(self, parent)
        self.filterDua.Hide()
        self.filterValue.Hide()

        columnName = ["Nomor KK", "Kepala Keluarga", "Anggota Keluarga", "Total Pendapatan", "Alamat"]
        self.lenCols = len(columnName)
        self.dataKeluargaGrid.AppendCols(self.lenCols)
        for col in range(self.lenCols):
            self.dataKeluargaGrid.SetColLabelValue(col, columnName[col])

        if self.dataKeluargaGrid.GetNumberRows() > 0:
            self.dataKeluargaGrid.DeleteRows(pos=0, numRows=self.dataKeluargaGrid.GetNumberRows())
        data = DB.dataKeluarga().showKeluarga()
        count = 0
        for row in data:
            noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
            self.dataKeluargaGrid.AppendRows(1)
            self.dataKeluargaGrid.SetRowSize(count, 30)
            for col in range(self.lenCols):
                self.dataKeluargaGrid.SetColSize(col, 160)
                self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
            self.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
            self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
            self.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
            self.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{int(totalPendapatan)}")
            self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
            count += 1

    def filterOneSelected( self, event ):
        value = self.filterSatu.GetValue()
        if value == "Tidak Ada":
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
                    self.dataKeluargaGrid.SetColSize(col, 160)
                    self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                self.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
                self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                self.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
                self.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{int(totalPendapatan)}")
                self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                count += 1

        elif value == "Total Pendapatan":
            self.filterDua.Show()
            self.filterValue.Show()
            if self.filterValue.GetValue() != "":
                self.filterValueChange(event=None)

        elif value == "Anggota Keluarga":
            self.filterDua.Show()
            self.filterValue.Show()
            if self.filterValue.GetValue() != "":
                self.filterValueChange(event=None)

    def filterValueChange( self, event ):
        if self.dataKeluargaGrid.GetNumberRows() > 0:
            self.dataKeluargaGrid.DeleteRows(pos=0, numRows=self.dataKeluargaGrid.GetNumberRows())
        value = self.filterSatu.GetValue()
        if value == "Total Pendapatan":
            if self.filterDua.GetValue() == "Lebih Dari":
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByTotalAbove(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 160)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, f"{noKK}")
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, f"{anggotaKeluarga}")
                    self.dataKeluargaGrid.SetCellValue(count, 3, f"Rp{int(totalPendapatan)}")
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

            elif self.filterDua.GetValue() == "Kurang Dari":
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByTotalBelow(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 160)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, str(noKK))
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, str(anggotaKeluarga))
                    self.dataKeluargaGrid.SetCellValue(count, 3, str(totalPendapatan))
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

        elif value == "Anggota Keluarga":
            if self.filterDua.GetValue() == "Lebih Dari":
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByAnggotaAbove(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 160)
                        self.dataKeluargaGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                    self.dataKeluargaGrid.SetCellValue(count, 0, str(noKK))
                    self.dataKeluargaGrid.SetCellValue(count, 1, kepalaKeluarga)
                    self.dataKeluargaGrid.SetCellValue(count, 2, str(anggotaKeluarga))
                    self.dataKeluargaGrid.SetCellValue(count, 3, str(totalPendapatan))
                    self.dataKeluargaGrid.SetCellValue(count, 4, alamat)
                    count += 1

            elif self.filterDua.GetValue() == "Kurang Dari":
                filterVal = self.filterValue.GetValue()
                data = DB.dataKeluarga().readByAnggotaBelow(filterVal)
                count = 0
                for row in data:
                    noKK, kepalaKeluarga, anggotaKeluarga, totalPendapatan, alamat = row
                    self.dataKeluargaGrid.AppendRows(1)
                    self.dataKeluargaGrid.SetRowSize(count, 30)
                    for col in range(self.lenCols):
                        self.dataKeluargaGrid.SetColSize(col, 160)
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
        insert = DB.dataKeluarga().setKeluarga(noKK, kepalaKeluarga, anggota, total, alamat)
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

class searchModal(wxFilePy.searchData):
    def __init__(self, parent, noKK):
        wxFilePy.searchData.__init__(self, parent)
        data = DB.dataKeluarga().searchDetailKeluarga(noKK)
        for x in data[0]:
            nomorKK, kepala, anggota, total, alamat = x
            self.nomorKK.SetLabel(f"{nomorKK}")
            self.kepKeluarga.SetLabel(kepala)
            self.anggota.SetLabel(f"{anggota}")
            self.total.SetLabel(f"Rp{int(total)}")
            self.alamat.SetLabel(alamat)

        columnName = ["Nomor Induk Keluarga", "Nama Lengkap"]
        lenCols = len(columnName)
        self.searchGrid.AppendCols(lenCols)
        for col in range(lenCols):
            self.searchGrid.SetColLabelValue(col, columnName[col])

        if self.searchGrid.GetNumberRows() > 0:
            self.searchGrid.DeleteRows(pos=0, numRows=self.searchGrid.GetNumberRows())

        count = 0
        for y in data[1]:
            nik, nama, nokk = y
            self.searchGrid.AppendRows(1)
            self.searchGrid.SetRowSize(count, 30)
            for col in range(lenCols):
                self.searchGrid.SetColSize(col, 200)
                self.searchGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
            self.searchGrid.SetCellValue(count, 0, f"{nik}")
            self.searchGrid.SetCellValue(count, 1, nama)
            count += 1

class rekomModal(wxFilePy.rekomDana):
    def __init__(self, parent):
        wxFilePy.rekomDana.__init__(self, parent)
        columnName = ["Nomor KK", "Kepala Keluarga", "Alamat", "Saran Bantuan"]
        self.lenCols = len(columnName)
        self.rekomGrid.AppendCols(self.lenCols)
        for col in range(self.lenCols):
            self.rekomGrid.SetColLabelValue(col, columnName[col])

    def umrChange( self, event ):
        if self.rekomGrid.GetNumberRows() > 0:
            self.rekomGrid.DeleteRows(pos=0, numRows=self.rekomGrid.GetNumberRows())
        umrValue = self.umrInput.GetValue()
        data = DB.bantuan().analyze(umrValue)
        if data:
            count = 0
            for row in range(len(data[0])):
                self.rekomGrid.AppendRows(1)
                self.rekomGrid.SetRowSize(count, 30)
                for col in range(self.lenCols):
                    self.rekomGrid.SetColSize(col, 150)
                    self.rekomGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
                self.rekomGrid.SetCellValue(count, 0, f"{data[0][row][0]}")
                self.rekomGrid.SetCellValue(count, 1, data[0][row][1])
                self.rekomGrid.SetCellValue(count, 2, data[0][row][4])
                self.rekomGrid.SetCellValue(count, 3, f"Rp{data[1][row]}")
                self.rekomGrid.SetCellTextColour(count, 3, colour="black")
                count += 1

class rekapModal(wxFilePy.rekapData):
    def __init__(self, parent):
        wxFilePy.rekapData.__init__(self, parent)

        columnName = ["Nomor KK", "Besar Bantuan"]
        self.lenCols = len(columnName)
        self.rekapGrid.AppendCols(self.lenCols)
        for col in range(self.lenCols):
            self.rekapGrid.SetColLabelValue(col, columnName[col])

        if self.rekapGrid.GetNumberRows() > 0:
            self.rekapGrid.DeleteRows(pos=0, numRows=self.rekapGrid.GetNumberRows())
        data = DB.rekap().riwayatBantuan()
        count = 0
        for row in data:
            id, noKK, bantuan = row
            self.rekapGrid.AppendRows(1)
            self.rekapGrid.SetRowSize(count, 30)
            for col in range(self.lenCols):
                self.rekapGrid.SetColSize(col, 180)
                self.rekapGrid.SetCellAlignment(count, col, wx.ALIGN_LEFT, wx.ALIGN_CENTER)
            self.rekapGrid.SetCellValue(count, 0, f"{noKK}")
            self.rekapGrid.SetCellValue(count, 1, f"Rp{int(bantuan)}")
            count += 1

app = wx.App()
frame = MainGui(parent=None)
frame.Show()
app.MainLoop()