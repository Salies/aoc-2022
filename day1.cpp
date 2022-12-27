#include <fstream>
#include <algorithm>
#include <iostream>
#include <string>

// not the best of practices, but it's just a coding challenge
using namespace std;

int main(void) {
    ifstream infile("inputs/day1.txt");

    unsigned int aux = 0, max[3] = {0, 0, 0};
    string line;
    while(getline(infile, line)) {
        if(line.size()) {
            aux += atoi(line.c_str());
            continue;
        }

        if(aux > max[0]) {
            max[0] = aux;
            sort(max, max + 3);
        }
        
        aux = 0;
    }

    cout << "The top elf is carrying " << max[2] << " calories." << endl;
    cout << "The top three elves are carrying " << max[0] + max[1] + max[2] << " calories in total." << endl;

    return 0;
}