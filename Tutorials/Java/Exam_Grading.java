import java.util.*;

public class Exam_Grading {
    public static void main(String[] args){

        Scanner scn = new Scanner(System.in);
        int marks = scn.nextInt();

        if (marks > 90) {
            System.out.println("Excellent");
        } else if (marks > 80) {
            System.err.println("Good");
        } else if (marks > 70) {
            System.out.println("Fair");
        } else if (marks > 60) {
            System.out.println("Meet Expectation");
        } else {
            System.out.println("Below Par");
        }

        // String grade = marks > 90 ? "Excellent" : (marks > 80 ? "Good" : (marks > 70 ? "Fair" : (marks > 60 ? "Meet Expectation" : "Below Par")));
        // System.out.println(grade);

        scn.close();
    }
}