const express = require("express");
const path = require('path');
const port = 8800;


const app = express();

const db = require('./config/mongoose');
const employee = require('./models/Schema');

app.set('view engine' , 'ejs');
app.set('views', path.join(__dirname, 'views'));

app.use(express.urlencoded());
app.use(express.static('assets'));

var empId = [
    {
        name : "shashank",
        age : '19',
        ph : '3464377745',
        email : "a@gmail.com",
        city : 'surat'
    },

    {
        name : "sankha",
        age : '21',
        ph : '2464377745',
        email : "b@gmail.com",
        city : 'silliguri'
    },

    {
        name : "nilay",
        age : '29',
        ph : '3564377745',
        email : "c@gmail.com",
        city : 'delhi'
    },
];

app.get('/team' , function(req , res){
        
    employee.find({} , function(err , allemp){
        if(err)
        {
            console.log("error is occuring");
            return;
        }

        return res.render('details' , 
        {
            title : "Employee-Managment" ,
            empId : allemp
        });
    });
});

app.post('/enter-detail' , function(req , res){

    employee.create({
        name : req.body.name,
        age : req.body.age,
        ph : req.body.ph,
        email : req.body.email,
        city : req.body.city
    } , function(err , alemp){
        if(err)
        {
            console.log("error while fetching data");
            return;
        }
        console.log("_________" , alemp);
        return res.redirect('back');
    });

});


app.listen(port , function(err){
    if(err)
    {
        console.log("ERROR :( ");
        return;
    }
    console.log(`server is successfully working on port ${port} `);
});

app.get('/delete' , function(req,res){
    let id = req.query.id;

    employee.findByIdAndDelete(id , function(err){
        if(err)
        {
            console.log("Error while deleting data :(");
            return;
        }
        return res.redirect('back');
    })
})