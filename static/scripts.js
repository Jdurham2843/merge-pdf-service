var counter = 4;

$('#add-button').click(function(){
	$('#inputs-container').append('<div class="input-wrapper"><label for="file' + counter + '">File ' + counter + ' </label><input type="file" name="file[]"/></div>');
	counter++;
});
