import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBOperations {
    static Generator lpgenerator = new Generator();
    static SQLQueries sqlQueries = new SQLQueries();
    static Connect connect = new Connect();

    public void addTenUsers() throws SQLException {
        PreparedStatement statement = connect.statement(sqlQueries.ADD_USER);
        for (int i = 0; i < 10; i++) {
            statement.setString(1, lpgenerator.loginGenerator());
            statement.setString(2, lpgenerator.pwdGenerator());
            statement.executeUpdate();
        }
    }

    public void deleteTable() throws SQLException {
        PreparedStatement statement = connect.connectDB().prepareStatement(sqlQueries.DELETE_TABLE);
        statement.executeUpdate();
    }

    public void createTable() throws SQLException {
        PreparedStatement statement = connect.statement(sqlQueries.CREATE_TABLE);
        statement.executeUpdate();
    }

    public void loadUsers(String query) {
        List<User> users = new ArrayList<>();
        try {
            ResultSet rs = connect.resultSet(query);
            while (rs.next()) {
                users.add(new User(rs.getInt(1), rs.getString(2), rs.getString(3)));
            }
        } catch (SQLException ex) {
            ex.printStackTrace();
        }
        users.forEach(user -> System.out.println(user.toString()));
    }
}