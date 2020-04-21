import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import worker.AutomationEngineer;
import worker.Engineer;
import worker.TestEngineer;

import java.util.Arrays;
import java.util.Collection;

@RunWith(Parameterized.class)

public class BaseEnTest {
    private Engineer en;

    public BaseEnTest(Engineer  en) {
        this.en=en;
    }

    @Parameterized.Parameters
    public static Collection<Object[]> primeNumbers() {
        return Arrays.asList (new Object[][] {
            {new TestEngineer ()},
            {new AutomationEngineer ()}
        });
    }

    @Test
    public void verifyDefaultAnxietyByTestEngineer() {
        Assert.assertEquals("Default engineer anxiety is not correct!", 3, en.getAnxiety());
    }

    @Test
    public void verifySetAnxietyByTestEngineer() {
        en.setAnxiety(2);
        Assert.assertEquals("Engineer anxiety was set not correct!", 2, en.getAnxiety());
    }

    @Test
    public void verifyRandomSkillByAutomationEngineer() {
        Assert.assertTrue("Random engineer skill is not correct!",
                1 <= en.getSkill() && en.getSkill() <= 10);
    }

    @Test
    public void verifySetSkillByAutomationEngineer() {
        en.setSkill(2);
        Assert.assertEquals("Engineer skill was set not correct!", 2, en.getSkill());
    }
}
