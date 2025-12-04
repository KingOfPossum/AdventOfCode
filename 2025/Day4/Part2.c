#include <stdio.h>
#include <string.h>

#define file "Input.txt"

void printField(int rows,int cols, char field[rows][cols]) {
    printf("\n");
    for(int row=0;row<rows;row++) {
        printf("[");
        for(int col=0;col<cols;col++) {
            printf("%c ",field[row][col]);
        }
        printf("]\n");
    }
}

int checkValid(int rows,int cols,char field[rows][cols]) {
    int sum = 0;
    //Check if valid
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (field[row][col] == '@') {
                int count = 0;
                if (row > 0 && (field[row-1][col] == '@' || field[row-1][col] == 'x')) {
                    count++;
                }
                if (row < rows-1 && (field[row+1][col] == '@' || field[row+1][col] == 'x')) {
                    count++;
                }
                if (col > 0 && (field[row][col-1] == '@' || field[row][col-1] == 'x')) {
                    count++;
                }
                if (col < cols-1 && (field[row][col+1] == '@' || field[row][col+1] == 'x')) {
                    count++;
                }
                if (col > 0 && row > 0 && (field[row-1][col-1] == '@' || field[row-1][col-1] == 'x')) {
                    count++;
                }
                if (col < cols-1 && row > 0 && (field[row-1][col+1] == '@' || field[row-1][col+1] == 'x')) {
                    count++;
                }
                if (col > 0 && row < rows-1 && (field[row+1][col-1] == '@' || field[row+1][col-1] == 'x')) {
                    count++;
                }
                if (col < cols-1 && row < rows-1 && (field[row+1][col+1] == '@' || field[row+1][col+1] == 'x')) {
                    count++;
                }

                if (count < 4) {
                    field[row][col] = 'x';
                    sum++;
                }
            }
        }
    }

    return sum;
}

void removeValid(int rows,int cols,char field[rows][cols]) {
    for (int row = 0; row < rows; row++) {
        for (int col = 0; col < cols; col++) {
            if (field[row][col] == 'x') {
                field[row][col] = '.';
            }
        }
    }
}

int main(int argc,char *argv[]) {
    FILE *fp = fopen(file,"r");

    char buffer[1024];
    int rows = 0;
    int cols = 0;

    //Get sizes
    while (fgets(buffer,sizeof(buffer),fp)) {
        rows = (int)strlen(buffer);
        cols += 1;
    }

    fclose(fp);

    //Fill field

    fp = fopen(file,"r");
    char field[rows][cols];
    for (int row = 0; row < rows; row++) {
        fgets(buffer,sizeof(buffer),fp);
        for (int col = 0; col < cols; col++) {
            field[row][col] = buffer[col];
        }
    }
    fclose(fp);

    printField(rows,cols,field);

    int sum = 0;
    int localSum = 0;

    do {
        printField(rows,cols,field);

        localSum = checkValid(rows,cols,field);
        sum += localSum;
        printf("Local Sum : %d\n",localSum);

        removeValid(rows,cols,field);

        printField(rows,cols,field);
    } while (localSum != 0);

    printf("Sum : %d",sum);
}