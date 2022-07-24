from re import S
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.uic import loadUi
from Menu import *
import pymysql



class Menu(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('menu.ui', self)
        self.tampilData()
        self.Btntambah.clicked.connect(self.tambahDataGaji)
        self.tabelgaji.itemSelectionChanged.connect(self.tampilDataGaji)
        self.Btnperbarui.clicked.connect(self.perbaruiDataGaji)
        self.Btnhapus.clicked.connect(self.hapusDataGaji)
        self.Btncari.clicked.connect(self.cariDataGaji)

    def tampilPesan(self, pesan):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Information)
        mess.setWindowTitle("Notification")
        mess.setText(pesan)
        mess.exec()

    def tampilData(self):
        #membuat koneksi ke server mysql
        con = pymysql.connect(db='gaji', user='root', password='',host='localhost', port=3306, autocommit=True)
        #menampilkan data pada tabel
        cursor = con.cursor()
        cursor.execute("SELECT * FROM tbl_gaji")
        data_gaji = cursor.fetchall()
        n_gaji = len(data_gaji)
        self.tabelgaji.setRowCount(n_gaji)
        baris = 0
        for x in data_gaji:
            self.tabelgaji.setItem(baris, 0, QTableWidgetItem(x[0]))
            self.tabelgaji.setItem(baris, 1, QTableWidgetItem(x[1]))
            self.tabelgaji.setItem(baris, 2, QTableWidgetItem(str(x[2])))
            self.tabelgaji.setItem(baris, 3, QTableWidgetItem(str(x[3])))
            self.tabelgaji.setItem(baris, 4, QTableWidgetItem(x[4]))
            self.tabelgaji.setItem(baris, 5, QTableWidgetItem(str(x[5])))
            baris = baris+1

    def tambahDataGaji(self):
        try:
            #mengambil data pada form
            namakaryawan = self.EditNama.displayText()
            jabatan = self.EditJabatan.displayText()
            gajipokok = self.EditGajiPokok.displayText()
            tahunmasukkerja = self.EditTahunMasuk.displayText()
            statuskerja = self.EditStatusKerja.displayText()
            tahunhabiskontrak = self.TahunhabisKontrak.displayText()

            if namakaryawan!= "" and jabatan!= "" and gajipokok!= "" and tahunmasukkerja!= "" and statuskerja!= "" and tahunhabiskontrak!= "":

                con = pymysql.connect(
                    db='gaji', user='root', password='', host='localhost', port=3306, autocommit=True)

                query = "INSERT INTO tbl_gaji(namakaryawan, jabatan, gajipokok, thnmasuk, statuskerja, thhbskontrak) VALUES(%s,%s,%s,%s,%s,%s)"
                data = (namakaryawan, jabatan, gajipokok,
                        int(tahunmasukkerja), statuskerja, int(tahunhabiskontrak))
                cursor = con.cursor()
                cursor.execute(query, data)
                con.commit()
                con.close()
                self.tampilPesan("Data anda berhasil dimasukkan!")
                self.tampilData()
                self.hapusTeks()
            else:
                self.tampilPesan('LENGKAPIN data anda dahulu')
        except:
            self.tampilPesan('Terjadi Kesalahan Saat Menambahkan Data')

    def cariDataGaji(self):
        #menyimpan kata kunci
        kata_kunci = self.carinamakaryawan.displayText()
    #membuat koneksi ke server MySQL
        con = pymysql.connect(db='gaji', user='root', password='',host='localhost', port=3306, autocommit=True)
        #mencari data buku berdasarkan kata kunci yang dimasukkan
        query = "SELECT * FROM tbl_gaji WHERE namakaryawan LIKE '%" + \
            kata_kunci+"%' OR jabatan LIKE '%"+kata_kunci+"%' "
        cursor = con.cursor()
        cursor.execute(query)
        data_gaji = cursor.fetchall()
        #menutup koneksi
        con.close()
        n_datagaji = len(data_gaji)
        self.tabelgaji.setRowCount(n_datagaji)
        baris = 0

        for x in data_gaji:
            self.tabelgaji.setItem(baris, 0, QTableWidgetItem(x[0]))
            self.tabelgaji.setItem(baris, 1, QTableWidgetItem(x[1]))
            self.tabelgaji.setItem(baris, 2, QTableWidgetItem(str(x[2])))
            self.tabelgaji.setItem(baris, 3, QTableWidgetItem(str(x[3])))
            self.tabelgaji.setItem(baris, 4, QTableWidgetItem(x[4]))
            self.tabelgaji.setItem(baris, 5, QTableWidgetItem(str(x[5])))
            baris = baris+1

    def tampilDataGaji(self):
        #menyimpan detail data buku yang dipilih
        data = self.tabelgaji.selectedItems()
        namakaryawan = data[0].text()
        jabatan = data[1].text()
        gajipokok = data[2].text()
        tahunmasukkerja = data[3].text()
        statuskerja = data[4].text()
        tahunhabiskontrak = data[5].text()

        self.EditNama.setText(namakaryawan)
        self.EditJabatan.setText(jabatan)
        self.EditGajiPokok.setText(gajipokok)
        self.EditTahunMasuk.setText(tahunmasukkerja)
        self.EditStatusKerja.setText(statuskerja)
        self.TahunhabisKontrak.setText(tahunhabiskontrak)
   
    def perbaruiDataGaji(self):
        try:
            namakaryawan = self.EditNama.displayText()
            jabatan = self.EditJabatan.displayText()
            gajipokok = self.EditGajiPokok.displayText()
            tahunmasukkerja = self.EditTahunMasuk.displayText()
            statuskerja = self.EditStatusKerja.displayText()
            tahunhabiskontrak = self.TahunhabisKontrak.displayText()

            if namakaryawan!= "" and jabatan!= "" and gajipokok!= "" and tahunmasukkerja!= "" and statuskerja!= "" and tahunhabiskontrak!= "":
                #membuat koneksi ke server MySQL
                con = pymysql.connect(db='gaji', user='root', password='', host='localhost', port=3306, autocommit=True)
            #memperbauri data 
                query = "UPDATE tbl_gaji SET jabatan=%s,gajipokok=%s,thnmasuk=%s,statuskerja=%s,thhbskontrak=%s, WHERE namakaryawan=%s"
                data = (jabatan, gajipokok, int(tahunmasukkerja), statuskerja, int(tahunhabiskontrak), namakaryawan)
                cursor = con.cursor()
                cursor.execute(query, data)
                con.commit()
            #menutup koneksi
                con.close()
            #menampilkan pesan menggunakan fungsi tampilPesan
                self.tampilPesan('Data berhasil diperbarui!')
            #menampilkan data buku menggunakan fungsi tampilDataBuku
                self.tampilData()
                self.hapusTeks()
            else:
                self.tampilPesan('dipilih dulu datanya')
        except:
            self.tampilPesan('Terjadi kesalahan saat mengubah data')

    def tampilJendelakonfirmasi(self, pesan):
        mess = QMessageBox()
        mess.setIcon(QMessageBox.Question)
        mess.setWindowTitle('Konfirmasi')
        mess.setText(pesan)
        mess.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        return mess.exec()

    def hapusTeks(self):
        self.EditNama.setText('')
        self.EditJabatan.setText('')
        self.EditGajiPokok.setText('')
        self.EditTahunMasuk.setText('')
        self.EditStatusKerja.setText('')
        self.TahunhabisKontrak.setText('')

    def hapusDataGaji(self):
        try:
            #menyimpan data gaji
            jendela_konfirmasi = self.tampilJendelakonfirmasi(
                'Apakah anda yakin akan menghapus data ini?')
            namakaryawan = self.EditNama.displayText()
            if namakaryawan != '':
                if jendela_konfirmasi == QMessageBox.Ok:
                    #menciptakan koneksi ke server MySQL
                    con = pymysql.connect(db='gaji', user='root', password='', host='localhost', port=3306, autocommit=True)
                    #menghapus data gaji
                    query = "DELETE FROM tbl_gaji WHERE namakaryawan= %s "
                    data = (namakaryawan,)
                    cursor = con.cursor()
                    cursor.execute(query, data)
                    con.commit()
                    #menutup koneksi
                    con.close()
                    self.tampilPesan('Data berhasil dihapus')
                    self.tampilData()
                    self.hapusTeks()
            else:
                self.tampilPesan('Pilih dulu bang yang mau dihapus')
        except:
            self.tampilPesan('Terjadi Kesalahan saat menghapus data')
