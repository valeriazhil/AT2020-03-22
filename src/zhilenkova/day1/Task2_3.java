package zhilenkova.day1;

//3. Используя for вывести каждое четное число от 2 до 20 включительно и больше 10.

public class Task2_3 {
    public static void main(String[] args) {
        System.out.println("Четные числа от 2 до 20:");
        for (int i = 2; i <= 20; i = i+2){
            System.out.printf(i + " ");
        }

        System.out.println('\n' +  "Четные числа от 2 до 20 и больше 10:");
        for (int i = 2; i <= 20; i = i+2){
            if (i>12) {
                System.out.printf(i + " ");}
        }
    }
}
