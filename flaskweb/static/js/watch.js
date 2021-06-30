
var watch = setInterval(myWatch,1000)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString(); //연월일 제외 시분초만 나옴
    document.getElementById("demo").innerHTML = now}