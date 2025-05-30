#include<bits/stdc++.h>
using namespace std;

int main() {
    int a;
    // std::cin >> a;
    // std::cout << a;
    // std:: is needed when we don't use the using namespace std; line


// defining pairs
pair<int, int> p = {1, 3};
cout << p.first << " " << p.second;

pair<int, pair<int, int>> q = {1, {2, 3}};
cout << p.first << " " << q.second.first << " " << q.second.second;

pair<int, int> arr[] = {{1, 2}, {3, 4}, {5, 6}};
cout << arr[1].second;
}