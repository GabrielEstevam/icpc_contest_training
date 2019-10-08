package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1013 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        String linha[];
        int a, b, c, maior;
        
        linha = leitura.readLine().split(" ");
        a = Integer.parseInt(linha[0]);
        b = Integer.parseInt(linha[1]);
        c = Integer.parseInt(linha[2]);
        
        maior = (a+b+Math.abs(a-b))/2;
        maior = (maior+c+Math.abs(maior-c))/2;
        
        System.out.println(maior+" eh o maior");
    }
    
}

