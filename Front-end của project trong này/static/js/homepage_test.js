var map;

function initmap() {
  map = new google.maps.Map($('#map'), {
    center: {lat: 21.028511, lng: 105.804817},
    zoom:12
  })
};

$('#number-submit').click(function addField() {
  var num = $(this).prev().val();

  if (num <= 0) {
    alert('Incorrect number');
    return;
  }

  var container = $('#location-input');

  while (container.hasChildNodes()) {
      container.removeChild(container.lastChild);
  };

  for (i=0; i<num; i++) {
    var new_div = document.createElement('div');
    new_div.className = 'form-inline my-2 my-lg-0';
    container.appendChild(new_div);
    var locationInput = document.createElement("input");
    locationInput.id = 'user' + (i+1);
    locationInput.type = 'text';
    locationInput.className = 'search-box form-control mr-sm-2 person-bar';
    locationInput.placeholder = ('User ' + (i+1));
    new_div.appendChild(locationInput);
  };
})
