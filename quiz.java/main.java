import java.util.Scanner;  // Import the Scanner class

public class main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);  // Create a Scanner object

        String[] questions = {"what is your name", "what is your favorite subject"};
        String[] answers = {"loyd", "cs"};

        int sizeOfArray = questions.length - 1;
        String message = "Pick a question from 0 to ";

        System.out.print( message + sizeOfArray + ": ");
        int question_selector = scanner.nextInt();

        System.out.println(questions[question_selector]);
        String answer = scanner.nextLine().toLowerCase(null);

        if( answer == answers[question_selector]){
            System.out.println("You're Correct!");
        }
        else{
            System.out.println("You're wrong!");
        }




        
    }
}
