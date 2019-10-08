package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1006 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        double a, b, c, AVG;
        a = Double.parseDouble(leitura.readLine());
        b = Double.parseDouble(leitura.readLine());
        c = Double.parseDouble(leitura.readLine());
        AVG = (a*2+b*3+c*5)/10;
        
        System.out.println("MEDIA = "+String.format("%.1f",AVG));
    }
    
}
