package matematica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1193 {
 
    public static void main(String[] args) throws IOException {
 
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(in);
        
        int instancias, i;
        String entrada[];
        
        instancias = Integer.parseInt(leitura.readLine());
        for (i = 0; i < instancias; i++) {
            entrada = leitura.readLine().split(" ");
            System.out.println("Case "+(i+1)+":");
            if (entrada[1].charAt(0) == 'b') {
                // Binary
                System.out.println(Long.parseLong(entrada[0],2)+" dec");
                System.out.println(Long.toString(Long.parseLong(entrada[0],2),16)+" hex");
            } else if (entrada[1].charAt(0) == 'd') {
                // Decimal
                System.out.println(Long.toHexString(Long.parseLong(entrada[0]))+" hex");
                System.out.println(Long.toBinaryString(Long.parseLong(entrada[0]))+" bin");
            } else {
                // Hexa
                System.out.println(Long.toString(Long.parseLong(entrada[0],16))+" dec");
                System.out.println(Long.toString(Long.parseLong(entrada[0],16),2)+" bin");
            }
            System.out.println();
        }
    
    }
 
}