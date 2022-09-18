class oper {
 constructor() {}
 
 static add(a, b) {
  return a + b;
 }

 static subtract(a, b) {
  return a - b;
 }
 
 static multiply(a, b) {
  return a * b;
 }
 
 static divide(a, b) {
  if(b!=0)
   return a/b;
  return "error";
 }
  
 static mod(a, b) {
  return a % b;
 }
}