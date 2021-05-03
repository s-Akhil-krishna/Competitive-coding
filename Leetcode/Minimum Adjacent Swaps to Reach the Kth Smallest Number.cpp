class Solution {
public:
    int getMinSwaps(string num, int k) {
        string source(num);
        string target(num);
        for(int i=0;i<k;i++){
            next_permutation(target.begin(),target.end());
            // cout << target << endl;
        }
        
        int sz = num.size();
        int ans =0;
        for(int i=0;i<sz;i++){
            if(source[i]!=target[i]){
                int j = i + 1;
                while(source[j]!=target[i])j++;
                for(;j>i;j--){
                    swap(source[j-1],source[j]);
                    ans++;
                }
            }
        }
        return ans;
    }
};
