let display = document.getElementById('display');
// Array.from function converts the HTML Collection into an array
let buttons = Array.from(document.getElementsByClassName('btn'));
console.log(buttons);

// We will map through our buttons array and apply a click event listener to every button in our array

buttons.map(button =>{
    button.addEventListener('click',(e)=>{
        switch(e.target.innerText){
                case 'C':
                display.innerText = '';
                break;

                case '←':
                    display.innerText = display.innerText.slice(0,-1);
                    break;

                case '=':
                try{
                    display.innerText = eval(display.innerText);
                }catch{
                    display.innerText = "Invalid"
                }
                break;


                case 'C':
                    display.innerText = '';
                    break;

            default :
            display.innerText += e.target.innerText;
        }
    });
})