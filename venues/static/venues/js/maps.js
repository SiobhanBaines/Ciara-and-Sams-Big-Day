    // Initialize and add the map

    function initMap() {
        // location of church
        const churchLat = parseFloat(document.getElementById('lat-1').value);
        const churchLng = parseFloat(document.getElementById('lng-1').value);
        // location of reception
        const receptionLat = parseFloat(document.getElementById('lat-2').value);
        const receptionLng = parseFloat(document.getElementById('lng-2').value);
        const options = [{
            // church
                zoom: 13,
                center: {
                    lat: churchLat,
                    lng: churchLng,
                },
            },
            {
            // reception
                zoom: 13,
                center: {
                    lat: receptionLat,
                    lng: receptionLng,
                },
            },
        ];
        // Position marker
        for (let i = 0; i < options.length; i++) {
            const map = new google.maps.Map(document.getElementById(`map-${i + 1}`), options[i]);
            const marker = new google.maps.Marker({
                position: {
                    lat: options[i].center.lat,
                    lng: options[i].center.lng,
                    icon: options[i].icon,
                    map,
                },
            });
            marker.setMap(map)
        }
    }