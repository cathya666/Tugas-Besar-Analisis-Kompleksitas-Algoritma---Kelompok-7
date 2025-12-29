import time
import matplotlib.pyplot as plt
import sys
import random

# Mengatur batas kedalaman rekursi agar fungsi rekursif bisa berjalan untuk N besar.
# PENTING: Untuk N hingga 10.000, batasan ini sangat diperlukan.
sys.setrecursionlimit(20000)

## 1. IMPLEMENTASI FUNGSI (Logic dari Kode Go Anda)

# Skema Iteratif: hitungTotalIteratif (O(1) Ruang)
def hitung_total_iteratif(A):
    """Menghitung total elemen array secara iteratif."""
    total = 0
    # Logic: for _, harga := range A { total = total + harga }
    for harga in A:
        total = total + harga
    return total

# Skema Rekursif: sumRecursive (O(N) Ruang)
def sum_recursive(A, n):
    """Menghitung total elemen array secara rekursif."""
    # Base case: if n == 0 { return 0 }
    if n == 0:
        return 0
    # Rekurens: return sumRecursive(A, n - 1) + A[n - 1]
    return sum_recursive(A, n - 1) + A[n - 1]

## 2. PENGUJIAN WAKTU EKSEKUSI

# Ukuran input yang akan diuji (N) - Contoh: 100 hingga 10.000 dengan interval 500
N_values = [n for n in range(100, 10001, 500)]

# List untuk menyimpan hasil waktu eksekusi
time_iterative = []
time_recursive = []

print("Memulai pengujian waktu (N hingga 10.000)...")

for N in N_values:
    # Membuat array input dummy (Harga barang acak) dengan ukuran N
    input_array = [random.randint(1, 1000) for _ in range(N)]

    # --- UJI SKEMA ITERATIF ---
    start_time = time.time()
    hitung_total_iteratif(input_array)
    end_time = time.time()
    time_iterative.append(end_time - start_time)

    # --- UJI SKEMA REKURSIF ---
    try:
        start_time = time.time()
        sum_recursive(input_array, N)
        end_time = time.time()
        time_recursive.append(end_time - start_time)
    except RecursionError:
        # Menangkap error jika Stack Overflow terjadi (walaupun batas sudah dinaikkan)
        print(f"RecursionError di N={N}. Data rekursif mungkin tidak lengkap.")
        time_recursive.append(None) # Menggunakan None jika gagal

print("Pengujian selesai.")

## 3. PEMBUATAN GRAFIK

plt.figure(figsize=(10, 6))

# Plot data
# Gunakan filter untuk menghilangkan None jika ada RecursionError
plt.plot(N_values, time_iterative, label='Skema Iteratif (O(1) Ruang)', color='blue', marker='o', markersize=4)
plt.plot([N for N, t in zip(N_values, time_recursive) if t is not None],
         [t for t in time_recursive if t is not None],
         label='Skema Rekursif (O(N) Ruang)', color='red', marker='x', markersize=4)

# Menambahkan Keterangan Grafik
plt.title('Perbandingan Waktu Eksekusi: Penjumlahan Total Belanja')
plt.xlabel('Ukuran Input (N: Jumlah Elemen Array)')
plt.ylabel('Waktu Eksekusi (Detik)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.figtext(0.5, 0.01, 'Analisis menunjukkan Iteratif memiliki Overhead lebih rendah daripada Rekursif pada kompleksitas O(N).', ha='center', fontsize=9)
plt.show()
