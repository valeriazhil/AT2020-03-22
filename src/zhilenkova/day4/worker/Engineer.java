package zhilenkova.day4.worker;

import zhilenkova.day4.entity.Result;
import zhilenkova.day4.entity.Test;

public abstract class Engineer {
    int anxiety = 3;
    int skill;

    public int getAnxiety() {
        return anxiety;
    }

    public int getSkill() {
        return skill;
    }

    public void setSkill() {
        this.skill = (int) (1 + Math.random() * 10);
    }

    public Result executeTest(Test test) {
        return null;
    }


}