Project-Akhir-DDP_Kelompok-3-Sistem manajemen perawatan hewan peliharaan-Pet Shop HAE

Nama Anggota :
              
              Evan Setiawan     2509116036

              Elena Dementieva  2509116008
              
              Wahid Nur Hakim   2509116016
              
Kelas        : Sistem Informasi A'25

Tugas        : Projek Akhir Dasar-Dasar Pemrograman

Tema         : Sistem Manajemen Perawatan Hewan Peliharaan Hae Pet Shop


Deskripsi Singkat HAE PetShop

Program sistem manajemen Hae Petshop merupakan sebuah Sistem Manajemen Perawatan Hewan Peliharaan yang dirancang untuk mengelola berbagai aspek operasional petshop secara terintegrasi dengan sistem pengelolaan. Program ini bertujuan menyediakan multiplatform yang mencakup manajemen pengguna, inventaris barang, data hewan, transaksi pembelian, dan layanan perawatan hewan.

Alur algoritma program dimulai dengan sistem verifikasi data yang memungkinkan pengguna melakukan registrasi akun baru atau login dengan username dan username yang sudah terdaftar. Program membedakan akses berdasarkan peran pengguna, dimana admin memiliki kendali penuh untuk melakukan operasi CRUD pada data barang dan hewan, sedangkan user dapat mengakses sistem untuk mengelola hewan peliharaan mereka sendiri, berbelanja kebutuhan hewan, dan menggunakan layanan perawatan. Sistem ini dirancang dengan mekanisme validasi input yang ketat sehingga dapat memastikan integritas data, termasuk pengecekan panjang input, tipe data, dan handling terhadap interupsi keyboard.

Pada sisi administrasi, algoritma program mengimplementasikan manajemen data persisten melalui penyimpanan file JSON yang memungkinkan data pengguna, barang, dan hewan tetap tersimpan meskipun program ditutup. Untuk pengalaman pengguna yang lebih baik, program memanfaatkan modul PrettyTable untuk menampilkan data dalam format tabel yang terstruktur dan mudah dibaca. Sistem transaksi pada program ini mengintegrasikan keranjang belanja yang dapat menampung baik barang kebutuhan hewan maupun layanan perawatan, dengan mekanisme pembayaran yang terhubung dengan saldo pengguna.

Algoritma pembayaran dirancang dengan logika yang memverifikasi kecukupan saldo sebelum memproses transaksi, dilengkapi dengan fitur top-up untuk menambah saldo dan sistem pembuatan nota transaksi otomatis. Untuk manajemen hewan, program memungkinkan user mendaftarkan hewan peliharaan mereka dengan validasi data yang, serta menampilkan daftar hewan yang terdaftar under setiap user. Secara keseluruhan, program ini menunjukkan implementasi algoritma yang terstruktur dalam mengelola kompleksitas sistem petshop modern dengan tetap menjaga usability dan keamanan data.


Fitur program:

menu utama: disini adalah menu sebelum masuk sebagai admin/user dan juga kalian bisa daftar sebagai user baru

role admin: sebagai admin kalian mendapatkan fitur full CRUD (membuat data, membaca data, mengubah data, menghapus data)
            
            membuat data: disini kalian dapat membuat data barang yang isinya nama, kategori, dan harga
            
            membaca cata: disini kalian dapat membaca data barang ataupun hewan
            
            mengubah data: disini kalian dapat mengubah data barang ataupun data hewan jika berubah
            
            menghapus data: disini kalian dapat menghapus data barang atau data hewan jika sudah tidak diperlukan

role user: sebagai user kalian disini bisa mengelola, belanja kebutuhan hewan, perawatan hewan, melihat rincian pembelian, dan transaksi
          
          kelola hewan: disini berisi dua menu yang isinya daftarkan hewan atau melihat hewan kita yang sudah terdaftar
          
          belanja kebutuhan hewan: disini kalian bisa belanja kebutuhan dan makanan hewan kesayangan kalian lengkap dengan harga
          
          perawatan: disini kalian bisa memilih perawatan untuk hewan kesayangan kalian seperti vaksin, grooming, dan check up kesehatan
          
          rincian pembelian: disini kalian bisa melihat item atau perawatan yang kalian telah pilih dan bisa juga kalian menghapus item
                             telah kalian pilih jika terlalu banyak atau tidak diperlukan
          
          transaksi: disini kalian bisa cek saldo kalian 
                     -kemudian kalian bisa topup jika saldo kalian habis atau tidak mencukupi dengan minimal topup 50.0000 dan maksimal
                      topup 2.000.000 
                     -selanjutnya kalian bisa membayar yang ada di keranjang kalian dan setelah membayar akan muncul                                             nota pembayaran yang berisi nama user, tanggal dan jam pembayaran kemudian subtotal item belanja dan perawatan yang
                      yang kita pilih



cara penggunaan program:

menu utama:

<img width="483" height="180" alt="image" src="https://github.com/user-attachments/assets/ca5c15de-919f-426c-8d66-79f037070a1e" />

ini adalah tampilan menu utama yang berisi daftar/masuk/keluar dengan memilih angka 1/2/3

isi menu daftar: 

<img width="208" height="76" alt="image" src="https://github.com/user-attachments/assets/ea913c9a-ac2f-40e0-9990-4ab43180b386" />

ini adalah isi menu daftar dan contoh pengisian nya minimal 3 karakter dan maksimal 20 karakter

isi menu login:

<img width="241" height="89" alt="image" src="https://github.com/user-attachments/assets/536e86b1-37bd-4fc7-8ff5-ac6f8ee1743d" />

ini adalah isi menu masuk kita ambil contoh masuk sebagai admin, disini untuk password sudah ditutupi oleh pwinput agar tidak terlihat

isi menu keluar

<img width="379" height="110" alt="image" src="https://github.com/user-attachments/assets/66c4a72d-a675-4f95-a7aa-73994bd1b168" />

ini adalah isi menu keluar yang berisi ucapan terimakasih sudah mengunjungi program ini


menu admin:

<img width="531" height="298" alt="image" src="https://github.com/user-attachments/assets/7f646d29-4854-4d1b-97a3-b7da0144e11e" />

ini adalah tampilan menu utama yang berisi tambah data/lihat data/ubah data/hapus data/kembali dengan memilih angka 1/2/3/4/5

isi menu tambah data:

<img width="147" height="95" alt="image" src="https://github.com/user-attachments/assets/dba9e529-93ea-40b4-9866-b7895ca7dbf4" />

pertama akan muncul 3 submenu pilihan ingin tambah data barang atau data hewan dengan memilih angka 1/2 dan 3 untuk kembali

jika memilih tambah barang:

<img width="241" height="153" alt="image" src="https://github.com/user-attachments/assets/83f2345c-e501-40e0-b1df-89f4b4d1392b" />

akan muncul pengisian nama barang kemudian ditanya barang ini masuk ke kategori kebutuhan/makanan dengan memilih angka 1/2

<img width="444" height="224" alt="image" src="https://github.com/user-attachments/assets/adb2f743-033f-46d1-93f1-2c6a3657260f" />

kemudian kita akan mengisi harga barang dengan minimal harga 10.000 dan maksimal 2.000.000

<img width="448" height="278" alt="image" src="https://github.com/user-attachments/assets/fd1e6691-8781-4272-b7f2-8881aa0453c7" />

setelah menginput nama, kategori, dan harga barang akan muncul pesan "apakah data suda benar" jika iya maka data akan tersimpan ke database jika tidak maka akan penambahan data akan dibatalkan seperti dibawah ini dan untuk memilih menggunakan (y/n)

<img width="252" height="89" alt="image" src="https://github.com/user-attachments/assets/c68de030-4da0-455e-bcd2-0895a6979970" />

<img width="262" height="61" alt="image" src="https://github.com/user-attachments/assets/11c9d6b6-7fb7-48a8-bd51-f846ad94c60d" />


isi menu baca data:

<img width="428" height="393" alt="image" src="https://github.com/user-attachments/assets/94762d16-6637-412f-b257-90bfb332ecb9" />

ini adalah isi menu baca data maka akan memunculkan informasi data barang dan data hewan yang ada di database

isi menu ubah data:

<img width="193" height="90" alt="image" src="https://github.com/user-attachments/assets/c493d065-f8f9-4000-b4ef-ee497779051c" />

disini akan muncul 3 submenu ingin ubah data barang atau data hewan dengan memilih angka 1/2 dan 3 untuk kembali
isi menu ubah data dsini mirip seperti tambah data namun disini kita mengubah data yang sudah ada sebelumnya ada ada pesan "apakah data suda benar" diakhir pengisian data

isi menu hapus data:

<img width="179" height="87" alt="image" src="https://github.com/user-attachments/assets/d2e4c69f-dd72-4bdf-80bc-10619b967aec" />













