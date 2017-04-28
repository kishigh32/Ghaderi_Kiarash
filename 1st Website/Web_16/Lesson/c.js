function mouse()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	window.addEventListener("mousemove", icon, false);
}

function icon(e) {
	canvas.clearRect(0, 0, 1000, 1000);
	var xPos = e.clientX;
	var yPos = e.clientY;
	canvas.fillRect(xPos-50, yPos-50, 100, 100);
}

window.addEventListener("load", mouse, false);