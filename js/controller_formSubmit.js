$(document).ready(function(){


$('form.problem_form').on('submit',function(){

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

	if(data.problem_text.length < 10){
		submitBool = false;
		Notifier.warning('Add some more detail!','Too $hort.');
	}

	var submitBool = false;
	var summitEmailPattern =/^[A-Za-z0-9._-]+@(mysummitps|summitsanjose|gmail)+\.[a-z]{3}$/;
	var match = data.student_email.match(summitEmailPattern);
	if(match !== null)
	{
		submitBool = true;
	}
	else
	{
		Notifier.warning('Tried to be funny, punk? Only Summit emails accepted.', 'Bad Email');
	}

	if(submitBool){	
	$.ajax({
		url: url,
		type: type,
		data: data,
		success: function(data,textStatus){
				Notifier.success('Help will arrive shortly.','Ticket Submitted');
				if(submitBool){
				$('input:submit').attr("disabled", true);
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