package zhilenkova.day4;

import zhilenkova.day4.entity.AutomatedTest;
import zhilenkova.day4.entity.ManualTest;
import zhilenkova.day4.entity.TestLevel;
import zhilenkova.day4.worker.AutomationEngineer;
import zhilenkova.day4.worker.TestEngineer;

public class JustDoIt {
    public static void main(String[] args) {
        TestEngineer testEngineer = new TestEngineer();
        AutomatedTest automatedTest = new AutomatedTest(TestLevel.GUI,15);
        AutomationEngineer automationEngineer = new AutomationEngineer();
        ManualTest manualTest = new ManualTest(TestLevel.API, 3);

        System.out.println( " Test 1 " + manualTest.apply(automationEngineer) +
                "\n Test 2 " + automatedTest.apply(testEngineer) +
                "\n Test 3 "+ manualTest.apply(testEngineer) +
                "\n Test 4 " + automatedTest.apply(automationEngineer));

    }
}
