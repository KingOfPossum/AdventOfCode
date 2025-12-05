#include <stdio.h>
#include <stdlib.h>

#define file "Input.txt"

struct list {
    long long data;
    struct list *next;
};

void add(struct list **head, const long long num) {
    if ((*head) == NULL) {
        (*head) = malloc(sizeof(struct list));
        (*head)->data = num;
        (*head)->next = NULL;
        return;
    }

    struct list *newNode = malloc(sizeof(struct list));
    newNode->data = num;
    newNode->next = (*head);
    (*head) = newNode;
}

void printList(const struct list *head) {
    printf("\n[");

    struct list *tmp = head;
    while (tmp != NULL) {
        printf("%lld ", tmp->data);
        tmp = tmp->next;
    }

    printf("]\n");
}

int contains(struct list *head, long long num) {
    struct list *tmp = head;

    while (tmp != NULL) {
        if (tmp->data == num) {
            return 1;
        }
        tmp = tmp->next;
    }

    return 0;
}

int main(int argc, char *argv[]) {
    FILE *fp = fopen(file,"r");
    char buffer[1024];

    struct list *head = NULL;

    int rangesLength = 0;
    while (fgets(buffer,sizeof(buffer),fp)) {
        if (buffer[0] == '\n') {
            break;
        }

        long long rangeBegin,rangeEnd;
        sscanf(buffer,"%lld-%lld", &rangeBegin, &rangeEnd);

        for (long long i = rangeBegin;i <= rangeEnd;i++) {
            add(&head,i);
            //printList(head);
        }

        rangesLength++;
        printf("%s",buffer);
    }

    fclose(fp);

    printf("\n\n");

    int sum = 0;

    fp = fopen(file,"r");

    for (int i = 0;i < rangesLength+1;i++) {
        fgets(buffer,sizeof(buffer),fp);
    }

    while (fgets(buffer,sizeof(buffer),fp)) {
        printf("%s",buffer);
        int num = atoi(buffer);
        if (contains(head,num)) {
            sum++;
        }
    }

    printf("\nSUM : %d",sum);
}