let urls;
fetch('/static/js/urls.json').then(response => response.json()).then(data => urls = data);
