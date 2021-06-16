import sqlite3
from datetime import datetime

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('bantuanWarga.db')
        self.cursor = self.conn.cursor()

    def executeQuery(self, query, retVal=False):
        res = self.cursor.execute(query)
        result = res.fetchall()
        self.conn.commit()
        if retVal:
            return result

    def checkVal(self, query):
        result = self.cursor.execute(query)
        return result.fetchone()

    def close(self):
        self.conn.close()

class dataKeluarga(Database):
    def setKeluarga(self, noKK, kepalaKeluarga, anggota, total, alamat):
        self.executeQuery("CREATE TABLE IF NOT EXISTS Keluarga (noKK int primary key, kepalaKeluarga varchar, anggotaKeluarga int, totalPendapatan int, alamat varchar)")
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is None and noKK and kepalaKeluarga and anggota and total and alamat:
            query2 = f"INSERT INTO Keluarga VALUES ('{noKK}', '{kepalaKeluarga}', '{anggota}', '{total}', '{alamat}')"
            self.executeQuery(query2)
            return True
        else:
            return False

    def showKeluarga(self):
        list = self.executeQuery("SELECT * FROM Keluarga ORDER BY kepalaKeluarga", True)
        return list

    def lowerTotal(self):
        query = f"SELECT * FROM Keluarga ORDER BY totalPendapatan"
        list = self.executeQuery(query, True)
        return list

    def readByTotalBelow(self, total):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan < '{total}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        return list

    def readByTotalAbove(self, total):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan > '{total}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        return list

    def readByAnggotaBelow(self, anggota):
        query = f"SELECT * FROM Keluarga WHERE anggotaKeluarga < '{anggota}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        return list

    def readByAnggotaAbove(self, anggota):
        query = f"SELECT * FROM Keluarga WHERE anggotaKeluarga > '{anggota}' ORDER BY kepalaKeluarga"
        list = self.executeQuery(query, True)
        return list

    def updateTotalPendapatan(self, noKK, total):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None and noKK and total:
            query2 = f"UPDATE Keluarga SET totalPendapatan = '{total}' WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            return True
        else:
            return False

    def updateAlamat(self, noKK, alamat):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None and noKK and alamat:
            query2 = f"UPDATE Keluarga SET alamat = '{alamat}' WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            return True
        else:
            return False

    def delKeluarga(self, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None and noKK:
            query2 = f"DELETE FROM Keluarga WHERE noKK = '{noKK}'"
            query3 = f"DELETE FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
            self.executeQuery(query2)
            self.executeQuery(query3)
            return True
        else:
            return False

    def searchDetailKeluarga(self, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        list = self.executeQuery(query, True)
        if check is not None and noKK:
            query2 = f"SELECT * FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
            list2 = self.executeQuery(query2, True)
            return list, list2
        else:
            return False

class anggotaKeluarga(dataKeluarga):
    def addKeluarga(self, noKK, kepalaKeluarga, anggota, total, alamat, nik):
        check = self.setKeluarga(noKK, kepalaKeluarga, anggota, total, alamat)
        if check:
            self.executeQuery("CREATE TABLE IF NOT EXISTS Anggota_Keluarga (NIK int primary key, nama varchar, noKK int, foreign key(noKK) REFERENCES Keluarga(noKK))")
            query = f"INSERT INTO Anggota_Keluarga VALUES ('{nik}', '{kepalaKeluarga}', '{noKK}')"
            self.executeQuery(query)
            return True
        else:
            return False

    def setAnggota(self, nikAnggota, nama, noKK):
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None and nikAnggota and nama and noKK:
            query2 = f"SELECT * FROM Anggota_Keluarga WHERE NIK = '{nikAnggota}'"
            check2 = self.checkVal(query2)
            if check2 is None:
                query3 = f"INSERT INTO Anggota_Keluarga VALUES ('{nikAnggota}', '{nama}', '{noKK}')"
                self.executeQuery(query3)
                self.updateAnggota(noKK)
                return True
            else:
                return False
        else:
            return False

    def delAnggota(self, noKK, nikAnggota):
        query = f"SELECT * FROM Anggota_Keluarga WHERE noKK = '{noKK}' and NIK = '{nikAnggota}'"
        check = self.checkVal(query)
        if check is not None and noKK and nikAnggota:
            query2 = f"DELETE FROM Anggota_Keluarga WHERE NIK = '{nikAnggota}'"
            self.executeQuery(query2)
            self.updateAnggota(noKK)
            return True
        else:
            return False

    def updateAnggota(self, noKK):
        query = f"SELECT count(*) FROM Anggota_Keluarga WHERE noKK = '{noKK}'"
        list = self.executeQuery(query, True)
        query2 = f"UPDATE Keluarga SET anggotaKeluarga = '{list[0][0]}' WHERE noKK = '{noKK}'"
        self.executeQuery(query2)

class bantuan(Database):
    def analyze(self, umr):
        query = f"SELECT * FROM Keluarga WHERE totalPendapatan <= '{umr}'"
        list = self.executeQuery(query, True)
        anggota = []
        limit = []
        if list and umr:
            for row in list:
                anggota.append(row[2])
                limit.append(int(umr) - row[3])
            for x in range(len(anggota)):
                if anggota[x] > 1:
                    for y in range(anggota[x] - 1):
                        limit[x] += 100000
            return list, limit
        else:
            return False

class rekap(Database):
    def catatBantuan(self, noKK, donation):
        now = datetime.now()
        date = now.strftime("%Y-%m-%d %H:%M:%S")
        self.executeQuery("CREATE TABLE IF NOT EXISTS Rekap_Data (idRekap INTEGER PRIMARY KEY, noKK int, bantuan int, tanggal varchar, FOREIGN KEY(noKK) references Keluarga(noKK))")
        query = f"SELECT * FROM Keluarga WHERE noKK = '{noKK}'"
        check = self.checkVal(query)
        if check is not None and noKK and donation and date:
            query2 = f"INSERT INTO Rekap_Data VALUES (null, '{noKK}', '{donation}', '{date}')"
            self.executeQuery(query2)
            return True
        else:
            return False

    def riwayatBantuan(self):
        list = self.executeQuery("SELECT * FROM Rekap_Data ORDER BY tanggal", True)
        kepalaKeluarga = []
        for row in list:
            kepalaKeluarga.append(self.executeQuery(f"SELECT kepalaKeluarga FROM Keluarga WHERE noKK = '{row[1]}'", True))
        return kepalaKeluarga, list

    def newestData(self):
        list = self.executeQuery("SELECT * FROM Rekap_Data ORDER BY tanggal DESC", True)
        kepalaKeluarga = []
        for row in list:
            kepalaKeluarga.append(
                self.executeQuery(f"SELECT kepalaKeluarga FROM Keluarga WHERE noKK = '{row[1]}'", True))
        return kepalaKeluarga, list
