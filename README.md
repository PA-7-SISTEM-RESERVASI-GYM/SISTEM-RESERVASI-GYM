# PA-DDP-KELOMPOK-7-SISTEM-RESERVASI-GYM
Syavira Firnanda Prawiro (2509116072), Mikhel Febian (2509116056), Zahra Syifa Salsabilla (2509116057)

# Sistem Reservasi Gym
Sistem Reservasi Gym ini merupakan aplikasi berbasis Python yang dirancang untuk mempermudah proses pengelolaan kegiatan di pusat kebugaran. Melalui sistem ini, pengguna dapat melakukan reservasi kelas, membeli produk, serta melakukan top-up saldo secara praktis. Sementara itu, admin dapat mengelola data seperti kelas, produk, membership, saldo top-up, dan riwayat transaksi pengguna.

# Flowchart Sistem Reservasi Gym

## Menu Utama
![Flowchart PA Menu utama](https://github.com/user-attachments/assets/aaf3054c-772c-4c67-8b83-17c2fceb85e5)

Flowchart menu utama ini menggambarkan alur utama sistem reservasi gym, mulai dari login, registrasi, hingga keluar. Pengguna dapat membuat akun baru atau masuk menggunakan akun yang sudah ada. Setelah login, sistem membedakan akses antara admin dan user sesuai perannya.

## Menu Admin
![Menu admin revisi](https://github.com/user-attachments/assets/23ae38ce-f069-41b3-90a1-22b0e2f4ca1c)

Flowchart ini menjelaskan alur kerja halaman admin pada sistem reservasi gym, di mana admin dapat mengelola data produk, membership, reservasi, dan karyawan. Setiap menu memiliki fitur untuk melihat, menambah, mengedit, dan menghapus data. Setelah selesai, admin dapat kembali ke menu utama.

## CRUD Admin
![CRUD admin revisi](https://github.com/user-attachments/assets/f6a64cc3-e936-44f1-be0a-ee79c51cf761)

Flowchart ini menggambarkan proses CRUD (Create, Read, Update, Delete) pada sistem admin. Admin dapat melihat, menambah, mengedit, dan menghapus data yang tersimpan di file JSON. Setiap tindakan divalidasi dengan pengecekan ID dan menampilkan pesan keberhasilan atau kesalahan sesuai hasil proses.

## Menu User
![Menu user revisi](https://github.com/user-attachments/assets/94993054-4609-4531-b6ff-4b3aca59b07e)

Flowchart ini menjelaskan alur aktivitas pengguna dalam sistem reservasi gym, mulai dari pembelian produk, pemesanan kelas, hingga top-up saldo dan melihat invoice. Setiap proses mencakup pengecekan data, validasi saldo, serta penyimpanan transaksi ke file JSON. Setelah transaksi selesai, sistem menampilkan hasil seperti invoice atau saldo terbaru pengguna.

# Alur Panduan Penggunaan Program
## 1.	Penggunaan Library dan Modul 
<img width="833" height="110" alt="image" src="https://github.com/user-attachments/assets/002e9068-2642-4012-9536-deada23107c5" />

Di awal program ini kami menggunakan beberapa library dan modul seperti os, json, pwinput, prettytable, dan datetime. Os sendiri berfungsi untuk membersihkan tampilan layar terminal agar lebih bersih dan rapi. Json untuk membaca dan menulis data dalam format Json. Pwinput untuk mengubah karakter password menjadi tanda *. Prettytable untuk menampilkan data dengan bentuk tabel. Terakhir datetime untuk mendapatkan informasi tanggal dan waktu.

## 2.	Halaman Menu Utama
<img width="833" height="379" alt="image" src="https://github.com/user-attachments/assets/80db4f7c-cd72-4c94-9379-1cc62eeb8e81" />

Di halaman ini, program akan menampilkan menu utama dengan memberikan 3 pilihan. Yang pertama login, kedua registrasi, dan terakhir keluar aplikasi.Jika pengguna memilih pilihan 1 pengguna akan masuk ke tampilan menu login, jika pengguna memilih pilihan 2 maka pengguna akan ditampilkan menu registrasi, terakhir jika pengguna memilih opsi 3 maka pengguna akan keluar dari aplikasi atau program Di sini program juga menyediakan perulangan while True agar menu dapat dijalankan sampai pengguna dapat memilih menu keluar saat run nanti.

## 3.	Menu Registrasi
<img width="833" height="438" alt="image" src="https://github.com/user-attachments/assets/a247c8df-5cf3-487e-ac2d-e42d03645aa5" />

Menu Registrasi dapat dijalankan ketika pengguna memilih opsi 2 pada  menu utama. Registrasi digunakan untuk pengguna yang belum memiliki akun. Saat masuk, program membuka file users.json untuk membaca data pengguna yang ada. Jika file belum ada atau rusak, program akan membuat daftar pengguna kosong. Setelah itu, pengguna diminta untuk memasukkan username yang baru. Program akan memeriksa apakah username tersebut sudah digunakan oleh pengguna lain terlebih dahulu jika sudah ada, pengguna harus memasukkan username lain. Setelah username valid, pengguna diminta untuk memasukkan password dan melakukan konfirmasi. Jika konfirmasi tidak cocok, pengguna harus mengulanginya sampai benar. Setelah semua data valid, program akan membuat ID pengguna secara otomatis berdasarkan jumlah data yang ada, lalu menyimpan username, password, dan saldo awal 0 ke dalam users.json. Selanjutnya, program akan menampilkan pesan “Registrasi berhasil” lalu meminta pengguna untuk login.

## 4.	Menu Login
<img width="833" height="424" alt="image" src="https://github.com/user-attachments/assets/98c19265-cd88-40d7-8dcc-413923740bf4" />
<img width="833" height="124" alt="image" src="https://github.com/user-attachments/assets/b1a3d67b-59e9-4507-8c7b-32d48045f032" />

Menu login dapat  dijalankan ketika pengguna memilih opsi 1 pada menu utama. Login dapat digunakan jika pengguna sudah memiliki akun. Pengguna diminta memasukkan username dan password untuk verifikasi. Jika data sesuai dan username adalah “admin”, program menampilkan pesan sambutan untuk admin dan menjalankan fungsi admin(). Jika username bukan admin, program akan memeriksa data dan menganggap pengguna sebagai user; jika sesuai, program akan menampilkan pesan “Login Berhasil! Selamat Datang [username]” dan dijalankan fungsi user(). Pengguna memiliki tiga kali kesempatan untuk login, tetapi jika pengguna gagal tiga kali, program akan menampilkan pesan “Maaf, kesempatan Anda habis!” lalu menghentikan proses login.

## 5.	Menu Admin
<img width="833" height="373" alt="image" src="https://github.com/user-attachments/assets/5497dd81-e2c1-4a3c-8f5f-a456fd0ea8f2" />

Program menu admin dapat dijalankan ketika pengguna berhasil login sebagai admin. Program menampilkan daftar menu yang terdiri dari Manajemen Produk, Membership, Reservasi, Top-Up, dan Kembali. Admin diminta memilih opsi dari 1 hingga 5 dalam perulangan while True, sehingga menu akan terus tampil hingga admin memilih untuk kembali. Setiap angka memiliki fungsi masing-masing: angka 1 membuka Manajemen Produk, angka 2 Manajemen Membership, angka angka 3 Manajemen Reservasi, angka 4 Manajemen Top-Up, dan angka 5 mengembalikan admin ke menu utama melalui fungsi menu_utama(). Jika admin memasukkan pilihan di luar rentang tersebut, program menampilkan pesan kesalahan dan meminta input ulang.

## 6.	Manajemen Produk
<img width="833" height="414" alt="image" src="https://github.com/user-attachments/assets/ae3f94c7-02d4-402a-9017-02264af74b98" />

Program ini dapat dijalankan jika pengguna memilih opsi 1. Fungsi manajemen_produk() menampilkan menu utama pengelolaan produk yang berisi pilihan untuk melihat, menambah, mengedit, menghapus produk, atau kembali ke menu admin. Semua data produk disimpan dalam file produk.json yang digunakan oleh setiap fungsi terkait. Setelah menampilkan menu, program meminta admin memilih opsi dari 1 hingga 5. Pilihan 1 menampilkan daftar produk melalui fungsi Lihat_produk(), pilihan 2 menambahkan produk baru dengan Tambah_produk(), pilihan 3 mengedit data melalui Edit_produk(), dan pilihan 4 menghapus produk menggunakan Hapus_produk(). Jika admin memilih opsi 5, program akan memanggil fungsi admin() untuk kembali ke menu sebelumnya dan menghentikan perulangan.Jika admin memasukkan angka selain 1 sampai 5, program akan menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”, dan meminta admin untuk memasukkan pilihan ulang yang benar.

## 7.	Fungsi Lihat Produk
<img width="833" height="324" alt="image" src="https://github.com/user-attachments/assets/6e64c68e-971c-4b16-9992-d804adf27d0f" />

Fungsi Lihat_produk digunakan untuk menampilkan daftar produk yang tersimpan dalam file json. Ketika dijalankan program akan menampilkan judul “Daftar Produk Tersedia” dan mencoba membaca data produk dengan menggunakan blok try-except agar tidak error jika file tidak ada atau formatnya salah. Jika data kosong, program menampilkan pesan “Belum ada produk yang tersimpan” dan berhenti. Jika sudah ada data, program akan membuat tabel menggunakan PrettyTable untuk menampilkan ID, Nama Produk, Harga, Stok, dan Kategori secara rapi. Setiap produk ditambahkan ke tabel menggunakan item.get(), lalu tabel dicetak dan data dikembalikan agar dapat digunakan oleh fungsi lain.

## 8.	Fungsi Tambah Produk
<img width="833" height="431" alt="image" src="https://github.com/user-attachments/assets/76e2f79d-e630-48f4-87e8-ad888d239981" />
<img width="833" height="192" alt="image" src="https://github.com/user-attachments/assets/9a469ea8-072b-4e81-8651-293a2d1f44f7" />

Fungsi Tambah Produk digunakan untuk menambahkan produk baru ke dalam file json. Program ini menampilkan menu “Tambah Produk” dan meminta pengguna memasukkan ID, nama produk, harga, stok, serta kategori. Nilai harga dan stok diperiksa agar berupa angka positif saja dengan memanfaatkan blok try-except. Jika file data belum tersedia, program akan membuat daftar kosong terlebih dahulu. Setelah semua input dinyatakan valid, system akan memastikan tidak ada duplikasi ID maupun nama produk sebelum menyimpan data baru tersebut ke file json.

## 9.	Fungsi Edit Produk
<img width="833" height="428" alt="image" src="https://github.com/user-attachments/assets/61da21eb-9010-4e49-be53-91f6fc8e865b" />

Fungsi Edit_Produk(json_file) digunakan untuk mengedit data produk dalam file json. Program menampilkan daftar produk, meminta pengguna memasukkan ID produk yang ingin diubah, lalu menampilkan data lamanya. Pengguna bisa mengganti nama dan harga produk atau menekan enter untuk melewati. Program juga memeriksa agar harga tidak negatif dan file json harus ada. Fungsi ini digunakan untuk memperbarui data.

## 10.	Fungsi Hapus Produk
<img width="833" height="328" alt="image" src="https://github.com/user-attachments/assets/48f473f7-4d9f-43a7-9c64-2db1ab57630a" />

Fungsi ini berfungsi untuk menghapus data produk dari file JSON berdasarkan ID yang dimasukkan oleh pengguna. Pertama, program menampilkan judul "Hapus Produk", lalu membuka file json dan memuat isinya ke dalam variabel data. Jika file tidak ditemukan atau kosong, maka program membuat daftar kosong. Selanjutnya, program meminta pengguna untuk memasukkan ID produk yang ingin dihapus. Kemudian program akan mencari produk dengan ID tersebut di dalam data. Jika ditemukan, produk akan dihapus dari daftar, kemudian data yang sudah diperbarui disimpan kembali ke file json. Setelah itu, program akan menampilkan pesan bahwa produk berhasil dihapus dan menampilkan daftar produk terbaru. Jika ID tidak ditemukan, maka program akan menampilkan pesan bahwa produk dengan ID tersebut tidak ada.

## 11.	Manajemen Member
<img width="833" height="416" alt="image" src="https://github.com/user-attachments/assets/697841e5-1480-4925-a051-d6b029930a15" />

Program ini dapat dijalankan jika pengguna memilih opsi 2. Fungsi ini berfungsi untuk mengelola data membership di program ini. Ketika dijalankan, program akan menampilkan menu “Manajemen Membership” dengan 5 pilihan, yaitu Lihat, Tambah, Edit, dan Hapus data membership, serta kembali ke menu sebelumnya. Program menggunakan file berjudul member.json sebagai tempat penyimpanan data. Kemduian pengguna diminta memasukkan pilihan, lalu program akan menjalankan fungsi sesuai nomor yang dipilih. Setelah setiap tindakan seperti lihat, tambah, edit, atau hapus selesai dilakukan, menu manajemen akan ditampilkan kembali. Jika pengguna memilih opsi “Kembali”, program akan keluar dari menu manajemen. Bila input tidak sesuai, program akan menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”.

## 12.	Fungsi Lihat Member
<img width="833" height="353" alt="image" src="https://github.com/user-attachments/assets/79edb99a-3e03-47fb-bca9-5c01ff588576" />

Fungsi ini berfungsi untuk menampilkan daftar paket membership yang ada di sebuah file json. Saat fungsi Lihat_member) dijalankan, program akan menampilkan judul “Daftar Paket Membership Tersedia” lalu mencoba membuka dan membaca file json yang diberikan. Jika file tidak ditemukan atau isinya rusak, maka program akan membuat data kosong, jika data kosong, program akan menampilkan pesan “Belum ada paket membership yang tersimpan” dan langsung berhenti. Namun, jika data tersedia, program akan membuat tabel menggunakan PrettyTable yang berisi ID, Nama Paket, Durasi, Harga, Stok, dan Deskripsi. Setelah semua data dimasukkan ke dalam tabel, tabel akan ditampilkan ke layar, lalu fungsi akan mengembalikan data tersebut.

## 13.	Fungsi Tambah Member
<img width="833" height="430" alt="image" src="https://github.com/user-attachments/assets/38a61d52-11da-4271-97b0-0254f9f72e4d" />
<img width="833" height="227" alt="image" src="https://github.com/user-attachments/assets/9746fe3a-6f8a-4654-b5f4-9148ccdea8f9" />

Fungsi Tambah_member ini berfungsi untuk menambahkan data paket membership baru ke dalam file json. Ketika dijalankan, program menampilkan judul “Tambah Paket Membership” lalu membuka file json untuk membaca data yang sudah ada. Jika file tidak ditemukan atau rusak, maka dibuat data kosong. Pengguna kemudian diminta mengisi ID, nama paket, durasi, harga, stok, dan deskripsi paket. Program memvalidasi agar harga dan stok tidak bernilai negatif serta memastikan input berupa angka. Setelah semua data dimasukkan, program akan memeriksa apakah ID atau nama paket sudah ada di data sebelumnya. Jika sudah ada, program akan menampilkan pesan bahwa paket tersebut sudah terdaftar. Jika belum, data baru ditambahkan ke file json, disimpan, dan pesan sukses ditampilkan. Terakhir, program akan memanggil fungsi Lihat_member untuk menampilkan daftar paket membership yang sudah diperbarui.

## 14.	Fungsi Edit Member
<img width="833" height="426" alt="image" src="https://github.com/user-attachments/assets/98930c12-57a9-42bf-ae26-a65b2d4b545a" />
<img width="833" height="364" alt="image" src="https://github.com/user-attachments/assets/814b70f1-f0ae-47c8-864e-aa3bb66e19cb" />
<img width="833" height="89" alt="image" src="https://github.com/user-attachments/assets/a8afbc68-b063-4a59-804c-c5d3046d3b66" />

Fungsi Edit_member ini berfungsi untuk mengubah data paket membership yang sudah ada di file json. Saat dijalankan, program akan menampilkan judul “Edit Paket Membership” dan membuka file json. Jika file tidak ada, program akan menampilkan pesan error dan berhenti. Setelah itu, program menampilkan daftar paket yang ada lalu meminta pengguna untuk memasukkan ID paket yang ingin diedit. Jika ID ditemukan, data lama akan ditampilkan dan pengguna bisa mengganti nilai-nilainya seperti nama paket, durasi, harga, stok, dan deskripsi. Atau pengguna bisa menekan enter jika ingin mempertahankan data lama. Program memvalidasi agar harga dan stok tidak bernilai negatif serta memastikan input angka benar. Setelah semua perubahan selesai, data akan diperbarui dalam file json dan disimpan kembali. Setelah itu, program akan menampilkan pesan “Paket berhasil diedit”. Jika data tidak ada, program akan menampilkan pesan “Paket dengan ID tersebut tidak ditemukan”.

## 15.	Fungsi Hapus Member
<img width="833" height="327" alt="image" src="https://github.com/user-attachments/assets/31a68d18-635a-4b3f-9dfb-238aad7a2078" />

Fungsi Hapus_member ini berfungsi untuk menghapus data paket membership yang ada di file json. Saat dijalankan, program akan menampilkan judul “Hapus Paket Membership” lalu membuka file json dan membaca isinya. Jika file tidak ada, program akan membuat daftar kosong. Selanjutnya, program akan  menampilkan daftar paket menggunakan fungsi Lihat_member() dan meminta pengguna untuk memasukkan ID paket yang ingin dihapus. Program akan mencari data dengan ID tersebut, jika ada, data akan dihapus dari daftar dan file json lalu  diperbarui dengan data yang baru. Setelah itu, program akan menampilkan pesan “Paket berhasil dihapus”. Jika ID tidak ada, maka program akan menampilkan pesan bahwa “Paket dengan ID tersebut tidak ditemukan”.	

## 16.	Manajemen Reservasi
<img width="833" height="403" alt="image" src="https://github.com/user-attachments/assets/ca5ad397-8420-4cf3-9812-8f2a89694872" />

Program ini dapat dijalankan jika pengguna memilih opsi 3. Fungsi	 manajemen_reservasi() ini berfungsi untuk mengelola data reservasi yang tersimpan dalam file json yang berjudul reservasi.json. Ketika dijalankan, program akan menampilkan menu utama yang berisi pilihan untuk Lihat, Tambah, Edit, Hapus reservasi, atau kembali ke menu sebelumnya. Pengguna akan diminta untuk memasukkan ngkaa pilihan, lalu program akan menjalankan fungsi sesuai pilihan pengguna tersebut seperti Lihat_reservasi(), Tambah_reservasi(), Edit_reservasi(), atau Hapus_reservasi(). Setelah selesai, program akan menampilkan kembali menu manajemen reservasi agar pengguna bisa memilih opsi yang lain. Jika pengguna memilih “5. Kembali”, program keluar dari menu. Jika input tidak valid, program menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”.

## 17.	Fungsi Lihat Reservasi
<img width="833" height="385" alt="image" src="https://github.com/user-attachments/assets/e1c29917-ae96-492e-be4f-1197a7823eef" />

Program Lihat_reservasi(json_file1) ini berfungsi untuk menampilkan daftar kelas atau data reservasi yang tersimpan dalam file JSON. Saat dijalankan, program mencoba membuka file dan membaca isinya; jika file tidak ditemukan atau kosong, program menampilkan pesan bahwa belum ada data kelas tersimpan. Jika data tersedia, program membuat tabel menggunakan library PrettyTable dengan kolom seperti ID, Nama Kelas, Hari, Waktu, Trainer, Kapasitas, Harga, Lokasi, dan Peserta Terdaftar. Setiap data dari file JSON dimasukkan ke dalam tabel, lalu tabel tersebut ditampilkan ke layar agar pengguna dapat melihat seluruh daftar kelas yang tersedia.

## 18.	Fungsi Tambah Reservasi
<img width="833" height="426" alt="image" src="https://github.com/user-attachments/assets/d40d30b1-00e5-4432-aa33-17b378f6e037" />

Fungsi Tambah_reservasi() ini berfungsi untuk menambahkan data kelas baru ke dalam file json yang berisi simpanan daftar reservasi. Pertama, program akan menampilkan judul lalu membuka file json dan memuat data yang ada. Jika file belum ada, maka program akan membuat daftar kosong. Selanjutnya, pengguna diminta utnuk mengisi detail kelas seperti ID, nama kelas, hari, waktu, nama trainer, kapasitas, harga, lokasi, dan jumlah peserta terdaftar. Untuk input angka seperti kapasitas, harga, dan peserta, program menggunakan perulangan agar pengguna hanya bisa memasukkan angka yang benar dan tidak bernilai negatif. Setelah semua data diisi, program akan memeriksa apakah ID atau nama kelas sudah ada di data yang sebelumnya untuk menghindari duplikasi. Jika tidak ada duplikasi, data baru akan ditambahkan ke dalam daftar, lalu disimpan kembali ke file json. Terakhir, program menampilkan pesan “Kelas baru berhasil ditambahkan” lalu memanggil fungsi Lihat_reservasi() untuk menampilkan daftar kelas yang sudah disimpan.

## 19.	Fungsi Edit Reservasi
<img width="833" height="437" alt="image" src="https://github.com/user-attachments/assets/6952f9cc-dc45-46eb-8d00-98b065cd8b77" />

Fungsi edit_reservasi(json_file1) ini digunakan untuk mengedit data kelas yang tersimpan di file JSON. Program akan menampilkan judul menu "Edit Reservasi", lalu membuka file JSON yang berisi data kelas. Jika file tidak ada, program akan menampilkan pesan “File tidak ditemukan”. Jika data berhasil dibaca, pengguna diminta untuk memasukkan ID kelas yang ingin diedit. Program akan mencari ID yang dimasukkan di dalam data; jika ada, program akan menampilkan data lama dan meminta pengguna untuk mengisi data baru seperti nama kelas, hari, waktu, trainer, kapasitas, harga, lokasi, dan jumlah peserta. Pengguna bisa menekan enter jika ingin mempertahankan data yang lama. Sistem akan memeriksa agar nilai numerik seperti kapasitas, harga, dan peserta tidak bernilai negatif. Setelah selesai, data yang telah diubah akan disimpan kembali ke file JSON, lalu program menampilkan pesan “Kelas berhasil diedit”. Jika ID yang dimasukkan tidak ditemukan, maka akan muncul pesan “Kelas dengan ID tersebut tidak ada”.

## 20.	Fungsi Hapus Reservasi
<img width="833" height="375" alt="image" src="https://github.com/user-attachments/assets/fedafa09-a51c-4c95-a046-ccfab7146809" />

Fungsi ini digunakan untuk menghapus data kelas dari file JSON. Program akan menampilkan judul menu "Hapus Reservasi", lalu membuka file JSON yang berisi daftar kelas. Jika file tidak adaa, program akan membuat daftar kosong. Setelah itu, program akan amenampilkan daftar kelas yang ada dan meminta pengguna memasukkan ID kelas yang ingin dihapus. Program kemudian mencari ID yang dimasukkan di dalam data. Jika ada, data kelas tersebut akan dihapus dari daftar, lalu file JSON diperbarui dengan data terbaru. Setelah penghapusan berhasil, program akan menampilkan pesan “Kelas berhasil dihapus” dan menampilkan daftar kelas yang tersisa. Namun, jika ID yang dimasukkan tidak ada, program akan menampilkan pesan “Kelas dengan ID tersebut tidak ada”.

## 21.	Manajemen Top-Up
<img width="833" height="430" alt="image" src="https://github.com/user-attachments/assets/0e19ed4b-0c8b-4ac0-8c74-19c92c8e78e2" />

Program ini dapat dijalankan jika pengguna memilih opsi 4. Program pada ini adalah fungsi manajemen top up saldo yang digunakan admin untuk mengelola data top up dalam sistem. Ketika fungsi dijalankan, program akan menampilkan menu “Manajemen Top Up Saldo” yang berisi lima pilihan: Lihat top-up, Tambah top-up, Edit top-up, Hapus to- up, dan kembali. Selanjutnya, program akan meminta admin utnuk memasukkan pilihan. Jika admin memilih opsi 1 sampai 4, program akan menjalankan fungsi yang sesuai Lihat_topup, Tambah_topup, Edit_topup, atau Hapus_topup dengan membaca dan menyimpan data dari file topup.json. Setelah menjalankan fungsi tersebut, program akan kembali menampilkan menu top up agar admin bisa memilih lagi. Jika admin memilih opsi 5, program akan kembali ke menu admin utama. Bila admin memasukkan angka selain 1 sampai 5, sistem akan menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”.

## 22.	Fungsi Lihat Top-Up
<img width="833" height="319" alt="image" src="https://github.com/user-attachments/assets/e3f3a029-a008-404c-841a-d5dd912f909a" />

Fungsi ini berfungsi untuk menampilkan daftar top up dari file data. Ketika fungsi ini dijalankan, program akan menampilkan judul “Daftar Top Up”. Lalu, program membuka file topup.json untuk membaca data top up yang sudah ada. Jika file tidak ditemukan atau kosong, maka program akan membuat daftar kosong dan menampilkan pesan “Belum ada data top up yang tersimpan”. Jika data ada, program akan menampilkan dalam bentuk tabel menggunakan modul PrettyTable, dengan kolom “ID”, “Kode Top Up”, dan “Nominal”. Setelah semua data ditampilkan dalam tabel, program mengembalikan data tersebut agar bisa digunakan kembali oleh bagian program yang lain.

## 23.	Fungsi Tambah Top-Up
<img width="833" height="430" alt="image" src="https://github.com/user-attachments/assets/5d58a078-17bd-4ce7-8d2b-0effe0de60fa" />

Fungsi	 ini berfungsi untuk menambah data top up baru ke dalam sistem. Ketika fungsi Tambah_topup() dijalankan, program akan menampilkan judul “Tambah Top Up” dan membuka file topup.json untuk membaca data yang sudah ada. Jika file belum ada atau kosong, maka program akan membuat daftar data baru. Lalu, admin akan diminta untuk memasukkan ID top up, kode top up, dan nominal. Program akan memeriksa apakah input nominal berupa angka dan dan bukan angka yang bernilai negatif Jika input salah, pengguna akan diminta untuka mengulang. Setelah itu, program akan mengecek apakah ID atau kode top up yang dimasukkan sudah berada di dalam data, jika sudah ada maka proses akan dibatalkan. Jika belum, data baru akan ditambahkan ke dalam daftar, lalu disimpan kembali ke file topup.json. Setelah berhasil, program akan menampilkan pesan “Top up baru berhasil ditambahkan” dan menampilkan daftar top up terbaru.

## 24.	Fungsi Edit Top-Up
<img width="833" height="436" alt="image" src="https://github.com/user-attachments/assets/f7172f8b-6c52-4456-88f8-94127c482b8c" />
<img width="833" height="192" alt="image" src="https://github.com/user-attachments/assets/7155cebf-adb7-43d9-99af-9ea298313e98" />

Fungsi ini berfungsi untuk mengedit data yang ada di dalam file.  Jika fungsi Edit_topup() dijalankan, program akan menampilkan judul “Edit Data Top Up” dan membuka file topup.json. Jika file tidak ada, program akan menampilkan pesan “File tidak ditemukan” lalu berhenti. Jika berhasil membaca data, program akan menampilkan daftar top up yang ada dan meminta admin untuk memasukkan ID top up yang ingin diedit. Jika ID tersebut ada, program akan menampilkan data lama dan meminta admin untuk memasukkan kode top up baru serta nominal baru. Admin bisa menekan enter untuk melewati bagian yang tidak ingin diubah. Program akan memastikan bahwa nominal yang dimasukkan berupa angka dan bukan angka negatif. Setelah perubahan data selesai, data baru akan disimpan kembali ke file topup.json. Jika ID yang dimasukkan tidak ada, program akan menampilkan pesan “Data Top-up dengan ID tersebut tidak ditemukan”.

## 25.	Fungsi Hapus Top-Up
<img width="833" height="379" alt="image" src="https://github.com/user-attachments/assets/7503cad6-b667-4c29-a837-a2b16fe4f39d" />

Fungsi ini berfungsi untuk menghapus data top up yang ada dari sistem. Saat fungsi ini dijalankan, program akan menampilkan judul “Hapus Data Top Up” dan membuka file topup.json untuk membaca data yang disimpan. Jika file tidak ditemukan atau kosong, maka program akan membuat daftar data kosong. Setelah itu, data top up yang ada akan ditampilkan, lalu admin akan diminta untuk memasukkan ID top up yang ingin dihapus. Program akan mencari data dengan ID tersebut, jika ada, admin akan diminta untuk melakukana konfirmasi penghapusan (ya/tidak). Jika admin memilih “tidak”, proses akan dibatalkan. Jika admin memilih “ya”, data akan dihapus dari daftar, kemudian file topup.json diperbarui dan disimpan kembali. Setelah itu, program akan menampilkan pesan “Data top up berhasil dihapus”. Jika ID yang dimasukkan tidak ada, program akan menampilkan pesan bahwa “Data Top-Up dengan ID tersebut tidak ditemukan”.

## 26.	Fungsi Load_Json dan Save_Json
<img width="833" height="153" alt="image" src="https://github.com/user-attachments/assets/e6c9e991-abce-480a-a387-2ac7db8e458a" />

Disini kami menggunakan fungsi load_json dan save-json. Fungsi load_json() bertugas membuka file JSON dari nama file yang diberikan, lalu membaca dan mengembalikan isi datanya. Jika file tidak ada atau tidak ditemukan atau terjadi kesalahan saat membaca, fungsi ini akan mengembalikan daftar kosong [] agar program tidak error. Fungsi save_json() digunakan untuk menyimpan data ke dalam file JSON. Fungsi ini akan membuka file dalam mode tulis 'w', lalu menyimpan data yang diberikan dalam format JSON.

## 27.	Menu User
<img width="833" height="428" alt="image" src="https://github.com/user-attachments/assets/ad6c48e6-5af4-49e4-a1c2-307a9436293d" />

Fungsi ini dapat dijalankan jika pengguna masuk sebagai user. Fungsi ini akan menampilkan daftar pilihan seperti Beli Produk, Reservasi, Top Up Saldo, Lihat Invoice, dan Kembali. Untuk menjalankan program ini pengguna diminta untuk memasukkan pilihan yang mereka inginkan. Jika pengguna memasukkan angka1 akan ditampilkan fungsi beli_produk(), Jika pengguna memasukkan angka 2 akan ditampilkan fungsi reservasi_kelas(), Jika pengguna memasukkan angka 3 akan ditampilkan fungsi top_up_saldo(), Jika pengguna memasukkan angka 4 akan ditampilkan fungsi lihat_invoice(). Jika pengguna memasukkan angka 5 “Kembali”, maka program akan memanggil fungsi menu_utama(). Jika pengguna memasukkan pilihan yang tidak valid, program akan menampilkan pesan “Pilihan tidak valid, Silakan coba lagi”, dan meminta untuk input ulang.

## 28.	Fungsi Beli Produk
<img width="833" height="425" alt="image" src="https://github.com/user-attachments/assets/78d5779b-52d6-4094-8dd5-bb95cabd30c8" />
<img width="833" height="407" alt="image" src="https://github.com/user-attachments/assets/af101129-32eb-45eb-add7-29461e478d33" />
<img width="833" height="78" alt="image" src="https://github.com/user-attachments/assets/16f93213-2750-4560-aced-32d523bb254b" />

Fungsi ini digunakan untuk pengguna agar dapat membeli produk yang disediakan pihak gym. Program akan menampilkan daftar produk yang tersedia dari 3 file json yang ada yaitu produk.json, users.json, dan invoice.json. Setelah itu, program akan memeriksa apakah pengguna yang sedang login sudah terdaftar dan apakah ada produk yang diinginkan tersedia. Jika produk ada, program akan menampilkan daftar produk dengan menggunakan tabel. Pengguna akan diminta untuk memasukkan ID produk yang ingin dibeli. Program akan memeriksa stok dan meminta pengguna memasukkan jumlah yang ingin dibeli. Jika jumlah yang dimasukkan sesuai dan saldo pengguna mencukupi, program akan menghitung total harga, mengurangi saldo pengguna juga stok produk sesuai pembelian, dan membuat data invoice baru yang berisi detail transaksi seperti tanggal, nama produk, jumlah, dan total harga. Setelah itu, semua data yang telah diperbarui user, produk, dan invoice akan disimpan kembali ke file JSON masing-masing. Lalu program akan menampilkan pesan “Pembelian berhasil” dan menampilkan sisa saldo pengguna, juga ID invoice dari hasil transaksi tersebut.

## 29.	Fungsi Reservasi Kelas
<img width="833" height="417" alt="image" src="https://github.com/user-attachments/assets/9bffae56-b2ab-42bf-9bd3-39efb066de7d" />
<img width="833" height="411" alt="image" src="https://github.com/user-attachments/assets/1a6a1a38-af22-43e5-a19e-59eee5e42337" />
<img width="833" height="68" alt="image" src="https://github.com/user-attachments/assets/95340496-fe71-461a-b24c-59d79aa1f1d7" />

Fungsi ini berfungsi untuk mengatur semua proses pemesanan kelas oleh pengguna. Saat fungsi ini dijalankan, program akan menampilkan daftar kelas yang tersedia dengan data seperti nama kelas, hari, waktu, trainer, harga, kapasitas, dan jumlah peserta. Setelah itu, pengguna diminta untuk memilih ID kelas yang ingin dipesan. Program lalu akan mengecek apakah kelas tersebut ada dan masih memiliki kuota. Jika kuota kelas penuh, proses akan dihentikan. Pengguna lalu diminta untuk memasukkan jumlah peserta yang akan ikut, dan program akan memastikan jumlahnya cocok dan tidak melebihi kapasitas. Selanjutnya, total biaya akan dihitung dan ditampilkan, lalu pengguna diminta untuk melakukan konfirmasi reservasi. Jika dikonfirmasi dan saldo pengguna cukup, saldo pengguna akan dikurangi sesuai harga, jumlah peserta kelas, dan data transaksi akan disimpan ke file users.json, reservasi.json, dan invoice.json. Selanjutnya, program menampilkan pesan “Reservasi berhasil” beserta sisa saldo pengguna.

## 30.	Fungsi Top-Up Saldo
<img width="833" height="337" alt="image" src="https://github.com/user-attachments/assets/0d8e7fbc-97c4-49c7-9735-18b0608d0644" />

Fungsi ini berfungsi untuk menambah saldo pengguna. Saat fungsi ini dijalankan, program akan menampilkan saldo pengguna saat ini, lalu meminta pengguna memasukkan kode top-up. Kode tersebut akan dicek di dalam data topup.json untuk memastikan validitasnya. Jika kode tidak valid, proses akan dibatalkan. Jika valid, nominal top-up ditampilkan dan pengguna diminta melakukan konfirmasi. Bila pengguna melakukan konfirmasi “ya”, saldo pengguna akan bertambah sesuai nominal top-up dan data pengguna disimpan kembali ke file users.json. Lalu, program akan menampilkan pesan “Top-up berhasil” beserta saldo terbaru pengguna.

## 31.	Fungsi Struk Terbaru
<img width="833" height="244" alt="image" src="https://github.com/user-attachments/assets/9c2565b0-274e-4c8c-a6fc-03437b43e402" />

Fungsi ini berfungsi untuk menampilkan struk transaksi terakhir dari pengguna. Program akan mengambil data dari file invoice.json, lalu mencari semua transaksi pengguna berdasarkan username. Transaksi terbaru akan diambil dari urutan terakhir dalam daftar tersebut, kemudian ditampilkan dalam format struk yang berisi ID invoice, tanggal transaksi, nama pelanggan, jenis transaksi, deskripsi, jumlah item, total harga, dan waktu cetak saat ini. Lalu setelah selesai, program akan menampilkan pesan “Terima kasih telah bertransaksi di GymFit”.

## 32.	Fungsi Lihat Invoice
<img width="833" height="327" alt="image" src="https://github.com/user-attachments/assets/8984c0ec-1a4a-4e49-97e6-1391dce4f56f" />

Fungsi ini berfungsi untuk menampilkan seluruh riwayat transaksi dari pengguna. Program akan membaca data dari file invoice.json, lalu memfilter semua transaksi yang sesuai dengan username pengguna. Jika tidak ada transaksi, maka akan muncul pesan “Belum ada transaksi untuk user ini”. Jika ada, program menampilkan daftar invoice yang berisi ID, tanggal, jenis transaksi, deskripsi, jumlah item, dan total harga masing-masing transaksi. Setelah semua data ditampilkan, program akan menghitung total keseluruhan dari semua transaksi dan menampilkannya bersamaan dengan pesan “Terima kasih telah bertransaksi di GymFit”.

# Cara Menjalankan Aplikasi Sistem Reservasi GYM

## Login Sebagai Admin
<img width="578" height="529" alt="image" src="https://github.com/user-attachments/assets/743abc83-bae9-4f85-bacd-a07da145cc01" />

Proses dimulai dari Menu Utama dengan tiga opsi utama: Login, Registrasi, dan Keluar Aplikasi.
Setelah pengguna berhasil login sebagai Admin, sistem akan menampilkan Menu Admin yang berisi beberapa fitur utama, yaitu:
- Manajemen Produk
- Manajemen Membership
- Manajemen Reservasi
- Manajemen Top Up
- Kembali ke Menu Utama

Interface ini dirancang dengan tampilan berbasis teks (CLI) untuk menjaga kesederhanaan, kecepatan akses, dan efisiensi penggunaan.

### 1. Manajemen Produk
<img width="576" height="378" alt="image" src="https://github.com/user-attachments/assets/cd2f1252-a161-47a0-acc8-348cac291d72" />

Cuplikan ini menampilkan tahapan navigasi setelah Admin memilih opsi “Manajemen Produk” dari menu utama Admin.
Pada bagian ini, sistem menampilkan lima fitur utama yang berfungsi untuk mengelola data produk, yaitu:
- Lihat Produk – Menampilkan daftar produk yang tersedia dalam sistem.
- Tambah Produk – Menambahkan data produk baru ke dalam database.
- Edit Produk – Mengubah informasi produk yang sudah terdaftar.
- Hapus Produk – Menghapus produk dari sistem.
- Kembali – Mengembalikan pengguna ke menu Admin sebelumnya.

Antarmuka ini berbasis Command Line Interface (CLI) untuk menjaga kesederhanaan, efisiensi, dan kemudahan akses bagi pengguna.

#### 1. Lihat Produk
<img width="564" height="526" alt="image" src="https://github.com/user-attachments/assets/17e59fd7-001f-44d3-af87-e6248a1901c2" />

Cuplikan ini menampilkan hasil dari pilihan menu “Lihat Produk” pada bagian Manajemen Produk.
Pada tahap ini, sistem menampilkan tabel berisi seluruh data produk yang tersimpan di database, dengan atribut sebagai berikut:
- ID – Kode unik untuk setiap produk.
- Nama Produk – Nama item yang dijual.
- Harga – Harga satuan produk.
- Stok – Jumlah produk yang tersedia.
- Kategori – Jenis atau pengelompokan produk (misalnya Perlengkapan atau Nutrisi).

Tampilan berbasis teks ini dibuat untuk memberikan kemudahan dalam memantau data produk secara cepat dan efisien langsung melalui terminal.

### 2. Tambah Produk
<img width="440" height="639" alt="Cuplikan layar 2025-10-26 220104" src="https://github.com/user-attachments/assets/23ca69b4-3d85-47a1-b9c0-1888ce417d67" />

Cuplikan ini menunjukkan proses penambahan produk baru ke dalam sistem.
Pengguna menginput data seperti ID produk, nama, harga, stok, dan kategori, kemudian sistem menyimpan data tersebut ke dalam file JSON.
Setelah proses berhasil, sistem menampilkan pesan “Produk Baru berhasil ditambahkan!” dan memperbarui daftar produk yang tersedia di terminal.

### 3. Edit Produk
<img width="436" height="768" alt="Cuplikan layar 2025-10-26 220340" src="https://github.com/user-attachments/assets/1642d029-d54f-49a9-86b3-8a3f7a8df76a" />

Gambar ini memperlihatkan proses pengeditan data produk yang sudah ada.
Pengguna memasukkan ID produk yang ingin diedit, lalu sistem menampilkan data lama sebagai referensi.
Setelah pengguna memperbarui informasi seperti nama, harga, atau stok, sistem menyimpan perubahan dan menampilkan pesan “Produk berhasil diedit!”.
Fitur ini memungkinkan admin memperbarui informasi produk secara efisien melalui antarmuka CLI.

### 4. Hapus Produk
<img width="354" height="759" alt="Cuplikan layar 2025-10-26 220504" src="https://github.com/user-attachments/assets/d1b94859-4a6d-4dee-8341-a502a9e9f9cd" />

Cuplikan ini menunjukkan proses penghapusan data produk dari sistem.
Pengguna memasukkan ID produk yang ingin dihapus, kemudian sistem meminta konfirmasi sebelum benar-benar menghapus data dari file JSON.
Jika pengguna memilih “ya”, maka sistem menampilkan pesan “Produk berhasil dihapus!” dan memperbarui daftar produk yang tersisa

### 5. Kembali
<img width="351" height="266" alt="image" src="https://github.com/user-attachments/assets/a796ea44-904c-4cc2-897c-04cbfc5a9507" />

Cuplikan ini menunjukan proses untuk kembali ke menu utama admin.

## 2. Manajemen Membership
<img width="351" height="259" alt="image" src="https://github.com/user-attachments/assets/992d09b6-de1e-4f55-9acd-3e2219c9b47f" />

Navigasi Menu Admin menampilkan 5 pilihan: Manajemen Produk, Manajemen Membership, Manajemen Reservasi, Manajemen Top Up, dan Kembali.
Pengguna memilih opsi 2 untuk masuk ke menu Manajemen Membership.

### 1. Lihat membership
<img width="557" height="237" alt="Cuplikan layar 2025-10-26 221557" src="https://github.com/user-attachments/assets/cb58e2a0-df3a-45ae-aa10-07e15f074839" />

Tampilan menu utama Manajemen Membership dengan 5 opsi: Lihat, Tambah, Edit, Hapus Membership, dan Kembali.
Ditampilkan pula daftar paket membership tersedia dengan detail ID, nama paket (Gold), durasi (2 jam), harga (1000000), dan stok (1).

### 2. Tambah Membership
<img width="481" height="443" alt="Cuplikan layar 2025-10-26 222910" src="https://github.com/user-attachments/assets/0d09e69a-4275-4c06-97d9-e0c39f37864a" />

Fitur tambah paket membership baru. Admin menginput data paket baru dengan ID 2, nama "Platinum", durasi 3 jam, harga 750000, stok 2, dan deskripsi "Bebas menggunakan semua alat".
Sistem berhasil menambahkan paket dan menampilkannya dalam daftar paket membership tersedia.

### 3. Edit Membership
<img width="659" height="609" alt="Cuplikan layar 2025-10-26 222209" src="https://github.com/user-attachments/assets/5d7886c9-da64-4c8e-9d2d-cc22341f89f4" />

Proses edit paket membership dengan ID 1 (Gold). Sistem menampilkan data lama dan meminta input baru untuk nama paket, durasi (diubah menjadi 1 jam), harga (500000), stok (2), dan deskripsi.
Setelah konfirmasi, paket berhasil diedit.

### 4. Fitur hapus paket membership.
<img width="425" height="487" alt="Cuplikan layar 2025-10-26 222256" src="https://github.com/user-attachments/assets/17e2a3d5-680c-43da-bc98-0400d44ef2b8" />


Sistem menampilkan daftar paket tersedia (Gold dengan durasi 1 jam, harga 500000, stok 2).
Setelah memasukkan ID paket yang ingin dihapus dan konfirmasi, paket berhasil dihapus dan daftar menjadi kosong.

### 5. Kembali
<img width="431" height="303" alt="Cuplikan layar 2025-10-26 223744" src="https://github.com/user-attachments/assets/4d78ec3c-3537-4622-a1bd-55c8bc74bc4f" />

Selesai mengelola Membership, sistem kembali ke Menu Admin utama yang menampilkan 5 pilihan: Manajemen Produk, Manajemen Membership, Manajemen Reservasi, Manajemen Top Up, dan Kembali.

## 3. Manajemen Reservasi
<img width="432" height="304" alt="image" src="https://github.com/user-attachments/assets/f2fd5544-a8ef-4cce-ae3d-f1116094d89e" />

Navigasi dari Menu Admin ke Manajemen Reservasi. Admin memilih opsi 3 untuk masuk ke menu Manajemen Reservasi yang menampilkan 5 pilihan: Lihat, Tambah, Edit, Hapus Reservasi, dan Kembali.

### 1. Lihat Reservasi
<img width="767" height="364" alt="Cuplikan layar 2025-10-26 223951" src="https://github.com/user-attachments/assets/abf274fe-d160-4c10-9a49-2bd81f4c4160" />


Fitur Lihat Reservasi menampilkan daftar kelas tersedia dalam bentuk tabel lengkap dengan informasi: ID kelas, Nama Kelas, Hari, Waktu, Trainer, Kapasitas, Harga, Lokasi, dan Peserta Terdaftar. Contoh: Kelas Yoga di Studio 1 setiap Jumat pukul 07.00-08.30 dengan trainer Diana.

### 2. Tambah Reservasi
<img width="781" height="589" alt="Cuplikan layar 2025-10-26 224128" src="https://github.com/user-attachments/assets/33a3176f-74c7-4c99-8ec5-1bf8486b3efb" />

Proses tambah reservasi baru untuk kelas Karate (K125). Admin menginput data: hari (senin), waktu kelas (11.00-12.30), nama trainer (Master King), kapasitas (20), harga (600000), lokasi (Dojo lantai 2), dan peserta terdaftar (12). Kelas baru berhasil ditambahkan ke daftar.

### 3. Edit reservasi
<img width="801" height="799" alt="Cuplikan layar 2025-10-26 224216" src="https://github.com/user-attachments/assets/f2b7b82f-1fd5-4401-a28c-4b6eed2d74ae" />


Fitur edit reservasi kelas. Admin memilih kelas K125 (Karate) untuk diedit. Sistem menampilkan data lama dan meminta input baru. Admin mengubah nama trainer menjadi "Master Shifu", kapasitas menjadi 20, dan peserta terdaftar menjadi 12. Kelas berhasil diedit dengan konfirmasi perubahan.

### 4. Hapus Reservasi
<img width="795" height="728" alt="Cuplikan layar 2025-10-26 224248" src="https://github.com/user-attachments/assets/48b23ddf-ebbe-4ad5-b64c-ed1bcb251042" />

Proses hapus reservasi kelas. Sistem menampilkan daftar kelas tersedia, admin memasukkan ID kelas yang ingin dihapus (K125 - Karate), mengkonfirmasi penghapusan, dan kelas berhasil dihapus dari sistem. Daftar kelas diperbarui tanpa kelas K125.

### 5. Kembali
<img width="442" height="305" alt="Cuplikan layar 2025-10-26 224304" src="https://github.com/user-attachments/assets/42884421-40d8-469e-8376-c8488517e65a" />

Selesai mengelola reservasi, sistem kembali ke Menu Admin utama yang menampilkan 5 pilihan: Manajemen Produk, Manajemen Membership, Manajemen Reservasi, Manajemen Top Up, dan Kembali.

## 4. Manajemen Top Up

<img width="565" height="357" alt="Cuplikan layar 2025-10-26 225622" src="https://github.com/user-attachments/assets/f6ac1fd2-2f95-47ed-9193-30ef622ed38e" />

Navigasi dari Menu Admin ke Manajemen Top Up Saldo. Admin memilih opsi 4 untuk masuk ke menu Manajemen Top Up Saldo yang menampilkan 5 pilihan: Lihat Daftar Top Up, Tambah Kode Top Up, Edit Kode Top Up, Hapus Kode Top Up, dan Kembali.

### 1. Lihat Daftar Top Up
<img width="557" height="390" alt="Cuplikan layar 2025-10-26 225640" src="https://github.com/user-attachments/assets/b594ddd6-85f6-4f59-ace4-8134da679b97" />

Fitur Lihat Daftar Top Up menampilkan tabel kode voucher top up yang tersedia dengan informasi: ID (TP001-TP004), Kode Top Up (GYM12345, GYM67890, dll), dan Nominal (200000, 150000, 100000, 500000).

### 2. Tambah Kode Top Up
<img width="570" height="560" alt="Cuplikan layar 2025-10-26 225659" src="https://github.com/user-attachments/assets/f2ef15b6-d3ee-4849-a583-24adad814ea8" />

Proses tambah kode top up baru. Admin menginput ID (TP005), kode top up (GYM54321), dan nominal (1000000). Voucher top up baru berhasil ditambahkan dan ditampilkan dalam daftar dengan total 5 voucher tersedia.

### 3. Edit Kode Top Up
<img width="554" height="699" alt="Cuplikan layar 2025-10-26 225722" src="https://github.com/user-attachments/assets/497f2034-6629-4138-92fa-11cc5ca978f1" />

Fitur edit kode top up. Admin memilih voucher TP005 untuk diedit. Sistem menampilkan data lama (kode: GYM54321, nominal: 1000000) dan meminta konfirmasi untuk lewati atau input baru. Setelah konfirmasi, data top up berhasil diedit.

### 4. Hapus Kode Top Up
<img width="563" height="747" alt="Cuplikan layar 2025-10-26 225741" src="https://github.com/user-attachments/assets/9406aca9-35c4-46e2-84c9-782295f5fac2" />

Proses hapus kode top up. Sistem menampilkan daftar voucher tersedia, admin memasukkan ID yang ingin dihapus (TP005), mengkonfirmasi penghapusan (ya/tidak), dan voucher berhasil dihapus. Daftar diperbarui menjadi 4 voucher (TP001-TP004).

### 5. Kembali
<img width="562" height="364" alt="Cuplikan layar 2025-10-26 225752" src="https://github.com/user-attachments/assets/a687fddc-37c2-4754-80a8-e439ca5d8d61" />

Selesai mengelola top up saldo, sistem kembali ke Menu Admin utama yang menampilkan 4 pilihan: Manajemen Produk, Manajemen Membership, Manajemen Reservasi, Manajemen Top Up, dan Kembali.

## 5. Kembali
<img width="584" height="330" alt="Cuplikan layar 2025-10-26 230728" src="https://github.com/user-attachments/assets/d8ea942f-349c-467d-a0ec-7af6be949cd6" />

Admin memilih opsi 5 (Kembali) dari Menu Admin untuk logout dan kembali ke Menu Utama. Sistem menampilkan 3 pilihan: Login, Registrasi, dan Keluar Aplikasi, menandakan admin telah berhasil keluar dari panel administrasi.












