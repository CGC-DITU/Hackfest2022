
const calc = document.getElementById("calc");
const ctx = calc.getContext("2d");
ctx.fillStyle = "rgb(51, 51, 51)";
ctx.fillRect(0, 0, 600, 400);
let s = "";
const dis = {
 x : 0,
 y : 0,
 wd : 500,
 ht : 200
};
const num = {
 x : 0,
 y : 200,
 wd : 500,
 ht : 400
};
const key = {
 x : 0,
 y : 200,
 wd : 300,
 ht : 400
};
const op = {
 x : 300,
 y : 200,
 wd : 200,
 ht : 400
};

const k = [];
const o = [];
o.length = 6;
const sp = 5;
const k_w = key.wd/3 - sp, k_h = key.ht/4 - sp;
const o_w = op.wd/3, o_h = op.ht/o.length;
for(let i = 1; i < 10; i ++) {
 k[i] = {
  num :"" + i,
  x : ((i-1) % 3)*(k_w + sp) + sp,
  y : op.y + Math.floor((i-1)/3)*(k_h + sp) + sp
 };
}
k[0] = {
 num : "0",
 x : 1*(k_w + sp) + sp,
 y : op.y + 3*(k_h + sp) + sp
};
k[10] = {
 num : ".",
 x : sp,
 y : op.y + 3*(k_h + sp) + sp
};
k[11] = {
 num : "=",
 x : 2*(k_w + sp) + sp,
 y : op.y + 3*(k_h + sp) + sp
};
for(let i = 0; i < o.length; i ++) {
 o[i] = {
  op : " ",
  x : op.x + sp,
  y : dis.ht + i*o_h + sp
 }
}
console.log(o);
o[0].op = "+";
o[1].op = "-";
o[2].op = "*";
o[3].op = "/";
o[4].op = "%";
o[5].op = "<-";
function clearDisplay() {
 ctx.fillStyle = "rgb(51, 51, 51)";
 ctx.fillRect(dis.x, dis.y, dis.wd, dis.ht);
}

clearDisplay();

ctx.fillStyle = "rgb(190, 185, 210)";
ctx.fillRect(num.x, num.y, num.wd, num.ht);

ctx.fillStyle = "rgb(170, 185, 210)";
ctx.fillRect(key.x, key.y, key.wd, key.ht);

ctx.fillStyle = "rgb(190, 185, 180)";
ctx.fillRect(key.x, key.y, key.wd, key.ht);

//numpad
ctx.fillStyle = "rgb(160, 185, 170)";
for(let i = 0; i < 12; i ++) {
  ctx.fillRect(k[i].x, k[i].y, k_w, k_h);
}

//operators
ctx.fillStyle = "rgb(170, 170, 185)";
for(let i = 0; i < o.length; i ++) {
  ctx.fillRect(o[i].x, o[i].y, op.wd-2*sp, o_h-2*sp);
}

//text
ctx.font = Math.floor(k_h*0.8) + "px Ariel";
ctx.fillStyle = "black";
for(let i = 0; i < 12; i ++) {
 ctx.fillText(k[i].num, k[i].x + (k_w + sp)/4, k[i].y + 3*(k_h + sp)/4);
}
for(let i = 0; i < o.length; i ++) {
 ctx.fillText(o[i].op, o[i].x + (o_w + sp), o[i].y + 3*(o_h + sp)/4);
}
function mouse(event) {
 let input = "";
 for(let i = 0; i < 12; i ++) {
  if(event.clientX < k[i].x + k_w && event.clientX > k[i].x && event.clientY < k[i].y + k_h && event.clientY > k[i].y)
   input = k[i].num;
 }
 for(let i = 0; i < o.length; i ++) {
  if(event.clientX < o[i].x + 200-2*sp && event.clientX > o[i].x && event.clientY < o[i].y + k_h && event.clientY > o[i].y)
   input = o[i].op;
 }
 if(input == "<-") {
  if(s.length>1)
   s = s.substring(0, s.length-1);
  display(s);
 } else if(input == "=") {
  display(calculate(s));
  s = "";
 } else {
  s += input;
  display(s);
 }
}

function display(s) {
 clearDisplay();
 ctx.fillStyle = "white";
 ctx.fillText(s, dis.x, dis.y + dis.ht/2);
}

function calculate(s) {
 let res = 0, a = 0, b = 0, operator = "", i;
 for(i = 0; i < s.length; i ++) {
  if(s.charAt(i) == '+' || s.charAt(i) == '-' || s.charAt(i) == '*' || s.charAt(i) == '/' || s.charAt(i) == '%') {
   a = s.substring(0, i);
   b = s.substring(i+1, s.length);
   console.log(a, b);
   b = calculate(s.substring(i+1, s.length));
   operator = s.charAt(i);
   break;
  }
 }
 if(i == s.length) {
  console.log("after ", s)
  return s;
 }
 a = parseInt(a);
 b = parseInt(b);
 switch(operator) {
  case "+" :
   res = oper.add(a, b);
   break;
  case "-" :
   res = oper.subtract(a, b);
   break;
  case "*" :
   res = oper.multiply(a, b);
   break;
  case "/" :
   res = oper.divide(a, b);
   break;
  case "%" :
   res = oper.mod(a, b);
   break;
 }
 return res;
}

