/*
 * Convert donor register form to JSON
 * and send to the server!
 */

// Convert HTML form to JSON
function toJSONString(form){
	// Create an empty object first
	var obj = {};

	// Select elements from the HTML form
	var elements = form.querySelectorAll("input, select");

	// Get each element and add to the object
	for (var i = 0; i < elements.length; ++i){
		var element = elements[i];
		var name = element.name;
		var value = element.value;

		if (name){ // Checking if object's name exists
			obj[name] = value;
		}
	}
	return JSON.stringify(obj);
}

document.addEventListener("DOMContentLoaded", function(){
	// Get the form from HTML
	var form = document.getElementById("jsonForm");

	// Action when user press "Submit"
	form.addEventListener("submit", function(e){
		// Prevent event from creating default form
		e.preventDefault();

		// Create a JSON form from HTML form
		var json = toJSONString(this);

		// Print JSON to the console
		console.log(json);

		// Sending data
		var xhr = new XMLHttpRequest();
		var url = "/register_blood_donation";
		xhr.open("POST", url, true);
		xhr.setRequestHeader("Content-Type", "application/json");
		xhr.onreadystatechange = function(){
			// Call the function when the state changes
			if (this.readyState === XMLHttpRequest.DONE && this.status === 200){
				console.log("Donor's register has sent to the server!");
			}
		};
		xhr.send(json);
	}, false);
});