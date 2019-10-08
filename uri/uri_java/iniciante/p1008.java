package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class p1008 {

    public static void main(String[] args) throws IOException {
        InputStreamReader entrada = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(entrada);
        
        int numero_funcionario, horas;
        double valor_hora, salario;
        numero_funcionario = Integer.parseInt(leitura.readLine());
        horas = Integer.parseInt(leitura.readLine());
        valor_hora = Double.parseDouble(leitura.readLine());
        salario = horas*valor_hora;
        
        System.out.println("NUMBER = "+numero_funcionario);
        System.out.println("SALARY = U$ "+String.format("%.2f", salario));
    }
    
}
