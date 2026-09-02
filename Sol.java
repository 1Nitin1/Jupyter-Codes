//Hello hi
import java.io.*;
import java.util.*;
public class Sol {
   static int[] dp;
   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int x = Integer.parseInt(st.nextToken());
      int[] arr = new int[n];
      st = new StringTokenizer(br.readLine());
      for(int i = 0; i < n; i++) {
         arr[i] = Integer.parseInt(st.nextToken());
      }
      dp = new int[n];
      Arrays.fill(dp, -1);
      int ans = solve(arr, x, 0);
      out.println(ans);
      out.flush();
   }
   private int solve(int[] arr,int x,int idx){
      if
   }
   
}