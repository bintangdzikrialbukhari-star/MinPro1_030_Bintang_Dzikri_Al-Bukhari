Nama : Bintang Dzikri Al Bukhari
NIM : 2609116030
Program Studi : Sistem Informasi

## Tentang Program Ini.
Program ini saya buat untuk mengelola sistem penitipan barang pada loker pintar (Smart Locker). Pengguna dapat memilih ukuran loker yang sesuai, pengamanan loker dengan PIN yang pengguna buat sendiri, dan mengambil kembali barang dengan verifikasi PIN yang telah pengguna buat/masukan saat menitipkan barang, serta peengguna dapat memantau?memeriksa status dari semua loker apakah loker tersebut terisi/kosong

## Materi yang ada di program ini.
### 1. Tuple = UKURAN = ("kecil", "sedang", "besar")
   dipergunakan untuk menyimpan kategori ukuran dari loker yang nilainya tetap dan tidak dapat berubah.
### 2. Nested List = loker
   digunakan untuk menyimpan data dari banyaknya loker di program dengan menyimpan secara struktur dan sesuai format.
   [nomor loker, ukuran, status, PIN]
### 3. While Loop = While True
   digunakan untuk proses pemilihan di menu utama (Titip barang, Ambil barang, Cek status, Keluar)
### 4. If/else 
   digunakan dalam menangani di halaman Menu Utama, Ukuran Loker, Validasi Nomor Loker, Verifikasi PIN saat pengambilan barang
### 5. For Loop
   digunakan pada :
   1. Mencari loker yang kosong sesuai permintaan pengguna
   2. Menyimpan PIN
   3. Menghapus dan mengosongkan data PIN setelah pengambilan barang

## Menu pada program & cara menjalankan program.

<img width="646" height="205" alt="Screenshot 2026-09-12 171418" src="https://github.com/user-attachments/assets/f746d0d6-3bcc-41ec-b37f-9555fb92bc2c" />

### MENITIPKAN BARANG

<img width="692" height="372" alt="Screenshot 2026-09-12 173222" src="https://github.com/user-attachments/assets/b2e62893-651a-497d-a1ec-f08d439a64a0" />

1. Membuka file Python
2. Run Program
3. Masukan angka 1 jika ingin mennitipkan barang
4. Masukan Angka 1-3 untuk memilih ukuran dari loker
5. Masukan PIN
6. Selesai

### MENGAMBIL BARANG

<img width="647" height="292" alt="Screenshot 2026-09-12 173237" src="https://github.com/user-attachments/assets/92fed20f-d8a4-4b6e-9832-dabd4e4d9b1a" />

1. Membuka file Python
2. Run Program
3. Masukan angka 2 jika ingin mengambil barang
4. Masukan PIN
5. Selesai

### MENGECEEK STATUS LOKER

<img width="672" height="442" alt="Screenshot 2026-09-12 173250" src="https://github.com/user-attachments/assets/34319771-e4a9-4568-9721-40997b6a0727" />

1. Membuka file Python
2. Run Program
3. Pilih angka 3  untuk mengecek status loker
4. Selesai

### KELUAR

<img width="655" height="241" alt="image" src="https://github.com/user-attachments/assets/75ecf6d4-68df-42fa-aa62-6d0d0926ddbe" />

1. Membuka file Python
2. Run Program
3. Pilih angka nomor 4 untuk keluar dari program
4. Selesai

## Flowchart.

<img width="2501" height="1557" alt="download" src="https://github.com/user-attachments/assets/60c6bee2-1852-4524-bb7d-7448dd9de72e" />

ini adalah hasil dari alur flowchart dari program Smart Locker.

## Proses Program di List.

### 1. Menambahkan proses data baru
   di data ini saya telah menambahkan proses penambahan data saat di menu pilihan 1, peengguna diminta untuk menginput PIN loker untuk bisa menitipkan barang

### 2. Menampilkan seluruh data
   di data ini saya menambahkan proses menampilkan seluruh data pada menu ke 3, dimana pengguna meeminta menampilkan seluruh status dan loker yang tersedia

### 3. Mengubah data yang sudah ada
   di data in saya telah menambahkan proses mengubah data yang sudah ada, dimana pada proses ini tidak di tampilkan di output melainkan di dalam coding, mengubah data       yang awalnya "kosong" menjadi "terisi"

### 4. Menghapus data
   di data ini saya juga menamahkan proses menghapus data, dimana saat pengguna mengambil barang lalu password yang awalnya sudah terisi menjadi hilang karena proses        sebelumnya telah berhasil.
  
