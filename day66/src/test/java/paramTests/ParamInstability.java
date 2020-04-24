package paramTests;

import entity.AutomatedTest;
        import entity.ManualTest;
        import entity.TestLevel;
        import org.junit.Assert;
        import org.junit.Test;
        import org.junit.runner.RunWith;
        import org.junit.runners.Parameterized;

        import java.util.Arrays;
        import java.util.Collection;

@RunWith(Parameterized.class)
public class ParamInstability {
    private final entity.TestE test;
    private final int expected;

    public ParamInstability(entity.TestE test, int expected) {
        this.test = test;
        this.expected = expected;
    }

    @Parameterized.Parameters
    public static Collection<Object[]> primeNumbers() {
        return Arrays.asList(new Object[][]{
                {new ManualTest(TestLevel.UNIT, 0), 1},
                {new ManualTest(TestLevel.API, 1), 1},
                {new AutomatedTest(TestLevel.API, 10), 10},
                {new AutomatedTest(TestLevel.GUI, 11), 10},
        });
    }

    @Test
    public void verifyInstability() {
        Assert.assertEquals("Test instability is not correct!", expected, test.getInstability());
    }
}
