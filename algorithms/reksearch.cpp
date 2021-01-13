#include <iostream>
using namespace std;

const int n = 10;
int tab[n] = {1, 2, 4, 5, -44, 78, 14, 20, 0, 100};

void search(int tab[], int left, int right, int x){
    // x is looking for number
    if (left > right)
        cout << "The number you are looking for doesn't exist" << endl;
    else
        if (tab[left] == x)
            cout << "the number you are looking for is: " << x << endl;
        else
            search(tab, left + 1, right, x);
}

int main() {
    search(tab, 0, n-1, 99);
    search(tab, 0, n-1, 100);
    return 0;
}
