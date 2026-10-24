#include <stdio.h>

int main() {
    int option;
    float v1, v2, result;

    while (1) {
        printf("Pilih program\n");
        printf("1. Penjumlahan\n");
        printf("2. Pengurangan\n");
        printf("3. Perkalian\n");
        printf("4. Pembagian\n");
        printf("5. Exit\n");
        printf("Masukkan Pilihan : ");
        scanf("%d", &option);

        if (option == 5) {
            printf("Terimakasih, telah menggunakan kalkulator Aulia\n");
            break;
        } else if (option < 1 || option > 5) {
            printf("Input anda salah, silahkan coba lagi\n");
        } else {
            printf("Masukkan nilai pertama : ");
            scanf("%f", &v1);
            printf("Masukkan nilai kedua : ");
            scanf("%f", &v2);

            if (option == 1) {
                result = v1 + v2;
                printf("Hasil Penjumlahan antara %.2f dengan %.2f adalah %.2f\n", v1, v2, result);
            } else if (option == 2) {
                result = v1 - v2;
                printf("Hasil Pengurangan antara %.2f dengan %.2f adalah %.2f\n", v1, v2, result);
            } else if (option == 3) {
                result = v1 * v2;
                printf("Hasil Perkalian antara %.2f dengan %.2f adalah %.2f\n", v1, v2, result);
            } else if (option == 4) {
                result = v1 / v2;
                printf("Hasil Pembagian antara %.2f dengan %.2f adalah %.2f\n", v1, v2, result);
            }
        }
    }

    return 0;
}