class Solution {
    int left = 0, right = 0;
    int maxLength = 0;
    public String longestPalindrome(String s) {
        for(int i=0; i<s.length(); i++){
            findPalindrome(s, i, i);
            findPalindrome(s, i, i+1);
        }
        return s.substring(left, right+1);
    }
    private void findPalindrome(String s, int start, int end){
        while(start >=0 && end<s.length() && s.charAt(start) == s.charAt(end)){
            if((end-start+1) > maxLength){
                left = start;
                right = end;
                maxLength = end - start + 1;
            }
            start --;
            end ++;
        }
    }
}