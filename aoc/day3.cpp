#include <fstream>
#include <iostream>
#include <string>
#include <map>

using namespace std;

// always subtracting 1 less because counting starts at 1
unsigned short get_priority(char &c) {
    if(c >= 'A' && c <= 'Z')
        return (int)c - 38;
    return (int)c - 96;
}

// refnum prevents the need for unique appearances
void string_to_map(string &s, map<char, unsigned short> &sfreq, unsigned short refnum = 0) {
    for(auto &c : s)
        if(sfreq[c] == refnum)
            sfreq[c]++;
}

int main(void) {
    ifstream infile("inputs/day3.txt");

    unsigned int sum = 0;
    string line, first_sack, second_sack;
    map<char, unsigned short> sfreq;

    while(infile >> line) {
        // Part one
        first_sack = line.substr(0, line.length()/2);
        second_sack = line.substr(line.length()/2);
        // Find the character that appears in both strings
        string_to_map(first_sack, sfreq);
        for(auto &c : second_sack)
            if(sfreq[c] == 1) {
                sum += get_priority(c);
                break;
            }
        sfreq.clear();
    }

    cout << "Part one: " << sum << endl;

    // Part 2
    infile.clear();
    infile.seekg(0, ios::beg);

    sum  = 0;
    // Read file in groups of three lines
    while(getline(infile, line)) {
        for(int i = 0; i < 2; i++) {
            string_to_map(line, sfreq, i);
            getline(infile, line);
        }
        for (auto &c : line) {
            if (sfreq[c] == 2) {
                sum += get_priority(c);
                break;
            }
        }
        sfreq.clear();
    }

    cout << "Part two: " << sum << endl;
}