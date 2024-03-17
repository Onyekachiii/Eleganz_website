/*
 *****************************************************
 *	CUSTOM JS DOCUMENT                              *
 *	Single window load event                        *
 *   "use strict" mode on                            *
 *****************************************************
 */
$(window).on("load", function() {

    "use strict";

    var preLoader = $('.preloader');
    var faqsAccordion = $('#faqs-accordion');
    var fancybox = $('.fancybox');
    var linksListsItem = $('.links-lists li');
    var cartOpen = $('.cartIcon, .whishlistIcon');
    var userIcon = $('.userIcon');
    var closeCart = $('.closeCart');
    var closeMenu = $('.closeMenu');
    var shoppingCart = $('.shopping-cart');
    var userMenu = $('.user-menu');
    var userMenuLiA = $('.user-menu li a');
    var priceRange = $("#slider-range");
    var amnt = $("#amount");
    var body = $('body');
    var closeNewsLetter = $('.close-news-letter');
    var newsLetterPopup = $('#newsLetterPopup');
    var closeQuickView = $('.close-quick-view');
    var quickViewPopup = $('.quick-view-popup');
    var quickviewBtn = $('.quickview-box-btn');

    // ============================================
    // PreLoader On window Load
    // =============================================
	
	if (preLoader.length) {
		preLoader.addClass('loaderout');
	}
	
    //========================================
    // Accordion 
    //======================================== 	

    if (faqsAccordion.length) {
        faqsAccordion.accordion();
    }

    //========================================
    // LightBox / Fancybox
    //======================================== 	

    if (fancybox.length) {
        fancybox.fancybox();
    }

    //========================================
    // Sidebar List Toggle 
    //======================================== 	

    linksListsItem.on('click', function(e) {

        if ($(this).find('>ul').hasClass('active')) {

            $(this).children('ul').removeClass('active').children('li').slideUp();

            linksListsItem.parent('ul').children('li').removeClass('active');

            $(this).addClass('active');
            if ($(this).hasClass('collapse-link')) {
                $(this).children('a').children('i').removeClass('fa-angle-down');
                $(this).children('a').children('i').addClass('fa-angle-right');
                e.preventDefault();
            }

            e.stopPropagation();
        } else {
            $(this).children('ul').addClass('active').children('li').slideDown();

            linksListsItem.parent('ul').children('li').removeClass('active');
            $(this).addClass('active');
            if ($(this).hasClass('collapse-link')) {
                $(this).children('a').children('i').removeClass('fa-angle-right');
                $(this).children('a').children('i').addClass('fa-angle-down');
            }
            e.stopPropagation();
        }
    });

    //***************************************
    // Mini Cart Settings
    //****************************************

    if (cartOpen.length) {

        closeCart.on('click', function() {
            if ($(this).parent('.shopping-cart').hasClass('active')) {
                $(this).parent('.shopping-cart').removeClass('active');
            }
        });
        cartOpen.on('click', function() {
            if (userMenu.hasClass('active')) {
                userMenu.removeClass('active');
            }
            if ($(this).next('.shopping-cart').hasClass('active')) {
                $(this).next('.shopping-cart').removeClass('active');
            } else if (shoppingCart.hasClass('active')) {
                shoppingCart.removeClass('active');
                $(this).next('.shopping-cart').addClass('active');
            } else {
                $(this).next('.shopping-cart').addClass('active');
            }
        });
    }

    //***************************************
    // User Menu Settings
    //****************************************

    if (userIcon.length) {

        closeMenu.on('click', function() {
            if ($(this).parent('.user-menu').hasClass('active')) {
                $(this).parent('.user-menu').removeClass('active');
            }
        });

        userMenuLiA.on('click', function() {
            if ($(this).parent('li').parent('.user-menu-items').parent('.user-menu').hasClass('active')) {
                $(this).parent('li').parent('.user-menu-items').parent('.user-menu').removeClass('active');
            }
        });

        userIcon.on('click', function() {
            if (shoppingCart.hasClass('active')) {
                shoppingCart.removeClass('active');
            }
            if ($(this).next('.user-menu').hasClass('active')) {
                $(this).next('.user-menu').removeClass('active');
            } else if (userMenu.hasClass('active')) {
                userMenu.removeClass('active');


                $(this).next('.user-menu').addClass('active');
            } else {
                $(this).next('.user-menu').addClass('active');
            }

        });

    }

    //***************************************
    // Newsletter Popup Settings
    //****************************************

    if (newsLetterPopup.length) {
        setTimeout(function() {
            newsLetterPopup.fadeIn();
            newsLetterPopup.addClass('showpopup');
        }, 3000);

        closeNewsLetter.on('click', function(e) {
            e.preventDefault();
            newsLetterPopup.removeClass('showpopup');
        });
    }

    //***************************************
    // Quick View Popup Settings
    //****************************************


    if (quickViewPopup.length) {
        quickviewBtn.on('click', function(e) {
            e.preventDefault();
            var productId = $(this).data('product-id');
            getProductData(productId);
        });
    
        closeQuickView.on('click', function(e) {
            e.preventDefault();
            quickViewPopup.removeClass('showpopup');
        });
    
        // Function to fetch product data based on product ID
        function getProductData(productId) {
            $.ajax({
                url: '/get-product-data/',  // URL of your Django endpoint to fetch product data
                method: 'GET',
                success: function(response) {
                    var product = response.find(item => item.id === productId);
                    updateQuickViewPopup(product);
                },
                error: function(xhr, status, error) {
                    console.error('Failed to fetch product data:', error);
                }
            });
        }
    
        // Function to update Quick View popup with product details
        function updateQuickViewPopup(product) {
            quickViewPopup.addClass('showpopup');
            quickViewPopup.find('.prod-info-section .wa-product-main-image img').attr('src', product.image);
            quickViewPopup.find('.prod-info-section .title-box h2').text(product.title);
            quickViewPopup.find('.prod-info-section .title-box .price span').text(product.price);
            quickViewPopup.find('.prod-info-section .title-box .price span').text(product.old_price);
            // Update other product details as needed
        }
    }
    
    

    //***************************************
    // Price Rannge Filter Settings
    //****************************************

    if (priceRange.length) {
        priceRange.slider({
            range: true,
            min: 0,
            max: 500,
            values: [75, 300],
            slide: function(event, ui) {
                amnt.val("$" + ui.values[0] + " - $" + ui.values[1]);
            }
        });

        amnt.val("$" + priceRange.slider("values", 0) +
            " - $" + priceRange.slider("values", 1));
    }

    //***************************************
    // Checkout Page Effect function Calling
    //****************************************

    checkoutPageEffect();

    //***************************************
    // Map initialization function Calling
    //****************************************

    initMap();


    //***************************************
    // All Owl Carousel function Calling
    //****************************************

    owlCarouselInit();



}); // End of the window load event


//***************************************
// Checkout Page Effect function
//****************************************

function checkoutPageEffect() {
    "use strict";

    var showlogin = $('.showlogin');
    var loginDiv = $('.login');
    var showcoupon = $('.showcoupon');
    var checkout_coupon = $('.checkout_coupon');
    var differentAddress = $('#ship-to-different-address-checkbox');
    var shippingFields = $('.shipping-fields');
    var createAccountCheck = $('#createaccount');
    var createAccount = $('.create-account');
    var paymentMethodCheque = $('#payment_method_cheque');
    var paymentBox = $('.payment_box.payment_method_cheque');
    var paymentMethodPaypal = $('#payment_method_paypal');
    var paymentBoxPaypal = $('.payment_box.payment_method_paypal');


    showlogin.on('click', function(e) {
        e.preventDefault();
        loginDiv.slideToggle("slow");
    });

    showcoupon.on('click', function(e) {
        e.preventDefault();
        checkout_coupon.slideToggle("slow");
    });

    differentAddress.change(function() {
        if (this.checked) {
            shippingFields.slideToggle('slow');
        } else {
            shippingFields.slideToggle('slow');
        }
    });

    createAccountCheck.change(function() {
        if (this.checked) {
            createAccount.slideToggle('slow');
        } else {
            createAccount.slideToggle('slow');
        }
    });


}

//***************************************
// Contact Page Map
//****************************************  

function initMap() {
    "use strict";

    var mapDiv = $('#gmap_canvas');

    if (mapDiv.length) {
        var myOptions = {
            zoom: 10,
            scrollwheel: false,
            draggable: true,
            center: new google.maps.LatLng(-37.81614570000001, 144.95570680000003),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById('gmap_canvas'), myOptions);
        var marker = new google.maps.Marker({
            map: map,
            position: new google.maps.LatLng(-37.81614570000001, 144.95570680000003)
        });
        var infowindow = new google.maps.InfoWindow({
            content: '<strong>Envato</strong><br>Envato, King Street, Melbourne, Victoria<br>'
        });
        google.maps.event.addListener(marker, 'click', function() {
            infowindow.open(map, marker);
        });

        infowindow.open(map, marker);
    }

}

//***************************************
// All owl Carousels 
//****************************************   

function owlCarouselInit() {

    "use strict";

    //==========================================
    // owl carousels settings
    //===========================================

    var home1MainSlider = $('#home1-main-slider');
    var bestSeller = $('#best-seller');
    var homeBlogCarousel = $("#home-blog-carousel");
    var waPartnerCarousel = $('.wa-partner-carousel');
    var waSlideImage = $('#wa-slide-image');
    var advertSingle = $('.advert-single');
    var instaGallery = $('#insta-gallery');

    if (home1MainSlider.length) {
        home1MainSlider.owlCarousel({
            autoPlay: true,
            items: 1,
            singleItem: true,
            navigation: true,
            pagination: true,

        });
    }
    if (advertSingle.length) {
        advertSingle.carousel({
		  interval: 4000,
		  pause: false
		})
    }

    if (bestSeller.length) {
        bestSeller.owlCarousel({
            autoPlay: false,
            items: 4,
            navigation: true,
            pagination: false,
            itemsDesktop: [1199, 4],
            itemsDesktopSmall: [979, 3]

        });
    }

    if (homeBlogCarousel.length) {
        homeBlogCarousel.owlCarousel({
            autoPlay: false,
            items: 3,
            navigation: true,
            pagination: false,
            itemsDesktop: [1199, 3],
            itemsDesktopSmall: [979, 3]

        });
    }

    if (waPartnerCarousel.length) {
        waPartnerCarousel.owlCarousel({
            autoPlay: true,
            items: 6,
            itemsDesktop: [1199, 5],
            itemsDesktopSmall: [979, 4],
            itemsTablet: [768, 3],
            itemsMobile: [767, 2],
            margin: 0,
            navigation: false,
            pagination: false

        });
    }
    if (waSlideImage.length) {
        waSlideImage.owlCarousel({
            autoPlay: true,
            items: 4,
            itemsDesktop: [1199, 4],
            itemsDesktopSmall: [979, 3],
            itemsMobile: [979, 3],
            margin: 5,
            navigation: true,
            pagination: false
        });
    }
    if (instaGallery.length) {
        instaGallery.owlCarousel({
            autoPlay: true,
            items: 5,
            itemsDesktop: [1199, 4],
            itemsDesktopSmall: [979, 3],
            itemsMobile: [979, 2],
            margin: 0,
            navigation: true,
            pagination: false
        });
    }

}

/*
*************************
*	END OF THE JS 		*
*	DOCUMENT            *
*************************
*/