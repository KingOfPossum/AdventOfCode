#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FILENAME "Input.txt"

struct stack {
    char crate;
    struct stack *prev;
};

char pop(struct stack **s) {
    if (*s == NULL) {
        return ' ';
    }

    char topCrate = (*s)->crate;
    struct stack *oldTop = *s;
    *s = (*s)->prev;
    free(oldTop);
    return topCrate;
}

void push(struct stack **s,char newElem) {
    struct stack *newStack = malloc(sizeof(struct stack));
    newStack->crate = newElem;
    newStack->prev = *s;
    *s = newStack;
}

void printStack(struct stack *s) {
    if (s == NULL) {
        printf("Stack is empty\n");
        return;
    }

    struct stack *p = s;
    printf("%c ",p->crate);
    p = p->prev;
    while (p != NULL) {
        printf(" -> %c",p->crate);
        p = p->prev;
    }
    printf("\n");
}

int main(int argc, char *argv[]) {
    FILE *fp = fopen(FILENAME,"r");
    char buffer[256];
    int maxHeight = 0;

    // Calculate the maximal Height of the stacks (The height of the biggest stack)
    while (buffer[0] != '\n') {
        maxHeight++;
        fgets(buffer,sizeof(buffer),fp);
    }
    maxHeight -= 2;

    fclose(fp);

    printf("Max Stack Height : %d\n",maxHeight);

    // Read the actual stacks
    char *txt[maxHeight];
    fp = fopen(FILENAME,"r");
    for (int i = 0; i < maxHeight; i++) {
        fgets(buffer,sizeof(buffer),fp);
        txt[i] = malloc(strlen(buffer) + 1);
        strcpy(txt[i],buffer);
        printf("Line %d (%lu): %s",i,strlen(txt[i]),txt[i]);
    }
    printf("\n");

    // Get number of stacks
    fgets(buffer,sizeof(buffer),fp);
    char *n = strtok(buffer," ");
    int numberOfStacks = -1;
    while (n != NULL) {
        numberOfStacks++;
        n = strtok(NULL," ");
    }
    printf("Number of Stacks : %d\n",numberOfStacks);

    fclose(fp);

    struct stack *stacks[numberOfStacks];
    // Construct the stacks
    for (int i = 0;i < numberOfStacks;i++) {
        stacks[i] = NULL;
        for (int j = maxHeight - 1; j >= 0;j--) {
            int c = 1 + i * 4;
            if (c > strlen(txt[j])) {
                continue;
            }

            if (txt[j][c] != ' ' && txt[j][c] != '\n') {
                push(&stacks[i],txt[j][c]);
            }
        }
        printStack(stacks[i]);
    }

    // Skip the first lines until the rearrangement part begins
    fp = fopen(FILENAME,"r");
    for (int i = 0;i < maxHeiTDCHVHJTG
ght + 2;i++) {
        fgets(buffer,sizeof(buffer),fp);
    }

    while (fgets(buffer,sizeof(buffer),fp) != NULL) {
        printf("%s",buffer);
        int amount,from,to;
        sscanf(buffer,"move %d from %d to %d",&amount,&from,&to);
        printf("%d %d %d\n",amount,from,to);

        for (int i = 0; i < amount; i++) {
            char elem  = pop(&stacks[from-1]);
            push(&stacks[to-1],elem);
        }
    }

    for (int i = 0;i < numberOfStacks;i++) {
        printStack(stacks[i]);
    }

    for (int i = 0;i < numberOfStacks;i++) {
        char elem = pop(&stacks[i]);
        printf("%c",elem);
    }

    printf("\n");

    return EXIT_SUCCESS;
}