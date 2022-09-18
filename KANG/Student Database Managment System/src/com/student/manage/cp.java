
package com.student.manage;

import java.sql.Connection;
import java.sql.DriverManager;

public class cp {
    
    public static Connection con;
    
    public static Connection createC()
    {
        try{
            // load the driver
            Class.forName("com.mysql.jdbc.Driver");
            
            // create the connection
            String user = "root";
            String password = "Loma7860907!@#";
            String url = "jdbc:mysql://localhost:3306/student_manager?useSSL=false";
            
            con = DriverManager.getConnection(url, user, password);
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        return con;
    }
}
