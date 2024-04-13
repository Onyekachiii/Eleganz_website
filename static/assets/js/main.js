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
    var closeQuickView2 = $('.close-quick-view2');
    var quickView2Popup = $('.quick-view2-popup');
    var quickview2Btn = $('.quickview2-box-btn');

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


    // if (quickView2Popup.length) {
    //     quickview2Btn.on('click', function(e) {
    //         e.preventDefault();
    //         var paymentMethod = document.querySelector('input[name="payment_method"]:checked').value;
    //         if (paymentMethod === 'cheque') {
    //             modal.style.display = "block";
    //         } else {
    //             document.getElementById("checkoutForm").submit();
    //             }
    //     });
    
    //     closeQuickView2.on('click', function(e) {
    //         e.preventDefault();
    //         quickView2Popup.removeClass('showpopup');
    //     });
    
    //     // Function to fetch product data based on product ID
    //     function getProductData(productId) {
    //         $.ajax({
    //             url: '/get-product-data/',  // URL of your Django endpoint to fetch product data
    //             method: 'GET',
    //             success: function(response) {
    //                 var product = response.find(item => item.id === productId);
    //                 updateQuickView2Popup(product);
    //             },
    //             error: function(xhr, status, error) {
    //                 console.error('Failed to fetch product data:', error);
    //             }
    //         });
    //     }
    
    //     // Function to update Quick View popup with product details
    //     function updateQuickView2Popup(product) {
    //         quickView2Popup.addClass('showpopup');
    //         quickView2Popup.find('.prod-info-section .wa-product-main-image img').attr('src', product.image);
    //         quickView2Popup.find('.prod-info-section .title-box h2').text(product.title);
    //         quickView2Popup.find('.prod-info-section .title-box .price span').text(product.price);
    //         quickView2Popup.find('.prod-info-section .title-box .price span').text(product.old_price);
    //         // Update other product details as needed
    //     }
    // }

    
    
    

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

console.log("Hello World from function.js!")


$(document).ready(function() {
    console.log("I'm in")

    $(document).on("click", ".add-to-wishlist", function(){
        let product_id = $(this).attr("data-product-item");
        let this_val = $(this);
    
        console.log("PRODUCT ID: ", product_id);
    
        $.ajax({
            url: '/add-to-wishlist/',
            data: {
                'id': product_id,
            },
            dataType: 'json',
            beforeSend: function(){
                console.log("Adding to wishlist...");
            },
            success: function(response){
                this_val.html("✓");
                if (response.bool === true){  // Corrected to response.bool
                    console.log("Added to wishlist");
                }
            }
        });
    });
    

    // Removing from wishlist
    $(document).on("click", ".delete-wishlist-product", function(){
        let wishlist_id = $(this).attr("data-wishlist-product");
        let this_val = $(this);

        console.log("WISHLIST ID: ", wishlist_id);

        $.ajax({
            url: "/remove-from-wishlist/",
            data: {
                'id': wishlist_id,
            },
            dataType: 'json',
            beforeSend: function(){
                console.log("Removing from wishlist...");
            },
            success: function(response){
                location.reload()
                $("#wishlist-list").html(response.data);
                
            }
        });
    });


    $(".add-to-cart-btn").on("click", function(){
        let this_val = $(this);
        let index = this_val.attr("data-index");
        let quantity = $(".product-quantity-"+ index).val();
        let product_title = $(".product-title-"+ index).val();
        let product_image = $(".product-image-"+ index).val();
        let product_pid = $(".product-pid-"+ index).val();
        let product_id = $(".product-id-"+ index).val();
    
        // Modify this line to fetch the price using the correct class
        let product_price = $("#current-product-price-"+ index).text(); 
    
        console.log("PRODUCT ID: ", product_id);
        console.log("PRODUCT PID: ", product_pid);
        console.log("PRODUCT QUANTITY: ", quantity);
        console.log("PRODUCT IMAGE: ", product_image);
        console.log("PRODUCT TITLE: ", product_title);
        console.log("PRODUCT PRICE: ", product_price);
    
        $.ajax({
            url: '/add-to-cart',
            data: {
                'id': product_id,
                'pid': product_pid,
                'qty': quantity,
                'image': product_image,
                'title': product_title,
                'price': product_price
            },
            dataType: 'json',
            beforeSend: function(){
                console.log('Adding products to cart...');
            },
            success: function(response){
                this_val.html("✓");
                console.log('Added products to cart!');
                $(".cart-items-count").text(response.totalcartitems);
            }
        });
    });
    

   
    
    
    $(".delete-product").on("click", function(){
        let product_id = $(this).attr("data-product");
        let this_val = $(this);
        console.log("PRODUCT ID: ", product_id);
    
        $.ajax({
            url: "/delete-from-cart",
            data: {
                "id": product_id,
            },
            dataType: 'json',
            beforeSend: function(){
                this_val.hide();
            },
            success: function(response){
                this_val.show();
                $(".cart-items-count").text(response.totalcartitems);
                location.reload()
                $("#cart-list").html(response.data); // Update the cart list
            }
        });
    });
    
    // To update items from cart page
    
    $(".update-product").on("click", function(){
    
        let product_id = $(this).attr("data-product")
        let this_val = $(this)
        let product_qty = $(".product-qty-"+ product_id).val()
    
        console.log("PRODUCT ID: ", product_id);
        console.log("PRODUCT QTY: ", product_qty);
    
        $.ajax({
            url:'/update-cart',
            data:{
                'id':product_id,
                'qty':product_qty,
            },
            dataType:'json',
            beforeSend:function(){
                this_val.hide()
            },
            success:function(response){
                this_val.show()
                $(".cart-items-count").text(response.totalcartitems)
                location.reload()
                $("#cart-list").html(response.data)
            }
        })
    
    });


    // Get the modal
  var modal = document.getElementById('bankTransferModal');

  // Get the button that opens the modal
  var btn = document.getElementById("placeOrderButton");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close")[0];

  // When the user clicks the button, open the modal 
  btn.onclick = function() {
    var paymentMethod = document.querySelector('input[name="payment_method"]:checked').value;
    if (paymentMethod === 'cheque') {
      modal.style.display = "block";
    } else {
      document.getElementById("checkoutForm").submit();
    }
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    modal.style.display = "none";
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }

  // Handle the "Payment Made" button click
  document.getElementById("paymentMadeButton").onclick = function() {
    var formData = new FormData();
    formData.append('paymentEvidence', document.getElementById('paymentEvidence').files[0]);

    fetch('/process_payment/', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.ok) {
          window.location.href = '/order-completed/';
        } else {
          alert('Failed to submit payment evidence. Please try again.');
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Failed to submit payment evidence. Please try again.');
      });
  }

    

});
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


    loginDiv.hide();
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
            autoPlay: true,
            items: 5,
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