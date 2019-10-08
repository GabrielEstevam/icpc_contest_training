package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1017 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int tempo, velocidade;
        double litros;
        
        tempo = Integer.parseInt(leitura.readLine());
        velocidade = Integer.parseInt(leitura.readLine());
        litros = (tempo*velocidade)/12.0;
        
        System.out.println(String.format("%.3f",litros));
    }
    
}

