#include <stdio.h>
#include <string.h>

int isValid(long num) {
    //printf("Checking for num %d\n",num);
    char numStr[20];
    sprintf(numStr, "%lu", num);

    int len = strlen(numStr);

    if (len % 2 == 1) {
        return 1;
    }

    int mid = len / 2;
    char left[mid +1];
    char right[len - mid +1];

    strncpy(left,numStr,mid);
    left[mid] = '\0';
    strcpy(right,numStr+mid);

    //printf("Left : %s | Right : %s\n",left,right);

    if (strcmp(left,right) == 0) {
        return 0;
    }

    /*
    for (int i = 0; i < len/2;i++) {
        char pattern[i+1];
        strncpy(pattern,numStr,i+1);
        pattern[i+1] = '\0';
        //printf("Pattern %s\n\n",pattern);

        int count = 0;

        for (int j = 0;j < len - i;j++) {
            char c[i+1];
            strncpy(c,numStr+j,i+1);
            c[i+1] = '\0';
            //printf("%s\n",c);

            if (strcmp(pattern,c) == 0) {
                count++;
            }
        }

        if (count == 2) {
            printf("Pattern %s\n",pattern);
            return 0;
        }
    }
    */

    return 1;
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen("Input.txt","r");

    long sum = 0;
    char buffer[256];
    fgets(buffer,255,fp);
    buffer[strcspn(buffer, "\n")] = '\0';

    char *line = strtok(buffer,",");
    while(line!=NULL) {
        printf("%s\n",line);

        long rangeBegin,rangeEnd;
        sscanf(line,"%lu-%lu",&rangeBegin,&rangeEnd);

        for (long i = rangeBegin; i <= rangeEnd; i++) {
            if (!isValid(i)) {
                //printf("Invalid number %lu\n",i);
                sum += i;
            }
        }

        line = strtok(NULL,",");
    }

    printf("Sum : %lu\n",sum);
}