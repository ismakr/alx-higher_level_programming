-- creates the MySQL server user user_0d_1.
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS;
GRANT ALL ON user_0d_1 TO 'user_0d_1'@'localhost';
