django.jQuery(document).ready(function(){
    function CustomInitInstanceWYSIWYG(ed) {
        var s = ed.settings;
        var realID = '#'+ed.id+"_ifr";
        /*tinymce.dom.Event.add(ed.getWin(), 'focus', function(e) {
            if(django.jQuery(realID)) {
                django.jQuery(realID).css({width:'740px'});
            }
        });
        tinymce.dom.Event.add(ed.getWin(), 'blur', function(e) {
            if(django.jQuery(realID)) {
                django.jQuery(realID).css({width:'740px'});
                django.jQuery("#id_product_desc").val(tinyMCE.get('id_product_desc').getContent());
            }
        });*/
    }
    tinyMCE.init({
        mode : "exact",
        elements: "id_product_desc",
        theme : "simple",
        language : "en",
        theme_simple_toolbar_align: "left",
        init_instance_callback: CustomInitInstanceWYSIWYG
        });
    
    tinyMCE.init({
        mode : "exact",
        elements: "id_aboutus",
        theme : "simple",
        language : "en",
        theme_simple_toolbar_align: "left",
        init_instance_callback: CustomInitInstanceWYSIWYG
        });
});