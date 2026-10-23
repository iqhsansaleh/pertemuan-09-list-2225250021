def rata_rata(data):
    """Menghitung rata-rata dari list data, menangani list kosong untuk mencegah ZeroDivisionError."""
    if not data:
        return 0.0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    """Menyaring nilai mahasiswa yang lulus berdasarkan batas kelulusan (default 60)."""
    return [nilai for nilai in data if nilai >= batas]


def analisis_nilai():
    # 1. Menyiapkan list nilai (minimal 10 nilai mahasiswa sesuai spesifikasi)
    nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

    # 2. Menghitung banyak data menggunakan len()
    jumlah_data = len(nilai)

    # 3. Menghitung total, minimum, maksimum, dan rata-rata
    total_nilai = sum(nilai) if jumlah_data > 0 else 0
    min_nilai = min(nilai) if jumlah_data > 0 else 0
    max_nilai = max(nilai) if jumlah_data > 0 else 0
    rerata = rata_rata(nilai)

    # 4 & 5. Menentukan list nilai yang lulus dan jumlahnya
    list_lulus = nilai_lulus(nilai, batas=60)
    jumlah_lulus = len(list_lulus)

    # 6. Menghitung jumlah belum lulus dari total data dikurangi jumlah lulus
    jumlah_belum_lulus = jumlah_data - jumlah_lulus

    # 7. Menampilkan seluruh hasil dengan format yang mudah dibaca
    print("=" * 45)
    print("     PROGRAM ANALISIS NILAI MAHASISWA")
    print("=" * 45)
    print(f"Daftar Seluruh Nilai  : {nilai}")
    print(f"Banyak Data (Jumlah)  : {jumlah_data}")
    print("-" * 45)
    print(f"Total Nilai           : {total_nilai}")
    print(f"Rata-rata Nilai       : {rerata:.2f}")
    print(f"Nilai Minimum         : {min_nilai}")
    print(f"Nilai Maksimum        : {max_nilai}")
    print("-" * 45)
    print(f"Batas Kelulusan       : 60")
    print(f"Jumlah Mahasiswa Lulus: {jumlah_lulus}")
    print(f"Daftar Nilai Lulus    : {list_lulus}")
    print(f"Jumlah Belum Lulus    : {jumlah_belum_lulus}")
    print("=" * 45)


if __name__ == "__main__":
    analisis_nilai()

    # Pengujian tambahan untuk menangani list kosong (Test Case Wajib)
    print("\n--- Uji Kasus List Kosong ---")
    list_kosong = []
    print(f"Data Kosong           : {list_kosong}")
    print(f"Hasil Rata-rata ([]): {rata_rata(list_kosong)}")
    print(f"Hasil List Lulus ([]): {nilai_lulus(list_kosong)}")