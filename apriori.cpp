#include <iostream>
#include <vector>
#include <string.h>
#include <set>
#include <map>

using namespace std;
typedef long long int ll;

char* dataset_path = "webdocs.dat";

int transaction_count()
{
	int count = 0;
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	fp = fopen(dataset_path, "r");
	while ((read = getline(&line, &len, fp)) != -1) 
	{
		count++;
    }
    fclose(fp);
    if (line)
        free(line);
    return count;
}

map <ll,ll> frequency()
{
	map<ll,ll> individual_freq;
	int count = 0;
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	fp = fopen(dataset_path, "r");
	while ((read = getline(&line, &len, fp)) != -1) 
	{
		char *ptr = strtok(line, " ");
		while(ptr!=NULL)
		{
			int store = atoi(ptr);
			individual_freq[store] ++;
			ptr = strtok(NULL, " ");
		}
    }

    fclose(fp);
    if (line)
        free(line);
    return individual_freq;
}


int main()
{
	map<ll,ll> item_freq= frequency();
	cout<<item_freq[1]<<endl;
	return 0;
}
