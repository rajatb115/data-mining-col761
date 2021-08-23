#include<bits/stdc++.h>
using namespace std;

void frequent_sequence(vector<list<string>> database,map<string,int> link,string key, int sup,queue<string> seq){
    vector<list<string>> projectedDB;
    for(auto j = database.begin(); j!= database.end(); j++){
        list<string> temp;
       for(auto k = j->begin(); k!= j->end(); k++){
           if((*k).compare(key)==0){
               temp.assign(++k,j->end());
               break;
           }
       }
       projectedDB.push_back(temp);
    }
    
    map<string,int> countSup;
    for(auto i = link.begin(); i!= link.end(); i++){
        //count support of all links(item)
        for(auto j = projectedDB.begin(); j!= projectedDB.end(); j++){
            for(auto k = j->begin(); k!= j->end(); k++){
                if((*k).compare(i->first)==0){
                    if(countSup.find(i->first) != countSup.end()){
                        countSup[i->first]= countSup.find(i->first)->second+1;
                    }
                    else
                        countSup[i->first]= 1;
                
                    break;
                }
            }
        }
    }

    for(auto i = countSup.cbegin(); i!= countSup.cend();){
        if(i->second<sup){
            countSup.erase(i++);
        }
        else
            ++i;
    }
    if(countSup.size()==0){
        //print stack
        while (!seq.empty())
        {
            cout <<seq.front()<<" ";
            seq.pop();
        }
        cout<<"\n";
    }
    for(auto i = countSup.begin(); i!= countSup.end(); i++){
        seq.push(i->first);
        frequent_sequence(projectedDB,countSup,i->first,sup,seq);
    }


}

int main(){
    ifstream inputFile;
    ofstream outputFile;
    int support = 100;
    inputFile.open("paths_finished.dat");
	outputFile.open("frequent_path.dat");
    string line;
    map<string,int> link;
    vector<list<string>> database;
	if(!inputFile.is_open())
    {
            exit(EXIT_FAILURE);
    
    }
    while(inputFile>>line){  
        set<string> uniqueItem; 
        char *token = strtok(const_cast<char*>(line.c_str()), ";"); 
        list<string> item;
        while (token != nullptr) 
        { 
            uniqueItem.insert(string(token)); 
            item.push_back(string(token));
            token = strtok(nullptr, ";"); 
        } 
        database.push_back(item);
        for (auto it = uniqueItem.begin(); it != uniqueItem.end(); it++){
            if(link.find(*it) != link.end()){
                link[*it]= link.find(*it)->second+1;
            }
            else
                link[*it]= 1;
        }
    } 
    int count = 0;
    for(auto i = link.cbegin(); i!= link.cend();){
        if(i->second<support){
            link.erase(i++);
        }
        else
            ++i;
    }
    for(auto i = link.begin(); i!= link.end(); i++){
        queue<string> seq;
        seq.push(i->first);
        frequent_sequence(database,link,i->first,support,seq);
    }
    //cout<<count;
}
