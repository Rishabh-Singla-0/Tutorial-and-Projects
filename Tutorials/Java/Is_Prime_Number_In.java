import java.util.*;

public class Is_Prime_Number_In {
    public static void main(String[] args) {
        
        Scanner scn = new Scanner(System.in);

        System.out.print("Enter The Lower Range: ");
        int low = scn.nextInt();

        System.out.print("Enter The Higher Range: ");
        int high = scn.nextInt();

        System.out.println("The Prime Number Between " + low + "-" + high + " are: ");

        for (int i = low ; i <= high; i++){

            int count = 0;

            for ( int j = 2 ; j * j <= i ; j++ ) {
                if ( i % j == 0 ) {
                    count++;
                    break;
                }
            }

            if ( count == 0 ) {
                System.out.println(i + " is a Prime Number");
            }
        }

        scn.close();
    }
}
