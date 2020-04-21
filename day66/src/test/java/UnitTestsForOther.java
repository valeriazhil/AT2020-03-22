import entity.TestE;
import org.junit.Assert;
import org.junit.Test;
import worker.AutomationEngineer;
import worker.Engineer;
import worker.TestEngineer;


public class UnitTestsForOther {

    private TestE test;
    private final Engineer testEngineer = new TestEngineer ();
    private final Engineer automationEngineer = new AutomationEngineer ();


    @Test
    public void verifyDefaultAnxietyByTestEngineer() {
        Assert.assertEquals("Default engineer anxiety is not correct!", 3, testEngineer.getAnxiety());
    }

    @Test
    public void verifySetAnxietyByTestEngineer() {
        testEngineer.setAnxiety(2);
        Assert.assertEquals("Engineer anxiety was set not correct!", 2, testEngineer.getAnxiety());
    }

    @Test
    public void verifyRandomSkillByAutomationEngineer() {
        Assert.assertTrue("Random engineer skill is not correct!",
                1 <= automationEngineer.getSkill() && automationEngineer.getSkill() <= 10);
    }

    @Test
    public void verifySetSkillByAutomationEngineer() {
        automationEngineer.setSkill(2);
        Assert.assertEquals("Engineer skill was set not correct!", 2, automationEngineer.getSkill());
    }


}
