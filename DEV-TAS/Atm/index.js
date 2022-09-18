
        function withd(){
            if(document.getElementById("bt1").value < 50000 - document.getElementById("bt").value){
            alert("Transaction successful")
         return document.getElementById("bt1").value = 50000 - document.getElementById("bt").value}
        
        else{
            alert("Transaction Failed")
        }
    }
   
        function depos(){
            if (document.getElementById("bt4").value<0) {
                alert("Transaction Failed")
            }
            alert("Transaction successful")
            return document.getElementById("bt2").value = 50000 + document.getElementById("bt4").value
        }