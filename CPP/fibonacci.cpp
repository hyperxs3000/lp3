#include<iostream>

using namespace std;
int fibb(int n)
{
    if(n==1 ||n==0)
    {

        return n;

    }
    
     return fibb(n-1)+fibb(n-2);
    
}

void iterative(int n)
{
    int a=0,b=1,c=0;
    for(int i=0;i<=n;i++)
    {
        cout<<a<<" ";
        int item=b;
        b=a+b;
        a=item;
        
    }
}
int main()
{
    int n=6;
    cout<<fibb(n)<<"\n";
    iterative(n);
}