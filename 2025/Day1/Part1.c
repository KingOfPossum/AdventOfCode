#include <stdio.h>
#include <stdlib.h>

void processInput(char *txt,int *currentPos) {
    const char direction = txt[0];
    const int amount = atoi(txt + 1);

    if (direction == 'L') {
        *currentPos = (*currentPos - amount) % 100;
        if (*currentPos < 0) {
            *currentPos = (100 + *currentPos);
        }
    }
    else if (direction == 'R') {
        *currentPos = (*currentPos + amount) % 100;
    }
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen("Input.txt","r");

    char buffer[256];
    int currentPos = 50;
    int password = 0;

    while (fgets(buffer,sizeof(buffer),fp)) {
        printf("\n%s",buffer);
        processInput(buffer,&currentPos);
        printf("Pos : %d",currentPos);
        if (currentPos == 0) {
            password += 1;
        }
    }

    printf("\nPassword : %d",password);
}