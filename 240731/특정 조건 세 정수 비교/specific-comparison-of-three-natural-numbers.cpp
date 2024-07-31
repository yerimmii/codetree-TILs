#include <iostream>
using namespace std;

int main() {
    int a, b, c;
    int min;

    cin >> a >> b >> c;

    if (a < b) {
        if (a < c) {
            min = a;
        } else {
            min = c;
        }
    } else {
        if (b < c) {
            min = b;
        } else {
            min = c;
        }
    }

    cout << (a == min) << " " << (a == b && b == c);

    return 0;
}