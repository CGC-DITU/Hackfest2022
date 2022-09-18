var candidates = [];
function checkIDPass(){
    var username = document.getElementById('user').value;
    var password = document.getElementById('pass').value;
    if(username==="guest" && password ==="123"){
        window.location.href = "admin.html";
        alert("Login Successful");
        return false;
    }
    else
        alert("Wrong ID PASS");
};

function recordCandidate(){
    let candidate = {
        fname: document.getElementById('fname').value,
        lname: document.getElementById('lname').value,
        pname: document.getElementById('pname').value
    }
    candidates.push(candidate);
    alert("Candidate added successfully");
    document.getElementById('fname').value = "";
    document.getElementById('lname').value = "";
    document.getElementById('pname').value = "";
    localStorage.setItem('myCan',JSON.stringify(candidates));
}

  
  
  
  var question = "VOTE FOR THE RIGHT CANDIDATE"
  
  var table = document.getElementById("table");
  document.getElementById("question").innerText = question;
  var arr = localStorage.getItem('myCan');
  candidates = JSON.parse(arr);
  updateOptions(candidates);
  
  function updateOptions(options){
    options.forEach(item => {
    // Create row
    var row = document.createElement("div");
    row.classList.add("tr");
    
    // Create cells
    var cell1 = document.createElement("div");
    cell1.classList.add("td");
    cell1.classList.add("check");
    cell1.innerHTML = "<i class='far fa-square'></i>";
    
    var cell2 = document.createElement("div");
    cell2.classList.add("td");
    cell2.innerText = item.fname;
    
    var cell3 = document.createElement("div");
    cell3.classList.add("td");
    cell3.innerText = item.lname;

    var cell4 = document.createElement("div");
    cell4.classList.add("td");
    cell4.innerText = item.pname;
    
    // Append cells to row
    row.appendChild(cell1);
    row.appendChild(cell2);
    row.appendChild(cell3);
    row.appendChild(cell4);
    
    // Append row to table
    table.appendChild(row);
  })
  }
  
  var rows = document.getElementsByClassName("tr");
  for(i = 0; i < rows.length; i++){
    rows[i].addEventListener("click", function(e){
      var active = document.querySelector(".tr.active");
      if(active){
        active.classList.remove("active");
      }
      
      this.classList.add("active");
      
      document.getElementById("vote").classList.add("shown");
    })
  }
  
  document.getElementById("vote").addEventListener("click", function(e){
    this.classList.add("loading");
    
    var choice = document.querySelector(".tr.active .td:nth-child(2)").innerText;
    setTimeout(() => {
      document.getElementById("content").innerHTML = `<h1>You chose ${choice}.</h1><h2>Thank you for voting!</h2><button class="shown">Results <i class='fas fa-arrow-left'></i></button>`;
    }, 1000);
  })