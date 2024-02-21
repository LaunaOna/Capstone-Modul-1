# Study Case: Penjualan Barang Toko
import os # clear screen
os.system('cls')

import getpass

while True:
    print('Program Cashier Toko Buku Ona')
    print('-----------------------------')

    userName = input('\nMasukan username Anda: ')
    password = getpass.getpass('Masukan password Anda: ') #invisible input

    if userName == ('Launa') and password == ('123'):
        print('-----------------------------')
        print('--------Login diterima-------')
        print('-----------------------------')
        break
    
    else:
        print('-----------------------------')
        print('------Silahkan Coba lagi-----')
        print('-----------------------------')

listBuku = [
    {
        'kode': 'A101',
        'nama': 'Kimia',
        'stock': 130,
        'harga': 55000
    },
    {
        'kode': 'B102',
        'nama' : 'Fisika',
        'stock': 328,
        'harga': 67000
    },
    {
        'kode': 'C103',
        'nama': 'Novel',
        'stock': 450,
        'harga': 45000
    }
]

cart = []

def pilihan_daftar_buku(): # Function 1
    while True:
        pilihan = input('''
        Menu Tampilan Daftar Buku:
            1. Semua Index
            2. Index Tertentu
            3. Keluar
        
        Masukan Angka yang Anda ingin jalankan: ''')

        if pilihan == '1':
            daftar_buku()
        elif pilihan == '2':
            index_buku_tertentu()
        elif pilihan == '3':
            break
        else:
            print('\nAngka yang Anda masukkan tidak ada di Menu\n')

def daftar_buku(): # Function 1.1
    print('Daftar Buku\n')
    print('Index\t|Kode \t|Nama\t|Stock\t|Harga')
    for i in range(len(listBuku)) :
        print('{}\t|{}\t|{}\t|{}\t| {}'.format(i,listBuku[i]['kode'],listBuku[i]['nama'],listBuku[i]['stock'],listBuku[i]['harga']))

def index_buku_tertentu(): # Function 1.2
    while True:
        try: #digunakan agar saat ada index yang dimasukan tidak ada, akan looping ke awal kembali, tidak error
            indexBuku = int(input('Masukan index yang ingin ditampilkan: '))
            print('Index\t|Kode \t|Nama\t|Stock\t|Harga')
            print('{}\t|{}\t|{}\t|{}\t| {}'.format(indexBuku,listBuku[indexBuku]['kode'],listBuku[indexBuku]['nama'],listBuku[indexBuku]['stock'],listBuku[indexBuku]['harga']))
            break
        except IndexError:
            print('\nIndex yang Anda masukkan tidak ada di Menu\n')

def stock_buku(): # Function 2
    daftar_buku()
    while True:
        pilihan_stock_buku = input('''
        Menu Stock Buku:
            1. Menambah stock buku
            2. Mengurangi stock buku
            3. Menambah list buku baru                          
            4. Selesai                     
            
        Masukan Angka yang Anda ingin jalankan: ''')
        
        if pilihan_stock_buku == '1':
            tambah_stock_buku()
        elif pilihan_stock_buku == '2':
            kurang_stock_buku()
        elif pilihan_stock_buku == '3':
            tambah_list_buku()
        elif pilihan_stock_buku == '4':
            break
        else:
            print('\nAngka yang Anda masukkan tidak ada di Menu\n')
            

def tambah_stock_buku(): # Function 2.1
    while True:
        try:
            indexBuku = int(input('Masukkan index buku yang ingin stocknya ditambah: '))
            stockBaru = int(input('Masukan tambahan stock: '))
            listBuku[indexBuku]['stock'] += stockBaru
            print('Anda sudah menambahkan buku {} sebanyak {} \n'.format(listBuku[indexBuku]['nama'], stockBaru))
            print('Berikut stock barunya:')
            print('Daftar Buku\n')
            print('Index\t| Nama \t\t| Stock\t| Harga')
            for i in range(len(listBuku)) :
                print('{}\t| {} \t| {}\t| {}'.format(i,listBuku[i]['nama'],listBuku[i]['stock'],listBuku[i]['harga']))
            break
        except IndexError:
            print('\nTidak ada Index tersebut\n')


def kurang_stock_buku(): # Function 2.2
    while True:
        try:
            indexBuku = int(input('Masukkan index buku yang ingin stocknya dikurang: '))
            stockBaru = int(input('Masukan pengurangan stock: '))
            listBuku[indexBuku]['stock'] -= stockBaru
            print('Anda sudah mengurangi buku {} sebanyak {} \n'.format(listBuku[indexBuku]['nama'], stockBaru))
            print('Berikut stock barunya:')
            print('Daftar Buku\n')
            print('Index\t| Nama \t\t| Stock\t| Harga')
            for i in range(len(listBuku)) :
                print('{}\t| {} \t| {}\t| {}'.format(i,listBuku[i]['nama'],listBuku[i]['stock'],listBuku[i]['harga']))
            break       
        except IndexError:
            print('\nTidak ada Index tersebut\n')

def tambah_list_buku(): # Function 2.3
    while True:
        namaBuku = input('Masukkan Nama Buku Baru: ')
        kodeBuku = (input('Masukan Kode Buku Baru: '))
        stockBuku = int(input('Masukkan Stock Buku: '))
        hargaBuku = int(input('Masukkan Harga Buku: '))

        if any( # untuk mengecek kode pada dictionary yang ada di dalam list
            dictionary.get('kode') == kodeBuku
            for dictionary in listBuku
        ):
            print('\nMaaf kode sudah ada, silahkan input ulang \n')
        else:
            listBuku.append({
                'nama': namaBuku,
                'kode': kodeBuku,
                'stock': stockBuku,
                'harga': hargaBuku
                })
            print('\nData baru berhasil diperbaharui\n')
            print('Berikut Daftar Barunya:')
            daftar_buku()
            break

def menghapusBuku() : # Function 3
    daftar_buku()
    while True:
        try:
            indexBuku = int(input('Masukkan index buku yang ingin dihapus: '))
            del listBuku[indexBuku]
            print('\nBerikut daftar yang sudah diperbaharui:\n')
            daftar_buku()
            break
        except IndexError:
            print('\nTidak ada Index tersebut\n')   
    
def transaksi(): # Function 4
    daftar_buku()
    while True :
        try:
            indexBuku = int(input('Masukkan index buku yang ingin dibeli: '))
            qtyBuku = int(input('Masukkan jumlah yang ingin dibeli: '))
            if(qtyBuku > listBuku[indexBuku]['stock']) :
                print('Stock tidak cukup, stock {} tinggal {}'.format(listBuku[indexBuku]['nama'],listBuku[indexBuku]['stock']))
            else :
                cart.append({
                    'nama': listBuku[indexBuku]['nama'], 
                    'qty': qtyBuku, 
                    'harga': listBuku[indexBuku]['harga'], 
                    'index': indexBuku
                })
                print('Isi Cart :')
                print('Nama\t| Qty\t| Harga')
                for item in cart :
                    print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
                checker = input('Mau beli yang lain? (ya/tidak) = ')
                if(checker == 'tidak') :
                    break
        except IndexError:
            print('\nTidak ada Index tersebut\n')
            
    print('Daftar Belanja :')
    print('Nama\t| Qty\t| Harga\t| Total Harga')
    totalHarga = 0
    for item in cart :
        print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
        totalHarga += item['qty'] * item['harga']    
    while True :
        print('Total Yang Harus Dibayar = {}'.format(totalHarga))
        jmlUang = int(input('Masukkan jumlah uang: '))
        if(jmlUang > totalHarga) :
            kembali = jmlUang - totalHarga
            print('Terima kasih \n\nUang kembali: {}'.format(kembali))
            for item in cart :
                listBuku[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        elif(jmlUang == totalHarga) :
            print('Terima kasih')
            for item in cart :
                listBuku[item['index']]['stock'] -= item['qty']
            cart.clear()
            break
        else :
            kekurangan = totalHarga - jmlUang
            print('Uang yang Anda input kurang sebesar {}'.format(kekurangan))

while True :
    pilihanMenu = input('''
    "Selamat Datang di Program Cashier Toko Buku Ona :)"

        List Menu :
        1. Menampilkan Daftar Buku
        2. Stock Buku
        3. Menghapus Buku
        4. Transaksi
        5. Exit Program

        Masukkan Angka yang ingin dijalankan : ''')
    
    if(pilihanMenu == '1') :
        pilihan_daftar_buku()
    elif(pilihanMenu == '2') :
        stock_buku()
    elif(pilihanMenu == '3') :
        menghapusBuku()
    elif(pilihanMenu == '4') :
        transaksi()
    elif(pilihanMenu == '5') :
        break
    else:
        print('\nAngka yang Anda masukkan tidak ada di Menu\n')

    
