// TeamHE - Han Zhang, Edwin Zheng
// SoftDev
// K27 - Where Does JS Live?
// 2022-2-04
// time spent: 30min
function fac(num) {
if (num < 0) 
        return "Error : enter positive number";
else if (num == 0) 
    return 1;
else {
    return (num * fac(num - 1));
}
}
let facx = fac(4);
document.getElementById("fac4").innerHTML = facx;

function fib(n) {
    if (n <= 1) 
        return 1;
    else {
        return (fib(n - 1) + fib (n - 2))
    }
}
let fibx = fib(4);
document.getElementById("fib4").innerHTML = fibx;