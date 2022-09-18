// const { on } = require('events');
const mongoose = require('mongoose');

mongoose.connect('mongodb://localHost/employee');

const db = mongoose.connection;

db.on('error' , console.error.bind(console , "error in connecting to database"));

db.once('open' , function(){
    console.log("Database is successfully working")
});