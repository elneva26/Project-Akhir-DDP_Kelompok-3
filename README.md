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


- Fitur program:

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
________________________________________________________________________________________________________________________________________________________________________
flowchart:
menu utama:

<img width="8290" height="8315" alt="Flowchart PA DDP - malam-Menu Utama drawio" src="https://github.com/user-attachments/assets/674dd81f-dc9a-4c42-bf18-c03fcef6aaab" />

menu admin


![WhatsApp Image 2025-10-26 at 23 23 08](https://github.com/user-attachments/assets/1011cfed-3bd8-4002-b408-cd155992d2e8)




menu user


![WhatsApp Image 2025-10-26 at 23 23 08 (1)](https://github.com/user-attachments/assets/c03aeb0b-be2d-44b6-a566-b923ba592ef5)




________________________________________________________________________________________________________________________________________________________________________
- cara penggunaan program:

- menu utama:

<img width="483" height="180" alt="image" src="https://github.com/user-attachments/assets/ca5c15de-919f-426c-8d66-79f037070a1e" />

ini adalah tampilan menu utama yang berisi daftar/masuk/keluar dengan memilih angka 1/2/3

- isi menu daftar: 

<img width="208" height="76" alt="image" src="https://github.com/user-attachments/assets/ea913c9a-ac2f-40e0-9990-4ab43180b386" />

ini adalah isi menu daftar dan contoh pengisian nya minimal 3 karakter dan maksimal 20 karakter

- isi menu login:

<img width="241" height="89" alt="image" src="https://github.com/user-attachments/assets/536e86b1-37bd-4fc7-8ff5-ac6f8ee1743d" />

ini adalah isi menu masuk kita ambil contoh masuk sebagai admin, disini untuk password sudah ditutupi oleh pwinput agar tidak terlihat

- isi menu keluar

<img width="379" height="110" alt="image" src="https://github.com/user-attachments/assets/66c4a72d-a675-4f95-a7aa-73994bd1b168" />

ini adalah isi menu keluar yang berisi ucapan terimakasih sudah mengunjungi program ini


________________________________________________________________________________________________________________________________________________________________________

menu admin:

<img width="531" height="298" alt="image" src="https://github.com/user-attachments/assets/7f646d29-4854-4d1b-97a3-b7da0144e11e" />

ini adalah tampilan menu admin yang berisi tambah data/lihat data/ubah data/hapus data/kembali dengan memilih angka 1/2/3/4/5

- isi menu tambah data:

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


- isi menu baca data:

<img width="428" height="393" alt="image" src="https://github.com/user-attachments/assets/94762d16-6637-412f-b257-90bfb332ecb9" />

ini adalah isi menu baca data maka akan memunculkan informasi data barang dan data hewan yang ada di database

- isi menu ubah data:

<img width="193" height="90" alt="image" src="https://github.com/user-attachments/assets/c493d065-f8f9-4000-b4ef-ee497779051c" />

disini akan muncul 3 submenu ingin ubah data barang atau data hewan dengan memilih angka 1/2 dan 3 untuk kembali
isi menu ubah data dsini mirip seperti tambah data namun disini kita mengubah data yang sudah ada sebelumnya ada ada pesan "apakah data suda benar" diakhir pengisian data

- isi menu hapus data:

<img width="179" height="87" alt="image" src="https://github.com/user-attachments/assets/d2e4c69f-dd72-4bdf-80bc-10619b967aec" />

disini akan muncul 3 submenu ingin hapus data barang atau data hewan dengan memilih angka 1/2 dan 3 untuk kembali

<img width="373" height="210" alt="image" src="https://github.com/user-attachments/assets/ace3e379-2fe9-4b11-9e32-80c21780fa2c" />

disini kita ambil contoh hapus data barang, disini akan memunculkan data barang dan saat kita ingin menghapus kita bisa memilih no item yang ingin dihapus kita ambil contoh pilih no 2

<img width="359" height="221" alt="image" src="https://github.com/user-attachments/assets/c3632fea-030e-4aa1-a1b4-46b11d9694a4" />

itu adalah pesan jika data barang berhasil dihapus penggunaan untuk data hewan pun juga sama hanya berbeda isi datanya saja

- isi menu kembali

<img width="559" height="181" alt="image" src="https://github.com/user-attachments/assets/08369b0c-fa83-495b-90a6-f9563c8c7ac1" />

jika kita memilih menu keluar maka akan kembali ke menu utama


________________________________________________________________________________________________________________________________________________________________________

menu user:

<img width="489" height="291" alt="image" src="https://github.com/user-attachments/assets/365ef32e-1439-42b7-afbe-e529eb676af5" />

ini adalah tampilan menu user yang berisi kelola hewan/belanja kebutuhan hewan/perawatan/rincian pembelian/transaksi/kembali dengan memilih angka 1/2/3/4/5/6

- isi menu kelola hewan:

<img width="179" height="83" alt="image" src="https://github.com/user-attachments/assets/67359081-7300-4393-839b-0eea4d07f0df" />

disini akan ada 3 submenu yang isinya daftarkan hewan/lihat hewan saya dengan memilih angka 1/2 dan 3 untuk kembali ke menu user

- isi submenu daftarkan hewan
 
<img width="276" height="185" alt="image" src="https://github.com/user-attachments/assets/a09bb108-69ee-4206-aef1-283194e083d5" />

disitu kita akan mengisi nama, jenis, dan umur dari hewan kesayangan kita dan dilanjut pesan "apakah data suda benar" jika iya maka data akan tersimpan ke database HAE dan jika tidak maka pendaftaran hewan dibatalkan untuk memilih menggunakan (y/n)

-isi submenu lihat hewan saya:

<img width="302" height="135" alt="image" src="https://github.com/user-attachments/assets/28399b3c-83f8-4ba6-8a9f-97611f003457" />

di submenu lihat hewan saya maka akan memunculkan data hewan peliharaan kita seperti nama, jenis, dan umur nya

- isi menu data belanja kebutuhan hewan:

<img width="297" height="224" alt="image" src="https://github.com/user-attachments/assets/91f4c95e-558d-409a-b409-c4cd07631ef5" />

disini pertama akan memunculkan tabel kebutuhan dan makanan hewan selanjutnya untuk memilih item yang kita mau dengan memilih no item yang kita mau kita ambil contoh item no 1
setelah memilih item yang kita mau kita akan diminta mengisi jumlah item yang ingin kita beli dengan minimal 1 dan maksimal 10 setelah suda makan item akan masuk ke keranjang user

- isi menu perawatan:

<img width="799" height="280" alt="image" src="https://github.com/user-attachments/assets/7392565f-99d7-4cd0-8f77-152c07090215" />

disini pertama akan memunculkan tabel perawatan yang berisi vaksin, grooming, dan check up kesehatan untuk memilih perawatan kita bisa memilih angka yang ada didalem tabel 1/2/3 kita ambil contoh 1 yaitu vaksin selanjutnya kita akan memasukkan jumlah hewan yang ingin melakukan perawatan kita ambil contoh 2 hewan yang ingin melakukan perawatan

- isi menu rincian pembelian:

<img width="515" height="224" alt="image" src="https://github.com/user-attachments/assets/d2f4324b-5ab9-4ea8-85dc-6c1f600a10e0" />

disini akan memunculkan tabel rincian pembelian yang berisi item dan perawatan yang telah kita pilih dan banyaknya item yang kita pilih atau beli disini juga ada subtotal harga pembelian kita dan juga ada opsi menghapus item atau perawatan yang telah kita pilih jika salah pilih/beli kita bisa hapus dengan pilih angka 1 dan pilih no item atau perawatan yang ingin kita hapus dan untuk kembali ke menu user kita bisa pilih angka 2

- isi menu transaksi

<img width="193" height="92" alt="image" src="https://github.com/user-attachments/assets/12491dc2-f743-4d58-83fd-9a3657e0f0b9" />

di menu transaksi ini akan ada beberapa submenu yaitu cek saldo/ topup/bayar keranjang/kembali



cek saldo: di cek saldo akan memunculkan data saldo yang kita punya

<img width="226" height="132" alt="image" src="https://github.com/user-attachments/assets/20cea70e-3970-4522-9d22-649090f17e56" />


topup: kita bisa topup e-money kita jika habis atau tidak cukup dengan minimal 50.000 dan maksimal 2.000.000

<img width="441" height="140" alt="image" src="https://github.com/user-attachments/assets/44920f9c-21d8-4a55-abef-d3b47dddd841" />


bayar keranjang: disini kita bisa auto membayar belanja kebutuhan dan perawatan hewan kita jika saldo kita mencukupi yang kemudian dimunculkan nota pembayarannya

<img width="454" height="302" alt="image" src="https://github.com/user-attachments/assets/772eb6f1-ddf2-4c73-b36d-74302acbd936" />


- isi menu kembali

<img width="478" height="179" alt="image" src="https://github.com/user-attachments/assets/03bc42fa-53b4-4731-a1ff-9d1ac807e9bc" />

jika kita memilih menu kembali maka akan kembali ke menu utama

________________________________________________________________________________________________________________________________________________________________________

begitulah cara penggunaan "Sistem Manajemen Perawatan Hewan Peliharaan Hae Pet Shop" semoga dengan adanya program ini kalian dapat terbantu kedepannya sekian dari kami
terima kasih































