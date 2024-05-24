# Analisis Performa Bike Sharing Dataset (2011-2012)

## Performa Peminjaman Sepeda

Performa peminjaman sepeda pada tahun 2011 hingga 2012 menunjukkan peningkatan yang cukup baik. Peningkatan signifikan terjadi antara kuartal 2 hingga kuartal 3 setiap tahunnya, diikuti dengan penurunan pada kuartal akhir tahun.

## Situasi dan Kondisi dengan Peminjaman Tertinggi

Analisis menunjukkan bahwa situasi dan kondisi dengan total peminjaman sepeda tertinggi dalam dua tahun tersebut adalah sebagai berikut:

- **Musim Gugur** memiliki total peminjaman tertinggi dibandingkan tiga musim lainnya.
- **Cuaca cerah dan sedikit berawan** merupakan kondisi cuaca dengan tingkat peminjaman tertinggi.
- **Waktu dengan peminjaman tertinggi** terjadi antara pukul 5 hingga 6 sore dan pukul 8 pagi.
- **Hari Senin hingga Jumat** menunjukkan lebih banyak peminjam sepeda, sedangkan pada hari **Sabtu dan Minggu** cukup ramai sejak pukul 12 siang hingga 3 sore.

## Statistik Peminjam Sepeda

- **Registered Customer**: Jumlah peminjam sepeda yang sudah terdaftar jauh lebih banyak dibandingkan peminjam biasa.
- **Casual Customer**: Meski jumlahnya lebih sedikit dibandingkan peminjam terdaftar, ada kebutuhan untuk memperluas pemasaran bisnis untuk menarik perhatian peminjam baru.

## Kesimpulan dan Rekomendasi

Berdasarkan analisis data peminjaman sepeda selama tahun 2011 dan 2012, terlihat bahwa ada pola musiman dan harian yang mempengaruhi jumlah peminjaman. Untuk meningkatkan jumlah peminjaman, strategi pemasaran perlu difokuskan pada:

- Menarik peminjam baru yang belum terdaftar.
- Memanfaatkan periode waktu dan kondisi cuaca yang telah terbukti memiliki tingkat peminjaman tinggi.

Dengan demikian, perusahaan dapat meningkatkan performa bisnis dan memperluas basis pelanggan yang lebih beragam.

# Dashboard Bike Sharing Dataset (2011-2012)

Untuk menjalankan dashboard ini di _local_ ada beberapa langkah yang perlu dilakukan

## Instal _Dependencies_

Untuk menginstall dependencies, anda dapat menjalankan code ini

### Anaconda

```
conda create --name main-ds python=3.11.9
conda activate main-ds
pip install -r requirements.txt
```

### Shell/Terminal

```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Dashboard di Local

```
cd dashboard
streamlit run dashboard.py
```
# BikeSharingDataset-Dicoding
