import org.junit.FixMethodOrder;
import org.junit.runner.RunWith;
import org.junit.runners.MethodSorters;
import org.junit.runners.Suite;
import paramTests.ParamTestsForApply;
import paramTests.ParamTestsForSkillAndAnxiety;
import  paramTests.ParamInstability;

@RunWith(Suite.class)
@Suite.SuiteClasses({ParamTestsForApply.class, ParamTestsForSkillAndAnxiety.class, ParamInstability.class})
@FixMethodOrder(MethodSorters.NAME_ASCENDING)
public class JUnit4Runner {
}
