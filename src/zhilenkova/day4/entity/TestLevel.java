package zhilenkova.day4.entity;

public enum TestLevel {
    UNIT(1),
    API(3),
    GUI(9);
    public int COMPLEXITY;

    TestLevel(int complexity) {
        this.COMPLEXITY=complexity;
    }
}