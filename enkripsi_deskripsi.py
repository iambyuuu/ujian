import string

pesan = string.printable

def enkripsi(isi):
          global pesan
          
          key = int(input("MASUKKAN KODE :  "))
          cipher = ''
          for a in isi :
                    if a in pesan:
                              y = pesan.find(a)
                              y = (y + key)%100
                              cipher = cipher + pesan[y]
                    else :
                              cipher = cipher + a
          
          return cipher

def deskripsi(cipher):
          global pesan
          
          key = int(input("MASUKKAN KODE :  "))
          isi = ''
          for a in cipher :
                    if a in pesan:
                              y = pesan.find(a)
                              y = (y - key)%100
                              isi = isi + pesan[y]
                    else :
                              isi = isi + a
          
          return isi

if __name__ == '__main__' :
          print('-----------------------------------------')
          print("WELCOME IN TUGAS UJIAN 3 PT.HASHMICRO")
          print(input('-----------------------------------------'))
          kategori = int(input('1. Enkripsi Message\n2. Deskripsi Message\n-----------------------------------------\nPilih Mode Pesan  :'))

          if kategori == 1:
                    isi = input('Masukkan Pesan :')
                    print(enkripsi(isi))
                    print('-----------------------------------------')
                    print ('*MOHON UNTUK "DIINGAT" KODE NOMORNYA DAN "SALIN" KODE CIPHER UNTUK MEMBUKA ENKRIPSI !!')
          elif kategori == 2:
                    cipher = input('Masukkan Kode Pesan :')
                    print(deskripsi(cipher))
                    print('-----------------------------------------')
                    print ('TERIMAKASIH SUDAH MEMBACA PESANNYA. HARAP UNTUK DIBALAS :)')
          else :
                    print('GAGAL, HARAP ULANG KEMBALI')