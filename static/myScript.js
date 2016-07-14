$(document).ready(function() {

	var swiper = new Swiper('.swiper-container', {
        nextButton: '.swiper-button-next',
        prevButton: '.swiper-button-prev',
        pagination: '.swiper-pagination',
        paginationClickable: true,
        // Disable preloading of all images
        preloadImages: false,
        // Enable lazy loading
        lazyLoading: true,
        autoplay: 3000,
        autoplayDisableOnInteraction: false,
        loop: true
    });

    $('.clientCheck').click(function(){
        $('.clientCheck').toggleClass('myCheckboxActive');
    });
    $('.teenlancerCheck').click(function(){
        $('.teenlancerCheck').toggleClass('myCheckboxActive');
    });
    $('.bronzeCheck').click(function(){
        $('.bronzeCheck').toggleClass('myCheckboxActive');
    });
    $('.silverCheck').click(function(){
        $('.silverCheck').toggleClass('myCheckboxActive');
    });
    $('.goldCheck').click(function(){
        $('.goldCheck').toggleClass('myCheckboxActive');
    });
    $('.platinumCheck').click(function(){
        $('.platinumCheck').toggleClass('myCheckboxActive');
    });




    $('.myBioArea').hide();
    $('.bioSave').hide();
    $('.bioEdit').click(function(){
        $('.myBioArea').toggle('slow', function(){

        });
        $('.bioSave').toggle('slow', function(){

        });
    });

    $('.bioSave').click(function(){
        $('.myBioArea').toggle('slow', function(){

        });
        $('.bioSave').toggle('slow', function(){

        });
    });

    

    $('.myTextArea').hide();
    $('.saveButton').hide();
    
    $('.editButton').click(function(){
        $('.myTextArea').toggle('slow', function(){

        });
        $('.saveButton').toggle('slow', function(){

        });
    });

    $('.saveButton').click(function(){
        $('.myTextArea').toggle('slow', function(){

        });
        $('.saveButton').toggle('slow', function(){

        });
    });

    $('.mySkillArea').hide();
    $('.skillSave').hide();
    $('.skillEdit').click(function(){
        $('.mySkillArea').toggle('slow', function(){

        });
        $('.skillSave').toggle('slow', function(){

        });
    });

    $('.skillSave').click(function(){
        $('.mySkillArea').toggle('slow', function(){

        });
        $('.skillSave').toggle('slow', function(){

        });
    });
    
    $(".dropdown-menu li a").click(function(){
      $(this).parents(".dropdown").find('.dropToggle').html($(this).text() + ' <i class="fa fa-caret-down pull-right"></i>');
      $(this).parents(".dropdown").find('.dropToggle').val($(this).data('value'));
    });


      


});