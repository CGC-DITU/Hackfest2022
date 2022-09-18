const express = require('express');
const ejs = require('ejs');
const bodyParser = require('body-parser');

const app = express();

app.set('view engine','ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('Public'));


app.get("/",(req,res)=>{
    res.render('home');
});

app.get('/ResumeBuilder',(req,res)=>{
    res.render('adddet')
});

app.post('/Final',(req,res)=>{
    const name = req.body.Name;
    const email = req.body.Email;
    const Number = req.body.number;
    const Quali = req.body.qulification;
    const technology = req.body.techs;
    const EXP = req.body.exp;
    const TEXTAREA = req.body.textarea;
    res.render('Final' , {NAME : name , EMAIL: email , NUMBER:Number , QUALIFICATIONS:Quali,TECHNOLOGIES:technology, EXP : EXP,TEXTAREA:TEXTAREA});
});

app.get('/about',(req,res)=>{
    res.render('About')
})


app.listen(3000,()=>{
    console.log("Server running at Localhost")
})