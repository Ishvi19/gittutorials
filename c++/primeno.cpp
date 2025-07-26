#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int i=2;
int sum = 0;
while(i<n){
    if(n%i==0){
    cout << "Not Prime" << endl;
    }
    else{
        cout<< "Prime" <<endl;
        return 0;
    }
    i=i+1;
}
return 0;
}