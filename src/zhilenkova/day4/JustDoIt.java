package zhilenkova.day4;

import zhilenkova.day4.entity.AutomatedTest;
import zhilenkova.day4.entity.ManualTest;
import zhilenkova.day4.entity.TestLevel;
import zhilenkova.day4.worker.AutomationEngineer;
import zhilenkova.day4.worker.TestEngineer;

public class JustDoIt {
    public static void main(String[] args) {

        TestEngineer testEngineer = new TestEngineer();
        AutomatedTest automatedTest = new AutomatedTest(TestLevel.GUI,1);
        AutomationEngineer automationEngineer = new AutomationEngineer();
        ManualTest manualTest = new ManualTest(TestLevel.API, 5);
        System.out.println(automatedTest.apply(testEngineer) +
                " | " + manualTest.apply(automationEngineer) +
                " | " + manualTest.apply(testEngineer));

    }
}
