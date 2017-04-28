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
	var pic = new Image();
	pic.src = "http://cdn3-www.dogtime.com/assets/uploads/gallery/german-shepherd-dog-breed-pictures/laying-1.jpg";
	canvas.drawImage(pic, xPos, yPos, 200, 200);
}

window.addEventListener("load", mouse, false);