# Pertemuan 09 - List dan Pengolahan Data Numerik

Nama: Iqhsan Saleh  
NIM: 2225250021  
Kelas: 3A (S1 Pendidikan Matematika)

## Tujuan

Mengolah kumpulan data numerik dengan list Python untuk menghasilkan ringkasan statistik dan informasi kelulusan mahasiswa.

## Struktur Program

- `praktik/analisis_nilai_mahasiswa.py`: Implementasi fungsi `rata_rata(data)` untuk menghitung rata-rata dengan penanganan list kosong, fungsi `nilai_lulus(data, batas=60)` untuk memfilter nilai yang lulus, serta skrip utama untuk menampilkan ringkasan analisis statistik nilai.

## Cara Menjalankan

```bash
python praktik/analisis_nilai_mahasiswa.py
```

## Test Case

| Data | Yang diperiksa | Hasil yang diharapkan | Hasil aktual | Status |
| --- | --- | --- | --- | --- |
| `[60, 70, 80]` | Rata-rata | `70.00` | `70.00` | Lulus |
| `[60, 70, 80]` | Minimum / maksimum | `60 / 80` | `60 / 80` | Lulus |
| `[60, 70, 80]` | Jumlah lulus | `3` | `3` | Lulus |
| `[59, 60, 61]` | Batas kelulusan | `2 lulus` | `2 lulus` | Lulus |
| `[]` | Penanganan list kosong pada fungsi rata-rata | Tidak error | Tidak error (`0.0`) | Lulus |

## Refleksi

- **Hal yang dipahami:** Penggunaan struktur data *list* di Python efisien untuk mengelola kumpulan data numerik. Pengecekan kondisi awal, seperti list kosong, penting untuk mencegah `ZeroDivisionError`.
- **Kesalahan yang berhasil diperbaiki:** Memastikan fungsi perhitungan rata-rata memeriksa kondisi list kosong sebelum membagi total nilai dengan panjang list (`len`).
