const express = require('express');
const ejs = require('ejs');
const bodyParser = require('body-parser');

const app = express();

app.set('view engine','ejs');
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('public'));


app.get('/',(req,res)=>{
    res.render('home')
});


app.get('/next',(req,res)=>{
    res.render('next')
});

app.get('/theater',(req,res)=>{
    res.render('theater')
});

app.get('/PVR',(req,res)=>{
    res.render('pvr')
});

app.get('/timings',(req,res)=>{
    res.render('timings')
});

app.get('/tickets',(req,res)=>{
    res.render('BookPvr')
});

app.post('/success',(req,res)=>{
    const Name = req.body.name;
    const Email = req.body.email;
    const Number = req.body.number;
    const Time = req.body.time;
    const seat = req.body.seat;
    const TotSeat = req.body.totSeat;
    const bill = seat*TotSeat;
    res.render('Success' ,{name:Name , number: Number,email:Email ,details: Time,price:bill});
});

app.get('/INOX',(req,res)=>{
    res.render('inox')
});

app.get('/timingInox',(req,res)=>{
    res.render('timingsInox')
});

app.get('/Bookinox',(req,res)=>{
    res.render('Bookinox');
});

app.post('/success',(req,res)=>{
    const Name = req.body.name;
    const Email = req.body.email;
    const Number = req.body.number;
    const Time = req.body.time;
    const seat = req.body.seat;
    const TotSeat = req.body.totSeat;
    const bill = seat*TotSeat;
    res.render('Success' ,{name:Name , number: Number,email:Email ,details: Time,price:bill});
});

app.listen(3000,(req,res)=>{
    console.log("Running Successfully")
});