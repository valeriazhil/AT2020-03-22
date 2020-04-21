package mytest;

import org.junit.Assert;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;

import java.util.Arrays;
import java.util.Collection;


@RunWith(Parameterized.class)

public class ParamApply {
    private Engineer en;
    private TestE test;
    private int skill;
    private Result expected;


    public ParamApply(Engineer en, int skill, TestE test, Result expected) {
        this.en=en;
        this.test=test;
        this.skill=skill;
        this.expected=expected;
    }

    @Parameterized.Parameters
    public static Collection<Object[]> primeNumbers() {
        return Arrays.asList (new Object[][] {
                {new TestEngineer (), 1, new ManualTest (TestLevel.UNIT,5), Result.PASSED},
                {new TestEngineer (), 10, new ManualTest (TestLevel.UNIT,5), Result.PASSED},
                {new TestEngineer (), 1, new ManualTest (TestLevel.API,9), Result.PASSED},
                {new TestEngineer (), 10, new ManualTest (TestLevel.API,9), Result.PASSED},


                {new TestEngineer (), 1, new AutomatedTest (TestLevel.API,1), Result.PASSED},
                {new TestEngineer (), 10, new AutomatedTest (TestLevel.API,1), Result.PASSED},
                {new TestEngineer (), 1, new AutomatedTest (TestLevel.GUI,8), Result.FAILED},
                {new TestEngineer (), 10, new AutomatedTest (TestLevel.GUI,8), Result.PASSED}
        });
    }

    @Test
    public void verifyExecuteTest () {
        en.setSkill (skill);
        Assert.assertEquals ("Hah", expected, en.executeTest(test));
    }
    }

