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

int calculatePoints(const char opMove, const char ownMove) {
    int points = getPointsForShape(ownMove);

    if ((opMove == 'A' && ownMove == 'X') || (opMove == 'B' && ownMove == 'Y') || (opMove == 'C' && ownMove == 'Z')) {
        return points + 3;
    }
    if ((opMove == 'A' && ownMove == 'Z') || (opMove == 'B' && ownMove == 'X') || (opMove == 'C' && ownMove == 'Y')) {
        return points;
    }
    return points + 6;
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
        int points = calculatePoints(buffer[0],buffer[2]);
        sum += points;
    }

    printf("\nTotal points : %d",sum);
    fclose(fp);
    return EXIT_SUCCESS;
}