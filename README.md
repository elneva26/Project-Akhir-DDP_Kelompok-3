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

Algoritma pembayaran dirancang dengan logika yang memverifikasi kecukupan saldo sebelum memproses transaksi, dilengkapi dengan fitur top-up untuk menambah saldo dan sistem pembuatan nota transaksi otomatis. Untuk manajemen hewan, program memungkinkan user mendaftarkan hewan peliharaan mereka dengan validasi data yang ketat, serta menampilkan daftar hewan yang terdaftar under setiap user. Secara keseluruhan, program ini menunjukkan implementasi algoritma yang terstruktur dalam mengelola kompleksitas sistem petshop modern dengan tetap menjaga usability dan keamanan data.
