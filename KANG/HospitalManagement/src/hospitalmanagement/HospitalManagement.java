/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package hospitalmanagement;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

class patients{
    String name;
    String address;
    int age;
    String sex;
    String phone;

    public patients(String name, String address, int age, String sex, String phone) {
        this.name = name;
        this.address = address;
        this.age = age;
        this.sex = sex;
        this.phone = phone;
    }
}


class hospital{
    String name;
    ArrayList<String> Doctors;
    ArrayList<patients> Patients;
    String city;
    int total_beds = 100;
    int available_beds;
    int bed_price;
    int rating;

    public hospital(String name, ArrayList<String> Doctors, ArrayList<patients> Patients, String city, int bed_price, int rating) {
        this.name = name;
        this.Doctors = Doctors;
        this.Patients = Patients;
        this.city = city;
        this.available_beds = total_beds - this.Patients.size();
        this.bed_price = bed_price;
        this.rating = rating;
    }
    
    public void printHospitalData(){
        System.out.println("Hospital Name: " + this.name);
        System.out.println("Location: "+this.city);
        System.out.println("Number of Doctors currently in this hospital: "+this.Doctors.size());
        System.out.println("Number of Patients in the hospital: "+this.Patients.size());
        System.out.println("Number of Available Beds: "+this.available_beds);
        System.out.println("Price of a Bed: "+this.bed_price);
        System.out.println("Hospital Rating: "+this.rating);
    }
    
    public void printPatientDetails(){
        System.out.println("Hospital: "+this.name);
        int i=1;
        for (patients Patient : this.Patients) {
            System.out.println("Patient Number: "+(i++));
            System.out.println("Name: "+Patient.name);
            System.out.println("Age: "+Patient.age);
            System.out.println("Sex: "+Patient.sex);
            System.out.println("Address: "+Patient.address);
            System.out.println("Phone Number: "+Patient.phone);
        }
    }
    
}
public class HospitalManagement {
    
    public static void main(String[] args) {
        int N;
        Scanner sc = new Scanner(System.in);
        ArrayList<hospital> h = new ArrayList<>();
        System.out.print("Enter the number of hospitals: ");
        N = sc.nextInt();
        for(int i=0;i<N;i++){
            System.out.print("Enter Hospital Name: ");
            String name = sc.next();
            System.out.print("Enter the number of doctors present in the hospital: ");
            int n = sc.nextInt();
            ArrayList<String> doctors = new ArrayList<>();
            for(int j=0;j<n;j++){
                System.out.print("Enter the name of "+(j+1)+" doctor: ");
                doctors.add(sc.next());
            }
            
            ArrayList<patients> pat = new ArrayList<>();
            System.out.print("Enter the number of patients: ");
            n = sc.nextInt();
            for(int j=0;j<n;j++){
                System.out.print("Enter the name of the patient: ");
                String pname = sc.next();
                System.out.print("Enter the address of the patient: ");
                String add = sc.next();
                System.out.print("Enter the age of the patient: ");
                int age=sc.nextInt();
                System.out.print("Enter the sex of the patient: ");
                String sex = sc.next();
                System.out.print("Enter the phone number of the patient: ");
                String phone = sc.next();
                pat.add(new patients(pname,add,age,sex,phone));
                
            }
            System.out.print("Enter the city of Hospital: ");
            String city = sc.next();
            System.out.print("Enter the bed price of Hospital: ");
            int bed_price = sc.nextInt();
            System.out.print("Enter the rating of Hospital: ");
            int rating = sc.nextInt();
            h.add(new hospital(name,doctors,pat,city,bed_price,rating));
        }
        int opt;
        while(true){
            
            System.out.println("Choose Option: ");
            System.out.println("1. Print Hospital Data");
            System.out.println("2. Print Patient Data");
            System.out.println("3. Sort Hospital By Name");
            System.out.println("4. Sort Hospital By Ratings");
            System.out.println("5. Sort Hospital by Beds Available");
            System.out.println("6. Sort Hospitals by Bed Pricing");
            System.out.println("7. Exit");
            
            opt = sc.nextInt();
            switch(opt){
                case 1: for(int i=0;i<h.size();i++)
                            h.get(i).printHospitalData();
                    break;
                case 2: for(int i=0;i<h.size();i++)
                            h.get(i).printPatientDetails();
                    break;
                case 3: h.sort((hospital h1,hospital h2)->h1.name.compareTo(h2.name));
                        System.out.println("Sorted by name: ");
                        for (hospital h1 : h) {
                            System.out.println("Name: "+h1.name);
                        }
                    break;
                case 4: h.sort((hospital h1,hospital h2)->h1.rating - h2.rating);
                        System.out.println("Sorted by Rating: ");
                        for(hospital h1:h){
                            System.out.println("Name: "+h1.name + " Rating: "+h1.rating);
                        }
                    break;
                case 5: h.sort((hospital h1,hospital h2)-> h1.available_beds-h2.available_beds);
                        System.out.println("Sorted by available beds: ");
                        for(hospital h1:h){
                            System.out.println("Name: "+h1.name + " Avaialable Beds: "+h1.available_beds);
                        }
                    break;
                case 6: h.sort((hospital h1,hospital h2)->h1.bed_price - h2.bed_price);
                        System.out.println("Sorted by bed Pricing: ");
                        for(hospital h1:h){
                            System.out.println("Name: "+h1.name + " Bed Pricing: "+h1.bed_price);
                        }
                    break;
                case 7: System.exit(0);
                default: System.out.println("Invalid Option");                    
            }
            
        }
    }
    
}
