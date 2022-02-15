//retrieve node in DOM via ID
var c = document.getElementById("slate")

//instantiate a CanvasRenderingContext 2D object
var ctx = c.getContext("2d");

//init global state var 
var mode = "rect";

//var toggleMode tunction(e) 
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect" ) {
        mode = "circ";
    } else {
        mode = "rect"
    }
}

var drawRect = function(e) {
	var mouseX = e.offsetX;
	var mouseY = e.offsetY;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.beginPath();
	ctx.rect(mouseX, mouseY, 50, 50);
	ctx.fillStyle = '#ff0000'; 
	ctx.fill(); 
	ctx.stroke();
}

//var drawCircle = function(e) 
var drawCircle = (e) => {
    var mouseX = e.offsetX;
	var mouseY = e.offsetY;
	console.log("mouseclick registered at ", mouseX, mouseY);
	ctx.beginPath();
	ctx.arc(mouseX, mouseY, 25, 2 * Math.PI, false);
	ctx.fillStyle = '#00ff00';
	ctx.fill();
	ctx.stroke();
}

//var draw = function(e)
var draw = (e) => {
    if (mode === "rect") {
		drawRect(e);
	} else {
		drawCircle(e);
	}
}

//var wipeCanvas = function() {
var wipeCanvas = () => {
    console.log("wiping canvas...");
	ctx.clearRect(0, 0, slate.width, slate.height);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener("click", toggleMode);
var clearB = document.getElementById("buttonClear");
clearB.addEventListener("click", wipeCanvas);
