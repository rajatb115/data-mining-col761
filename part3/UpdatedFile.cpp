#include<bits/stdc++.h>
using namespace std;
int main(){
    ifstream inputFile;
    ofstream outputFile;
    outputFile.open("paths_finished.dat");
	inputFile.open("path.txt");
    string line;
	if(!inputFile.is_open())
    {
            exit(EXIT_FAILURE);
    
    }
    while(inputFile>>line){
        stack<string> path;
        string output,link;
        int start = 0;
        int end = line.find(";");
        while (end != -1) {
            link = line.substr(start, end - start);
            if(link.compare("<") == 0){
            path.pop();
            output.append(path.top());
            output.append(";");
            }
            else{
                path.push(link);
                output.append(link);
                output.append(";");
            }
            start = end + 1;
            end = line.find(";", start);

        }
        link = line.substr(start, end - start);
        if(link.compare("<") == 0){
            path.pop();
            output.append(path.top());
            output.append(";");
        }
        else{
            path.push(link);
            output.append(link);
            output.append(";");
        }
        output.pop_back();
        outputFile<<output<<"\n";
    }
	inputFile.close();
}