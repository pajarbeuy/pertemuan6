
def buat_response(success, message, data=None):
    return {
        "success": success,
        "message": message,
        "data": data
    }


if __name__ == "__main__":
    print(buat_response(True, "Berhasil"))
