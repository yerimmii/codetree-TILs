#include <iostream>
using namespace std;

int main() {
    double ft;

    cin >> ft;
    
    cout << fixed;
    cout.precision(1);
    cout << ft * 30.48;

    return 0;
}