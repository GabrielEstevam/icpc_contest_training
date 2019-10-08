package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1015 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        String linha1[];
        String linha2[];
        Double x1, y1, x2, y2, d;
        
        linha1 = leitura.readLine().split(" ");
        linha2 = leitura.readLine().split(" ");
        x1 = Double.parseDouble(linha1[0]);
        y1 = Double.parseDouble(linha1[1]);
        x2 = Double.parseDouble(linha2[0]);
        y2 = Double.parseDouble(linha2[1]);
        d = Math.sqrt(Math.pow(x2-x1,2)+Math.pow(y2-y1,2));
        
        System.out.println(String.format("%.4f",d));
    }
    
}
