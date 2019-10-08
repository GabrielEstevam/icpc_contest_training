package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1018 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int valor, i, k;
        int cedula[] = {100,50,20,10,5,2,1};
        
        valor = Integer.parseInt(leitura.readLine());
        System.out.println(valor);
        
        for (i = 0; i < 7; i++) {
            k = valor/cedula[i];
            valor%=cedula[i];
            System.out.println(k+" nota(s) de R$ "+cedula[i]+",00");
        }
    }
}

