$('.btn.favorite').click(function() {
    var $obj = $(this);
    var target_id = $obj.attr('id').split('_')[1];
    $obj.prop('disabled', true);
    $.ajax({
	url: $obj.attr('href'),
	type: 'POST',
	data: {target_model: $obj.attr('model'),
	       target_object_id: target_id},
	success: function(response) {
	    if (response.status == 'added') {
		$obj.children().removeClass('icon-star-empty').addClass('icon-star');}
	    else {
		$obj.children().removeClass('icon-star').addClass('icon-star-empty');}
	    $obj.parent('.favorite').children('.fav-count').text(response.fav_count);
	    $obj.prop('disabled', false);
	}
    });
});
