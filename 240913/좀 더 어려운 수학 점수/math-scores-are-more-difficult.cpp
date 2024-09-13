#include <iostream>
using namespace std;

int main() {
    int mathA, engA, mathB, engB;
    char student;
    
    cin >> mathA >> engA >> mathB >> engB;

    if (mathA == mathB) {
        student = engA > engB ? 'A' : 'B';
    } else {
        student = mathA > mathB ? 'A' : 'B';
    }

    cout << student;

    return 0;
}