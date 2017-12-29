$(document).ready(function main() {
  // create map
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 21.028511, lng: 105.804817},
    zoom: 12
  });

  $('#number-submit').click(function addField() {
    var num = $('#number-input').val();

    // check user input is bigger than 0 or not
    if (num<=0) {
      alert('Incorrect number');
      return;
    };

    var container = document.getElementById("location-input");

    // delete previous fields
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    };

    // add new fields
    for (i=0; i<num; i++) {
      var new_div = document.createElement('div');
      new_div.className = 'form-inline my-2 my-lg-0 new_div ';
      container.appendChild(new_div);
      var locationInput = document.createElement("input");
      locationInput.id = 'user' + (i+1);
      locationInput.type = 'text';
      locationInput.className = 'search-box form-control mr-sm-2 person-bar user_box';
      locationInput.placeholder = ('Địa chỉ người ' + (i+1));
      new_div.appendChild(locationInput);
    };

    // create autocomplete function for searchboxes
    var inputs = $('.search-box');

    for (j=0; j<inputs.length; j++) {
      autocompleteBox = new google.maps.places.Autocomplete(inputs[j], {
        //bias the search result to current mapbound
        bounds: map.getBounds()
      });
    }
    autocompleteBox.addListener('places_changed', function() {
      var place = autocompleteBox.getPlaces();
      marker = new google.maps.Marker({
        map: map,
        icon: icon,
        title: place.name,
        position: place.geometry.location
      });
      markers.push(marker);
    })
  });
})
