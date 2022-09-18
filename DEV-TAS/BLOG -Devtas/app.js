const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");

const _= require('lodash')

const homeStartingContent = "Welcome to DevTas Blog Website You Can Add your Daily Happenings in it ... It is Like your daily Diary  Just Hit Compose Above And Start adding Your daily happening"
const contactContent = "You can Contact To DevTas by your prayers";

const app = express();

let composeTexts =[];

app.set('view engine', 'ejs');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static("public"));



app.get("/", (req, res) => {
  res.render("home", { getPara: homeStartingContent , post : composeTexts });
})

app.get("/contact", (req, res) => {
  res.render('contacts' , {getContact : contactContent})
})

app.get("/about",(req,res)=>{
  res.render('about', { getAbout : aboutContent })
})

app.get("/compose",(req,res)=>{
  res.render('compose');
})

app.post("/compose",(req,res)=>{
  const post = {
    titleText : req.body.composeText,
    postText : req.body.postBody
  };
  composeTexts.push(post);
  res.redirect('/')
})

app.get('/post/:topic',(req,res)=>{
  let reqTit = _.lowerCase(req.params.topic);
  composeTexts.forEach((texts)=>{
    let orTitle = _.lowerCase(texts.titleText);
    if(reqTit === orTitle){
      res.render('post',{heading:texts.titleText , paraGraph:texts.postText})
    }else{
      console.log("Not Found");
    }
  });
})

app.listen(3000, () => {
  console.log("Server started on port 3000");
});