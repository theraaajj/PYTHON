// print linearly from N to 1 using recursion
// N, ..., 4, 3, 2, 1


#include<iostream>
using namespace std;

void f(int n, int i){
    if(i>n)
     return;
    cout << n << endl;
    f(n-1, i);
};

int main(){
    int n;
    cin>>n;
    f(n, 1);
    return 0;
}