#include <fstream>
#include <iostream>
#include <string>
#include <map>
#include <array>

using namespace std;

int main(void) {
    ifstream infile("inputs/day2.txt");

    // A data strucutre based solution
    std::map<char, array<char, 3>> rule;
    rule['A'] = {'X', 'Y', 'Z'}; // rock
    rule['B'] = {'Y', 'Z', 'X'}; // paper
    rule['C'] = {'Z', 'X', 'Y'}; // scissors

    // default points for char, position in rule, bonus points
    std::map<char, array<unsigned short, 3>> points;
    points['X'] = {1, 2, 0};
    points['Y'] = {2, 0, 3};
    points['Z'] = {3, 1, 6};

    char input, answer;
    unsigned int sum_one = 0, sum_two = 0;
    string line;
    while(getline(infile, line)) {
        input = line[0];
        answer = line[2];

        sum_one += points[answer][0];
        sum_two += points[rule[input][points[answer][1]]][0] + points[answer][2];

        if(answer == rule[input][0]) {
            sum_one += 3;
            continue;
        }
        if(answer == rule[input][1])
            sum_one += 6;
    }

    cout << "Total score, part one: " << sum_one << endl;
    cout << "Total score, part two: " << sum_two << endl;

    return 0;
}