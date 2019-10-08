package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1020 {
    
    public static void main(String args[]) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int dias;
        
        dias = Integer.parseInt(leitura.readLine());
        
        System.out.println(dias/365+" ano(s)");
        dias%=365;
        System.out.println(dias/30+" mes(es)");
        dias%=30;
        System.out.println(dias+" dia(s)");
    }
}

