document.addEventListener('DOMContentLoaded', function () {
    function obtenerDatosDesdeFlask() {
        return fetch('http://127.0.0.1:5000/ph') 
            .then(response => {
                console.log(response);  
                return response.json();
            })
            .catch(error => {
                console.error('Error al obtener datos desde Flask:', error);
                return {};
            });
    }

    function actualizarInterfaz() {
        obtenerDatosDesdeFlask().then(datos => {
            document.getElementById('ph-value').textContent = datos.ph.toFixed(2);
            document.getElementById('humidity-value').textContent = datos.humedad + '%';
            document.getElementById('light-value').textContent = datos.luz + ' luz';
            document.getElementById('fertilizer-value').textContent = datos.fertilizante + '%';

            // Actualiza el estado del agua
            const waterBar = document.getElementById('water-bar');
            waterBar.textContent = (datos.agua > 50) ? 'Ácida' : 'Alcalina';

            // Actualiza las barras de progreso lineales
            actualizarBarraLineal('humidity-bar', datos.humedad);
            actualizarBarraLineal('light-bar', datos.luz);
            actualizarBarraLineal('fertilizer-bar', datos.fertilizante);
        });
    }

    // Función para actualizar las barras de progreso lineales
    function actualizarBarraLineal(barId, porcentaje) {
        const bar = document.getElementById(barId);
        const progressBar = bar.querySelector('.progress-bar');

        progressBar.style.width = porcentaje + '%';

        // Cambia a verde si el porcentaje es mayor al 20%
        progressBar.classList.toggle('green', porcentaje > 20);
    }

    setInterval(actualizarInterfaz, 5000);
    actualizarInterfaz();
});
