var map = L.map('map').setView([4,608215, -74,191166], 20);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

async function loadpolgom() 
try{
    let responde = await fetch ("Piamonte.geojson");
    let data = await responde.json();
    l.geoJSON(data,
        {
            style: {Color: "Blue"},
        }
    ).addTo(Mapas);
} 
    catch(error){
        console.error("Cant load")
    }