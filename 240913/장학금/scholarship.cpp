#include <iostream>
using namespace std;

int main() {
    int mid, fin;
    int money;

    cin >> mid >> fin;

    if (mid >= 90) {
        if (fin >= 95) {
            money = 100000;
        } else if (fin >= 90) {
            money = 50000;
        } else {
            money = 0;
        }
    } else {
        money = 0;
    }

    cout << money;

    return 0;
}