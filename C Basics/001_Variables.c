#include <stdio.h>
// #include <string.h>

int main() {
    char ch;
    short int k;
    long int l;
    long long int m;
    int a;
    float b;
    double d;

    printf("Character size %d\n", sizeof(ch));
    printf("Integer size %d\n", sizeof(a));
    printf("Float size %d\n", sizeof(b));
    printf("Double size %d\n", sizeof(d));
    printf("Short Integer size %d\n", sizeof(k));
    printf("Long Integer size %d\n", sizeof(l));
    printf("Long Long Integer size %d\n", sizeof(m));
    return 0;
}
