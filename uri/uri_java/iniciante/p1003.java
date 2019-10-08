package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 *
 * @author Gabriel Estevam
 */
public class p1003 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int a, b;
        a = Integer.parseInt(leitura.readLine());
        b = Integer.parseInt(leitura.readLine());
    
        System.out.println("SOMA = "+(a+b));
    }
}
