var placeSearch, autocomplete;
var address = '';
var zip = '';

var componentForm = {
  street_number: 'short_name',
  route: 'long_name',
  locality: 'long_name',
  postal_code: 'short_name'
};


function initAutocomplete() {
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocomplete = new google.maps.places.Autocomplete(
      /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
      {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', fillInAddress);
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();

  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for (var i = 0; i < place.address_components.length; i++) {
    var addressType = place.address_components[i].types[0];
    if (componentForm[addressType]) {
      var val = place.address_components[i][componentForm[addressType]];
      if(addressType == 'postal_code')
        zip = val;
      else
        address += val+' ';
    }
  }
  $("#id_zipcode").val(zip);
  $("#id_location").val(address);

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
  });

  var geocoder = new google.maps.Geocoder();

  geocodeAddress(geocoder, map);
}

function geocodeAddress(geocoder, resultsMap) {
  var address = document.getElementById('autocomplete').value;
  geocoder.geocode({'address': address}, function(results, status) {
    if (status === 'OK') {

      console.log(results[0]);
      resultsMap.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
        map: resultsMap,
        position: results[0].geometry.location
      });
      if (results[0].geometry.viewport)
          resultsMap.fitBounds(results[0].geometry.viewport);
      } else {
        console.log('Geocode was not successful for the following reason: ' + status);
      }
    });
}
