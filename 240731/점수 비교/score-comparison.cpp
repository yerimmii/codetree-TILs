#include <iostream>
using namespace std;

int main() {
    int mathA, mathB, engA, engB;

    cin >> mathA >> engA >> mathB >> engB;

    cout << ((mathA > mathB) && (engA > engB)); 

    return 0;
}