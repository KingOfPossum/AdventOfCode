#include <stdio.h>
#include <stdlib.h>

#define file "Input.txt"

struct tuple {
    long long x;
    long long y;
};

struct tuple combine(struct tuple t1,struct tuple t2) {
    struct tuple result;
    result.x = -1;
    result.y = -1;

    if (t1.x <= t2.x && t1.y >= t2.x) {
        result.x = t1.x;
    }
    else if (t2.x <= t1.x && t2.y >= t1.y) {
        result.x = t2.x;
    }

    if (t1.y >= t2.y && t1.x <= t2.y) {
        result.y = t1.y;
    }
    else if (t2.y >= t1.y && t2.x <= t1.y) {
        result.y = t2.y;
    }

    return result;
}

struct list {
    struct tuple data;
    struct list *next;
};

void add(struct list **head, struct tuple range) {
    if ((*head) == NULL) {
        (*head) = malloc(sizeof(struct list));
        (*head)->data = range;
        (*head)->next = NULL;
        return;
    }

    struct list *newNode = malloc(sizeof(struct list));
    newNode->data = range;
    newNode->next = (*head);
    (*head) = newNode;
}

void removeRange(struct list **head,struct tuple range) {
    if (*head == NULL) {
        return;
    }

    struct list *curr = *head;
    struct list *prev = NULL;

    while (curr != NULL) {
        if (curr->data.x == range.x && curr->data.y == range.y) {
            if (prev == NULL) {
                *head = curr->next;
            }
            else {
                prev->next = curr->next;
            }

            free(curr);
            return;
        }

        prev = curr;
        curr = curr->next;
    }
}

void printList(const struct list *head) {
    printf("\n[");

    struct list *tmp = head;
    while (tmp != NULL) {
        printf(" (%lld %lld) ", tmp->data.x,tmp->data.y);
        tmp = tmp->next;
    }

    printf("]\n");
}

int size(struct list *head) {
    struct list *tmp = head;
    int count = 0;
    while (tmp != NULL) {
        count++;
        tmp = tmp->next;
    }
    return count;
}

struct tuple get(struct list *head,int index) {
    struct list *tmp = head;
    for (int i = 0;i < index;i++) {
        tmp = tmp->next;
    }
    return tmp->data;
}

int main(int argc, char *argv[]) {
    FILE *fp = fopen(file,"r");
    char buffer[1024];

    int sum = 0;
    int rangeLines = 0;

    do {
        fgets(buffer,sizeof(buffer),fp);
        rangeLines++;
    } while (buffer[0] != '\n');

    rangeLines--;
    fclose(fp);

    struct list *ranges = NULL;

    fp = fopen(file,"r");

    for (int i = 0; i < rangeLines; i++) {
        fgets(buffer,sizeof(buffer),fp);

        struct tuple range;
        sscanf(buffer,"%lld-%lld",&range.x,&range.y);
        add(&ranges,range);
    }

    int finished = 0;
    while (!finished) {
        int foundOverlap = 0;
        int lenRanges = size(ranges);
        for (int i = 0;i < lenRanges;i++) {
            for (int j = 0;j < lenRanges;j++) {
                if (i == j) {
                    continue;
                }
                struct tuple t1 = get(ranges,i);
                struct tuple t2 = get(ranges,j);

                struct tuple overlap = combine(t1,t2);
                if (overlap.x != -1 && overlap.y != -1) {
                    printf("OVERLAP (%lld %lld) : t1 : (%lld %lld) | t2 : (%lld %lld)\n",overlap.x,overlap.y,t1.x,t1.y,t2.x,t2.y);

                    removeRange(&ranges,t1);
                    removeRange(&ranges,t2);
                    add(&ranges,overlap);
                    foundOverlap = 1;
                    break;
                }
            }
            if (foundOverlap) {
                break;
            }
        }
        if (!foundOverlap) {
            finished = 1;
        }
    }

    int len = size(ranges);
    for (int i = 0;i < len;i++) {
        struct tuple t1 = get(ranges,i);
        sum += t1.y - t1.x + 1;
    }

    printList(ranges);
    printf("Length : %d\n",size(ranges));
    printf("Lines for ranges : %d",rangeLines);
    printf("\nSUM : %d",sum);
}