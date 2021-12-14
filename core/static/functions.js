$(".link-inicio").click(function () {
        $('html, body').animate({
            scrollTop: $("#inicio").offset().top
        }, 500);
    });
$(".link-quem-somos").click(function () {
        $('html, body').animate({
            scrollTop: $("#quemsomos").offset().top
        }, 500);
    });
$(".link-equipe").click(function () {
        $('html, body').animate({
            scrollTop: $("#equipe").offset().top
        }, 500);
    });
$(".link-curso").click(function () {
        $('html, body').animate({
            scrollTop: $("#curso").offset().top
        }, 500);
    });
$(".link-aprovados").click(function () {
        $('html, body').animate({
            scrollTop: $("#aprovados").offset().top
        }, 500);
    });
$(".link-parceiros").click(function () {
        $('html, body').animate({
            scrollTop: $("#parceiros").offset().top
        }, 500);
    });
$(".link-contato").click(function () {
        $('html, body').animate({
            scrollTop: $("#contato").offset().top
        }, 500);
    });
aparecer();
       function aparecer(){
         $('.perfil-1').hide();
         $('.pop-up-1').click(function(){
            $('.perfil-1').slideToggle();
          });

         $('.perfil-2').hide();
         $('.pop-up-2').click(function(){
            $('.perfil-2').slideToggle();
          });

         $('.perfil-3').hide();
         $('.pop-up-3').click(function(){
            $('.perfil-3').slideToggle();
          });

         $('.perfil-4').hide();
         $('.pop-up-4').click(function(){
            $('.perfil-4').slideToggle();
          });
       }

$('.parceiros').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 1800,
    prevArrow: $('#parce-prev'),
    nextArrow: $('#parce-next'),
    responsive: [
        {
          breakpoint: 1030,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 780,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 620,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        }
      ]
});
$('.aprovados').slick({
    arrows:false,
    rows: 2, 
    slidesPerRow: 2,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 1800,
    responsive: [
        {
          breakpoint: 1030,
          settings: {
            rows: 2, 
            slidesPerRow: 2,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 780,
          settings: {
            rows: 2, 
            slidesPerRow: 2,
            slidesToScroll: 1,

          }
        },
        {
          breakpoint: 620,
          settings: {
            rows: 2, 
            slidesPerRow: 2,
            slidesToScroll: 1,

            }
        },
        {
          breakpoint: 480,
          settings: {
            rows: 2, 
            slidesPerRow: 1,  
            slidesToScroll: 1,

          }
        }
      ]
});
$('.eaj-carousel').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: false,
    autoplaySpeed: 1800,
    arrows: false,
    dots:true,
    responsive: [
        {
          breakpoint: 1030,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 780,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 620,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
          }
        }
      ]
});
$('.ifrn-carousel').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: false,
    arrows: false,
    dots:true,
    autoplaySpeed: 1800,
    // prevArrow: $('#cli-prev'),
    // nextArrow: $('#cli-next'),
    responsive: [
        {
          breakpoint: 1030,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 780,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 620,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
});
jQuery(document).ready(function(){

jQuery("#Topo").hide();

jQuery('a#Topo').click(function () {
         jQuery('body,html').animate({
           scrollTop: 0
         }, 400);
        return false;
   });

jQuery(window).scroll(function () {
         if (jQuery(this).scrollTop() >250) {
            jQuery('#Topo').fadeIn();
         } else {
            jQuery('#Topo').fadeOut();
         }
     });
});
$(window).on("beforeunload", function() {
        $(window).scrollTop(0);
      });


