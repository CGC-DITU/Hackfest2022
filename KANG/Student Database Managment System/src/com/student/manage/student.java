package com.student.manage;

public class student {
    private int student_id;
    private String student_fname;
    private String student_lname;
    private int student_age;
    private String student_phone_number;
    private String city;
    
    static int sid=0;
     public student()
     {
         super();
     }

    public int getStudent_id() {
        return student_id;
    }

    public String getStudent_fname() {
        return student_fname;
    }

    public String getStudent_lname() {
        return student_lname;
    }

    public int getStudent_age() {
        return student_age;
    }

    public String getStudent_phone_number() {
        return student_phone_number;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    
    public void setStudent_id(int student_id) {
        this.student_id = student_id;
    }

    public void setStudent_fname(String student_fname) {
        this.student_fname = student_fname;
    }

    public void setStudent_lname(String student_lname) {
        this.student_lname = student_lname;
    }

    public void setStudent_age(int student_age) {
        this.student_age = student_age;
    }

    public void setStudent_phone_number(String student_phone_number) {
        this.student_phone_number = student_phone_number;
    }

    public student(int student_id, String student_fname, String student_lname, int student_age, String student_phone_number, String city) {
        super();
        this.student_id = student_id;
        this.student_fname = student_fname;
        this.student_lname = student_lname;
        this.student_age = student_age;
        this.student_phone_number = student_phone_number;
        this.city = city;
    }

    public student(String student_fname, String student_lname, int student_age, String student_phone_number, String city) {
        super();
        this.student_id = sid;
        sid++;
        this.student_fname = student_fname;
        this.student_lname = student_lname;
        this.student_age = student_age;
        this.student_phone_number = student_phone_number;
        this.city = city;
    }

    
    @Override
    public String toString() {
        return "student{" + "student_id=" + student_id + ", student_fname=" + student_fname + ", student_lname=" + student_lname + ", student_age=" + student_age + ", student_phone_number=" + student_phone_number + '}';
    }
    
    
}
