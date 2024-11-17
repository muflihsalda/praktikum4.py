# praktikum4.py
# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas): return (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Perulangan untuk menambah data
while True: # Meminta input dari pengguna nim = input("Masukkan NIM mahasiswa: ") # Meminta NIM nama = input("Masukkan nama mahasiswa: ") nilai_tugas = float(input("Masukkan nilai tugas: ")) nilai_uts = float(input("Masukkan nilai UTS: ")) nilai_uas = float(input("Masukkan nilai UAS: "))

 ![image](https://github.com/user-attachments/assets/18e650b6-ddf6-4bd1-8cb7-f1123a8ae05b)

# Menampilkan daftar data dalam format tabel
![image](https://github.com/user-attachments/assets/372a0ad7-a8fe-4aae-b1e8-36af31f15714)

# Penjelasan Program
Fungsi hitung_nilai_akhir:

Fungsi ini menerima tiga parameter (nilai_tugas, nilai_uts, dan nilai_uas) dan menghitung nilai akhir berdasarkan bobot yang telah ditentukan:
Nilai Tugas: 30%
Nilai UTS: 35%
Nilai UAS: 35%
Nilai akhir dihitung dengan rumus: [ \text{nilai_akhir} = (\text{nilai_tugas} \times 0.3) + (\text{nilai_uts} \times 0.35) + (\text{nilai_uas} \times 0.35) ]

List data_mahasiswa:

List ini digunakan untuk menyimpan data mahasiswa yang telah diinput.
Perulangan while True:

Program akan terus meminta input data mahasiswa hingga pengguna memilih untuk berhenti.
Dalam setiap iterasi, pengguna diminta untuk memasukkan NIM, nama, dan nilai-nilai (tugas, UTS, UAS).
Setelah itu, nilai akhir dihitung dan data mahasiswa disimpan dalam list data_mahasiswa.
Menanyakan Tambah Data:

Setelah data mahasiswa dimasukkan, program menanyakan apakah pengguna ingin menambah data lagi. Jika pengguna memasukkan 'y', program akan kembali ke loop. Jika 't', program akan keluar dari loop.
Menampilkan Daftar Data Mahasiswa:

Setelah keluar dari loop, program akan menampilkan semua data mahasiswa dalam format tabel yang terstruktur.
# Flowchart
Berikut adalah representasi flowchart dari program tersebut:
![image](https://github.com/user-attachments/assets/a1976a05-8b1c-49a9-8edc-4a1513f98434)

Hasil Program

Setelah menjalankan program dan memasukkan data mahasiswa, hasil yang akan ditampilkan dalam tabel adalah sebagai berikut:

![image](https://github.com/user-attachments/assets/6b214646-938c-47ea-a284-e3ffce9dfcfd)






