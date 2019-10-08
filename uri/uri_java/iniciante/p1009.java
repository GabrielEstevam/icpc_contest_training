package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1009 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        double vendas, salario, total;
        String nome;
        nome = leitura.readLine();
        salario = Double.parseDouble(leitura.readLine());
        vendas = Double.parseDouble(leitura.readLine());
        total = salario + vendas*0.15;
        
        System.out.println("TOTAL = R$ "+String.format("%.2f", total));
    }
    
}
