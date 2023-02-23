#include <fstream>
#include <iostream>
#include <string>
#include <utility>

using namespace std;

int main(void) {
    ifstream infile("inputs/day4.txt");

    unsigned int count = 0, count_two = 0;
    string first_pair, second_pair;
    pair<unsigned int, unsigned int> f, s;
    while(getline(infile, first_pair, ',')) {
        getline(infile, second_pair);
        // Split by - and convert to int
        f = make_pair(stoi(first_pair.substr(0, first_pair.find('-'))), stoi(first_pair.substr(first_pair.find('-') + 1)));
        s = make_pair(stoi(second_pair.substr(0, second_pair.find('-'))), stoi(second_pair.substr(second_pair.find('-') + 1)));

        // if one range contains the other
        if((f.first <= s.first && s.second <= f.second) || (s.first <= f.first && f.second <= s.second))
            count++;

        // if ranges overlap
        if((f.first <= s.first && s.first <= f.second) || (s.first <= f.first && f.first <= s.second))
            count_two++;
    }
    cout << count << endl;
    cout << count_two << endl;
}