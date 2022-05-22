class Solution {
    public List<Integer> partitionLabels(String s) {
        int[] lastPosition = new int[26];
        for(int i=0; i<s.length(); i++){
            lastPosition[s.charAt(i) - 'a'] = i;
        }
        int j = 0, anchor = 0;
        List<Integer> answer = new ArrayList();
        for(int i=0; i<s.length(); i++){
            j = Math.max(j, lastPosition[s.charAt(i)-'a']);
            if(j == i){
                answer.add(i-anchor +1);
                anchor = i+1;
            }
        }
        return answer;
    }
}