import java.io.*;
import java.util.*;
public class Sol {
   
   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      long q = Long.parseLong(br.readLine());
      while(q-- > 0) {
         long a = Long.parseLong(br.readLine());
         long idx=9;
         long num = 9;
         for(int i=1;i<19;i++){
            if(idx>=a) break;
            idx += Math.pow(10,i)*9*(i+1); 
            num += Math.pow(10,i)*9; 
         }
         int size=(int)Math.log10(num)+1;
         long num2 = (num - (idx-a)/size);
         int digit=(int)((idx-a)%size);
         System.out.println(num2);
         out.println(String.valueOf(num2).charAt(size-digit-1));
      }
      
      out.flush();
   }
   
}