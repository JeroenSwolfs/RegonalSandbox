// Initialize map
const map = L.map('map').setView([52.1326, 5.2913], 7);
const loadingScreen = document.getElementById('loading-screen');

// Light monotone tile layer (Carto Light)
L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 20
}).addTo(map);

// Load ADM2 GeoJSON with clickable municipalities
function loadMunicipalityGeoJSON() {
    loadingScreen.style.display = 'flex'; // Show loading screen
    fetch('municipality_geoJSON')
    .then(response => response.json())
    .then(data => {
        console.log(data)
        L.geoJSON(data, {
            style: {
                color: 'blue',
                weight: 1,
                fill: true,
                fillColor: 'blue',
                fillOpacity: 0.1
            },
            onEachFeature: function(feature, layer) {
                layer.on('click', function() {
                    layer.bindPopup(`<b>${feature.properties.shapeName}</b>`).openPopup();
                });
                layer.on('mouseover', function() {
                    layer.setStyle({ weight: 2, color: 'red', fillOpacity: 0.2 });
                });
                layer.on('mouseout', function() {
                    layer.setStyle({ weight: 1, color: 'blue', fillOpacity: 0.1 });
                });
            }
        }).addTo(map);
    })
    .catch(err => console.error("Error loading GeoJSON:", err))
    .finally(() => {
        loadingScreen.style.display = 'none'; // Hide loading screen
    });
}

// fetch from a local api
// fetch('http://localhost:3000/api/data')
//     .then(response => response.json())
//     .then(data => {
//         console.log(data);
//         // Process and visualize the data on the map as needed
//     })
//     .catch(err => console.error("Error fetching API data:", err));