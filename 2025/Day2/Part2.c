#include <stdio.h>
#include <string.h>

int isValid(long num) {
    //printf("Checking for num %lu\n",num);
    char numStr[30];
    sprintf(numStr, "%lu", num);

    int len = strlen(numStr);

    for (int i = 1; i < len/2 + 1;i++) {
        if (len % i != 0) {
            //printf("Skipping : %d , %d\n",len,i);
            continue;
        }

        char pattern[i];
        strncpy(pattern,numStr,i);
        pattern[i] = '\0';
        //printf("Pattern %s\n\n",pattern);

        int count = 0;
        int valid = 0;

        for (int j = 0;j < len - i+1;j+=i) {
            char c[i];
            strncpy(c,numStr+j,i);
            c[i] = '\0';
            //printf("%s\n",c);

            if (strcmp(pattern,c) == 0) {
                count++;
            }
            else {
                valid = 1;
            }
        }

        if (count >= 2 && !valid) {
            //printf("Pattern %s\n",pattern);
            return 0;
        }
    }

    return 1;
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen("Input.txt","r");

    long sum = 0;
    char buffer[1024];
    fgets(buffer,sizeof(buffer),fp);
    buffer[strcspn(buffer, "\n")] = '\0';

    char *line = strtok(buffer,",");
    while(line!=NULL) {
        printf("%s\n",line);

        long rangeBegin,rangeEnd;
        sscanf(line,"%lu-%lu",&rangeBegin,&rangeEnd);

        for (long i = rangeBegin; i <= rangeEnd; i++) {
            if (!isValid(i)) {
                printf("Invalid number %lu\n",i);
                sum += i;
            }
        }

        line = strtok(NULL,",");
    }

    printf("Sum : %lu\n",sum);
}