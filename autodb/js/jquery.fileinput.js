$.fn.fileInput = function(){
	//apply events and styles for file input element
	var fileInput = $(this)
		.addClass('customfile-input') //add class for CSS
		.mouseover(function(){ upload.addClass('customfile-hover'); })
		.mouseout(function(){ upload.removeClass('customfile-hover'); })
		.focus(function(){
			upload.addClass('customfile-focus');
			fileInput.data('val', fileInput.val());
		})
		.blur(function(){
			upload.removeClass('customfile-focus');
			$(this).trigger('checkChange');
		})
		.bind('disable',function(){
			fileInput.attr('disabled',true);
			upload.addClass('customfile-disabled');
		})
		.bind('enable',function(){
			fileInput.removeAttr('disabled');
			upload.removeClass('customfile-disabled');
		})
		.bind('checkChange', function(){
			if(fileInput.val() && fileInput.val() != fileInput.data('val')){
				fileInput.trigger('change');
			}
		})
		.bind('change',function(){
			//get file name
			var fileName = $(this).val().split(/\\/).pop();
			//update the feedback
			uploadFeedback.val(fileName).addClass('customfile-feedback-populated');
		})
		.click(function(){ //for IE and Opera, make sure change fires after choosing a file, using an async callback
			fileInput.data('val', fileInput.val());
			setTimeout(function(){
				fileInput.trigger('checkChange');
			},100);
		});

	//create custom control container
	var upload = $('<label class="file"></label>');
	//create custom control button
	var uploadFeedback = $('<input type="text" class="customfile-feedback" value="Click to add a photo"/>').appendTo(upload);

	//match disabled state
	if(fileInput.is('[disabled]')){
		fileInput.trigger('disable');
	}

	upload.insertAfter(fileInput); //insert after the input
	fileInput.appendTo(upload);

	//return jQuery
	return $(this);
};