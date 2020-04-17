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



public class UnitTestsForApply {

    private static zhilenkova.day4.entity.Test test;
    private static Engineer engineer;

    private static final String MSG = "Test execution for %s by %s with anxiety %s isn't correct!";

    // Tests for apply method!Reductions: m-manual, T - Test,  a - automation, E - Engineer

    // Case one if ( true || false) -> true;  if: true

    @Test
    public void mTaEFailed() {
        test = new ManualTest(TestLevel.GUI, 10);
        engineer = new AutomationEngineer();
        engineer.setSkill(2);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.FAILED, test.apply(engineer));
    }

    // Case two if ( true || false) -> true;  if: false

    @Test
    public void mTaEPassed() {
        test = new ManualTest(TestLevel.API, 10);
        engineer = new AutomationEngineer();
        engineer.setSkill(10);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.PASSED, test.apply(engineer));
    }

    // Case three if ( false || true) -> true;  if: true
    @Test
    public void aTmEFailed() {
        test = new AutomatedTest(TestLevel.GUI, 9);
        engineer = new TestEngineer ();
        engineer.setSkill(6);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.FAILED, test.apply(engineer));
    }


    // Case four if ( false || true) -> true;  if: false

    @Test
    public void aTmEPassed() {
        test = new AutomatedTest(TestLevel.API, 10);
        engineer = new TestEngineer();
        engineer.setSkill(10);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.PASSED, test.apply(engineer));
    }

    // Case five if ( false || false) -> true;  if: true
    @Test
    public void aTaEFailed() {
        test = new AutomatedTest(TestLevel.GUI, 10);
        engineer = new AutomationEngineer ();
        engineer.setSkill(5);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.PASSED, test.apply(engineer));
    }


    // Case six if ( false || false) -> true;  if: false

    @Test
    public void mTmEFailed() {
        test = new ManualTest(TestLevel.GUI, 10);
        engineer = new TestEngineer ();
        engineer.setSkill(6);
        Assert.assertEquals(String.format(MSG,
                test.getClass().getSimpleName(), engineer.getClass().getSimpleName(), engineer.getAnxiety()),
                Result.PASSED, test.apply(engineer));
    }




    /*Testing class Test (setInstability method)
    if1(true) */
    @Test
    public void InstabilityT(){
        test = new ManualTest(TestLevel.GUI, 0);
        Assert.assertEquals(1, test.getInstability());
    }
    //if1(false) else if2(true)
    @Test
    public void InstabilityFT(){
        test = new ManualTest(TestLevel.GUI, 15);
        Assert.assertEquals(10, test.getInstability());
    }

    //if1(false) else if2(false)
    @Test
    public void InstabilityFF(){
        test = new ManualTest(TestLevel.GUI, 8);
        Assert.assertEquals(8, test.getInstability());
    }


}
