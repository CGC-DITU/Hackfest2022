const express = require('express');
const ejs = require('ejs');
const bodyParser = require('body-parser');


const app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

let employees = [
    {
        Name: "Aditya Singh",
        _id: 001,
        Designation: "SDE1",
        Experience: 5,
        Age: 26
    },
    {
        Name: "Harsheet Sharma",
        _id: 002,
        Designation: "SDE1",
        Experience: 5,
        Age: 26
    }
]


app.get('/', (req, res) => {
    res.render('home')
});




app.get('/addEmp', (req, res) => {
    res.render('newEmp');
});

app.post('/addEmp', (req, res) => {
    let name = req.body.name;
    let id = req.body.id;
    let designation = req.body.desig;
    let experience = req.body.exp;
    let age = req.body.age;

    employees.push({
        Name: name,
        _id: id,
        Designation: designation,
        Experience: experience,
        Age: age

    });
    res.render('Final', { getData: employees })
});

app.get('/delEmp', (req, res) => {
    res.render('delete')
})

app.post('/delEmp', (req, res) => {
    const getEmpId = req.body.id;
    let j = 0
    employees.forEach((employee) => {
        j = j + 1;
        if (employee._id === getEmpId) {
            employees.splice(j - 1, 1)
        }
    });
    res.render('Final', { getData: employees });
});

app.get('/modifyEmp', (req, res) => {
    res.render('Update')
})

app.post("/modifyEmp", (req, res) => {
    const getEMPId = req.body.EMPId;
    const getEMPName = req.body.EMPName;
    const getEMPDesig = req.body.EMPPost;

    var j = 0;
    employees.forEach((employee) => {
        j = j + 1;
        if (employee.empId === getEMPId) {
            (employee.empName = getEMPName),
                (employee.empDesig = getEMPDesig)
        }
    });
    res.render('Final', { getData: employees });
});




app.listen(3000, () => {
    console.log("running on Localhost 3000")
});