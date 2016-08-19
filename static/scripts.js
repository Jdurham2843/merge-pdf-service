$('#file1').on("change", function(){
	var fileList = [];
	for (var i = 0; i < this.files.length; i++){
		$('#file-sort-list').append('<li>' + this.files[i].name + '</li>');
	}

	$('#file-sort-list').sortable();


});

$('#submit-button').click(function() {
       	var mergeOrder = '';
	$('li').each(function(){
		if (mergeOrder === ''){
			mergeOrder  = $(this).text();
		}else{
			mergeOrder = mergeOrder + ',' + $(this).text();
		}
	});
	$('#merge-order').val(mergeOrder);
	alert('checkit');
	$('#myDropzone').submit();

});

