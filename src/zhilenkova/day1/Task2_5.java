package zhilenkova.day1;

//5. Циклически сдвинуть все элементы вправо на 2 позиции (1-й элемент станет 3-м, 2-й станет 4-м и т.д.)

import java.util.Scanner;

public class Task2_5 {
    public static void main(String[] args) {

        int [] mas1=getMas(); //Массив, который будем сдвигать
        int mas2 [] = new int[mas1.length+2];
        System.out.print("Массив  до  сдвига: ");
        shift(mas1, mas2);

    }

    private static int[] getMas() {
        Scanner input_size = new Scanner(System.in);
        System.out.println("Введите размер массива:");
        int size = input_size.nextInt();
        int[] array1 = new int[size], buffer = new int[size];
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите элементы массива через пробел: ");
        for (int i = 0; i < size; i++) {
            array1[i] = sc.nextInt();
        }
        return array1;
    }

    private static void shift(int[] mas1, int[] mas2) {
        for (int i = 0; i < mas1.length; i++) {
            System.out.print(mas1[i] + " ");
            mas2[i+2]=mas1[i];
            mas1[i]=mas2[i];
        }
        System.out.println();
        System.out.print("Массив после сдвига: ");
        for (int i : mas1) {
            System.out.print(i + " ");
        }
    }

}
