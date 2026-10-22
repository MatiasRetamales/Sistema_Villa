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

    // Buscador de viviendas en el modal de ingreso
document.addEventListener("DOMContentLoaded", function () {
    const vivienda = document.querySelector(
        '#modal-ingreso select[name="vivienda"]'
    );

    if (vivienda && typeof TomSelect !== "undefined" && !vivienda.tomselect) {
        new TomSelect(vivienda, {
            create: false,
            maxOptions: 1000,
            placeholder: "Escribe el número de casa...",
            searchField: ["text"],
            closeAfterSelect: true
        });
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




// Cambiar entre secciones

const botonesSeccion = document.querySelectorAll(".btn-seccion");
const secciones = document.querySelectorAll(".contenido-seccion");

botonesSeccion.forEach(function (boton) {
    boton.addEventListener("click", function () {
        const seccionSeleccionada = boton.dataset.seccion;

        secciones.forEach(function (seccion) {
            seccion.hidden = seccion.id !== `seccion-${seccionSeleccionada}`;
        });

        botonesSeccion.forEach(function (otroBoton) {
            otroBoton.classList.toggle("activo", otroBoton === boton);
        });
    });
});





// Buscador de tablas

function activarBuscador(idBuscador, idTabla) {
    const buscador = document.getElementById(idBuscador);
    const tabla = document.getElementById(idTabla);

    if (!buscador || !tabla) return;

    buscador.addEventListener("input", function () {
        const texto = buscador.value
            .trim()
            .toLocaleLowerCase("es");

        const filas = tabla.querySelectorAll("tbody tr");

        filas.forEach(function (fila) {
            // Ignorar la fila de mensaje cuando no hay registros.
            if (fila.querySelectorAll("td").length === 1) return;

            const contenido = fila.textContent.toLocaleLowerCase("es");

            fila.hidden = !contenido.includes(texto);
        });
    });
}

activarBuscador("buscar-ingresos", "tabla-ingresos");
activarBuscador("buscar-trabajo", "tabla-trabajo");
activarBuscador("buscar-administrativos", "tabla-administrativos");








/* Campos dinámicos para los acompañantes */

const cantidadAcompanantes = document.getElementById(
    "id_cantidad_acompanantes"
);

const contenedorAcompanantes = document.getElementById(
    "campos-acompanantes"
);

function actualizarCamposAcompanantes() {
    if (!cantidadAcompanantes || !contenedorAcompanantes) {
        return;
    }

    let cantidad = parseInt(cantidadAcompanantes.value, 10);

    if (isNaN(cantidad) || cantidad < 0) {
        cantidad = 0;
    }

    cantidad = Math.min(cantidad, 20);

    contenedorAcompanantes.replaceChildren();

    if (cantidad === 0) {
        return;
    }

    const titulo = document.createElement("h3");
    titulo.textContent = "Datos de los acompañantes";
    contenedorAcompanantes.appendChild(titulo);

    for (let i = 1; i <= cantidad; i++) {
        const grupo = document.createElement("div");
        grupo.className = "campo-acompanante";

        const tituloPersona = document.createElement("h4");
        tituloPersona.textContent = `Acompañante ${i}`;
        grupo.appendChild(tituloPersona);

        const labelNombre = document.createElement("label");
        labelNombre.htmlFor = `acompanante_nombre_${i}`;
        labelNombre.textContent = "Nombre completo";

        const inputNombre = document.createElement("input");
        inputNombre.type = "text";
        inputNombre.id = `acompanante_nombre_${i}`;
        inputNombre.name = `acompanante_nombre_${i}`;
        inputNombre.maxLength = 150;
        inputNombre.required = true;

        const labelRut = document.createElement("label");
        labelRut.htmlFor = `acompanante_rut_${i}`;
        labelRut.textContent = "RUT";

        const inputRut = document.createElement("input");
        inputRut.type = "text";
        inputRut.id = `acompanante_rut_${i}`;
        inputRut.name = `acompanante_rut_${i}`;
        inputRut.maxLength = 12;
        inputRut.placeholder = "Ej.: 12345678-9";
        inputRut.required = true;

        grupo.append(
            labelNombre,
            inputNombre,
            labelRut,
            inputRut
        );

        contenedorAcompanantes.appendChild(grupo);
    }
}

if (cantidadAcompanantes && contenedorAcompanantes) {
    cantidadAcompanantes.addEventListener(
        "input",
        actualizarCamposAcompanantes
    );

    cantidadAcompanantes.addEventListener(
        "change",
        actualizarCamposAcompanantes
    );

    actualizarCamposAcompanantes();
}

