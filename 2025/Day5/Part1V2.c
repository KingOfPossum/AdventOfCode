#include <stdio.h>
#include <stdlib.h>

#define file "Input.txt"

struct tuple {
    long long x;
    long long y;
};

int main(int argc, char *argv[]) {
    FILE *fp = fopen(file,"r");
    char buffer[1024];

    int sum = 0;
    int rangeLines = 0;

    do {
        fgets(buffer,sizeof(buffer),fp);
        rangeLines++;
    } while (buffer[0] != '\n');

    fclose(fp);

    struct tuple ranges[rangeLines-1];

    fp = fopen(file,"r");

    for (int i = 0; i < rangeLines-1; i++) {
        fgets(buffer,sizeof(buffer),fp);
        sscanf(buffer,"%lld-%lld",&ranges[i].x,&ranges[i].y);
        printf("(%lld , %lld)\n",ranges[i].x,ranges[i].y);
    }

    //Skip empty line
    fgets(buffer,sizeof(buffer),fp);

    while (fgets(buffer,sizeof(buffer),fp)) {
        long long num = atoll(buffer);
        for (int i = 0; i < rangeLines-1; i++) {
            if (num >= ranges[i].x && num <= ranges[i].y) {
                sum++;
                break;
            }
        }
    }

    printf("Lines for ranges : %d",rangeLines);
    printf("\nSUM : %d",sum);
}