#include<bits/stdc++.h>
using namespace std; 

int main(int argc, char **argv)
{
	string graph_id;
	int tid = 0,vertice,edge;
	int vert1,vert2,labele;
	char ch;
	string label;
	freopen(argv[1], "r", stdin);
	freopen(argv[2], "w", stdout);
	while(cin>>graph_id)
	{

		cout<<"t # "<<tid<<endl;
		tid ++;
		cin>>vertice;
		for(int i=0;i<vertice;i++)
		{
			cin>>label;
			cout<<"v "<<i<<" "<<label<<endl;
		}
		cin>>edge;
		while(edge--)
		{
			cin>>vert1>>vert2>>labele;
			cout<<"u "<<vert1<<" "<<vert2<<" "<<labele<<endl;
		}
	}
	return 0;
}
