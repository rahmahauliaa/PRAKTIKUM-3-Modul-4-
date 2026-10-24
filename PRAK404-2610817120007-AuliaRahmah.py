while True:
    print("Pilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    
    option = int(input("Masukkan Pilihan : "))

    if option == 5:
        print("Terimakasih, telah menggunakan kalkulator Aulia")
        break
    elif option < 1 or option > 5:
        print("Input anda salah, silahkan coba lagi")
    else:
        v1 = float(input("Masukkan nilai pertama : "))
        v2 = float(input("Masukkan nilai kedua : "))

        if option == 1:
            result = v1 + v2
            print(f"Hasil Penjumlahan antara {v1:.2f} dengan {v2:.2f} adalah {result:.2f}")
        elif option == 2:
            result = v1 - v2
            print(f"Hasil Pengurangan antara {v1:.2f} dengan {v2:.2f} adalah {result:.2f}")
        elif option == 3:
            result = v1 * v2
            print(f"Hasil Perkalian antara {v1:.2f} dengan {v2:.2f} adalah {result:.2f}")
        elif option == 4:
            result = v1 / v2
            print(f"Hasil Pembagian antara {v1:.2f} dengan {v2:.2f} adalah {result:.2f}")