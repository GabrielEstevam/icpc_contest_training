package matematica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1199 {
 
    public static void main(String[] args) throws IOException {
        
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(in);
        
        int i, k;
        String entrada, hexa = "";
        
        entrada = leitura.readLine();
        
        while (true) {
            try {
                k = Integer.parseInt(entrada);
                if (k < 0)
                    break;
                System.out.println("0x"+Integer.toString(Integer.parseInt(entrada),16).toUpperCase());
            } catch (Exception e) {
                for (i = 0; i < entrada.length()-2; i++) {
                    hexa += entrada.charAt(i+2);
                }
                System.out.println(Integer.parseInt(hexa,16));
                hexa = "";
            }
            entrada = leitura.readLine();
        }
    }
 
}