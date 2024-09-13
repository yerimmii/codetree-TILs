#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    string great;

    if ((n % 2 != 0 && n % 3 == 0) || (n % 2 == 0 && n % 5 == 0)) {
        great = "true";
    } else {
        great = "false";
    }

    cout << great;

    return 0;
}