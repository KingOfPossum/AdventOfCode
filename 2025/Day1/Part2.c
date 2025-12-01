#include <stdio.h>
#include <stdlib.h>

int processInput(char *txt,int *currentPos) {
    const char direction = txt[0];
    const int amount = atoi(txt + 1);
    int wentOverZero = 0;

    for (int i = 0;i < amount;i++) {
        if (direction == 'L') {
            *currentPos -= 1;
            if (*currentPos == 0) {
                wentOverZero += 1;
            }
            if (*currentPos == -1) {
                *currentPos = 99;
            }
        }
        else if (direction == 'R') {
            *currentPos += 1;
            if (*currentPos == 100) {
                *currentPos = 0;
                wentOverZero += 1;
            }
        }
    }

    /*
    if (direction == 'L') {
        if (*currentPos - amount <= 0) {
            wentOverZero = 1;
        }
        *currentPos = (*currentPos - amount) % 100;
        if (*currentPos < 0) {
            *currentPos = (100 + *currentPos);
        }
    }
    else if (direction == 'R') {
        if (*currentPos + amount >= 100) {
            wentOverZero = 1;
        }
        *currentPos = (*currentPos + amount) % 100;
    }
    */

    return wentOverZero;
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen("Input.txt","r");

    char buffer[256];
    int currentPos = 50;
    int password = 0;

    while (fgets(buffer,sizeof(buffer),fp)) {
        printf("\n%s",buffer);
        password += processInput(buffer,&currentPos);
        printf("Pos : %d",currentPos);
    }

    printf("\nPassword : %d",password);
}