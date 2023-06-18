import java.util.HashMap;
import java.util.Map;

public class Anagram {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }
        int[] freq = new int[26];
        for(int i=0;i<s.length();i++){
            freq[s.charAt(i)-'a'] += 1;
        }
        for(int i=0;i<t.length();i++){
            if( freq[t.charAt(i)-'a']==0){
                return false;
            }
            else {
                freq[t.charAt(i)-'a'] -= 1;
            }
        }
        return true;
    }
}
