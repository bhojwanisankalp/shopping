 //To execute the cart load method at time of page loading
  window.onload = loadCartItems;

  //To track the price per product
  let price_per_item = {}

  $( document ).ready(function() {
    //Set false on first load of the page.
    localStorage.setItem('is_cart_change', false); 
    
    setInterval(function(){ 
      //Check if changes are doene in cart.
      is_cart_change = JSON.parse(localStorage.getItem('is_cart_change')); 
      
      //Load the carts from database again if the changes are performed in cart.
      if(is_cart_change) {
        loadCartItems();
        localStorage.setItem('is_cart_change', false); 
      }
    }, 3000);
  });

  
  /**
   To refresh the cart with recent available products.
  */
  function loadCartItems() {

    products = JSON.parse(localStorage.getItem('cart'))
    if (products !== null) {
        ids = Object.keys(products);
        $.ajax({
        type: "GET",
        url: "/api/cart_products",
        data: {'ids[]': ids},
        success: function (response) {
            if(response.length > 0) {
              setCartRows(response)
            } else {

              $('#cart_items').html(`<div class="row justify-content-center"> 
                    <h3 class="text-grey">
                      Cart Empty
                    </h3>
                  </div>`);
            }
        },
        error: function (response) {
          console.log(response);
        },
      });  
    } else {
      $('#cart_items').html(html);
    }
    
  }

   /**
    To set the cart table with recent available products.
    @param HttpResponse from the API.
  */
  function setCartRows(response) {
    let html = '';
    let total_price = 0;
    response.forEach(element => {
        total_price += getPricePerProductQuantity(element.id, element.price)
        price_per_item[element.id] = element.price;
        //create cards for each product
         var row = ` <div class="row" id="${element.id}">
                        <div class="col-12 col-sm-12 col-md-2 text-center">
                                <img class="img-responsive" src="${element.image_url}" alt="prewiew" width="120" height="80">
                        </div>
                        <div class="col-12 text-sm-center col-sm-12 text-md-left col-md-6">
                            <h4 class="product-name"><strong>${element.name}</strong></h4>
                            <h4>
                                <small>${element.description}</small>
                            </h4>
                        </div>
                        <div class="col-12 col-sm-12 text-sm-center col-md-4 text-md-right row">
                            <div class="col-3 col-sm-3 col-md-6 text-md-right" style="padding-top: 5px">
                                <h6><strong>${element.price} <span class="text-muted">x</span></strong></h6>
                            </div>
                            <div class="col-4 col-sm-4 col-md-4">
                                <div class="quantity">
                                    
                                    <input type="number" step="1" max="99" min="1" value="${products[element.id]}" title="Qty" data-id="${element.id}" data-price="${element.price}" class="qty"
                                           size="4" onchange="changeQuantity(this)">
                                    
                                </div>
                            </div>
                            <div class="col-2 col-sm-2 col-md-2 text-right">
                                <button type="button" class="btn btn-outline-danger btn-xs" data-id="${element.id}" onclick="removeItem(this)">
                                    <i class="fa fa-trash" aria-hidden="true"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                    <hr>`;
          html += row;
    })
      $('#cart_items').html(html);
      $('#total_price').text(total_price);
  }

  /**
    To get the Price per product acccording to the quantity present in cart.
    @param Integer value for product id.
    @param Float value for product price.
    @return Float value for product price.
  */
  function getPricePerProductQuantity(product_id, price) {
      price = price * products[product_id]
      return price;
  }


  /**
    To change product \quantity dynamically.
    @param Target element.
  */
  function changeQuantity(element) {
      current_value = $(element).val();
      product_id = $(element).data('id');
      
      let total_price = 0;
      if (current_value <= 0) {
        current_value = $(element).val(1)
        alert('Invalid Quamtity value');
      }
      
      products[product_id] = current_value;
      localStorage.setItem('cart', JSON.stringify(products));
      
      for(var key in price_per_item) {
          total_price += getPricePerProductQuantity(key, price_per_item[key])
        }
      $('#total_price').text(total_price);
  }

  /**
    To remove product from cart on click.
    @param Target element.
  */
  function removeItem(element){
    var product_id = $(element).data('id');
     confirm = confirm("Are you sure you want to remove this product from the cart?");
     if(confirm) {
        var row = document.getElementById(`${product_id}`);
        row.remove();
        // $(`${product_id}`).detach();
        delete products[product_id];
        total = Object.keys(products).length
        localStorage.setItem('cart', JSON.stringify(products));
        localStorage.setItem('total', JSON.stringify(total));
     }
  }

  /**
    To clear whole the cart on click.
    @param Target element.
  */
  function clearCart(){
    confirm = confirm('Are you sure you want to clear the cart?')
    if(confirm) {
      localStorage.clear()
      localStorage.clear()
      $('#cart_items').html('')
      $('#total_price').text('');
    }
  }



