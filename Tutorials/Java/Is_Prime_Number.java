import java.util.*;

public class Is_Prime_Number {
    public static void main(String[] args) {

        Scanner scn = new Scanner(System.in);

        System.out.println("Enter a No. - ");
        int prime = scn.nextInt();

        int count=0;

        for ( int i = 2 ; i * i <= prime ; i++ ) {
            if ( prime % i == 0 ) {
                count++;
                break;
            }
        }

        if ( count == 0 ) {
            System.out.println(prime + " is a Prime Number");
        }
        else {
            System.out.println(prime + " is not a Prime Number");
        }

        scn.close();
    }
}