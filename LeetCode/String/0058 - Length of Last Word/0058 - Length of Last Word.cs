public class Solution {
    public int LengthOfLastWord(string s) {
        string[] split = s.Trim().Split(" ");
        string result = split[split.Length-1];
        return result.Length;
    }
}