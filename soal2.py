def validation_data(data, schema, *args, **kwargs):
    erors=[]

    # firld tambahan yang wajid divalidasi
    required_fields = kwargs.get("required_fileds", [])
    required_fields = set(required_fields)

    for f, aturan in schema.items():
        nilai= data.get(f)

        wajib = aturan.get("required", False) or f in required_fields

        if f not in data:
            if wajib:
                erors.append(f"{f}: field wajib tidak tersedia")
            continue

        tipe = aturan.get("type")

        # bool adalah subclass int di python, sehingga perlu
        # pengecekan khusus jika tipe yang diharapkan adalah int.
        if tipe is not None:
            if tipe is int and type(nilai) is not int:
                erors.append(f"{f}: harus bertipe int.")
                continue
            elif tipe is not int and not isinstance(nilai, tipe):
                erors.append(
                    f"{f}: harus bertipe {tipe.__name__}"
                )
                continue
        if "min" in aturan and nilai < aturan["min"]:
            erors.append(
                f"{f}: nilai minumum adalah {aturan['min']}."

            )
        if "max" in aturan and nilai > aturan["max"]:
            erors.append(
                f"{f}: nilai maksimum adalah {aturan["max"]}."

            )
    # memeriksa filed tambahan yang wajib ada.
    for f in required_fields:
        if f not in schema:
            erors.append(
                f"{f}: field wajib tidak terdaftar dalam schema."
            )

    for validator in args:
        hasil = validator(data)
        if hasil is not None and hasil is not True:
            erors.append(str(hasil))


    return len(erors) == 0, erors



if __name__ == "__main__":
    data= {
        "nama": "pajar",
        "umur": 20,
        "ipk": 3.99

    }
    schema = {
        "nama": {"type" : str, "required": True},
        "umur": {"type" : int, "min": 17, "max": 100},
        "ipk":{"type":float, "min": 0.0, "max": 4.0}

    }
    # Validator tambahan: IPK minimal 2.0.
    def cek_ipk(data):
        if data.get("ipk", 0) < 2.0:
            return "IPK harus minimal 2.0."
        return None

    is_valid, errors = validation_data(
        data,
        schema,
        cek_ipk,
        required_fields=["nama", "umur", "ipk"]
    )

    print("Valid:", is_valid)
    print("Errors:", errors)
