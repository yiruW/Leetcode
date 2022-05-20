class Solution {
    public boolean backspaceCompare(String s, String t) {
        int slow1=0, slow2 = 0;
        char[] c1 = new char[s.length()];
        char[] c2 = new char[t.length()];
        for(int fast1 = 0; fast1 < s.length(); fast1++){
            if(s.charAt(fast1) != '#'){
                c1[slow1]  = s.charAt(fast1);
                slow1 ++;
            }else{
                if(slow1 > 0){
                    slow1 --;
                }
            }
        }
        for(int fast2 = 0; fast2 < t.length(); fast2++){
            if(t.charAt(fast2) != '#'){
                c2[slow2]  = t.charAt(fast2);
                slow2 ++;
            }else{
                if(slow2 > 0){
                    slow2 --;
                }
            }
        }
        if(slow1 != slow2){return false;}
        for(int i=0; i<slow1; i++){
            if(c1[i] != c2[i]){
                return false;
            }
        }
        return true;
    }
}