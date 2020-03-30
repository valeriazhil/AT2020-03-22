package zhilenkova.day1;

/*
Используя Collection и Stream создать из массива коллекцию,
отфильтровать оставив только четные числа,
и вывести каждое число от 2 до 20 включительно
и больше 10 в порядке по возрастанию.
 */

import java.util.*;
import java.util.stream.Collectors;

public class Task2_6 {
    public static void main(String[] args) {
        int[] mas = getMas();

        List<Integer> masList = Arrays.stream(mas).boxed().collect(Collectors.toList());
        System.out.println("Коллекция из массива: ");
        System.out.println(masList);
        System.out.println("Коллекция отфильтрованная с четными числами: ");
        System.out.println(removeOddNumbers(masList));
        System.out.println("Коллекция отфильтрованная с четными числами от 2 до 20: ");
        System.out.println(removeNumbers1(masList));
        System.out.println("Коллекция отфильтрованная больше 10 в порядке по возрастанию: ");
        System.out.println(removeNumbers2(masList));
        //Сортировка
        Collections.sort(masList);
        System.out.println(masList);
    }

    //Создание массива
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

    //Удаление нечетных
    public static List<Integer> removeOddNumbers(List<Integer> list) {
        list.removeIf(i -> i % 2 != 0);
        return list;
    }

    //Удаление всего, кроме [2,20]
    public static List<Integer> removeNumbers1(List<Integer> list) {
        list.removeIf (i ->(i > 20) || (i < 2));
        return list;
    }

    //Удаление всего, кроме [10,20]
    public static List<Integer> removeNumbers2(List<Integer> list) {
        list.removeIf (i ->(i > 20) || (i < 10));
        return list;
    }

}