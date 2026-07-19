import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>(); 
        for (String c : completion){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        for (String p : participant){
            int left = map.getOrDefault(p, 0);
            if (left<=0) return p;
            else map.put(p, left-1);
        }
        
        return "";

    }
}