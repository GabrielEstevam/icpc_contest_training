package estruturas_e_bibliotecas;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class celula {
    int valor = 0;
    celula  ant = null;
    celula  seg = null;
}

public class p1110 {
 
    public static void main(String[] args) throws IOException {
 
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader leitura = new BufferedReader(input);
        
        int entrada;
        celula topo = null;
        boolean flag = true;

        entrada = Integer.parseInt(leitura.readLine());
        while (entrada != 0) {
            topo = cria_lista(entrada);
            System.out.print("Discarded cards:");
            if (topo != null) {
                while (topo != topo.ant) {
                    if (flag) {
                        System.out.print(" " + topo.valor);
                        flag = false;
                    } else {
                        System.out.print(", " + topo.valor);
                    }
                    topo = removerCelula(topo);
                    if (topo != null)
                        topo = topo.seg;
                }
            }
            System.out.println();
            if (topo != null)
                System.out.print("Remaining card: " + topo.valor);
            System.out.println();
            flag = true;
            entrada = Integer.parseInt(leitura.readLine());
        }
    
    }
    
    static celula cria_lista (int tamanho) {
        celula lista = null;
        int i;
        for (i = 1; i <= tamanho; i++) {
            lista = inserirCelula(lista, tamanho-i+1);
        }
        return lista;
    }

    static celula inserirCelula (celula lista, int numero) {
        /* Inseri no inicio */
        celula nova = new celula();
        nova.valor = numero;
        if (lista == null) {
            nova.ant = nova;
            nova.seg = nova;
        } else {
            nova.seg = lista;
            nova.ant = lista.ant;
            lista.ant.seg = nova;
            lista.ant = nova;
        }
        return nova;
    }

    static celula removerCelula (celula Celula) {
        celula aux = Celula;
        if (Celula != null) {
            Celula.ant.seg = Celula.seg;
            Celula.seg.ant = Celula.ant;
            aux = aux.seg;
        }
        return aux;
    }
 
}