$(document).ready(function(){


$('form.problem_form_ext').on('submit',function(){

	var that = $(this),
		url=that.attr('action'),
		type=that.attr('method'),
		data={};

	that.find('[name]').each(function(index,value){ 
		var that=$(this), 
			name=that.attr('name'); 
			value=that.val(); 
			data[name]=value;
	});

	var submitBool = true;

	if(data.problem_text.length < 10){
		submitBool = false;
		Notifier.warning('Add some more detail!','Too $hort.');
	}
	
	if(submitBool){
	$.ajax({
		url: url,
		type: type,
		data: data,
		success: function(data,textStatus){
				Notifier.success('Help will arrive shortly.','Ticket Submitted');
				if(submitBool){
				$('#submitButton').attr("disabled", true);
				}		
		},
		error: function(xhr,textStatus,errorThrown){
				Notifier.warning('Available tickets are exhuasted for today.', 'Submission Failed');
		}

	});
}




return false;

});

});