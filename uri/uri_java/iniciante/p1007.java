package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1007 {

    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int a, b, c, d, DIFERENCA;
        a = Integer.parseInt(leitura.readLine());
        b = Integer.parseInt(leitura.readLine());
        c = Integer.parseInt(leitura.readLine());
        d = Integer.parseInt(leitura.readLine());
        DIFERENCA = (a*b-c*d);
        
        System.out.println("DIFERENCA = "+DIFERENCA);
    }
    
}
