#include<bits/stdc++.h>
using namespace std;
int main()
{
    cout<<"*********************** WELCOME TO ELERICITY MANAGEMENT SYSTEM ******************"<<endl;
    cout<<"RULES : "<<endl<<endl;
    cout<<"ENTER THE AMOUNT OF ELECTRICITY (KWH) USED TO CALCULATE THE COST(RUPEES)"<<endl;
    int units;
    cin>>units;
    if(units <= 50)
    {
        cout<<"The answer is ₹"<< (double)units*2.0;
    }
    else if(units <= 200)
    {
        cout<<"The answer is ₹"<< ((50*2.0) +( (units-50) * 2.50));
    }
    else if(units <= 400)
    {
        cout<<"The answer is ₹"<< ((50*2.0) +( (units-50) * 2.50));
    }
    else if(units <= 200)
    {
        cout<<"The answer is ₹"<< ((50*2.0) +( (units-50) * 2.50));
    }
    else if(units <= 200)
    {
        cout<<"The answer is ₹"<< ((50*2.0) +( (units-50) * 2.50));
    }
    else if(units <= 200)
    {
        cout<<"The answer is ₹"<< ((50*2.0) +( (units-50) * 2.50));
    }
}