function quantityUp(btn) {
  btn.parentNode.querySelector('input[type=number]').stepUp()
}

function quantityDown(btn) {
  btn.parentNode.querySelector('input[type=number]').stepDown()
}

function updateBacket() {
  $.ajax({

    url: URL_Current,
    method: "POST",
    data: {
      "delete": 1
    },
    success: function () {
      location.reload();
    }
  });
}