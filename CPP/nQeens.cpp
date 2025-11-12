#include<iostream>
#include<vector>
using namespace std;
int count=0;
void print(vector<vector<char>>board)
{
    count+=1;
    int n=board.size();
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cout<<board[i][j]<<" ";

        }
        cout<<"\n";
        
    }
    cout<<"------------------------\n";

}
bool issafe(vector<vector<char>>board,int row,int col)
{
    int n=board.size();
    //horizontal safety
    for(int i=0;i<n;i++)
    {
        if(board[row][i]=='Q')
        {
            return false;
        }
    }

    //verticle 
    for(int j=0;j<row;j++)
    {
        if(board[j][col]=='Q')
        {
            return false;
        }
    }
    //diagonal
    for(int i=row,j=col;i>=0 && j>=0;i--,j--)
    {
        if(board[i][j]=='Q')
        {
            return false;
        }
    }
    for(int i=row,j=col;i>=0 && j<n;i--,j++ )
    {
        if(board[i][j]=='Q')
        {
        return false;
        }
    }
    return true;
    
}
void nqueen(vector<vector<char>>board,int row)
{
    int n=board.size();
   
        if(row==n)
        {
            print(board);
            return ;
        }
        for(int j=0;j<n;j++)
        {
             if(issafe(board,row,j))
             {
            board[row][j]='Q';
            nqueen(board,row+1);
            board[row][j]='.';
            }
        }
}
int main()
{
    vector<vector<char>>board;
    int n=8;
    for(int i=0;i<n;i++)
    {
        vector<char>newrow;
        for(int j=0;j<n;j++)
        {
            newrow.push_back('.');

        }
        board.push_back(newrow);
    }
   nqueen(board,0);
   cout<<count;
    return 0;
}