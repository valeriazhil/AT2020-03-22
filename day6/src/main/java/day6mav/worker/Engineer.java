package day6mav.worker;

import day6mav.entity.Result;
import day6mav.entity.TestE;

import java.util.concurrent.ThreadLocalRandom;

public abstract class Engineer {
    int anxiety = 3;
    int skill;

    public int getAnxiety() {
        return anxiety;
    }

    public void setAnxiety(int anxiety) {
        this.anxiety = anxiety;
    }

    public int getSkill() {
        return skill;
    }

    public void setSkill(int skill) {
        this.skill = skill;
    }

    public void setRandomSkill() {
        this.skill = ThreadLocalRandom.current().nextInt(1, 11);
    }

    public Result executeTest(TestE test) {
        return test.apply(this);
    }
}