package zhilenkova.day4.entity;

import zhilenkova.day4.worker.AutomationEngineer;
import zhilenkova.day4.worker.Engineer;
import zhilenkova.day4.worker.TestEngineer;
//Т.к. в задаче не указано, что Function<Engineer, Result> нужно написать самим, то использую функциональный интерфейс Function<T,R>
import java.util.function.Function;

public abstract class Test implements Function<Engineer, Result> {
    private int complexity;
    private int instability;

    //getters
    public int getComplexity() {
        return complexity;
    }

    public int getInstability() {
        return instability;
    }

    //setters
    public void setComplexity(int complexity) {
        this.complexity = complexity;
    }


    public void setInstability(int instability) {
        this.instability = instability;
    }

    public Test(TestLevel testLevel) {
        this.complexity = testLevel.COMPLEXITY;
    }

    @Override
    public Result apply(Engineer engineer) {
        int anxiety;
        if ((this instanceof ManualTest && engineer instanceof AutomationEngineer) ||
                (this instanceof AutomatedTest && engineer instanceof TestEngineer))
            anxiety = engineer.getAnxiety();
        else
            anxiety = 1;
        if (complexity * instability * anxiety > 30)
            return Result.FAILED;
        else
            return Result.PASSED;
    }
}
