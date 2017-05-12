function drag() {
	mantis = document.getElementById("mantisShrimp");
	leftbox = document.getElementById("leftBox");
	
	mantis.addEventListener("dragstart", startDrag, false);
	mantis.addEventListener("dragend", endDrag, false);
	
	leftbox.addEventListener("dragenter", dragEnter, false);
	leftbox.addEventListener("dragleave", dragLeave, false);
	leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
	leftbox.addEventListener("drop", drop, false);
}

function startDrag(e) {
	var pic = '<img id = "mantisShrimp" src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKMTMZ8zBjhzQ1vl-MRcqYZ1nfPBKFskY--p2sp7w7eYus_Izi">';
	e.dataTransfer.setData('picture', pic);
}

function dragEnter(e) {
	e.preventDefault();
	leftbox.style.background = "blue";
	leftbox.style.border = "5px solid yellow";
}

function dragLeave(e) {
	e.preventDefault();
	leftbox.style.background = "blue";
	leftbox.style.border = "5px solid yellow";
}

function drop(e) {
	e.preventDefault();
	leftBox.innerHTML = e.dataTransfer.getData('picture');
}

function endDrag(e) {
	pic = e.target;
	pic.style.visibility = "hidden";
}

window.addEventListener("load", drag, false);