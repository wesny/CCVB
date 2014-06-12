//People Results Script	
$('.button-group').each( function( i, buttonGroup ) {
	var $buttonGroup = $( buttonGroup );
	$buttonGroup.on( 'click', 'button', function() {
		$buttonGroup.find('.is-checked').removeClass('is-checked');
		$( this ).addClass('is-checked');
	});
});

var $container = $('.graphs').isotope({
	itemSelector: '.pgraph',
	layoutMode: 'masonry',
});