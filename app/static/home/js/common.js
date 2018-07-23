$(function(){


    $('.checkbox').click(function () {
       if($(this).hasClass('active')){
           $(this).removeClass('active');
           $(this).find('input').val(0);
       }else{
           $(this).addClass('active');
           $(this).find('input').val(1);
       }
    });

    var tmp = 1

    $('#search_icon').click(function(){
        if(tmp){
            $('header .nav').css('display',"none");
            $('.search_from').css('display',"block");
            $(this).css('display',"none");
            tmp = 0
        }else{
            $('header .nav').css('display',"block");
            $('.search_from').css('display',"none");
            $(this).css('display',"block");
            tmp = 1
        }

    })

    $('.close_search_icon').click(function(){
            $('header .nav').css('display',"block");
            $('.search_from').css('display',"none");
            $('#search_icon').css('display',"block");
            tmp = 1;
    })

    $("input[name=search]").keydown(function(e){

        if (e.keyCode == "13") {
            if ($(this).val() !== "") {
                window.location.href = "?keywords="+ $(this).val();
                // alert($(this).val())
            };
        };

    })


})