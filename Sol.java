import java.io.*;
import java.util.*;
public class Sol {
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      int t = Integer.parseInt(br.readLine());
      while(t-- > 0) {
         int n = Integer.parseInt(br.readLine());
         int start=1;
         int end=3*n;
         for(int i = 0; i < n; i++) {
            out.print(start++ +" "+end-- +" "+end--+" ");
         }
         
         out.println();

      }
      out.flush();
   }
}
