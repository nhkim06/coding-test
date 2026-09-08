class Solution {
    public int solution(String[][] board, int h, int w) {
        int n = board.length;
        int m = board[0].length;
        int count = 0;
        
        int[] dh = {0, 1, -1, 0};
        int[] dw = {1, 0, 0, -1};
        
        for (int i=0; i<=3; i++){
            int h_check = h + dh[i];
            int w_check = w + dw[i];
            
            if ((h_check >= 0 && h_check < n) && (w_check >= 0 && w_check < n)){
                if (board[h][w].equals(board[h_check][w_check])) count++;
            }
            
        }
        
        return count;
    }
}

/*
문제 해석
- out : (h, w)좌표 기준, 이웃한 칸들 중 같은 색상 개수

*/