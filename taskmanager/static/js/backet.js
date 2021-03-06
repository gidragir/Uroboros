function quantityUp(btn) {
  btn.parentNode.querySelector('input[type=number]').stepUp();
  updateBacket(btn, 1);
}

function quantityDown(btn) {
  btn.parentNode.querySelector('input[type=number]').stepDown();
  updateBacket(btn, -1);
}

function addToBacket(btn) {
  var productId = btn.parentNode.querySelector('input[name=modalProductId]').value;
  var quantity = btn.parentNode.querySelector('input[name=modalQuantity]').value;

  $.ajax({
    type: "POST",
    url: urls['URL_backetOperation'],
    data: {
      "productId": productId,
      "quantity": quantity,
      "csrfmiddlewaretoken": token,
      "operation": "add"
    },
    success: function (data) {

      var modal = document.getElementById("productModal");
      modal.style.display = "none";
    }
  });
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

function deleteBacket(btn) {

  backet_id = btn.parentNode.querySelector('input[name=backet_id]').value;

  $.ajax({

    url: addToUrl(backet_id),
    type: "DELETE",
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", token);
    },
    success: function () {
      location.reload();
    }
  });
}

function makeOrder() {
  var user_id = document.getElementById('user_id').value;

  var mass = [];

  $.ajax({

    url: urls['URL_backetOperation'],
    type: "POST",
    data: {
      "user_id": user_id,
      "csrfmiddlewaretoken": token,
      "operation": "makeOrder"
    },
    success: function () {
      
    }
  });

}

function addToUrl(addedUrl) {
  return urls['URL_backetOperation'] + "/" + addedUrl;
}