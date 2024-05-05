$(document).ready(function() {
    $('#searchForm').submit(function(e) {
        e.preventDefault(); // Evitar que el formulario se envíe de forma convencional

        var searchTerm = $('#searchInput').val().toLowerCase(); // Obtener el término de búsqueda y convertirlo a minúsculas
        $('.product-item').each(function() {
            var title = $(this).find('a').text().toLowerCase(); // Obtener el título del producto y convertirlo a minúsculas
            if (title.includes(searchTerm)) {
                $(this).show(); // Mostrar el producto si el título coincide con el término de búsqueda
            } else {
                $(this).hide(); // Ocultar el producto si no coincide
            }
        });
    });
});
