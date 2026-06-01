public class Solution {
    public bool IsValid(string s) {
        if(s == String.Empty || s.Length==0 || s.Length%2!=0){
            return false;
        }
        Stack<char> a = new Stack<char>();
        char[] c = s.ToCharArray();
        
        for(int i=0;i<s.Length;i++){
            if(c[i]=='(' || c[i]=='{' || c[i]=='['){
                a.Push(c[i]);
            }
            else{
                if(a.Count == 0)
                    return false;
                if(c[i]==')' && a.Peek()=='('){
                    a.Pop();
                }
                else if(c[i]=='}' && a.Peek()=='{'){
                    a.Pop();
                }
                else if(c[i]==']' && a.Peek()=='['){
                    a.Pop();
                }
                else
                    return false;
            }
            
        } 
        if(a.Count > 0)
            return false;
        return true;
    }
}