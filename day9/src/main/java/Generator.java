import java.util.Random;
import java.util.stream.Collectors;

public class Generator {
    private static int leftLimit = 48;
    private static int rightLimit = 122;

    public String loginGenerator() {
        return new Random().ints(leftLimit, rightLimit).filter(i -> (i <= 57 || i >= 65) && (i <= 90 || i >= 97))
                .limit(5).mapToObj(i -> String.valueOf((char) i))
                .collect(Collectors.joining());
    }

    public String pwdGenerator() {
        return new Random().ints(leftLimit, rightLimit).filter(i -> (i <= 57 || i >= 65) && (i <= 90 || i >= 97))
                .limit(40).mapToObj(i -> String.valueOf((char) i))
                .collect(Collectors.joining());
    }


}
