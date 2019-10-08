package matematica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.*;

public class p1512 {
 
    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        String linha[];
        int a, b, n;
        
        linha = leitura.readLine().split(" ");
        n = Integer.parseInt(linha[0]);
        a = Integer.parseInt(linha[1]);
        b = Integer.parseInt(linha[2]);
        while (a != 0) {
            System.out.println(String.format("%.0f", Math.floor(n/a) + Math.floor(n/b) - Math.floor(n/MMC(a,b))));        
            
            linha = leitura.readLine().split(" ");
            n = Integer.parseInt(linha[0]);
            a = Integer.parseInt(linha[1]);
            b = Integer.parseInt(linha[2]);
        }
    }
    
    static int MMC (int a, int b) {
        BigInteger A = new BigInteger(""+a);
        BigInteger B = new BigInteger(""+b);
        BigInteger AB = A.multiply(B);
        BigInteger MMC = new BigInteger(""+euclides(a,b));
        MMC = AB.divide(MMC);
        return Integer.parseInt(""+MMC.toString());
    }

    static int euclides(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return euclides(b, a%b);
        }
    }
 
}