import java.io.*;
import java.util.*;
public class Sol {
   private static class Node{
      int val;
      int index;
      Node(int val,int index){
         this.val=val;
         this.index=index;
      }
   }
   static Deque<Node> dq=new ArrayDeque<>();
   public static void main(String[] args) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      PrintWriter out = new PrintWriter(System.out);
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int k = Integer.parseInt(st.nextToken());
      st = new StringTokenizer(br.readLine());
      int x = Integer.parseInt(st.nextToken());
      int a=Integer.parseInt(st.nextToken());
      int b=Integer.parseInt(st.nextToken());
      int c=Integer.parseInt(st.nextToken());
      int y=x;
      long xor=0;
      for(int i=0;i<k;i++){
         push(x, i);
      
         x=modded(a,b,c,x);
         
      }
      xor^=dq.peekFirst().val;
   
      for(int i=k;i<n;i++){
         
         if(dq.peekFirst().index==i-k){
            dq.pollFirst();
         }
         y=modded(a,b,c,y);
         
         push(x, i);
         x=modded(a,b,c,x);
         xor^=dq.peekFirst().val;
      }
      out.println(xor);
      out.flush();
      out.close();

   }
   private static int modded(int a, int b, int c, int x) {
      long ans=(((long)a%c)*((long)x%c))%c;
      ans=(ans+((long)b%c))%c;
      return (int)ans;
   }
   private static void push(int a,int index) {
      while(!dq.isEmpty() && dq.peekLast().val>=a){
         dq.pollLast();
      }
      dq.offerLast(new Node(a, index));
   }
}
