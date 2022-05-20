class Solution {
    public List<String> commonChars(String[] words) {
        List<String> result = new ArrayList<>();
        int[] hash = new int[26];
        for(int i=0; i<words[0].length(); i++){
            hash[words[0].charAt(i) - 'a'] += 1;
        }
        for(int i=1; i<words.length; i++){
            int[] compareHash = new int[26];
            for(int j=0; j<words[i].length(); j++){
                compareHash[words[i].charAt(j) - 'a'] += 1;
            }
            for(int j=0; j<26; j++){
                hash[j] = Math.min(hash[j], compareHash[j]);
            }
        }
        for(int i=0; i<hash.length; i++){
            while(hash[i] != 0){
                char c = (char) (i+'a');
                result.add(String.valueOf(c));
                hash[i] --;
            }
        }
        return result;
    }
}