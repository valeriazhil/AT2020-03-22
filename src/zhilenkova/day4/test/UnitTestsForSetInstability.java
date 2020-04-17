package zhilenkova.day4.test;

import zhilenkova.day4.entity.*;
import org.junit.Assert;
import org.junit.Test;



public class UnitTestsForSetInstability {

    private static zhilenkova.day4.entity.Test test;
    private static final String MSG = "Test instability is not correct!";

    //Case one if(true)-> instability=1
    @Test
    public void instabilityOne() {
        test = new ManualTest(TestLevel.GUI, 0);
        Assert.assertEquals( MSG, 1, test.getInstability () );
    }

    //Case one if(false)-> if (true) -> instability=10
    @Test
    public void instabilityTen() {
        test = new ManualTest(TestLevel.GUI, 16);
        Assert.assertEquals( MSG,10, test.getInstability () );
    }

    //Case three if(false)-> if (false)-> if (true) instability=instability
    @Test
    public void instabilityEquallyInstability() {
        test = new ManualTest(TestLevel.GUI, 5);
        Assert.assertEquals( MSG, 5, test.getInstability () );
    }

}
