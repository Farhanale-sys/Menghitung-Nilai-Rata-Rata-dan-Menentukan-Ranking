# Program untuk menghitung nilai rata-rata dan menentukan ranking siswa

def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

def tentukan_ranking(nilai):
    # Membuat tuple dari nilai dan indeksnya
    nilai_dan_indeks = [(n, i) for i, n in enumerate(nilai)]
    
    # Mengurutkan berdasarkan nilai secara menurun
    nilai_dan_indeks.sort(reverse=True, key=lambda x: x[0])
    
    # Menentukan ranking
    ranking = [0] * len(nilai)
    for rank, (_, index) in enumerate(nilai_dan_indeks, start=1):
        ranking[index] = rank
    
    return ranking

def main():
    # Input nilai siswa
    jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    nilai = []
    
    for i in range(jumlah_siswa):
        nilai_siswa = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
        nilai.append(nilai_siswa)
    
    # Menghitung rata-rata
    rata_rata = hitung_rata_rata(nilai)
    print(f"Nilai rata-rata: {rata_rata:.2f}")
    
    # Menentukan ranking
    ranking = tentukan_ranking(nilai)
    print("Ranking siswa:")
    for i, rank in enumerate(ranking):
        print(f"Siswa ke-{i + 1}: Rank {rank}")

if __name__ == "__main__":
    main()
