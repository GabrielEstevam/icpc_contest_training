package matematica;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;

public class p1169 {
 
    public static void main(String[] args) throws IOException {
 
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int instancias, casas, i, j;
        BigInteger pow = new BigInteger("1");
        BigInteger sum = new BigInteger("0");
        BigInteger two = new BigInteger("2");
        BigInteger one = new BigInteger("1");
        BigInteger zero = new BigInteger("0");
        BigInteger twelve_thousand = new BigInteger("12000");
        
        instancias = Integer.parseInt(leitura.readLine());
        for (i = 0; i < instancias; i++) {
            casas = Integer.parseInt(leitura.readLine());
            for (j = 0; j < casas; j++) {
                sum = sum.add(pow);
                pow = pow.multiply(two);
            }
            sum = sum.divide(twelve_thousand);
            System.out.println(sum.toString()+" kg");
            pow = one;
            sum = zero;
        }
        
 
    }
 
}