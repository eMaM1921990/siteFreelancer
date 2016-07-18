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


function Filter(){

}


function checkedID(){
    var rowJsonArray=[];
    $("tbody > tr").each(function() {
          $this = $(this);
          var id = $this.find("input[id=id]:checked");
           var val=0;
            if(id){
                val=id.val();
            }

          if(typeof val!=='undefined' && val!==0){
            rowJsonArray.push({
                "id":val

            });
          }
    });
    return rowJsonArray;

}

function restoreSelected(){
    var inputArr=checkedID();
    if(inputArr.length>0){
        $.ajax({
		url : "/restore_niches/",
		type : "POST",
		dataType : "json",
		data:{
			ids:JSON.stringify(inputArr),
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
		},
		success : function(responseText) {
			if(responseText.status){
                location.reload();
            }else{

            }

		},
		error : function(xhr, errmsg, err) {
			console.log(errmsg);

		}
    });
}


}


function blackListSelectedUsers() {
    var inputArr = checkedID();
    if (inputArr.length > 0) {
        $.ajax({
            url: "/blacklist_user/",
            type: "POST",
            dataType: "json",
            data: {
                ids: JSON.stringify(inputArr),
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            },
            success: function (responseText) {
                if (responseText.status) {
                    location.reload();
                } else {

                }

            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);

            }
        });
    }
}


function RestoreSelectedUsers() {
    var inputArr = checkedID();
    if (inputArr.length > 0) {
        $.ajax({
            url: "/restore_user/",
            type: "POST",
            dataType: "json",
            data: {
                ids: JSON.stringify(inputArr),
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value
            },
            success: function (responseText) {
                if (responseText.status) {
                    location.reload();
                } else {

                }

            },
            error: function (xhr, errmsg, err) {
                console.log(errmsg);

            }
        });
    }
}