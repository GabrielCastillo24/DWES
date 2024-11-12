       // Función para validar el formulario
       function validateForm(event) {
        var email = document.getElementsByName("f_email")[0].value;
        var password = document.getElementsByName("f_password")[0].value;
        
        // Verificar si los campos están vacíos
        if (email == "" || password == "") {
            alert("Por favor, complete ambos campos.");
            event.preventDefault();  // Impide que el formulario se envíe
        }
    }