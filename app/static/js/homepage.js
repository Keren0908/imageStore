window.onload = function(){

// Get the modal
var modal = document.getElementById('myModal');

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById('myImger');
var img_1 = document.getElementById('myImg_1');
var modalImg = document.getElementById("img01");
var modalImg_1 =document.getElementById("img02");
var captionText = document.getElementById("caption");
var captionText = document.getElementById("caption_1");
img.onclick = function(){
    modal.style.display = "block";
    modalImg.src = img.src
    modalImg_1.src = img_1.src

    captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
    modal.style.display = "none";
}

}
