package zhilenkova.day3;

public class Test {
    public static void main(String[] args) {

        Engineer_mt qaM = new Engineer_mt();
        qaM.setFirstName("Lera");
        qaM.setLastName("Zhil");
        qaM.setAge(25);
        System.out.println("First Name: " + qaM.getFirstName() + " " + "Last Name: "  + qaM.getLastName() + " Age: "+ qaM.getAge());
        qaM.speak();
        qaM.executeTests();
        qaM.inventCode();

        Engineer_at qaA = new Engineer_at();
        qaA.setFirstName("Lera");
        qaA.setLastName("Zhil");
        qaA.setAge(27);
        System.out.println("First Name: " + qaA.getFirstName() + " " + "Last Name: "  + qaA.getLastName() + " Age: "+ qaA.getAge());
        qaA.speak();
        qaA.executeTests();
        qaA.inventCode();

    }
}
