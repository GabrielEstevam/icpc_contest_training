package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1021 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        double valor;
        int i, k;
        int cedula[] = {100,50,20,10,5,2};
        double moeda[] = {1.0,0.5,0.25,0.1,0.05,0.01};
        
        valor = Double.parseDouble(leitura.readLine());
        
        System.out.println("NOTAS:");
        for (i = 0; i < 6; i++) {
            k = (int) (valor/cedula[i]);
            valor%=cedula[i];
            System.out.println(k+" nota(s) de R$ "+cedula[i]+".00");
        }
        
        System.out.println("MOEDAS:");
        k = (int) (valor/moeda[0]);
        System.out.println(k+" moeda(s) de R$ 1.00");
        valor %= moeda[0];
        k = (int) (valor / moeda[1]);
        System.out.println(k+" moeda(s) de R$ 0.50");
        valor %= moeda[1];
        k = (int) (valor / moeda[2]);
        System.out.println(k+" moeda(s) de R$ 0.25");
        valor %= moeda[2];
        k = (int) (valor / moeda[3]);
        System.out.println(k+" moeda(s) de R$ 0.10");
        valor %= moeda[3];
        k = (int) (valor / moeda[4]);
        System.out.println(k+" moeda(s) de R$ 0.05");
        valor %= moeda[4];
        k = (int) (valor / moeda[5]);
        System.out.println(k+" moeda(s) de R$ 0.01");
        valor %= moeda[5];
        System.out.println();
    }
}

