#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
bool compare(pair<double,int>p1,pair<double,int>p2)
{
    return p1.first>p2.first;
}
int fractional_knapsack(vector<int>val,vector<int>wt,int weight)
{

    int n=val.size();
    vector<pair<double,int>>ratio(n,make_pair(0.0,0));
    
    for(int i=0;i<n;i++)
    {
        double r =val[i]/wt[i];
        ratio[i].first=r;
        ratio[i].second=i;
    }
    sort(ratio.begin(),ratio.end(),compare);
    int ans=0;
    for(int j=0;j<n;j++)
    {
        int idx=ratio[j].second;
        if(wt[idx]<=weight)
        {
            weight-=wt[idx];
            ans+=val[idx];

        }
        else
        {
            ans+=ratio[j].first*weight;
            weight=0;
            break;
        }
        
    }
    cout<<"max val=";
    return ans;
}
int main()
{
    vector<int>val={60,100,120};
    vector<int>wt={10,20,30};
    int weight = 50;
    cout<<fractional_knapsack(val,wt,weight);

}