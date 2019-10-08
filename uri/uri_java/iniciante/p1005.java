package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1005 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        double a, b, AVG;
        a = Double.parseDouble(leitura.readLine());
        b = Double.parseDouble(leitura.readLine());
        AVG = (a*(0.35)+b*(0.75))/1.1;
        
        System.out.println("MEDIA = "+String.format("%.5f",AVG));
    }
}
