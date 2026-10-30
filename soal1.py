import statistics

def hitung_statistik(angka):
    if not angka:
        raise ValueError("List angka tidak boleh kosong.")

    hasil = {
        "mean":statistics.mean(angka),
        "median": statistics.median(angka),
        "modus" : statistics.multimode(angka),
        "range" : max(angka) - min(angka),
        "starndard_deviation" : (
            statistics.stdev(angka) if len(angka) > 1 else 0.0
        )
    }
    return hasil

if __name__ == "__main__":
    data = list(map(
        int,
        input("Masukan minimal 5 data, pisahkan dengan spasi: ").split()
    ))
    if len(data) < 5:
        print("Minamal 5 data")
    else:
        hasil = hitung_statistik(data)
        print(hasil)
    