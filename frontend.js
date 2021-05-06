var dataVar = document.getElementById("data");
var popOne = document.getElementById("popup1");
var Close = document.getElementById("close1");

if(dataVar){
    dataVar.addEventListener("click",function () {
            popOne.style.display = "flex";
    })
}
if(Close){
    Close.addEventListener("click",function () {
            popOne.style.display = "none";
    })
}

var wordVar = document.getElementById("word");
var popTwo = document.getElementById("popup2");
var Close = document.getElementById("close2");

if(wordVar){
    wordVar.addEventListener("click",function () {
            popTwo.style.display = "flex";
    })
}
if(Close){
    Close.addEventListener("click",function () {
            popTwo.style.display = "none";
    })
}

var projectVar = document.getElementById("project");
var popThree = document.getElementById("popup3");
var Close = document.getElementById("close3");

if(projectVar){
    projectVar.addEventListener("click",function () {
            popThree.style.display = "flex";
    })
}

if(Close){
    Close.addEventListener("click",function () {
            popThree.style.display = "none";
    })
}

function insert_result(response) {
     var maintext = document.getElementById("maintext");
     maintext.innerHTML = response;
}

function update_page() {
	var form = document.getElementById("form");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest()
	xmlHttpRqst.onload = function(e) {insert_result(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/pos/?" + queryString);
	xmlHttpRqst.send();
	
}

function machine_page() {
	var form = document.getElementById("form2");
	var formData = new FormData(form);
	var searchParams = new URLSearchParams(formData);
	var queryString = searchParams.toString();
	xmlHttpRqst = new XMLHttpRequest()
	xmlHttpRqst.onload = function(e) {insert_result(xmlHttpRqst.response);} 
	xmlHttpRqst.open( "GET", "/classify/?" + queryString);
	xmlHttpRqst.send();
	
}