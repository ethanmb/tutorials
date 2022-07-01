function getRecipes() {
	console.log("test");
    let ingredient = document.getElementById('ingredient').value
	/*
    if(ingredient === '') {
        return alert('Please enter an ingredient')
    }
	*/
	
    let recipeDiv = document.getElementById('recipes')
    recipeDiv.innerHTML = ''

    let xhr = new XMLHttpRequest()
    xhr.onreadystatechange = () => {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let response = JSON.parse(xhr.responseText)
            let recipes = response.recipes
        }
    }
    if(ingredient === '') {
       xhr.open('GET', `/recipes`, true)
    }
	else{
       xhr.open('GET', `/recipes?ingredient=${ingredient}`, true)
	}
    xhr.send()
}

//Attach Enter-key Handler To Text Input Field
const ENTER=13 //enter key keyCode
document.getElementById("ingredient")
    .addEventListener("keyup", function(event) {
    event.preventDefault();
    if (event.keyCode === ENTER) {
        document.getElementById("submit").click();
    }
});

//$(document).ready(function(){ //jQuery
document.addEventListener('DOMContentLoaded',function(){
	//This is called after the browser has loaded the web page
	document.getElementById("submit").click();
});