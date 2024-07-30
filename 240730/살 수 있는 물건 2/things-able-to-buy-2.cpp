#include <iostream>
using namespace std;

int main() {
    int n;

    cin >> n;

    if ((n-3000) >= 0) {
        cout << "book";
    } else if ((n-1000) >= 0) {
        cout << "mask";
    } else if ((n-500) >= 0) {
        cout << "pen";
    } else {
        cout << "no";
    }

    return 0;
}