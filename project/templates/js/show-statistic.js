document.addEventListener("DOMContentLoaded", function(){
	// Sending data
	var xhr = new XMLHttpRequest();
	var url = "/show_statistic";
	xhr.open("GET", url, true);
	xhr.setRequestHeader("Content-Type", "application/json");
	xhr.onreadystatechange = function(){
		// Call the function when the state changes
		if (this.readyState === 4 && this.status === 200){
			console.log(this.responseText);
			var json = this.responseText;

			document.getElementById("o+amount").textContent = json.Oplus_amount;
			document.getElementById("o-amount").textContent = json.Ominus_amount;
			document.getElementById("a+amount").textContent = json.Aplus_amount;
			document.getElementById("a-amount").textContent = json.Aminus_amount;
			document.getElementById("b+amount").textContent = json.Bplus_amount;
			document.getElementById("b-amount").textContent = json.Bminus_amount;
			document.getElementById("ab+amount").textContent = json.ABplus_amount;
			document.getElementById("ab-amount").textContent = json.ABminus_amount;
		}
	};
	xhr.send();
});