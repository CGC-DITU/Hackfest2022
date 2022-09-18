
package com.student.manage;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class StudentEntryInDataBase {
    public static boolean InsertStudent(student s)
    {
        // jdbc code...
        boolean flag = false;
       try
       {
            Connection con = cp.createC();
            
            String q ="insert into student_details(SID,SFname,SLName,SAge,SCity,SPhone_Number) values(?,?,?,?,?,?)";
            PreparedStatement pstmt = con.prepareStatement(q);
            
            // setting values of parameters
            
            pstmt.setInt(1, s.getStudent_id());
            pstmt.setString(2,s.getStudent_fname());
            pstmt.setString(3, s.getStudent_lname());
            pstmt.setInt(4, s.getStudent_age());
            pstmt.setString(5, s.getCity());
            pstmt.setString(6, s.getStudent_phone_number());
            
            // execute the query;
            pstmt.executeUpdate();
            flag = true;
            con.close();
            
       }
       catch(Exception e)
       {
           e.printStackTrace();
       }
       return flag;
    }
    
    public static boolean DeleteStudent(int sid)
    {
                // jdbc code...
        boolean flag = false;
       try
       {
            Connection con = cp.createC();
            
            String q ="delete from student_details where SID = ?";
            PreparedStatement pstmt = con.prepareStatement(q);
            
            // setting values of parameters
            pstmt.setInt(1, sid);
       
            // execute the query;
            int x = pstmt.executeUpdate();
            
            if(x>0)
                flag = true;
            con.close();
            
       }
       catch(Exception e)
       {
           e.printStackTrace();
       }
       return flag;
    }
    
    public static boolean updateRecord(int sid,String value,int opt)
    {
        boolean flag = false;
        
        try{
            Connection con = cp.createC();
            
            String q = new String();
            
            
            switch(opt)
            {
                case 0: q = "UPDATE student_details set SFName = '"+value+"' where SID = "+sid;
                        break;
                case 1: q = "UPDATE student_details set SLName = '"+value+"' where SID = "+sid;
                        break;
                case 2: q = "UPDATE student_details set SPhone_Number = '"+value+"' where SID = "+sid;
                        break;
                case 3: q = "UPDATE student_details set SCity = '"+value+"' where SID = "+sid;
                        break;
                case 4: q = "UPDATE student_details set SFName = "+value+" where SID = "+sid;
                        break;
            }
            
            PreparedStatement pstmt = con.prepareStatement(q);
            
            // executing the statment
            
            int x = pstmt.executeUpdate();
            if(x>0)
                flag=true;
            con.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        
        return flag;
    }
    
    public static ResultSet output()
    {
        ResultSet rs = null;
        try
        {
            Connection con = cp.createC();
            String q = "select * from student_details";
            PreparedStatement pstmt = con.prepareStatement(q);
            rs = pstmt.executeQuery();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        
        return rs;
    }
    
    public static int total_students()
    {
        int x=0;
        try{
            Connection con = cp.createC();
            String q = "select count(sid) from student_details";
            PreparedStatement pstmt = con.prepareStatement(q);
            ResultSet rs = pstmt.executeQuery();
            rs.next();
            x=rs.getInt(1);
            con.close();
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        return x;
    }
    
    
}
