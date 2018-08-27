$(document).ready(function(){
    $(".close-w3-modal").click(function(){
        $(".w3-modal").hide();
    });
    $("#show_add_client_modal").click(function(){
        $("#add_client_modal").show();
    });
    $("#add_client").click(function(){
        var client_name=$("#client_name_input").val();
        if(!!client_name){
            var data={name:client_name,csrfmiddlewaretoken:$("meta[name='csrf_token']").attr("content")};
            $.ajax({
                url:"add-client",
                type:"POST",
                data:data,
                error:function(e){
                    $(".w3-modal").hide();
                    $(".w3-panel","#alert_modal").addClass("w3-red");
                    $("#alert_msg").html(e.msg);
                    $("#alert_modal").show();
                    $("#client_name_input").val('');
                },
                success:function(r){
                    if(!r.error){
                        $(".w3-modal").hide();
                        $(".w3-panel","#alert_modal").removeClass("w3-red").addClass("w3-blue");
                        $("#alert_msg").html(r.response);
                        $("#alert_modal").show();
                        window.setTimeout(function(){window.location.reload();},2000);
                    }
                    else{
                        $(".w3-modal").hide();
                        $(".w3-panel","#alert_modal").removeClass("w3-blue").addClass("w3-red");
                        $("#alert_msg").html(r.msg);
                        $("#alert_modal").show();
                        $("#client_name_input").val('');
                    }
                }
            });
        }
        else{
            $(".w3-modal").hide();
            $(".w3-panel","#alert_modal").addClass("w3-red");
            $("#alert_msg").html("Name or Fee connot be empty.");
            $("#alert_modal").show();
        }
    });
    $(".delete-client.action").click(function(){
        $(this).prop("disabled",true);
    });
    $(".delete-client.abort").click(function(){
        $(this).siblings(".action").prop("disabled",false);
    });
    $(".delete-client.confirm").click(function(){
        var id=$(this).attr("data-id");
        if(!!id){
            $.ajax({
                url:"remove-client",
                type:"POST",
                data:{id:id,csrfmiddlewaretoken:$("meta[name='csrf_token']").attr("content")},
                error:function(e){
                    $(".w3-modal").hide();
                    $(".w3-panel","#alert_modal").addClass("w3-red");
                    $("#alert_msg").html(e.msg);
                    $("#alert_modal").show();
                    $("#client_name_input").val('');
                },
                success:function(r){
                    if(!r.error){
                        $(".w3-modal").hide();
                        $(".w3-panel","#alert_modal").removeClass("w3-red").addClass("w3-blue");
                        $("#alert_msg").html(r.response);
                        $("#alert_modal").show();
                        window.setTimeout(function(){window.location.reload();},2000);
                    }
                    else{
                        $(".w3-modal").hide();
                        $(".w3-panel","#alert_modal").removeClass("w3-blue").addClass("w3-red");
                        $("#alert_msg").html(r.msg);
                        $("#alert_modal").show();
                        $("#client_name_input").val('');
                    }
                }
            });
        }
        else{
            $(".w3-modal").hide();
            $(".w3-panel","#alert_modal").addClass("w3-red");
            $("#alert_msg").html("No zone selected to remove.");
            $("#alert_modal").show();
        }
    });
});
