import java.util.*;

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        int[][] dp = new int[n+1][m+1];
        boolean[][] puddle = new boolean[n+1][m+1];
        
        for (int[] p : puddles){
            puddle[p[1]][p[0]] = true;
        }
                   
        dp[1][1] = 1;
                   
        for (int y = 1; y<n+1; y++){
            for (int x = 1; x<m+1; x++){
                if (x == 1 && y == 1) continue;
                
                if (puddle[y][x]){
                    dp[y][x] = 0;
                    continue;
                }
                
                dp[y][x] = (dp[y][x-1] + dp[y-1][x]) % 1000000007;
                
            }
        }
        
        
        return dp[n][m];
    }
}