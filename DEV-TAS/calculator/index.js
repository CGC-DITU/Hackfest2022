let scr = document.getElementById('sc');
buttons = document.querySelectorAll('button');
let sv = '';
for (item of buttons) {
    item.addEventListener('click', (e) => {
        buttonText = e.target.innerText;
        console.log('Button text is ', buttonText);
        
        if (buttonText == 'C') {
            sv = "";
            scr.value = sv;
        }
        else if (buttonText == 'Sin') {
            scr.value = Math.sin(sv);
        }
        else if (buttonText == 'Cos') {
            scr.value = Math.cos(sv);
        }
        else if (buttonText == 'Log') {
            scr.value = Math.log(sv);
        }
        else if (buttonText == 'Log') {
            scr.value = Math.log(sv);
        }
        else if (buttonText == 'exp') {
            scr.value = Math.exp(sv);
        }
        else if (buttonText == 'tan') {
            scr.value = Math.tan(sv);
        }
        else if (buttonText == '=') {
            scr.value = eval(sv);
        }
        
        else {
            sv += buttonText;
            scr.value = sv;
        }

    })
}

