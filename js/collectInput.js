(function(){
	function toJSONString(form){
		var obj = {};
		var elements = form.querySelectorAll("input, select");

		for (var i = 0; i < elements.length; ++i){
			var element = elements[i];
			var name = element.name;
			var value = element.value;

			if (name){
				obj[name] = value;
			}
		}
		return JSON.stringify(obj);
	}

	document.addEventListener("DOMContentLoaded", function(){
		var form = document.getElementById("jsonForm");
		form.addEventListener("submit", function(e){
			e.preventDefault();
			var json = toJSONString(this);
			console.log(json);
		}, false);
	});
})();