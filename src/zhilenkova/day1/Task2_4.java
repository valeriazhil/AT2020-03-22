package zhilenkova.day1;

//4. Пройти по массиву и поменять местами каждые 2 соседних элемента.

import java.util.Scanner;

public class Task2_4 {
    public static void main(String[] args) {

        int[] mas = getMas();
        swapPairs(mas);
        printArray(mas);

    }

    private static int[] getMas() {
        int size;
        Scanner input_size = new Scanner(System.in);
        System.out.print("Введите размер массива: ");
        size = input_size .nextInt();
        int[]  mas= new int[size];
        for (int i = 0; i < mas.length; i++) {
            mas[i] = ((int)(Math.random() * 30));
            System.out.printf(mas[i] + " ");
        }
        return mas;
    }

    public static void swapPairs(int[] mas){
        System.out.println('\n' +"Перестановка массива по парам: ");
        int len=mas.length;
        if(len%2 ==0){
            for(int i=0; i<len; i=i+2){
                int c=mas[i]+mas[i+1];
                mas[i]=c-mas[i];
                mas[i+1]=c-mas[i+1];
            }
        }
        if(len%2 !=0){
            for(int j=0; j<len-1; j=j+2){
                int c=mas[j]+mas[j+1];
                mas[j]=c-mas[j];
                mas[j+1]=c-mas[j+1];
            }
            mas[len-1]=mas[len-1];
        }
    }

    public static void printArray(int[] mas){
        int len=mas.length;
        for(int i=0;i<len;i++)
            System.out.print(mas[i]+" ");
    }
}
