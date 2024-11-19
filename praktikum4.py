# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
    return (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Perulangan untuk menambah data
while True:
    # Meminta input dari pengguna
    nim = input("Masukkan NIM mahasiswa: ")  # Meminta NIM
    nama = input("Masukkan nama mahasiswa: ")
    nilai_tugas = float(input("Masukkan nilai tugas: "))
    nilai_uts = float(input("Masukkan nilai UTS: "))
    nilai_uas = float(input("Masukkan nilai UAS: "))
    
    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas)
    
    # Menyimpan data ke dalam list
    data_mahasiswa.append({
        'nim': nim,  # Menyimpan NIM
        'nama': nama,
        'nilai_tugas': nilai_tugas,
        'nilai_uts': nilai_uts,
        'nilai_uas': nilai_uas,
        'nilai_akhir': nilai_akhir
    })
    
    # Menanyakan apakah ingin menambah data lagi
    tambah_data = input("Apakah Anda ingin menambah data? (y/t): ")
    if tambah_data.lower() != 'y':
        break

# Menampilkan daftar data dalam format tabel
print("\nDaftar Data Mahasiswa:")
print(f"{'No':<5} {'NIM':<15} {'Nama':<20} {'Nilai Tugas':<15} {'Nilai UTS':<15} {'Nilai UAS':<15} {'Nilai Akhir':<15}")
print("="*100)  # Garis pemisah
for index, mahasiswa in enumerate(data_mahasiswa):
    print(f"{index + 1:<5} {mahasiswa['nim']:<15} {mahasiswa['nama']:<20} {mahasiswa['nilai_tugas']:<15} {mahasiswa['nilai_uts']:<15} {mahasiswa['nilai_uas']:<15} {mahasiswa['nilai_akhir']:<15.2f}")