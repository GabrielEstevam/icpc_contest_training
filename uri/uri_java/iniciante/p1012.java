package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1012 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        String linha[];
        Double a, b, c;
        
        linha = leitura.readLine().split(" ");
        a = Double.parseDouble(linha[0]);
        b = Double.parseDouble(linha[1]);
        c = Double.parseDouble(linha[2]);
        
        System.out.println("TRIANGULO: "+String.format("%.3f",((a*c)/2)));
        System.out.println("CIRCULO: "+String.format("%.3f",(3.14159*Math.pow(c,2))));
        System.out.println("TRAPEZIO: "+String.format("%.3f",(((a+b)*c)/2)));
        System.out.println("QUADRADO: "+String.format("%.3f",(b*b)));
        System.out.println("RETANGULO: "+String.format("%.3f",(a*b)));
    }
    
}
