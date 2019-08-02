pos = 1;

function f1(){
  alert("I Love You Too!")
}
function f2(){
  if (pos==1 || (pos!= 2 && pos!=3)) {
    btnNO.style.top=400;
    btnNO.style.left=400;
    pos=2;


  }
  else if (pos==2) {
    btnNO.style.top=500;
    btnNO.style.left=50;
    pos=3;

  }
  else if (pos==3) {
    btnNO.style.top=100;
    btnNO.style.left=400;
    pos=1;
  }
}
