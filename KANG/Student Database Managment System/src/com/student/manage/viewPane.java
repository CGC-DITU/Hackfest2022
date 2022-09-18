
package com.student.manage;

import java.sql.ResultSet;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;

/**
 *
 * @author vinaya khandelwal
 */
public class viewPane{
    
   
    
    
    public static void viewPanel()
    {
        JFrame jf = new JFrame();
        jf.setSize(550,300);
        JPanel jp = new JPanel();
        int n = StudentEntryInDataBase.total_students();
        if(n==0)
        {
            JOptionPane.showMessageDialog(null, "NO DATA AVAILABLE");
            return;
        }
        String[][] data = new String[n][6];
        int i=0;
        try{
            ResultSet rs = StudentEntryInDataBase.output();
            while(rs.next())
            {   
                String temp[] = {Integer.toString(rs.getInt("SID")),rs.getString("SFName"),rs.getString("SLName"),Integer.toString(rs.getInt("SAge")),rs.getString("SCity"),rs.getString("SPhone_Number")};
                data[i]=temp;
                i++;
            }
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
        String col[] ={"SID","SFNAME","SLNAME","SAGE","SCITY","SPHONE_NUMBER"};
        DefaultTableModel tm = new DefaultTableModel(data,col);
        JTable jt = new JTable(tm);
        jp.add(new JScrollPane(jt));
        jp.validate();
        jp.setSize(400,200);
        
        jf.add(jp);
        jf.setVisible(true);
    }
    
}
