package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1016 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int km;
        
        km = Integer.parseInt(leitura.readLine());
        
        System.out.println((km*2)+" minutos");
    }
    
}
