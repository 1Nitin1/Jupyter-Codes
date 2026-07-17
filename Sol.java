import java.io.*;
import java.util.*;
public class Sol {
   
   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      StringTokenizer st;
      int[][] board = new int[8][8];
      for(int i=0;i<8;i++){
         String s = br.readLine();
         for(int j=0;j<8;j++){
            if(s.charAt(j)=='*'){
               board[i][j] = -1;
            }
         }
      }
      out.println(solve(board,0));
      out.flush();
   }
   private static int solve(int[][] board,int row){
      if(row==8){
         return 1;
      }
      int ans = 0;
      for(int col=0;col<8;col++){
         if(board[row][col]<0){
            continue;
         }
         for(int r=0;r<8;r++){
            board[r][col]--;
         }
         for(int c=0;c<8;c++){
            board[row][c]--;
         }
         for(int r=row,c=col;r<8 && c<8;r++,c++){
            board[r][c]--;
         }
         for(int r=row,c=col;c>=0 && r<8;r++,c--){
            board[r][c]--;
         }
         ans += solve(board,row+1);
         for(int r=0;r<8;r++){
            board[r][col]++;
         }
         for(int c=0;c<8;c++){
            board[row][c]++;
         }
         for(int r=row,c=col;r<8 && c<8;r++,c++){
            board[r][c]++;
         }
         for(int r=row,c=col;c>=0 && r<8;r++,c--){
            board[r][c]++;
         }
      }
      return ans;
   }
}