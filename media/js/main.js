$(document).ready(function(){
	$('#inpheader').livequery(function(){
		var obj={};
		obj.v = $(this).val();
		$('.head').removeClass('active').removeClass('current');
		$('#'+obj.v).addClass('active').addClass('current');		
	});
	
        
	
});


$('.cls_sign').live('click',function(){
 var obj={};
 obj.t = $(this);
 //$('.cls_sign').removeClass('plus').addClass('minus');
 obj.t.parent().parent().parent().find('.ulchild').toggle('slow',function(){
	
	if($(this).css('display')== 'none'){
		obj.t.removeClass('minus').addClass('plus');
	}else{
		obj.t.removeClass('plus').addClass('minus');
	}
	});
})


$('h4').on('click','.cls_share',function(){

    var desc= $('#desc_'+$(this).data('id')).text().replace(/\n/g, "").substring(0,100);
    desc = desc + '...';
    var obj = {
        method: 'feed',
        link: window.top.location.href,
        picture: (SC.URL_PREFIX+$('#img_'+$(this).data('id')).attr('src')).replace('//media','/media'),
        name: $('#nm_'+$(this).data('id')).text(),
        caption: 'http://www.hemodiaz.com',
        description: desc
    };

    FB.ui(obj, function(response){})
});