#include <stdio.h>

int main() {
    int n, k;
    scanf("%d %d", &n, &k);

    int total_seluruh = 0;

    for (int i = 1; i <= n; i++) {
        int total_baris = 0;
        for (int j = i; j >= 1; j--) {
            printf("(%d * %d)", j, k);
            total_baris += (j * k);
            if (j > 1) {
                printf(" + ");
            }
        }
        printf(" = %d\n", total_baris);
        total_seluruh += total_baris;
    }
    printf("%d\n", total_seluruh);

    return 0;
}