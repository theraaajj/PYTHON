#include <iostream>
using namespace std;

int main()
{
    // character array can also act as a string
        // char arr[] = {'a', 'p', 'p', 'l', 'e'};
        // cout<<arr; 
    // output : appleÇ          (last one is a null character that gets added by default to signify word ends here, and the system won't check further)

        // char arr[] = {'a', 'p', 'p', 'l', 'e'};
        // for(int i=0; i<5; i++)
        // cout<<arr[i]; 
    // output : apple            (will also have a null value at last (\0))

    // variable size
        // char arr[10];
        // cin>>arr;
        // arr[2] = '\0';
        // cout<<arr;
    // input : rajaryan69
    // output : ra     , bcz at index 2, a null character was found and execution stopped

    // string
        // string s;
        // cin>>s;         
        // cout<<s;
    // input : rajaryan         output : rajaryan
    // input : raj aryan        output : raj
    // WHY?

    //NOTE:  cin has a property that as soon as SPACE, TAB, ENTER is hit, cin stops taking input there itself
    //       So in order to take a line as a string input, here's the syntax

        string name;
        getline(cin, name);
        cout<<name<<endl;
    // input : raj is a good boy
    // output : raj is a good boy

    // SIZE of a string
        cout<<name.size()<<endl;
    // output : 17

    // Concatenation of strings
        string a = "raj";
        string b = "aryan";
        string c = a+b;
        // string c = a.append(b);
        cout<<c<< endl;            // rajaryan

    // push and pop operations
        name.push_back('W');
        // name = name + 'W';
        cout<<name<<endl;             // raj aryanW
        name.pop_back();
        cout<<name<<endl;             // raj aryan 

    // ESCAPE CHARAACTER  ( \ )
    string n = "I want a \"marvel\" toy";
    cout<<n<<endl;                            // I want a "marvel" toy

    // How to print the \ character itself?
    string m = "\\";
    cout<<m<<endl;


    // Reverse of string
    string x = "raj aryan";
    int start = 0;
    int end = x.size()-1;
    while( start<end){
        swap(x[start], x[end]);
        start++, end--;    
    }
    cout<<x<<endl;                 // nayra jar

    // finding size of a string
    int size = 0;
    while(x[size]!='\0'){
        size++;
    }
    cout<<size<<endl;


    // checking pallindrome
    string z = "naman";
    start = 0, end = z.size()-1;

    while(start<end){
        if(z[start]!=z[end]){
            cout<<"Not Pallindrome"<<endl;
            return 0;
        }
        start++, end--;
    }
    cout<<"Pallindrome"<<endl;
}

