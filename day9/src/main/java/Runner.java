import java.sql.*;

public class Runner {
    public static void main(String[] args) throws SQLException {
        DBOperations operations = new DBOperations();
        SQLQueries queries = new SQLQueries();

        operations.deleteTable();
        operations.createTable();
        operations.addTenUsers();
        operations.loadUsers(queries.SELECT_ALL);
    }
}