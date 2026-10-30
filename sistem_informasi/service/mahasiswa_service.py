
from model.mahasiswa import buat_mahasiswa
from utils.response import buat_response


# Penyimpanan in-memory dengan NIM sebagai kunci.
mahasiswa_db = {}


def tambah_mahasiswa(nim, nama, prodi):
    if nim in mahasiswa_db:
        return buat_response(False, "NIM sudah terdaftar.")

    mahasiswa_db[nim] = buat_mahasiswa(nim, nama, prodi)
    return buat_response(
        True, "Mahasiswa berhasil ditambahkan.",
        mahasiswa_db[nim]
    )


def ambil_semua_mahasiswa():
    return buat_response(
        True,
        "Data mahasiswa berhasil diambil.",
        list(mahasiswa_db.values())
    )


def ambil_mahasiswa(nim):
    mahasiswa = mahasiswa_db.get(nim)

    if mahasiswa is None:
        return buat_response(False, "Mahasiswa tidak ditemukan.")

    return buat_response(True, "Data ditemukan.", mahasiswa)


def ubah_mahasiswa(nim, nama=None, prodi=None):
    mahasiswa = mahasiswa_db.get(nim)

    if mahasiswa is None:
        return buat_response(False, "Mahasiswa tidak ditemukan.")

    if nama is not None:
        mahasiswa["nama"] = nama

    if prodi is not None:
        mahasiswa["prodi"] = prodi

    return buat_response(True, "Data berhasil diperbarui.", mahasiswa)


def hapus_mahasiswa(nim):
    mahasiswa = mahasiswa_db.pop(nim, None)

    if mahasiswa is None:
        return buat_response(False, "Mahasiswa tidak ditemukan.")

    return buat_response(True, "Mahasiswa berhasil dihapus.", mahasiswa)


if __name__ == "__main__":
    print(tambah_mahasiswa("24001", "Pajar", "Sistem Informasi"))
    print(ambil_semua_mahasiswa())
    print(ubah_mahasiswa("24001", nama="Pajar Beuys"))
    print(hapus_mahasiswa("24001"))
