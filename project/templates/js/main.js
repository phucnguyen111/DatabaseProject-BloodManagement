

/////////////////////////////////////////
//connect to back end Nguyen Viet Hoang lam file python
// this is the id of the form
$(document).ready(() => {
  $("#jsonForm").submit(function (e) {
    showToast("Uploading...");

    e.preventDefault();

    var form = $(this);
    var url = form.attr("action");

    $.ajax({
      type: "POST",
      url: url,
      data: form.serialize(),
      success: function (data) {
        showToast(data);
      }
    });

    $("#jsonForm").trigger("reset");
  });
});

function showToast(val) {
  if ($("#snackbar").length) {
    $("#snackbar").text(val);
    //alert(val);
  } else {
    jQuery("<div/>", {
      id: "snackbar"
    })
      .text(val)
      .appendTo("body");

    //alert(val);

    $("#snackbar").attr("class", "show");

    setTimeout(() => {
      $("#snackbar").removeClass("show");
      $("#snackbar").remove();
    }, 3000);
  }
}

function navOpen() {
  if ($("#header").hasClass('visibler'))
    $("#header").removeClass('visibler');
  else
    $("#header").addClass('visibler');
}

function openIndex() {
  window.location.href="index.html"
}