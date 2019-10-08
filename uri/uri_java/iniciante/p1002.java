package iniciante;
import java.util.Scanner;

public class p1002 {
 
    public static void main(String args[]) {
        double A, r;
        
        Scanner entrada = new Scanner(System.in);
        r = Double.parseDouble(entrada.nextLine());
        A = r*r*3.14159;
        System.out.println("A="+ String.format("%.4f",A));
    }
}
