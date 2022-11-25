$(document).ready(function(){
	
	$('.cart').click(function(){
		$('.cart-content').fadeToggle();
	});
	
	$('.counter').startTimer();
	
$('.ov-0').owlCarousel({
    rtl:true,
    loop:true,
    margin:10,
    nav:true,
	autoplay:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
});
	
$('.ov1').owlCarousel({
    rtl:true,
    loop:true,
    margin:10,
    nav:true,
	autoplay:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
});

$('.ov2').owlCarousel({
    rtl:true,
    loop:false,
    margin:10,
    nav:true,
	autoplay:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
});
	
$('.ov3').owlCarousel({
    rtl:true,
    loop:false,
    margin:10,
    nav:true,
	autoplay:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:4
        }
    }
});


$('.ov-single').owlCarousel({
    rtl:true,
    loop:false,
    margin:10,
    nav:true,
	autoplay:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:4
        },
        1000:{
            items:4
        }
    }
});

$('.ov-single-two').owlCarousel({
    rtl:true,
    loop:false,
    margin:10,
    nav:true,
	autoplay:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:4
        },
        1000:{
            items:4
        }
    }
});

$(".s-img").elevateZoom();




	});
	