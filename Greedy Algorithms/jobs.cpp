#include<iostream> 
#include<algorithm> 
using namespace std; 

// A structure to represent a job 
struct Job 
{ 
long int id;     
long int deadline; 
long int profit; 
}; 

bool comparison(Job a, Job b) 
{ 
     return (a.profit > b.profit); 
} 


void printJobScheduling(Job arr[], long int n) 
{ 
    sort(arr, arr+n, comparison); 

  long int result[n]; 
    bool slot[n];   
    for (long int i=0; i<n; i++) 
        slot[i] = false;  
    for (long int i=0; i<n; i++) 
    { 
    for (long int j=min(n, arr[i].deadline)-1; j>=0; j--) 
    { 
        if (slot[j]==false) 
        { 
            result[j] = i; 
            slot[j] = true; 
            break; 
        } 
    } 
    } 
 
    for (long int i=0; i<n; i++) 
    if (slot[i]) 
        cout << arr[result[i]].id << " "; 

  //cout << arr[result[i]].profit <<" ";

} 

int main() 
{ 
    long int x=0;
    cout<<"Enter the jobs you want  to enter";
    cin>>x;
 Job P[x];
int start=clock();
    srand(time(0)); 
cout<<start;
    for( long int i=0; i<x; i++){                         
         P[i].id=i;
        P[i].deadline=1+rand()%10;
                P[i].profit=1+rand()%100;
        cout<< "jobid are"<<P[i].id<< " " << "deadline are"<<P[i].deadline<< " " << "profit are"<<P[i].profit<<endl;
    }
    
    int y = sizeof(P) / sizeof(P[0]); 
    cout << "Following is maximum profit sequence of jobsn"; 
    printJobScheduling(P, y); 
        int end=clock();
cout<<"\n"<<(end-start)/double(CLOCKS_PER_SEC)*1000<<endl;
    return 0; 
} 



