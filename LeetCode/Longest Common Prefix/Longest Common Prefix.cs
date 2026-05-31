public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        if(strs==null || strs.Length == 0){
            return "";
        }
        string result = String.Empty;
        for(int i=0;i<strs[0].Length;i++){
            char c = strs[0][i];
            int count=1;
            for(int a=1;a<strs.Length;a++){

                if(i>=strs[a].Length){
                    break;
                }
                char k = strs[a][i];
                if(c==k){
                    count++;
                }
            }
            if(count==strs.Length){
                result += c;
            }
            else{
                break;
            }
        }
        return result;
    }
}