/*
 * Show the success/failure of the register
 */

function getJSON(url, callback){
	var xhr = new XMLHttpRequest();
	xhr.open("GET", url, true);
	xhr.responseType = 'json';
	xhr.onload = function() {
		var status = xhr.status;
		if (status === 200) {
			callback(null, xhr.response);
		} else {
			callback(status, xhr.response);
		}
	};
	xhr.send();
};

document.addEventListener("DOMContentLoaded", function(){
	// Get the URL of the server
	var url = "/register_blood_donation";

	// Get callback
	var callback = function(err, data) {
		if (err !== null)
			alert('Something went wrong: ' + err);
		else
			alert('Your query count: ' + data.query.count);
	};

	// Get the form from server
	var json = getJSON(url, callback);
	var form = JSON.parse(json);

	// Get the current date (the day of register)
	var today = new Date();
	var d = String(today.getDate()).padStart(2, '0');
	var m = String(today.getMonth() + 1).padStart(2, '0'); // January is 0
	var d = today.getFullYear();
	today = d + '/' + m + '/' + y;

	// Change the content in both forms
	document.getElementById("reg-name").textContent = form.fname;
	document.getElementById("reg-pid").textContent = form.pid;
	document.getElementById("reg-phone").textContent = form.phone;

	// Change the content for the "success" form only
	document.getElementById("reg-blood-group").textContent = form.blood_group;
	document.getElementById("reg-amount").textContent = form.donate_amount;
	document.getElementById("reg-date").textContent = today;
});