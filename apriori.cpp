#include <bits/stdc++.h>
#include <iostream>
#include <vector>
#include <string.h>
#include <set>
#include <map>
#include <math.h>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;
typedef int ll;

char* dataset_path;

vector< vector<ll> > frequent_set;
vector< vector<ll> > prev_set;

vector< vector<ll> > candidate_set;
vector< vector<ll> > next_set;
vector<ll> count_subsets;
ll freq_set_size;


// c++ is taking 14 sec to read the file once
// python is taking 20 sec to read the file once

//Frequency in a map generator function generating map of frequency of item.
pair<map <ll,ll>,ll> frequency()
{
	map<ll,ll> individual_freq;
	ll count = 0;
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	fp = fopen(dataset_path, "r");
	while ((read = getline(&line, &len, fp)) != -1) 
	{
        count++;
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

    return make_pair(individual_freq,count);
}


//Vector sort function
bool sortbyvec(const vector <ll> &a,const vector <ll> &b)
{
	ll sizea = a.size();
	ll sizeb = b.size();
	ll size_min = min(sizea,sizeb);
	for(ll i=0;i<size_min;i++)
	{
		if(a[i] < b[i])
		{
			return true;
		}
		if( a[i] > b[i])
		{
			return false;
		}
	}
	return sizea < sizeb ;
}

// Checks if itemset i and itemset j can be combined
int check_combine(vector <ll> v1,vector <ll> v2)
{
	ll size= v1.size();
	for(ll i=0;i<size-1;i++)
	{
		if(v1[i]!=v2[i])
		{
            if(v1[i]<v2[i])
                return -1;
            else
                return 0;
			
		}
	}
	return 1;
}

// generates a (k-1) subset of vector v1 of size k removing element at position pos1
vector<ll> subset_gen(vector<ll> v1, int pos1)
{
	vector<ll> result;
	for(ll i=0;i<v1.size();i++)
	{
		if(i==pos1)
		{
			continue;
		}
		result.push_back(v1[i]);
	}
	return result;
}

//Checks if a given itemset exists in our list of previously generated sets
bool check_if_exists(vector<ll>v1)
{
	ll abc = prev_set.size();
	for(ll i=0;i<abc;i++)
	{
		if(prev_set[i]==v1)
		{
			return true;
		}
	}
	return false;
}

//Generates candidates
void generate_candidates()
{
    // cleaning the candidate_set
	candidate_set.clear();
    
	ll size = prev_set.size();
	freq_set_size = prev_set[0].size();
    
    
    if(freq_set_size == 1){
        // if the freq_set_size length is 1
        for(ll i=0;i<size;i++)
            for(ll j=i+1, j<size; j++){
                candidate_set.push_back([min(prev_set[i],prev_set[j]),max(prev_set[i],prev_set[j])]);
            }
    }else{
        // if the freq_set_size length is > 1
        for(ll i=0;i<size;i++)
        {
            for(ll j=i+1;j<size;j++)
            {   
                // Check if we can concatinate the two sets 
                // Concatination is only possible if set_size-1 elements in both the sets are maching.
                //  {1,5,7},{1,6,20} => for this condition we can break the inner "for" loop as no other merging is possible

                int tmp_res = check_combine(prev_set[i],prev_set[j])

                if(tmp_res == -1)
                {
                    continue;
                }

                if(tmp_res == 0){
                    break;
                }

                bool allowed_candidate = true;
                vector<ll> v_store = prev_set[i];
                v_store.push_back(prev_set[j][freq_set_size-1]);

                for(ll k=0;k<=freq_set_size;k++)
                {

                    vector<ll> store_res = subset_gen(v_store,k);
                    if(!check_if_exists(store_res))
                    {
                        allowed_candidate = false;
                        break;
                    }

                }

                if(allowed_candidate)
                {
                    candidate_set.push_back(v_store);
                }

            }
        }
        
    }
}

//Now we write functions for filtering the candidate set

//Finds if v1 is a subset of v2.
bool is_subset(vector<ll>v1,vector<ll>v2)
{
    ll size1= v1.size();
	ll size2 = v2.size();
    // If the length of candidate set is greater than the set then return false
    if(size1>size2)
        return false;
    
	ll pos1=0,pos2=0;
	
    
	while (pos1<size1 && pos2<size2)
	{
		if(v1[pos1]== v2[pos2])
		{
			pos1++;
		}
		pos2++;
        
        if(pos1==size1)
	   {
		  return true;
	   }
        
	}
    
	//if(pos1==size1)
	//{
	//	return true;
	//}
    
	return false; 
}

//Counts no of orders which are supersets for each candidate set
void count_total_subsets(int threshold)
{
	int count = 0;
	FILE * fp;
	char * line = NULL;
	size_t len = 0;
	ssize_t read;
	fp = fopen(dataset_path, "r");
	ll size = candidate_set.size();
    
    // tmp toggle when itemset count reached to certain threshold
    // bool tmp = false;
    
	while ((read = getline(&line, &len, fp)) != -1 ) 
	{
		vector<ll> v_store;
		char *ptr = strtok(line, " ");
		while(ptr!=NULL)
		{
			int store = atoi(ptr);
			v_store.push_back(store);
			ptr = strtok(NULL, " ");
		}
        
        // Removing extra unwanted reading of data using tmp_cnt.
        ll tmp_cnt = 0;
        
		for(ll i=0;i<size;i++)
		{ 
            
            
            // we can track count_subset and check that we need to skip it or not
            // will be helpful when the threshold is low. -> need to implement
            if(count_subsets[i]<threshold)
            {
				if(is_subset(candidate_set[i],v_store))
				{
					count_subsets[i]++;
				}
          
			}else{
                tmp_cnt++;
            }
            
		}
        
        if(tmp_cnt == size){
            break;
        }
        
    }
    
    fclose(fp);
    
}

//Filters the sets for required frequency threshold
void filter_set(int threshold)
{
	ll size= candidate_set.size();
    
    // cleaning the count_subsets
	count_subsets.clear();
    
	for(ll i=0;i<size;i++)
	{
		count_subsets.push_back(0);
	}
    
	count_total_subsets(threshold);
    
	for(ll i=0;i<size;i++)
	{
		if(count_subsets[i]>=threshold)
		{
			next_set.push_back(candidate_set[i]);
			frequent_set.push_back(candidate_set[i]);
		}
	}
    
}



int main(int argc, char ** argv)
{
    
	dataset_path = argv[1];
	pair<map<ll,ll>,ll> item_freq_count= frequency();
   	map<ll,ll> item_freq = item_freq_count.first;
    ll no_of_orders = item_freq_count.second;
    
	freopen(argv[3], "w", stdout);
    
    // Finding the threshold (taking ceil)
	float x = atof(argv[2])*0.01;
	ll threshold = ceil(x* no_of_orders);
    
    
    map <ll,ll>::iterator it;
	for(it= item_freq.begin(); it!= item_freq.end(); it++){
		if(it->second >= threshold)
		{
			vector<ll> v1;
			v1.push_back(it->first);
			//frequent_set.push_back(v1);
            cout<<it->first<<"\n";
			prev_set.push_back(v1);
		}
	}
    
	while(prev_set.size()>0)
	{
		generate_candidates();
		filter_set(threshold);
		prev_set = next_set;
		next_set.clear();
	}
   	
    
	//sort(frequent_set.begin(),frequent_set.end(),sortbyvec);
	/*
    for(ll i=0;i<frequent_set.size();i++)
	{
		for(ll j=0;j<frequent_set[i].size();j++)
		{	
 			cout<< frequent_set[i][j]<<" ";  
		}
		cout<<"\n";
	}*/
    
	return 0;
}
