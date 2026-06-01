public class Solution {
    public string AddBinary(string a, string b) {
        
        /*below logic will work only for the lower numbers which can be accomated in the int type
        ********************************
        int result1 = ConvertBinaryToNumber(a);
        Console.WriteLine(result1);
        int result2 = ConvertBinaryToNumber(b);
        Console.WriteLine(result2);
        return ConvertNumberToBinay(result1+result2);
        ****************************/

        char[] binary1 = a.ToCharArray();
        char[] binary2 = b.ToCharArray();
        Array.Reverse(binary1);
        Array.Reverse(binary2);
        
        int carry = 0;
        int i=0,k=0;
        string result = String.Empty;
        while(i <a.Length || k <b.Length || carry > 0){

            //there is a possibility and lenght of a and k are not same, to taking 0 if length doesn't match
            int val1=0;
            if(i<binary1.Length){
                val1 = binary1[i++] - '0';
            }

            int val2=0;
            if(k<binary2.Length){
                val2=binary2[k++] - '0';
            }

            int sum = val1 + val2 + carry;
            if(sum == 0){
                result += "0";
                carry = 0;
            }
            else if (sum == 1){
                result += "1";
                carry = 0;
            }
            else if (sum == 2){
                result += "0";
                carry = 1;
            }
            else if (sum == 3){
                result += "1";
                carry = 1;
            }

        }
        char[] charResult = result.ToCharArray();
        Array.Reverse(charResult);
        return new String(charResult);

    }

    public int ConvertBinaryToNumber(string binaryString){
        char[] c = binaryString.ToCharArray();
        int totalSum = 0;
        for(int i=0;i<binaryString.Length;i++){
            if(c[i]=='0' && i==0){
                return 0;
            }
            else if(c[i]=='1'){
                totalSum = (totalSum*2 + 1);
            }
            else if(c[i]=='0'){
                totalSum = totalSum*2;
            }
        }
        return totalSum;
    }

    public string ConvertNumberToBinay(int number){
        if(number == 0){
            return "0";
        }
        else if(number == 1){
            return "1";
        }
        else{
            int quotient = number/2;
            int remainder = number%2;
            if(quotient==0)
                return "1";
            else{
                string result = String.Empty;
                result = remainder.ToString();
                Console.WriteLine(result);
                while(quotient !=0){
                    remainder = quotient%2;
                    quotient = quotient/2;
                    result += remainder.ToString();
                    Console.WriteLine(result);
                }
                char[] c = result.ToString().ToCharArray();
                Array.Reverse(c);
                return new String(c);
            }
            
        }
    }
}