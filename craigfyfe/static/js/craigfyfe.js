

function carousels() {
  $('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    items: 1,
    autoHeight: true,
    center:true,
    animateOut: 'fadeOut',
    adnimateIn: 'fadeIn',
    autoplay: true,
    //autoplayTimeout:1000,
    autoplayHoverPause: true,
    lazyLoad: true,

  })
}
$('.container.main').imagesLoaded( function() {
  // images have loaded
    carousels();
});

function navSwtich() {
  if ($('.nav-wrapper').hasClass('nav-wrapper-on')) {
    $('a.close-nav').show();
  }
  else {
    $('a.close-nav').hide();
  }
}

navSwtich();

function toggleNav() {
  $('a.toggle-nav').click(function () {
    $('.nav-wrapper').toggleClass('nav-wrapper-on');
    $('a.close-nav').css('display', 'block');
    navSwtich();
  });
  $('a.close-nav').click(function () {
    $('.nav-wrapper').toggleClass('nav-wrapper-on');
    navSwtich();
  });

}

toggleNav();

function masonryGrid(wrapper) {
  $(wrapper).imagesLoaded(function () {
    $(wrapper).masonry({
      // options
      itemSelector: '.masonry-grid-item',

    });
  });
}

masonryGrid('.masonry-grid');


function colorActiveMenu(){
  var colors = new Array(['red'],['green'],['blue'],['yellow'],['purple'],['orange'],['DeepPink'],['DarkViolet'],['Turquoise']);
  var rand = colors[Math.floor(Math.random() * colors.length)];
  $('.navigation li.active a').css('border-bottom','2px solid').css('border-color', rand);
  //$('.navbar-toggle').css('background-color', rand);
} colorActiveMenu();

function menuItemHover(){

  $('.navigation li:not(.active) a').hover(function(){
    var colors = new Array(['red'],['green'],['blue'],['yellow'],['purple'],['orange'],['DeepPink'],['DarkViolet'],['Turquoise']);
    var rand = colors[Math.floor(Math.random() * colors.length)];
    $(this).css('border-bottom','2px solid');
    $(this).css('border-color',rand);
    $(this).css('border-color',rand);
  }, function () {
    $(this).css('border-color','#eee').css('border-bottom','0px');
  });
} menuItemHover();

function randomFooter(){
  var num = new Array(['1'],['2'],['3'],['4'],['5'],['6'],['7'],['8']);
  var rand = num[Math.floor(Math.random() * num.length)];

  $('footer.footer').css('background-image', 'url(/static/img/footer/' + rand + '.png)');
} randomFooter();