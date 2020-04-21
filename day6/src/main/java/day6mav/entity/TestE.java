package day6mav.entity;

import day6mav.worker.AutomationEngineer;
import day6mav.worker.Engineer;
import day6mav.worker.TestEngineer;

import java.util.function.*;

//Т.к. в задаче не указано, что Function<Engineer, Result> нужно написать самим, то использую функциональный интерфейс Function<T,R>

public abstract class TestE implements Function<Engineer, Result> {
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
        if (instability <= 0)
            this.instability = 1;
        else if (instability > 10)
            this.instability = 10;
        else
            this.instability = instability;
    }

     //класс Test должен иметь поля int complexity и int instability, которые инициализируется в конструкторе класса,
    public TestE(TestLevel testLevel, int instability) {
        this.complexity = testLevel.COMPLEXITY;
        this.setInstability(instability);
    }

    @Override
    public Result apply(Engineer engineer) {
        int anxiety;
        if ((this instanceof ManualTest && engineer instanceof AutomationEngineer) ||
                (this instanceof AutomatedTest && engineer instanceof TestEngineer))
            anxiety = engineer.getAnxiety();
        else
            anxiety = 1;
        if ((complexity * instability * anxiety) / engineer.getSkill ()> 30)
            return Result.FAILED;
        else
            return Result.PASSED;
    }
}

// Tests for apply method
// Case one if ( true || false) -> true;  if: true
// Case two if ( true || false) -> true;  if: false

// Case three if ( false || true) -> true;  if: true
// Case four if ( false || true) -> true;  if: false

// Case five if ( false || false) -> true;  if: true
// Case six if ( false || false) -> true;  if: false

