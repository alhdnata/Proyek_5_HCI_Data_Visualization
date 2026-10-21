# Proyek 5 — Human-Computer Interaction & Data Visualization

## Deskripsi

Proyek ini merupakan implementasi sederhana Human-Computer Interaction (HCI) dan Data Visualization menggunakan Python. Studi kasus yang digunakan adalah dashboard analisis penjualan produk.

Program memungkinkan pengguna memilih kategori produk, melihat ringkasan penjualan, membaca detail transaksi, dan membandingkan data melalui grafik.

## Tujuan

- Menerapkan interaksi pengguna melalui menu sederhana.
- Menyajikan informasi penjualan secara terstruktur.
- Memvisualisasikan data agar lebih mudah dipahami.
- Memungkinkan pengguna menyaring data berdasarkan kategori.
- Menyimpan hasil analisis untuk digunakan kembali.

## Teknologi

- Python
- Pandas
- Matplotlib
- CSV

## Fitur

1. Menampilkan total penjualan dan jumlah transaksi.
2. Menghitung total unit yang terjual.
3. Menentukan produk terlaris berdasarkan jumlah unit.
4. Menyaring data berdasarkan kategori.
5. Membuat grafik penjualan per produk dan kategori.
6. Mengekspor hasil filter ke CSV.

## Cara Menjalankan

Instal library yang diperlukan:

```bash
python -m pip install -r requirements.txt
```

Jalankan program:

```bash
python main.py
```

Pilih kategori produk melalui terminal. Masukkan `0` atau tekan Enter untuk menampilkan semua kategori.

## Struktur Proyek

```text
Proyek_5_HCI_Data_Visualization/
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── data_penjualan.csv
└── output/
    ├── data_terfilter.csv
    └── dashboard_penjualan.png
```

Dataset dibuat otomatis saat program pertama kali dijalankan jika file belum tersedia.

## Penerapan HCI

Prinsip HCI diterapkan melalui menu yang sederhana, instruksi yang jelas, serta penyajian ringkasan dan detail transaksi yang mudah dibaca. Pengguna dapat memilih kategori tanpa harus mengubah kode program.

## Penerapan Data Visualization

Matplotlib digunakan untuk membuat grafik batang yang membandingkan nilai penjualan antarproduk dan antarkategori. Grafik membantu pengguna mengenali produk dengan penjualan tinggi serta membandingkan kontribusi setiap kategori.

## Kesimpulan

Proyek ini menunjukkan bagaimana interaksi sederhana dan visualisasi data dapat membantu pengguna memahami informasi penjualan. Dataset yang digunakan merupakan data simulasi untuk keperluan pembelajaran, bukan transaksi bisnis nyata.
