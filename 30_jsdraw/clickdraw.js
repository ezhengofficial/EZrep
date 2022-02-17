// Team HE: Han Zhang, Edwin Zheng
// SoftDev
// K30 -- Canvas Based JS Drawing
// 2022-02-14

// Retrieve Canvas Node
var c = document.getElementById("slate");

// Instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

// Toggle Mode Type
var mode = "rect";
var toggler = document.getElementById("buttonToggle");


// Toggle Mode on Button Click

var toggleMode = (e) => {
    if (mode == "rect") {
        mode = "circle";
        toggler.innerHTML = "Circle"
    } else {
        mode = "rect";
        toggler.innerHTML = "Rect"
    }
}

toggler.addEventListener("click", toggleMode);

// Draw items

var draw = (e) => {
    if (mode == "rect") {
       drawRect(e);
    } else {
        drawCircle(e);
    }
}

var drawRect = (e) => {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;

    ctx.rect(mouseX, mouseY, 100, 150)
    ctx.fillStyle = "red"
    ctx.fill()
}

var drawCircle = (e) => {
    let mouseX = e.offsetX;
    let mouseY = e.offsetY;
    
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 50, 0, 2 * Math.PI)
    ctx.fillStyle = "red"
    ctx.fill()
    ctx.stroke()
}

var clearButton = document.getElementById("buttonClear")

var wipeCanvas = function() {
    ctx.clearRect(0, 0, c.clientWidth, c.height)
}

clearButton.addEventListener("click", wipeCanvas);

c.addEventListener("click", draw)