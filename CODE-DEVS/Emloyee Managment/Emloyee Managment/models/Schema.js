const mongoose = require('mongoose');

const eSchema = new mongoose.Schema({
    name :{
        type: String,
        required : true
    },

    age :{
        type: String,
        required : true
    },

    ph :{
        type: String,
        required : true
    },

    email :{
        type: String,
        required : true
    },

    city :{
        type: String,
        required : true
    },
});

const employee = mongoose.model('employee' , eSchema);

module.exports = employee;