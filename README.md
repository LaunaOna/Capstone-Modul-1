# Capstone-Modul-1
## Capstone Project Modul 1 - Launa (JCDSOL-013) - Penjualan Barang Toko - Python
### Program Cashier Toko Ona (Toko Buku)

Fitur-fitur yang ada:
Menampilkan Main Menu yang terdiri dari 5 menu: (menggunakan looping while agar setiap selesai dengan menu yg dipilih akan selalu kembali ke Main Menu, kecuali pilih no 5. Exit (break looping)

  1. Menampilkan daftar buku (function pilihan_daftar_buku dan looping dengan while)
     Di menu ini, user dapat memilih:
     (1) Semua Index (menampilkan semua list buku yang ada) -> menggunakan function daftar_buku.
     (2) Index tertentu (hanya menampilakan 1 index yang dipilih) -> menggunakan function index_buku_tertentu -> jika user            memasukan index yang tidak ada, maka user akan diarahkan untuk kembali menginput index yang benar (menggunakan               except index error, sehingga tidak keluar program, melainkan kembali ke looping while awal, sampai user menginput            dengan benar indexnya.
     (3) Keluar (keluar dari menu 'Menampilkan daftar buku') -> break dari looping while
  2. Stock Buku (function stock_buku dan looping dengan while)
     Di menu ini, user dapat memilih:
     (1) Menambah stock buku (menambah jumlah stock buku yang sudah ada)-> menggunakan function tambah_stock_buku -> jika             salah memasukan index juga akan kembali ke user input index awal karena menggunakan except indexerror.
     (2) Mengurang stock buku (mengurangi jumlah stock buku yang sudah ada) -> menggunakan function kurang_stock_buku ->              jika salah memasukan index juga akan kembali ke user input index awal karena menggunakan except indexerror.
     (3) Menambah List Baru (menambah list buku baru) -> mengguanakan function tambah_list_baru -> jika kode yang dimasukan           sama dengan kode yang sudah ada, maka user akan kembali menginput dari awal, agar kodenya tidak sama (karena buku            baru) menggunakan function `any (dictionary.get('kode') == kodeBuku`
                                     `for dictionary in listBuku`
  3. Menghapus Buku (menggunakan function menghapusBuku)
     Di menu ini, user dapat menghapus index tertentu dalam list buku. Jika user salah memasukan index, maka akan diarahakan      untuk kembali menginput index yang ada (menggunakan excepr indexerror juga)
  4. Transaksi (menggunakan function transaksi)
     Di menu ini, user yaitu cashier dapat melayani customer yang hendak membeli buku. Akan ada user input index buku yang        dibeli, berapa banyak, dan nanti akan ditampilkan daftar belanjaannya. Dan juga akan ada kembali dicek apakah sudah          selesai belanja atau mau lanjut belanja. Jika lanjut maka akan ke user input lagi sampai belanja selesai.
     Lalu selanjutnya akan ditampilkan daftar semua belanjaan dan harga yang perlu dibayar. Jika uang pas, uang lebih,            ataupun uang kurang pun ada di fitur ini, agar memudahkan cashier untuk melakukan transaksi dengan customer.  
  5. Exit Program (menggunakan break agar looping while Main Menu dapat dihentikan dan program selesai.

Demikian penjelasan mengenai fitur-fitur yang ada di Program Toko Buku Ona menggunakan bahasa pemrograman Python.

Terima kasih.
   
