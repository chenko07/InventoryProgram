#Program Gudang Toko Defis
#Author : Marchel Andrian Shevchenko (5200411552) - Informatika I (FTIE)- 2020
#Program ini menampilkan beberapa opsi pencarian

import pandas as pd
import datetime

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 10)

#Memunculkan Tampilan awal
print('''
      -----Data Barang Gudang Defis----- ''')
tanggal_saat_ini = datetime.date.today()
print('''  ''')           #memberikan jeda baris
print(tanggal_saat_ini)   #tanggal pada saat di akses

print('''
      Pilihan Pencarian
      1. Daftar Kategori Barang
      2. Daftar Rak
      3. Daftar Lokasi Barang
      ''')
pencarian=int (input("Masukan Pencarian: ")) #memasukan pilihan pencarian berdasarkan keinginan

#Bagian 1 Kategori Barang
if pencarian==1:
          print('Daftar Kategori Barang')
          print('''
                1. Sembako
                2. Alat Mandi 
                3. Alat Tidur
                4. Minuman 
                5. Makanan
                6. SEMUA KATEGORI 
                ''')
          nomor=int (input("Masukan Pilihan: ")) #memasukan pilihan berdasarkan kategori barang

#memunculkan pilihan nomor 1
          if nomor==1:
                print('''
                =SEMBAKO=
                ''')
                data = {'|Nama Barang|': ['', 'Beras', 'Galon', 'Kecap', 'Mie', 'Minyak', 'Telur'],
                      '|Lokasi Rak|': ['', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1'],
                      '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                      '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg'],
                      '|Barang Terjual|': ['', 5, 6, 10, 20, 10, 17],
                      '|Barang Sisa|': ['', 10, 6, 12, 80, 40, 43],
                      '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg']}
                users = pd.DataFrame(data)
                print(users)

#memunculkan pilihan nomor 2
          elif nomor==2:
                  print('''
                  =ALAT MANDI=
                  ''')
                  data = {'|Nama Barang|': ['', 'Sikat Gigi', 'Pasta Gigi', 'Sabun', 'Shampo', 'Gayung', 'Shower Cap'],
                        '|Lokasi Rak|': ['', 'A2', 'A2', 'A2', 'A2', 'A2', 'A2'],
                        '|Jumlah Barang|': ['', 50, 70, 45, 34, 20, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 40, 64, 35, 14, 10, 30],
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

#memunculkan pilihan nomor 3
          elif nomor==3:
                  print('''
                  =ALAT TIDUR=
                  ''')
                  data = {'|Nama Barang|': ['', 'Bantal', 'Guling', 'Selimut', 'Kasur', 'Sprei', 'Penutup Mata'],
                        '|Lokasi Rak|': ['', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 5, 6, 12, 80, 40, 30],
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

#memunculkan pilihan nomor 4
          elif nomor==4:
                  print('''
                  =MINUMAN=
                  ''')
                  data = {'|Nama Barang|': ['', 'Aqua', 'Pocari', 'Mizone', 'Kratingdeng', 'Adem Sari', 'Ultra Milk'],
                        '|Lokasi Rak|': ['', 'A3', 'A3', 'A3', 'A3', 'A3', 'A3'],
                        '|Jumlah Barang|': ['', 70, 80, 76, 66, 90, 120],       
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 60, 74, 66, 46, 80, 90],
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

#memunculkan pilihan nomor 5
          elif nomor==5:
                  print('''
                  =MAKANAN=
                  ''')
                  data = {'|Nama Barang|': ['', 'Chiki', 'Bitter Sweet', 'Kripik', 'Bento Box', 'Pudding', 'Geprek'],
                        '|Lokasi Rak|': ['', 'B2', 'B2', 'B2', 'B2', 'B2', 'B2'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Box', 'Pcs', 'Box', 'Cup', 'Box'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 5, 6, 12, 80, 40, 30],
                        '|Satuan|': ['', 'Pcs', 'Box', 'Pcs', 'Box', 'Cup', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

#memunculkan pilihan nomor 6                 
          elif nomor==6:
                  print('''
                  =SEMUA KATEGORI=
                  ''')

                  print('''
                        =SEMBAKO=
                        ''')
                  data = {'|Nama Barang|': ['', 'Beras', 'Galon', 'Kecap', 'Mie', 'Minyak', 'Telur'],
                        '|Lokasi Rak|': ['', 'A1', 'A1', 'A1', 'A1', 'A1', 'A1'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg'],
                        '|Barang Terjual|': ['', 5, 6, 10, 20, 10, 17],
                        '|Barang Sisa|': ['', 10, 6, 12, 80, 40, 43],
                        '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg']}
                  users = pd.DataFrame(data)
                  print(users)

                  print('''
                        =ALAT MANDI=
                        ''')
                  data = {'|Nama Barang|': ['', 'Sikat Gigi', 'Pasta Gigi', 'Sabun', 'Shampo', 'Gayung', 'Shower Cap'],
                        '|Lokasi Rak|': ['', 'A2', 'A2', 'A2', 'A2', 'A2', 'A2'],
                        '|Jumlah Barang|': ['', 50, 70, 45, 34, 20, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 40, 64, 35, 14, 10, 30],
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)
                  
                  print('''
                        =ALAT TIDUR=
                        ''')
                  data = {'|Nama Barang|': ['', 'Bantal', 'Guling', 'Selimut', 'Kasur', 'Sprei', 'Penutup Mata'],
                        '|Lokasi Rak|': ['', 'B1', 'B1', 'B1', 'B1', 'B1', 'B1'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 5, 6, 12, 80, 40, 30],
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

                  print('''
                        =MINUMAN=
                        ''')
                  data = {'|Nama Barang|': ['', 'Aqua', 'Pocari', 'Mizone', 'Kratingdeng', 'Adem Sari', 'Ultra Milk'],
                        '|Lokasi Rak|': ['', 'A3', 'A3', 'A3', 'A3', 'A3', 'A3'],
                        '|Jumlah Barang|': ['', 70, 80, 76, 66, 90, 120],       
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 60, 74, 66, 46, 80, 90],
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

                  print('''
                        =MAKANAN=
                        ''')
                  data = {'|Nama Barang|': ['', 'Chiki', 'Bitter Sweet', 'Kripik', 'Bento Box', 'Pudding', 'Geprek'],
                        '|Lokasi Rak|': ['', 'B2', 'B2', 'B2', 'B2', 'B2', 'B2'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Box', 'Pcs', 'Box', 'Cup', 'Box'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 5, 6, 12, 80, 40, 30],
                        '|Satuan|': ['', 'Pcs', 'Box', 'Pcs', 'Box', 'Cup', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

#Bagian 2 Kategori Rak
if pencarian==2:
          print('''
                Daftar Rak Gudang''')
          print('''
                1. A1
                2. A2
                3. A3
                4. B1
                5. B2
                ''')

          rak=int (input("Masukan Rak : "))

          if rak==1:
                print('''
                =RAK A1=
                ''')
                data = {'|Nama Barang|': ['', 'Beras', 'Galon', 'Kecap', 'Mie', 'Minyak', 'Telur'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg'],
                        '|Barang Terjual|': ['', 5, 6, 10, 20, 10, 17],
                        '|Barang Sisa|': ['', 10, 6, 12, 80, 40, 43],
                        '|Satuan|': ['', 'Kg', 'Pcs', 'Pcs', 'Pcs', 'Ltr', 'Kg']}
                users = pd.DataFrame(data)
                print(users)

          elif rak==2:
                  print('''
                  =RAK A2=
                  ''')
                  data = {'|Nama Barang|': ['', 'Sikat Gigi', 'Pasta Gigi', 'Sabun', 'Shampo', 'Gayung', 'Shower Cap'],
                        '|Jumlah Barang|': ['', 50, 70, 45, 34, 20, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 40, 64, 35, 14, 10, 30],
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif rak==3:
                  print('''
                  =RAK A3=
                  ''')
                  data = {'|Nama Barang|': ['', 'Aqua', 'Pocari', 'Mizone', 'Kratingdeng', 'Adem Sari', 'Ultra Milk'],
                        '|Jumlah Barang|': ['', 70, 80, 76, 66, 90, 120],       
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box'],
                        '|Barang Terjual|': ['', 10, 6, 10, 20, 10, 30],
                        '|Barang Sisa|': ['', 60, 74, 66, 46, 80, 90],
                        '|Satuan|': ['', 'Btl', 'Btl', 'Btl', 'Btl', 'Btl', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

          elif rak==4:
                  print('''
                  =RAK B1=
                  ''')
                  data = {'|Nama Barang|': ['', 'Bantal', 'Guling', 'Selimut', 'Kasur', 'Sprei', 'Penutup Mata'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif rak==5:
                  print('''
                  =RAK B2=
                  ''')
                  data = {'|Nama Barang|': ['', 'Chiki', 'Bitter Sweet', 'Kripik', 'Bento Box', 'Pudding', 'Geprek'],
                        '|Jumlah Barang|': ['', 15, 12, 22, 100, 50, 60],       
                        '|Satuan|': ['', 'Pcs', 'Box', 'Pcs', 'Box', 'Cup', 'Box']}
                  users = pd.DataFrame(data)

#Bagian 1 Lokasi Barang                  
if pencarian==3:
          print('''
                Daftar Barang''')
          print('''
                1. Beras
                2. Galon
                3. Kecap
                4. Mie
                5. Minyak
                6. Telur
                7. Sikat Gigi
                8. Pasta Gigi
                9. Sabun
                10. Shampo
                11. Gayung
                12. Shower Cap
                13. Aqua
                14. Pocari
                15. Mizone
                16. Kratingdeng
                17. Adem Sari
                18. Ultra Milk
                19. Bantal
                20. Guling
                21. Selimut
                22. Kasur
                23. Sprei
                24. Penutup Mata
                25. Chiki
                26. Bitter Sweet
                27. Kripik
                28. Bento Box
                29. Pudding
                30. Geprek
                ''')

          brg=int (input("Masukan Barang : "))

          if brg==1:
      
                data = {'|Nama Barang|': ['', 'Beras'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Kg'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'kg']}
                users = pd.DataFrame(data)
                print(users)

          elif brg==2:
                  
                  data = {'|Nama Barang|': ['', 'Galon'],
                      '|Jumlah Barang|': ['', 12],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 6],
                      '|Barang Sisa|': ['', 56],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==3:
                  
                  data = {'|Nama Barang|': ['', 'Kecap'],
                      '|Jumlah Barang|': ['', 22],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 12],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==4:
                  
                  data = {'|Nama Barang|': ['', 'Mie'],
                      '|Jumlah Barang|': ['', 100],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 20],
                      '|Barang Sisa|': ['', 80],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==5:
                  
                  data = {'|Nama Barang|': ['', 'Minyak'],
                      '|Jumlah Barang|': ['', 50],       
                      '|Satuan|': ['', 'Ltr'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 40],
                      '|Satuan|': ['', 'Ltr']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==6:
                  
                  data = {'|Nama Barang|': ['', 'Telur'],
                      '|Jumlah Barang|': ['', 60],       
                      '|Satuan|': ['', 'Kg'],
                      '|Barang Terjual|': ['', 17],
                      '|Barang Sisa|': ['', 43],
                      '|Satuan|': ['', 'Kg']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==7:
                  
                  data = {'|Nama Barang|': ['', 'Sikat Gigi'],
                      '|Jumlah Barang|': ['', 50],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 40],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==8:
                  
                  data = {'|Nama Barang|': ['', 'Pasta Gigi'],
                      '|Jumlah Barang|': ['', 70],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 6],
                      '|Barang Sisa|': ['', 64],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==9:
                  
                  data = {'|Nama Barang|': ['', 'Sabun'],
                      '|Jumlah Barang|': ['', 45],       
                      '|Satuan|': ['', 'Kg'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 35],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==10:
                  
                  data = {'|Nama Barang|': ['', 'Shampo'],
                      '|Jumlah Barang|': ['', 34],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 20],
                      '|Barang Sisa|': ['', 14],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==11:
                  
                  data = {'|Nama Barang|': ['', 'Gayung'],
                      '|Jumlah Barang|': ['', 20],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 10],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==12:
                  
                  data = {'|Nama Barang|': ['', 'Shower Cap'],
                      '|Jumlah Barang|': ['', 60],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 30],
                      '|Barang Sisa|': ['', 30],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==13:
                  
                  data = {'|Nama Barang|': ['', 'Bantal'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==14:
                  
                  data = {'|Nama Barang|': ['', 'Guling'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==15:
                  
                  data = {'|Nama Barang|': ['', 'Selimut'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==16:
                  
                  data = {'|Nama Barang|': ['', 'Kasur'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==17:
                  
                  data = {'|Nama Barang|': ['', 'Sprei'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==18:
                  
                  data = {'|Nama Barang|': ['', 'Penutup Mata'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==19:
                  
                  data = {'|Nama Barang|': ['', 'Aqua'],
                      '|Jumlah Barang|': ['', 70],       
                      '|Satuan|': ['', 'Btl'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 60],
                      '|Satuan|': ['', 'Btl']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==20:
                  
                  data = {'|Nama Barang|': ['', 'Pocari'],
                      '|Jumlah Barang|': ['', 80],       
                      '|Satuan|': ['', 'Btl'],
                      '|Barang Terjual|': ['', 6],
                      '|Barang Sisa|': ['', 74],
                      '|Satuan|': ['', 'Btl']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==21:
                  
                  data = {'|Nama Barang|': ['', 'Mizone'],
                      '|Jumlah Barang|': ['', 76],       
                      '|Satuan|': ['', 'Btl'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 66],
                      '|Satuan|': ['', 'btl']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==22:
                  
                  data = {'|Nama Barang|': ['', 'Kratingdeng'],
                      '|Jumlah Barang|': ['', 66],       
                      '|Satuan|': ['', 'Btl'],
                      '|Barang Terjual|': ['', 20],
                      '|Barang Sisa|': ['', 46],
                      '|Satuan|': ['', 'Btl']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==23:
                  
                  data = {'|Nama Barang|': ['', 'Adem Sari'],
                      '|Jumlah Barang|': ['', 90],       
                      '|Satuan|': ['', 'Btl'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 80],
                      '|Satuan|': ['', 'Btl']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==24:
                  
                  data = {'|Nama Barang|': ['', 'Ultra Milk'],
                      '|Jumlah Barang|': ['', 120],       
                      '|Satuan|': ['', 'Box'],
                      '|Barang Terjual|': ['', 30],
                      '|Barang Sisa|': ['', 90],
                      '|Satuan|': ['', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==25:
                  
                  data = {'|Nama Barang|': ['', 'Chiki'],
                      '|Jumlah Barang|': ['', 15],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 5],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==26:
                  
                  data = {'|Nama Barang|': ['', 'Bitter Sweet'],
                      '|Jumlah Barang|': ['', 12],       
                      '|Satuan|': ['', 'Box'],
                      '|Barang Terjual|': ['', 6],
                      '|Barang Sisa|': ['', 6],
                      '|Satuan|': ['', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==27:
                  
                  data = {'|Nama Barang|': ['', 'Kripik'],
                      '|Jumlah Barang|': ['', 22],       
                      '|Satuan|': ['', 'Pcs'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 12],
                      '|Satuan|': ['', 'Pcs']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==28:
                  
                  data = {'|Nama Barang|': ['', 'Bento Box'],
                      '|Jumlah Barang|': ['', 100],       
                      '|Satuan|': ['', 'Box'],
                      '|Barang Terjual|': ['', 20],
                      '|Barang Sisa|': ['', 80],
                      '|Satuan|': ['', 'Box']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==29:
                  
                  data = {'|Nama Barang|': ['', 'Pudding'],
                      '|Jumlah Barang|': ['', 50],       
                      '|Satuan|': ['', 'Cup'],
                      '|Barang Terjual|': ['', 10],
                      '|Barang Sisa|': ['', 40],
                      '|Satuan|': ['', 'Cup']}
                  users = pd.DataFrame(data)
                  print(users)

          elif brg==30:
                  
                  data = {'|Nama Barang|': ['', 'Geprek'],
                      '|Jumlah Barang|': ['', 60],       
                      '|Satuan|': ['', 'Box'],
                      '|Barang Terjual|': ['', 30],
                      '|Barang Sisa|': ['', 30],
                      '|Satuan|': ['', 'Box']}
                  users = pd.DataFrame(data)
                  print(users) 

#Bagian penutup
print('''
      Terima Kasih Telah Mengecek, Jangan Lupa Diperbaharui !
      ''')          

#Demikian kode untuk menyelesaikan tugas Algoritma Pemrograman Praktik pada Jumat, 11 Desember 2020
#Mohon maaf apabila ada kesalahan kode 
#Disclaimer : Kode serupa belum saya pernah temukan dimanapun, hanya mengikuti urutan algoritma sederhana
#Terima kasih telah membaca                                            
