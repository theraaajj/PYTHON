// sum of first N numbers using recursion

// parameterized way
// #include<iostream>
// using namespace std;

// void ans(int n, int sum){
//     if(n<1){
//         cout << sum << endl;
//         return;
//     }
//     ans(n-1, sum+n);
// };

// int main(){
//     int n;
//     cin >> n;
//     ans(n, 0);
//     return 0;
// }


// functional way

#include<iostream>
using namespace std;

int sum(int n){
    if (n==0)
     return 0;
    return (n + sum(n-1));
};

int main(){
    int n;
    cin >> n;
    cout << sum(n) << endl;
}