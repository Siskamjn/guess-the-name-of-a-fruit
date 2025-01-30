import random
import time

databuah = ['anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei', 'abiu',
             'alpukat', 'anjeng', 'bacang', 'baguk', 'belimbing', 'bengkuang', 'benda',
             'binjai', 'bisbul', 'blueberry', 'burahol', 'blewah', 'bit', 'cempedak',
             'ceplukan', 'cermai', 'ceri', 'cokelat', 'delima', 'duku', 'durian', 'duwet',
             'enau', 'enamenam', 'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang', 'jambuair',
             'jambubatu', 'jambubol', 'jambumawar', 'jambumede', 'jengkol', 'jeruk', 'jerukbali',
             'jerukkeprok', 'jerukkingkit', 'jeruknipis', 'jerukpurut', 'kapulasan', 'kawista',
             'kecapi', 'kedondong', 'kelapa', 'kelengkeng', 'kelubi', 'ketela', 'kemang', 'kepel',
             'kersen', 'kesemek', 'kokosan', 'kiwi', 'koldi', 'kurma', 'kelawi', 'kenitu', 'lai',
             'langsat', 'lemon', 'leci', 'lobak', 'maja', 'malaka', 'mangga', 'manggis', 'markisa',
             'melon', 'mengkudu', 'menteng', 'matoa', 'mentimun', 'namnam', 'nanas', 'nangka', 'naga',
             'nona', 'pepaya', 'persik', 'pir', 'pisang', 'pete', 'rambai', 'rambusa', 'rambutan', 'rukem',
            'sawo', 'semangka', 'sirsak', 'siwalan', 'srikaya', 'stroberi', 'sukun', 'terap', 'terong',
             'tomat', 'timunsuri', 'ubi', 'waluh', 'wuni','zaitun']

def pseudorandom(seed = None):
    a = 2
    b = 8
    c = 13
    
    if seed == None:
        seed = int(time.time())
    seed = (a*seed+b)%c
    buah = databuah[seed]
    return buah

skor_akhir = []
menu='Y'
while (menu == 'Y'):
        nama_buah_yang_ditebak = pseudorandom()
        jumlah_huruf_buah =len(nama_buah_yang_ditebak)
        kesempatan_nebak = jumlah_huruf_buah
        huruf_yang_ditebak = []
        print("Tebak nama buah yang terdiri dari",jumlah_huruf_buah, "huruf")
        while kesempatan_nebak > 0:
            kalah = 0
            print()
            print('Nama buah :', end =" " )
            for char in nama_buah_yang_ditebak:
                if char in huruf_yang_ditebak:
                    print(char, end =" ")
                else:
                    print("_", end =" ")
                    kalah += 1
            if kalah == 0:
                print()
                nilai = round(kesempatan_nebak/(jumlah_huruf_buah)*100, 2)
                print ("Skor Anda= ", nilai)
                print("SELAMAT, ANDA BERHASIL!!")
                skor_akhir.append(nilai)
                break
            print()
            print()
            print("Anda memiliki",kesempatan_nebak,"kali kesempatan untuk menebak huruf buah tersebut")
            tebakan = input("Tebakan anda ? ")
            huruf_yang_ditebak += tebakan
            if tebakan not in nama_buah_yang_ditebak:
                kesempatan_nebak -= 1
                print("Sayang sekali. Huruf", tebakan ,"tidak ada dalam nama buah tersebut.")
                if kesempatan_nebak == 0:
                    print()
                    nilai = 0
                    skor_akhir.append(nilai)
                    print("Anda Kalah !!!")
                    print("Nama buah tersebut: ",nama_buah_yang_ditebak)
            if tebakan in nama_buah_yang_ditebak:
                print("Benar. Huruf",tebakan,"ada dalam nama buah tersebut.")
        print()
        menu = (input("Mau main lagi (Y/N) ? "))
print()
skor_akhir_rata2 = round(sum(skor_akhir)/len(skor_akhir), 2)
print("Skor akhir kamu = ", skor_akhir_rata2)
print("Jumlah permainan = ", len(skor_akhir))
print()
print(" SELESAI ")