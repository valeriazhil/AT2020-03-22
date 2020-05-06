import java.sql.*;

public class Connect {
    private final String url = "jdbc:mysql://localhost:3306/megaapp" +
            "?verifyServerCertificate=false" +
            "&useSSL=false" +
            "&requireSSL=false" +
            "&useLegacyDatetimeCode=false" +
            "&amp" +
            "&serverTimezone=UTC";

    public Connection connectDB() throws SQLException {
        Connection connection = DriverManager.getConnection(url, "root", "");
        return connection;
    }

    public PreparedStatement statement(String query) throws SQLException {
        PreparedStatement statement = connectDB().prepareStatement(query);
        return statement;
    }

    public ResultSet resultSet (String query) throws SQLException {
        Statement statement = connectDB().createStatement();
        ResultSet resultSet = statement.executeQuery(query);
        return resultSet;
    }
}