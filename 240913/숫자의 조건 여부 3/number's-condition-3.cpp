#include <iostream>
using namespace std;

int main() {
    int a;
    string ans;

    cin >> a;

    if (a % 13 == 0 || a % 19 == 0) { ans = "True"; }
    else { ans = "False"; }

    cout << ans;

    return 0;
}