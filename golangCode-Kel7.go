package main

import (
	"fmt"
)

// --- FUNGSI UTAMA I/O (HANYA UNTUK MEMBACA DATA, BUKAN MENGHITUNG) ---

// readAllInput membaca N input harga barang dari pengguna
// dan menyimpannya dalam sebuah slice/array.
func readAllInput(n int) []int {
	inputData := make([]int, n)
	var harga int

	for i := 0; i < n; i++ {
		fmt.Printf("Input harga barang ke-%d: ", i+1)
		// Membaca input harga ke-i
		fmt.Scan(&harga)
		inputData[i] = harga
	}
	return inputData
}

// --- FUNGSI ALGORITMA (MENGHITUNG DARI ARRAY YANG SUDAH TERISI) ---

// 1. ITERATIF: Aman (O(1) Ruang)
// Menerima array yang sudah diisi
func hitungTotalIteratif(A []int, n int) int {
	total := 0
	for i := 0; i < n; i++ {
		total += A[i]
	}
	return total
}

// 2. REKURSIF: Riskan (O(N) Ruang)
// Menerima array dan ukurannya N
func sumRecursive(A []int, n int) int {
	// Base case
	if n == 0 {
		return 0
	}
	// Rekurens: elemen terakhir + rekursif dari sisa N-1 elemen
	return sumRecursive(A, n-1) + A[n-1]
}

// --- Main Program ---

func main() {
	var n int

	fmt.Print("Masukkan jumlah barang (N): ")
	fmt.Scan(&n) // Input N

	// ====================================================================
	// LANGKAH 1: INPUT DATA (Hanya Sekali)
	fmt.Println("\n=========================================")
	fmt.Printf("MOHON MASUKKAN %d HARGA BARANG:\n", n)
	dataInput := readAllInput(n) // Meminta N input dari pengguna
	fmt.Println("=========================================")

	// ====================================================================
	// LANGKAH 2: PENGHITUNGAN (Komputasi)

	fmt.Println("\n======= UJI ITERATIF (Komputasi) =======")
	// Fungsi Iteratif menghitung dari dataInput
	totalIteratif := hitungTotalIteratif(dataInput)
	fmt.Printf("Total belanja (iteratif): %d\n", totalIteratif)

	fmt.Println("\n======= UJI REKURSIF (Komputasi) =======")
	// Fungsi Rekursif menghitung dari dataInput
	totalRekursif := sumRecursive(dataInput, n)
	fmt.Printf("Total belanja (rekursif): %d\n", totalRekursif)

	fmt.Println("\n=========================================")
	fmt.Printf("VERIFIKASI: Total sama? %t\n", totalIteratif == totalRekursif)
}
