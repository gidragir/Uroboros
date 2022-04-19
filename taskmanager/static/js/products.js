let urls;
fetch('/static/js/urls.json').then(response => response.json()).then(data => urls = data);

function replaceText(element, text) {
  var replaceText = document.getElementById(element).getAttribute("replaceText");
  $('#' + element).text(replaceText.replace("#text", text));
}

function openProduct(btn) {

  var modal = document.getElementById("productModal");

  var productId = Number(btn.parentNode.getAttribute("productId"));

  $.ajax({

    url: urls['URL_ProductMore'],
    method: "GET",
    data: {
      "productId": productId
    },
    success: function (data) {

      $('#header').text(data.name);
      replaceText('description', data.description);
      replaceText('quantity', data.quantity);
      replaceText('price', data.price);
      document.getElementById("modalProductId").setAttribute("value", productId)
      document.getElementById("product-modal-img").setAttribute("src", "data:image/jpeg; base64, " + data.picture)

      modal.style.display = "block";
    }
  });

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