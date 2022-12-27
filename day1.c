#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

int main(void) {
    FILE *fp = fopen("inputs/day1.txt", "r");
    // I'll skip the formalities, it's just a coding challenge XD
    char *line = NULL;
    size_t len = 0;
    
    unsigned int aux = 0, max[3] = {0, 0, 0}, i;
    while(getline(&line, &len, fp) != -1) {
        if(line[0] != '\n') {
            aux += atoi(line);
            continue;
        }

        // Pretty sure this can be improved, can't bother
        for(i = 0; i < 3; i++) {
            if(aux > max[i]) {
                max[i] = aux;
                // sort from smallest (pos 0) to largest
                qsort(max, 3, sizeof(unsigned int), compare);
                break;
            }
        }
        aux = 0;
    }

    printf("The top elf is carrying %d calories.\n", max[2]);
    printf("The top three elves are carrying %d calories in total.\n", max[0] + max[1] + max[2]);

    fclose(fp);
    if(line) 
        free(line);
    return 0;
}