// Modal para registrar ingreso

    const botonIngreso = document.getElementById("btn-registrar-ingreso");
    const modalIngreso = document.getElementById("modal-ingreso");
    const cerrarModal = document.getElementById("cerrar-modal");

    botonIngreso.addEventListener("click", function () {
        modalIngreso.style.display = "flex";
    });

    cerrarModal.addEventListener("click", function () {
        modalIngreso.style.display = "none";
    });

    modalIngreso.addEventListener("click", function (event) {
        if (event.target === modalIngreso) {
            modalIngreso.style.display = "none";
        }
    });



// Modal para registrar salida

     const botonesSalida = document.querySelectorAll(".btn-abrir-salida");
    const modalSalida = document.getElementById("modal-salida");
    const cerrarModalSalida = document.getElementById("cerrar-modal-salida");
    const accesoIdSalida = document.getElementById("id_acceso_salida");

    botonesSalida.forEach(function (boton) {
        boton.addEventListener("click", function () {
            const accesoId = this.dataset.accesoId;

            accesoIdSalida.value = accesoId;
            modalSalida.style.display = "flex";
        });
    });

    cerrarModalSalida.addEventListener("click", function () {
        modalSalida.style.display = "none";
    });

    modalSalida.addEventListener("click", function (event) {
        if (event.target === modalSalida) {
            modalSalida.style.display = "none";
        }
    });