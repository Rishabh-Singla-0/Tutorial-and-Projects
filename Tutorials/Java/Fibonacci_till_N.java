import java.util.*;

public class Fibonacci_till_N {
    public static void main(String[] args) {
        
        Scanner scn = new Scanner(System.in);

        System.out.print("Enter The Limit of Fibonacci Series: ");
        int n = scn.nextInt();

        int a=0, b=1, c;

        for( int i = 1 ; i <= n ; i++ ) {

            System.out.println(a);
            
            c=a+b;
            a=b;
            b=c;
        }

        scn.close();
    }
}