/**
 * Created by emam on 15/07/16.
 */

function HandleNichRequest(){
    var action=$('#nichActionType').val();
    switch (parseInt(action)){
        case 1:
            removeSelectedNich();
            break;
        case 0:
            break;
        default :
            break;
    }

}

function removeSelectedNich(){
    var id=$('#nicheID:checked').val();
    $.ajax({
		url : "/delete_niches/",
		type : "POST",
		dataType : "json",
		data:{
			id:id, csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
		},
		success : function(responseText) {
            console.log(responseText);
			if(responseText.status){

                $('#'+id).remove();
            }else{

            }

		},
		error : function(xhr, errmsg, err) {
			console.log(errmsg);

		}
	});
}

function NichTableFilter(){
    $.ajax({
		url : "/delete_niches/",
		type : "POST",
		dataType : "json",
		data:{
			id:id
		},
		success : function(responseText) {
			if(responseText.status){
                $('').remove();
            }else{

            }

		},
		error : function(xhr, errmsg, err) {
			console.log(errmsg);

		}
	});
}