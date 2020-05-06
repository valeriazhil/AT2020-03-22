public class User {
    int user_id;
    String user_login;
    String user_password;

    public User(int user_id, String user_login, String user_password) {
        this.setUser_id(user_id);
        this.setUser_login(user_login);
        this.setUser_password(user_password);
    }

    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public String getUser_login() {
        return user_login;
    }

    public void setUser_login(String user_login) {
        this.user_login = user_login;
    }

    public String getUser_password() {
        return user_password;
    }

    public void setUser_password(String user_password) {
        this.user_password = user_password;
    }

    @Override
    public String toString() {
        return "user_id = " + user_id + ", user_login = " + user_login + ", user_password = " + user_password + "}";
    }
}