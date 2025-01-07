document.addEventListener("DOMContentLoaded", () => {
    const mapElement = document.getElementById("map");
    const lat = parseFloat(mapElement.dataset.lat);
    const lng = parseFloat(mapElement.dataset.lng);

    if (!isNaN(lat) && !isNaN(lng)) {
        const map = L.map("map").setView([lat, lng], 15);

        L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(map);

        L.marker([lat, lng]).addTo(map);
    } else {
        console.error("Latitude or longitude is missing or invalid.");
    }
});
