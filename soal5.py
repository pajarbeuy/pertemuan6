
import json
import requests


def main():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        users = response.json()

    except requests.RequestException as error:
        print("Gagal mengambil data API:", error)
        return

    # map + lambda: mengambil informasi yang diperlukan.
    data_users = list(map(
        lambda user: {
            "id": user["id"],
            "nama": user["name"],
            "email": user["email"],
            "kota": user["address"]["city"],
            "perusahaan": user["company"]["name"]
        },
        users
    ))

    # filter + lambda: hanya pengguna dengan email .com.
    users_com = list(filter(
        lambda user: user["email"].lower().endswith(".com"),
        data_users
    ))

    # sorted + lambda: urutkan berdasarkan nama.
    users_sorted = sorted(
        users_com,
        key=lambda user: user["nama"].lower()
    )

    hasil = {
        "jumlah_data_api": len(users),
        "jumlah_email_com": len(users_com),
        "data_pengguna": users_sorted
    }

    # Simpan hasil ke file JSON.
    with open("hasil_users.json", "w", encoding="utf-8") as file:
        json.dump(hasil, file, indent=4, ensure_ascii=False)

    print("Jumlah data API:", len(users))
    print("Jumlah email .com:", len(users_com))
    print("Hasil disimpan ke hasil_users.json")


if __name__ == "__main__":
    main()
