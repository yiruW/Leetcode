class Solution {
    List<String> res = new ArrayList<>();
    public List<String> letterCombinations(String digits) {
        if(digits == null || digits.length() == 0){return res;}
        String[] phoneButton = {"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        backTracking(digits, phoneButton, 0);
        return res;
    }
    StringBuilder temp = new StringBuilder();
    private void backTracking(String digits, String[] phone, int num){
        if(num == digits.length()){
            res.add(temp.toString());
            return;
        }
        String str = phone[digits.charAt(num) - '0'];
        for(int i=0; i<str.length(); i++){
            temp.append(str.charAt(i));
            backTracking(digits, phone, num+1);
            temp.deleteCharAt(temp.length() -1);
        }
        
    }
    
}