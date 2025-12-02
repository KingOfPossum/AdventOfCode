#include <stdio.h>
#include <string.h>

int isValid(long num) {
    //printf("Checking for num %d\n",num);
    char numStr[30];
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

    if (strcmp(left,right) == 0) {
        return 0;
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
                //printf("Invalid number %lu\n",i);
                sum += i;
            }
        }

        line = strtok(NULL,",");
    }

    printf("Sum : %lu\n",sum);
}