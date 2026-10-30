
def hitung_ipk(nilai_sks):
    """
    nilai_sks: list tuple (nilai_bobot, sks)
    """
    if not nilai_sks:
        raise ValueError("Data nilai tidak boleh kosong.")

    total_sks = sum(sks for _, sks in nilai_sks)

    if total_sks <= 0:
        raise ValueError("Total SKS harus lebih dari nol.")

    total_bobot = sum(
        bobot * sks for bobot, sks in nilai_sks
    )

    return round(total_bobot / total_sks, 2)


def konversi_nilai_huruf(nilai):
    if not 0 <= nilai <= 100:
        raise ValueError("Nilai harus berada di antara 0 dan 100.")

    if nilai >= 85:
        return "A"
    elif nilai >= 80:
        return "A-"
    elif nilai >= 75:
        return "B+"
    elif nilai >= 70:
        return "B"
    elif nilai >= 65:
        return "C+"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"


def generate_transkrip(mahasiswa, mata_kuliah):
    transkrip = {
        "mahasiswa": mahasiswa,
        "mata_kuliah": mata_kuliah,
        "total_sks": sum(
            mk["sks"] for mk in mata_kuliah
        )
    }

    return transkrip


if __name__ == "__main__":
    print("Testing utilitas akademik")

    data_nilai = [(4.0, 3), (3.5, 2), (3.0, 3)]
    print("IPK:", hitung_ipk(data_nilai))
    print("Huruf:", konversi_nilai_huruf(87))

    print(generate_transkrip(
        "Pajar",
        [{"nama": "Python", "sks": 3}]
    ))
