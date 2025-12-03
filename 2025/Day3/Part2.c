#include <stdio.h>
#include <string.h>

long long processLine(char *line) {
    line[strcspn(line, "\r\n")] = 0;
    int len = strlen(line);
    long long max = 0;

    int nums[12] = {0};
    int currentStartIndex = 0;

    for (int i = 0; i < 12; i++) {
        int bestIndex = 0;

        for (int j = currentStartIndex; j <= len - 12 + i;j++) {
            int num = line[j] - '0';
            if (num > nums[i]) {
                nums[i] = num;
                bestIndex = j;
            }
        }
        currentStartIndex = bestIndex + 1;
    }

    for (int i = 0; i < 12; i++) {
        max = max * 10 + nums[i];
    }
    printf("MAX : %lld\n",max);

    return max;
}

int main(int argc, const char * argv[]) {
    FILE *fp = fopen("Input.txt", "r");

    long long sum = 0;

    char buffer[1024];
    while(fgets(buffer,sizeof(buffer),fp)) {
        printf("%s",buffer);
        sum += processLine(buffer);
    }

    printf("SUM : %lld\n",sum);
}