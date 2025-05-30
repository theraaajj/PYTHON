#include<bits/stdc++.h>
using namespace std;

int main() {
    int a;
}

void explainVectors() {

      vector<int> v;        // dynamic array
      v.push_back(1);
      v.emplace_back(2);    // same as push_back, but faster.
      v.push_back(3);
      v.push_back(4);

      vector<pair<int, int>> x;
      x.push_back({1, 2});
      x.emplace_back(3, 4);     //automatically assumes it to be a pair

      vector <int> a(5, 100);   // defines a container of 5 size and all places assigned a 100
      vector <int> a(5);        // defines a container of 5 size and all places assigned a 0 or a garbage value
      // even it's size is defined here, but it can be increased simply by pushing the value

      vector <int> v1(5, 20);   //defines a container of 5 size and all places assigned a 20
      vector <int> v2(v1);      // a copy vector of v1




      vector<int>::iterator it = v.begin();      // v.begin() gives the memory addr of the first element of vector
      it++;
      cout << *(it) << " ";                      // *(it) gives the value stored at memory addr stored in "it"

      vector<int>::iterator it = v.end();        // point right after the memory addr of last value store

    //   vector<int>::iterator it = v.rend();       // reverse iterator
    //   vector<int>::iterator it = v.rbegin();     // reverse iterator

      cout << v.back() << " ";                  // last element


    // how to traverse a vector or print the elements?
    for( vector<int>::iterator it = v.begin(); it != v.end(); it++)
        cout << *(it) << " ";

    for( auto it = v.begin(); it != v.end(); it++)           // auto means auto assigning the data type 
        cout << *(it) << " ";

    for (auto it : v)
        cout << it << " ";


        
// {1, 2, 3, 4}
v.erase(v.begin()+1);     // erases the element at given addr; here 2

v.erase(v.begin()+1, v.begin()+3);   // erases 2 and 3

// Insert function
vector<int> a{5, 100};                // {100, 100, 100, 100, 100}
a.insert(a.begin(), 200);             // {200, 100, 100, 100, 100, 100}
a.insert(a.begin()+1, 2, 300);        // {200, 300, 300, 100, 100, 100, 100, 100}

cout << a.size();      //gives the size

a.pop_back();        // pops the last element

v1.swap(v2);        //swaps both

cout << a.empty();  // is the vector empty? {true/false}
}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainList(){

    list<int> ls;
    ls.push_back(2);        // {2}
    ls.emplace_back(4);     // {2, 4}
    ls.push_front(5);       // {5, 2, 4}

    ls.emplace_front();     // same

    // all other functions are same as vectors
    // begin, end, rbegin, rend, clear, insert, size, swap
}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainDeque(){
    deque<int> dq;
    dq.push_back(2);
    dq.emplace_back();
    dq.push_front(3);
    dq.emplace_front(5);

    dq.pop_back();
    dq.pop_front();

    dq.back();
    dq.front();

    
    // all other functions are same as vectors
    // begin, end, rbegin, rend, clear, insert, size, swap
}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainStack(){             //LIFO
     stack<int> st;
     st.push(1);        // {1}
     st.push(2);        // {2, 1}
     st.push(3);        // {3, 2, 1}
     st.push(4);        // {4, 3, 2, 1}
     st.emplace(5);     // {5, 4, 3, 2, 1}

     cout << st.top();  // print 5 i.e. the top element

    //  st[2] is invalid. stacks don't have indexing

    st.pop();           // st = {4, 3, 2, 1}

    cout << st.top();    // 4
    cout << st.size();   // 4 
    cout << st.empty();  // {}

    stack<int> st1, st2;
    st1.swap(st2);

    // all operations of stack have a time complexity of O(1)

}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainQueue(){          //FIFO
     queue<int> q;

     q.push(1);      // {1}
     q.push(2);      // {1, 2}
     q.emplace(3);   // {1, 2, 3}

     cout << q.back();    // 3
     cout << q.front();   // 1

     q.back() += 5;   // adds 5 to the last element that's 3 here, and makes it a 7

     q.pop();         // {2, 3}   due to FIFO removes the first element obv

}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainPQ(){
    priority_queue<int> pq;     // guy with the largest value elem resides at the top
    pq.push(5);      // {5}
    pq.push(2);      // {5, 2}
    pq.push(10);     // {10, 5, 2}
    pq.emplace(8);   // {10, 8, 5, 2}

    cout << pq.top();  // 10
    pq.pop();      // pops 10, the uppermost/highest element
    cout << pq.top();  // 8

    // size, swap, empty functions same as the others

    // M I N I M U M  HEAP
    priority_queue<int, vector<int>, greater<int>> raj;
    raj.push(5);        //{5}
    raj.push(2);        //{2, 5}
    raj.push(8);        //{2, 5, 8}
    raj.emplace(10);    //{2, 5, 8, 10}

    cout << raj.top();        //2


// time complexity
// push: log n
// pop: log n
// top: O(1)

}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//


// stores everything in the sorted order and they're unique

void explainSet(){
    set<int> st;
    st.insert(1);     // {1}
    st.insert(2);     // {1, 2}
    st.insert(2);     // {1, 2}
    st.emplace(4);    // {1, 2, 4}
    st.insert(3);     // {1, 2, 3, 4}

    // use insert instead of push
    

    // begin, eng, rbegin, rend, size, empty, swap all are the same

    // {1, 2, 3, 4}
    auto it = st.find(3);   // stores the iterator, i.e. pointer (address) of that value

    // {1, 2, 3, 4}
    auto it = st.find(6);   // if not in the set, it'll always return st.end() : an iterator at the position after the last element

    st.erase(5);           // takes constant time

    int cnt = st.count(1); // always gives one, coz no value is repeated

    auto it = st.find(2);
    st.erase(it);         // simple

    auto it1 = st.find(2);
    auto it2 = st.find(4);
    st.erase(it1, it2);        // deletes everything from memory address of 2 to mem addr just before 4

    // lower_bound function
    // upper_bound function

}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//


// stores everything in the sorted order but not unique

void explainMultiSet(){
    multiset<int> ms;
    ms.insert(1);   //{1}
    ms.insert(1);   // {1, 1}
    ms.insert(1);   // {1, 1, 1}

    ms.erase(1);    // all 1's erased

    int cnt = ms.count(1);

    // only to erase a single 1
    ms.erase(ms.find(1));

    // ms.erase(ms.find(1), ms.find(1)+2);      some error

    //rest all functions are the same as set
    
}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//


// stores everything in the unsorted order but unique

void explainUSet(){
    unordered_set<int> us;
    // lower_bound and upper_bound functions doesn't work here
    // rest all functions are the same
    // doesn't store in any particular order (unsorted)
    // it has a BETTER COMPLEXITY than sets mostly
    // except when collisions happen
}
// in the worst case (which happens once in a blue moon), the time complexity becomes O(n)



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//


void explainMap(){
    map<int, int> mp;            // there are multiple raj, but have different numbers assgnd
    // key : value pair ; therefore value can be same (here, raj), and key should be unique (here, roll numbers)
    // key and value can be of any datatypes, int, double, pairs, anything

    map<int, pair<int, int>> mpp;
    map<pair<int, int>, int> mpp2;

    mp[1]=2;                  // in the map mp, at key 1, store value 2
    mp.emplace({3, 1});
    mp.insert({2, 4});        // stores as key:value pair

/*
    {
        {1, 2}
        {2, 4}
        {3, 1}
    }
     map stores unique keys,
     in sorted order
*/

    for(auto it : mp){
        cout << it.first << " " << it.second << endl;
    }

    cout << mp[1];            // gives the value at key 1
    cout << mp[5];            // prints 0 or NULL

    auto it = mp.find(3);     // give the iterator, address
    cout << *(it).second;

    //this is the syntax
    auto it = mp.lower_bound(2);
    auto it = mp.upper_bound(3);

    // erase, swap, size, empty are same as above

}



// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//
// ++++++++++++++++++++++++++++++//



void explainMultiMaps(){
    // similar to maps, but can have multiple keys that are same
    // only mp[key] can't be used here
}

void explainUnorderedMaps(){
    // has unique keys but not sorted
    // works in O(1) time mostly
    // in worst can O(n), once in a blue moon
}

// these were all containers
// let's learn some algorithms in STL

bool comp(pair<int, int> p1, pair<int, int> p2){
    
}

void explainExtra(){

    // sorting in ascending way
    sort(a, a+n);
    sort(v.begin(), v.end());       // sorts the vector

    // or give the iterators to some specific portion of the vector

    // sorting in descending order
    sort(a, a+n, greater<int>);



    // sorting in my own way *********************************************
    pair<int, int> a[] = {{1, 2}, {2, 1}, {4, 1}}; 

    //sort it according to 2nd element
    //if 2nd element is same, then
    //sort according to 1st element, but in descending order

    sort(a, a+n, comp);         // comp a self-comparator, i.e. a boolean function


}