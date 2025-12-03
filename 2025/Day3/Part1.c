#include <stdio.h>
#include <string.h>

int processLine(char *line) {
    int len = strlen(line);
    int max = 0;

    for (int i = 0;i < len;i++) {
        int first = line[i] - '0';

        for(int j = i+1;j < len;j++) {
            int second = line[j] - '0';

            if (first*10+second > max) {
                max = first*10+second;
            }
        }
    }

    return max;
}

int main(int argc, const char * argv[]) {
    FILE *fp = fopen("Input.txt", "r");

    int sum = 0;

    char buffer[1024];
    while(fgets(buffer,sizeof(buffer),fp)) {
        printf("%s",buffer);
        sum += processLine(buffer);
    }

    printf("SUM : %d\n",sum);
}