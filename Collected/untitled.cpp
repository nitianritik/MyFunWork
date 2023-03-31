#include<bits/stdc++.h>
using namespace std;


int main()
{
   
   priority_queue <int, vector<int>, greater<int> > pq;


    for(int i=-2;i<=10;i++)
   	{
   		pq.push(i);
   	}


   	// for(int value : pq)
   	// {
   	// 	cout<<value<<" ";
   	// }

   	while(!pq.empty())
   	{
        cout<<"\t"<<pq.top()<<endl;
   		pq.pop();
   	}


	return 0;
}


// class Solution {
// public:
//     vector<int> kthSmallestPrimeFraction(vector<int>& arr, int k) {
        
        
        
        
//         vector<int> P;       
//         priority_queue<pair<double,pair<int,int>>,vector<pair<double,pair<int,int>>>,greater<pair<double,pair<int,int>>>> pq;
        
        
        
//         for(int i=0;i<arr.size();i++)
//         {
//             for(int j=i+1;j<arr.size();j++)
//             {
//                 pq.push({(double)(arr[i])/(double)(arr[j]),{arr[i],arr[j]}});
//             }
//         }
        
//         k--;
        
//         while(pq.size() && k--)
//         {
//             pq.pop();
//         }
        
//         return {pq.top().second.first,pq.top().second.second};
        
        
//     }
// };


//____________________________________________________________
// int main()
// {
//    vector<int> v = {1,2,3,4,5,6,7,8,9};
//    auto check = [](int x){ return x<0; };


//    cout<< none_of(v.begin(),v.end(),check);


// 	return 0;
// }


//____________________________________________________________________

// int main()
// {
//    int x=5,y=4;


//    auto sum =  [](int a,int b)
//                 { 
//                 	return (a+b); 
//                 };



   


// 	return 0;
// }

//___________________________________________________________________________________

// struct Node

// {

//   int data;
//   struct Node* left;
//   struct Node* right;


//   Node(int val)
//   {
//   	data  = val;
//   	left  = NULL;
//   	right = NULL;
//   }

// };


// int main()
// {


//  struct Node* root = new Node(1);
//  root->left  = new Node(2);
//  root->right = new Node(3);

//  root->left->left  = new Node(4);
//  root->left->right = new Node(5);

// cout<<root->left->right->data;


//  return 0;
// }


///______________________________________________________________________________




//     cout<<ceil((float)7/3)<<endl<<endl;
// 	return 0;


 // vector< vector<int> > v = { {1,2,3,4,5,6,7,8,9 },{9,8,7,6,5,4,3,2,1,0 }};

 //     for(auto value : v)
 //    {

 // 	  for(auto value2 : value)
 // 	   {
 // 		cout<<value2<<" ";
 // 	   }

 // 	  cout<<endl;
 //    }