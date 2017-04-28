function text()
{
	var x = document.getElementById("canvas");
	canvas = x.getContext("2d");
	
	var pic = new Image();
	pic.src = "http://cdn3-www.dogtime.com/assets/uploads/gallery/german-shepherd-dog-breed-pictures/laying-1.jpg";
	pic.addEventListener("load", function() { canvas.drawImage(pic, 0, 0, 200, 150)}, false);
}

window.addEventListener("load", text, false);