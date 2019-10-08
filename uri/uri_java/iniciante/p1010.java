package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1010 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        String item[][] = new String[2][3];
        String linha;
        Double total;
        
        linha = leitura.readLine();
        item[0] = linha.split(" ");
        linha = leitura.readLine();
        item[1] = linha.split(" ");
        
        total = Double.parseDouble(item[0][1])*Double.parseDouble(item[0][2]) + Double.parseDouble(item[1][1])*Double.parseDouble(item[1][2]);
        
        System.out.println("VALOR A PAGAR: R$ "+String.format("%.2f", total));
    }
    
}
