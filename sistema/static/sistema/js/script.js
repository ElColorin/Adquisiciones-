$(document).ready(function(){

	// AGREGANDO CLASE ACTIVE AL PRIMER ENLACE ====================
	$('.category_list .category_item[category="all"]').addClass('ct_item-active');

	// FILTRANDO PRODUCTOS  ============================================

	$('.category_item').click(function(){
		var catProduct = $(this).attr('category');
		console.log(catProduct);

		// AGREGANDO CLASE ACTIVE AL ENLACE SELECCIONADO
		$('.category_item').removeClass('ct_item-active');
		$(this).addClass('ct_item-active');

		// OCULTANDO PRODUCTOS =========================
		$('.product-item').css('transform', 'scale(0)');
		function hideProduct(){
			$('.product-item').hide();
		} setTimeout(hideProduct,400);

		// MOSTRANDO PRODUCTOS =========================
		function showProduct(){
			$('.product-item[category="'+catProduct+'"]').show();
			$('.product-item[category="'+catProduct+'"]').css('transform', 'scale(1)');
		} setTimeout(showProduct,400);
	});

	// MOSTRANDO TODOS LOS PRODUCTOS =======================

	$('.category_item[category="all"]').click(function(){
		function showAll(){
			$('.product-item').show();
			$('.product-item').css('transform', 'scale(1)');
		} setTimeout(showAll,400);
	});
});


$(document).ready(function(){
	$(".category_item").click(function(e){
		e.preventDefault();
		var category = $(this).attr("category");

		$.ajax({
			url: "{% url 'filter_products' %}",
			data: {
				'category': category
			},
			dataType: 'json',
			success: function(data){
				var products_html = '';
				for (var i = 0; i < data.products.length; i++) {
					products_html += `
						<div class="col product-item" category="${data.products[i].category.toLowerCase()}">
							<div class="card shadow-sm h-100">
								<div class="container-foto">
									<article class="articlefotos">
										<img src="${data.products[i].image_url}">
										<img src="${data.products[i].image_url}">
									</article>
								</div>
								<div class="card-body">
									<p class="card-title">${data.products[i].name}</p>
								</div>
								<div class="card-footer bg-transparent">
									<div class="d-flex justify-content-between align-items-center">
										<div class="btn-group">
											<a href="#" class="btn btn-primary">
												<i class="bi bi-info-circle-fill"> Detalles</i>
											</a>
										</div>
										<a href="#" class="btn btn-danger" type="button">
											<i class="bi-cart-fill me-1"> Agregar</i>
										</a>
									</div>
								</div>
							</div>
						</div>`;
				}
				$('.products-list').html(products_html);
			}
		});
	});
});