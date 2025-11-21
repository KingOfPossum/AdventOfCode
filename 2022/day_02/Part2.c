#include <stdio.h>
#include <stdlib.h>

int getPointsForShape(const char shape) {
    switch (shape) {
        case 'X':
            return 1;
        case 'Y':
            return 2;
        case 'Z':
            return 3;
        default:
            return 0;
    }
}

int calculatePoints(const char end,const char shape) {
    int points = getPointsForShape(shape);

    switch (end) {
        case 'X':
            return points;
        case 'Y':
            return points + 3;
        case 'Z':
            return points + 6;
        default:
            return 0;
    }
}

char getShape(const char opMove, const char neededEnd) {
    if (neededEnd == 'Y') {
        switch (opMove) {
            case 'A':
                return 'X';
            case 'B':
                return 'Y';
            case 'C':
                return 'Z';
            default:
                return ' ';
        }
    }
    else if (neededEnd == 'X') {
        switch (opMove) {
            case 'A':
                return 'Z';
            case 'B':
                return 'X';
            case 'C':
                return 'Y';
            default:
                return ' ';
        }
    }
    else {
        switch (opMove) {
            case 'A':
                return 'Y';
            case 'B':
                return 'Z';
            case 'C':
                return 'X';
            default:
                return ' ';
        }
    }
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen("Input.txt","r");
    if (fp ==NULL) {
        perror("Error while opening file!");
        return EXIT_FAILURE;
    }
    int sum = 0;
    char buffer[256];

    while (fgets(buffer,sizeof(buffer),fp)) {
        printf("%s",buffer);
        int points = calculatePoints(buffer[2],getShape(buffer[0],buffer[2]));
        sum += points;
    }

    printf("\nTotal points : %d",sum);
    fclose(fp);
    return EXIT_SUCCESS;
}