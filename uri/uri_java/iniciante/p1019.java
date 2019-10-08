package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1019 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int segundos, i, k;
        int hora_minuto[] = {3600,60};
        
        segundos = Integer.parseInt(leitura.readLine());
        
        for (i = 0; i < 2; i++) {
            k = segundos/hora_minuto[i];
            segundos%=hora_minuto[i];
            System.out.print(k+":");
        }
        System.out.println(segundos);
    }
}

