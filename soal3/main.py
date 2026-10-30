
from utilitas_akademik import (
    hitung_ipk,
    konversi_nilai_huruf,
    generate_transkrip
)


def main():
    mahasiswa = "Pajar"

    nilai = [
        (4.0, 3),
        (3.5, 2),
        (3.0, 3)
    ]

    mata_kuliah = [
        {"nama": "Python", "sks": 3, "nilai": 87},
        {"nama": "Basis Data", "sks": 2, "nilai": 78},
        {"nama": "Statistika", "sks": 3, "nilai": 72}
    ]

    ipk = hitung_ipk(nilai)

    print("Nama:", mahasiswa)
    print("IPK:", ipk)

    for mk in mata_kuliah:
        huruf = konversi_nilai_huruf(mk["nilai"])
        print(mk["nama"], ":", huruf)

    transkrip = generate_transkrip(mahasiswa, mata_kuliah)
    print("Transkrip:", transkrip)


if __name__ == "__main__":
    main()
