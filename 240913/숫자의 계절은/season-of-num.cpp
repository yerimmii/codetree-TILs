#include <iostream>
using namespace std;

int main() {
    int m;
    string season;

    cin >> m;

    if (m == 12 || m <= 2) {
        season = "Winter";
    } else if (m <= 5) {
        season = "Spring";
    } else if (m <= 8) {
        season = "Summer";
    } else if (m <= 11) {
        season = "Fall";
    }

    cout << season;

    return 0;
}