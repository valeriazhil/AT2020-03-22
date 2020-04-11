package zhilenkova.day4.test;

import zhilenkova.day4.entity.*;
import zhilenkova.day4.worker.*;
/*
import zhilenkova.day4.entity.AutomatedTest;
import zhilenkova.day4.entity.ManualTest;
import zhilenkova.day4.entity.Result;
import zhilenkova.day4.entity.TestLevel;
import zhilenkova.day4.worker.TestEngineer;
import zhilenkova.day4.worker.AutomationEngineer;
*/
import org.junit.Assert;
import org.junit.Test;



public class UnitTests {

    //для автоматизатора
    @Test
    public void automatedTestPassed() {
        AutomatedTest automatedTest = new AutomatedTest(TestLevel.API, 5);
        AutomationEngineer automationEngineer = new AutomationEngineer();
        Assert.assertEquals("Test 1. AT by automation engineer (test data: API(3), instability 5, anxiety 1:)", Result.PASSED, automatedTest.apply(automationEngineer));
    }

    @Test
    public void automatedTestFailed() {
        AutomatedTest automatedTest = new AutomatedTest(TestLevel.API, 5);
        TestEngineer testEngineer = new TestEngineer();
        Assert.assertEquals("Test 2. AT by manual engineer (test data:  API(3), instability 5, anxiety 3:)", Result.FAILED, automatedTest.apply(testEngineer));
    }

    //для мануальщика

     @Test
    public void manualTestPassed() {
        ManualTest manualTest = new ManualTest(TestLevel.UNIT, 2);
        AutomationEngineer automationEngineer = new AutomationEngineer();
        Assert.assertEquals("Test 3. MT by automation engineer (test data:  UNIT(1), instability 2, anxiety 3:)", Result.PASSED, manualTest.apply(automationEngineer));
    }

    @Test
    public void manualTestFailed() {
        ManualTest manualTest = new ManualTest(TestLevel.GUI, 4);
        TestEngineer testEngineer = new TestEngineer();
        Assert.assertEquals("Test 4. MT by manual engineer (test data:  GUI(9), instability 4, anxiety 1:)", Result.FAILED, manualTest.apply(testEngineer));
    }



}
