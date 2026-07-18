import java.io.*;
import java.util.*;
public class Sol {
   
   public static void main(String[] args) throws Exception {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      String s = br.readLine();
      int[] count = new int[26];
      for (int i = 0; i < s.length(); i++) {
         count[s.charAt(i) - 'A']++;
      }
      int oddCount = 0;
      char oddChar = ' ';
      for (int i = 0; i < 26; i++) {
         if (count[i] % 2 == 1) {
            oddCount++;
            oddChar = (char) (i + 'A');
         }
      }
      if (oddCount > 1) {
         out.println("NO SOLUTION");
      } else {
         StringBuilder half = new StringBuilder();
         for (int i = 0; i < 26; i++) {
            for (int j = 0; j < count[i] / 2; j++) {
               half.append((char) (i + 'A'));
            }
         }
         StringBuilder palindrome = new StringBuilder(half);
         if (oddCount == 1) {
            palindrome.append(oddChar);
         }
         palindrome.append(half.reverse());
         out.println(palindrome);
      }
      out.flush();
   }
   
}