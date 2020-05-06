public class SQLQueries {
    public final String SELECT_ALL = "select * from users";
    public final String ADD_USER = "INSERT INTO users (user_login, user_password) VALUES (?, ?)";
    public final String DELETE_TABLE = "drop table if exists users";
    public final String CREATE_TABLE = "create table users (user_id int not null auto_increment, user_login varchar(255), user_password char(40), primary key (user_id))";
}