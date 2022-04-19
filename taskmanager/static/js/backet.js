let urls;
fetch('/static/js/urls.json').then(response => response.json()).then(data => urls = data);

function quantityUp(btn) {
  btn.parentNode.querySelector('input[type=number]').stepUp();
  updateBacket(btn, 1);
}

function quantityDown(btn) {
  btn.parentNode.querySelector('input[type=number]').stepDown();
  updateBacket(btn, -1);
}

function updateBacket(btn, quantity) {

  productId = btn.parentNode.querySelector('input[name=productId]').value;

  $.ajax({

    url: urls['URL_backetOperation'],
    type: "POST",
    data: {
      "productId": productId,
      "quantity": quantity,
      "update": true,
      "csrfmiddlewaretoken": token,
      "operation": "update"
    },
    success: function () {
    }
  });
}