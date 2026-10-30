
def buat_mahasiswa(nim, nama, prodi):
    return {
        "nim": nim,
        "nama": nama,
        "prodi": prodi
    }


if __name__ == "__main__":
    print(buat_mahasiswa("24001", "Pajar", "Sistem Informasi"))
