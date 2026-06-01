using System.Text.RegularExpressions;

public class Solution {
    public bool IsPalindrome(string s) {
        string s1 = Regex.Replace(s, "[^a-zA-Z0-9]","");
        Console.WriteLine(s1);
        string s2 = new string(s1.Reverse().ToArray());
        Console.WriteLine(s2);
        if(s1.ToLower().Equals(s2.ToLower())){
            return true;
        }
        return false;
    }
}