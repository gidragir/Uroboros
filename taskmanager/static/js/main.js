function openSignInForm(btn) {

  var modal = document.getElementById("loginForm");

  modal.style.display = "block";

  var span = document.getElementsByClassName("close")[0];

  span.onclick = function () {
    modal.style.display = "none";
  };

  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
}

function userExit() {

  $.ajax({

    url: URL_Current,
    method: "GET",
    data: {
      "delete": 1
    },
    success: function () {
      location.reload();
    }
  });
}
