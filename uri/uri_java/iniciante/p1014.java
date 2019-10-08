package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1014 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int km;
        double litros, consumo;
        
        km = Integer.parseInt(leitura.readLine());
        litros = Double.parseDouble(leitura.readLine());
        consumo = km/litros;
        
        System.out.println(String.format("%.3f",consumo)+" km/l");
    }
    
}
