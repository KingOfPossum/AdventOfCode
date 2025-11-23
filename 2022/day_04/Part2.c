#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** getRanges(char* line) {
    char **ranges = malloc(2 * sizeof(char*));
    if (ranges == NULL) {
        free(ranges);
        return NULL;
    }

    ranges[0] = strtok(line,",");
    ranges[1] = strtok(NULL,",");

    return ranges;
}

void getRangeLimits(char* range,int *begin,int *end) {
    *begin = atoi(strtok(range,"-"));
    *end = atoi(strtok(NULL,"-"));
}

int main(int argc, char *argv[]) {
    FILE *fp = fopen("TestInput.txt","r");

    if (fp == NULL) {
        printf("Error while opening file!");
        return EXIT_FAILURE;
    }

    int numFullyContained = 0;

    char buffer[256];
    while (fgets(buffer,sizeof(buffer),fp)) {
        char **ranges = getRanges(buffer);
        if (ranges == NULL) {
            free(ranges);
            return EXIT_FAILURE;
        }

        int range1Begin,range1End,range2Begin,range2End = {0};

        getRangeLimits(ranges[0],&range1Begin,&range1End);
        getRangeLimits(ranges[1],&range2Begin,&range2End);

        if ((range1Begin - range2Begin <= 0 && range1End - range2End >= 0) || (range2Begin - range1Begin <= 0 && range2End - range1End >= 0)) {
            numFullyContained++;
        }

        free(ranges);
    }
    printf("SUM: %d\n",numFullyContained);

    return EXIT_SUCCESS;
}