
from service.mahasiswa_service import (
    tambah_mahasiswa,
    ambil_semua_mahasiswa,
    ambil_mahasiswa,
    ubah_mahasiswa,
    hapus_mahasiswa
)


def main():
    print(tambah_mahasiswa("24001", "Pajar", "Sistem Informasi"))
    print(tambah_mahasiswa("24002", "Budi", "Informatika"))

    print("\nSemua mahasiswa:")
    print(ambil_semua_mahasiswa())

    print("\nCari mahasiswa:")
    print(ambil_mahasiswa("24001"))

    print("\nUpdate mahasiswa:")
    print(ubah_mahasiswa("24001", prodi="Data Science"))

    print("\nHapus mahasiswa:")
    print(hapus_mahasiswa("24002"))

    print("\nData akhir:")
    print(ambil_semua_mahasiswa())


if __name__ == "__main__":
    main()
