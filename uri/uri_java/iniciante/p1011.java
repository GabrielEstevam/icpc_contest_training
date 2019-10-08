package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1011 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        Double raio, volume;
        
        raio = Double.parseDouble(leitura.readLine());
        volume = (4.0/3)*3.14159*Math.pow(raio,3);
        
        System.out.println("VOLUME = "+String.format("%.3f", volume));
    }
    
}
