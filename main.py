def cetak_nama(nama):
    # Tulis kode fungsi cetak_nama di bawah ini
    if (nama == ''):
        print('Tidak ada nama yang dicetak')
    else:
        jumlahkata = len(nama) + 1
        i = 0
        while i < jumlahkata:
          i += 1
          if (i == jumlahkata):
            print(nama[0:i] + ' !')
          else:
            print(nama[0:i])

    # Hapus pass jika implementasi sudah dibuat


def hitung_kesamaan(kata1, kata2):
    # Tulis kode fungsi hitung_kesamaan di bawah ini
    p = len(kata1)
    q = len(kata2)
    r = 0

    if (p > q):
        for element in range(q):
            a = kata1[element]
            b = kata2[element]

            if a == b:
                r += 1
        return r

    else:
        for element in range(p):
            a = kata1[element]
            b = kata2[element]

            if a == b:
                r += 1
        return r

    # Hapus pass jika implementasi sudah dibuat


def hitung(bil1, bil2, operator='+'):
    # Tulis kode fungsi hitung() di bawah ini
    if (operator == '+'):
        r = bil1 + bil2
    elif (operator == '-'):
        r = bil1 - bil2
    elif (operator == '/'):
        r = bil1 / bil2
    elif (operator == '*'):
        r = bil1 * bil2

    return r
    # Hapus pass jika implementasi sudah dibuat


# Mulai baris ini hingga baris paling bawah
# digunakan untuk mengetes fungsi yang telah dibuat.
# Tidak perlu mengubah bagian ini.
# Ketika dijalankan, program akan menampilkan contoh
# pemanggilan fungsi dan solusi yang seharusnya
# (untuk fungsi hitung_kesamaan() dan fungsi hitung()).
# Cocokkan hasil pemanggilan fungsi dengan solusi
# yang seharusnya.
def test():
    print("cetak_nama('Fikri'):")
    cetak_nama("Fikri")
    print()
    print("cetak_nama(''):")
    cetak_nama("")
    print()

    r = hitung_kesamaan('python', 'path')
    print(f"hitung_kesamaan('python', 'path') = {r} \t\t\t(solusi: 3)")
    r = hitung_kesamaan('masak', 'cuci')
    print(f"hitung_kesamaan('masak', 'cuci') = {r} \t\t\t(solusi: 0)")
    r = hitung_kesamaan('python', 'cacaca')
    print(f"hitung_kesamaan('python', 'cacaca') = {r} \t\t(solusi: 0)")
    print()

    r = hitung(4, 8)
    print(f'hitung(4, 8, "+") = {r} \t\t\t(solusi: 12)')
    r = hitung(4, 8, '-')
    print(f"hitung(4, 8, '-') = {r} \t\t\t(solusi: -4)")
    r = hitung(4, 8, '*')
    print(f"hitung(4, 8, '*') = {r} \t\t\t(solusi: 32)")


if __name__ == '__main__':
    test()
