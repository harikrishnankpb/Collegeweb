$(document).ready(function()
{"use strict";var header=$('.header');var headerSocial=$('.header_social');var menu=$('.menu');var menuActive=false;var burger=$('.hamburger');setHeader();$(window).on('resize',function()
{setHeader();setTimeout(function()
{$(window).trigger('resize.px.parallax');},375);});$(document).on('scroll',function()
{setHeader();});initMenu();initHomeSlider();initIsotope();initTestimonialsSlider();initScrolling();initInput();function setHeader()
{if($(window).scrollTop()>127)
{header.addClass('scrolled');headerSocial.addClass('scrolled');}
else
{header.removeClass('scrolled');headerSocial.removeClass('scrolled');}}
function initMenu()
{if($('.menu').length)
{var menu=$('.menu');if($('.hamburger').length)
{burger.on('click',function()
{if(menuActive)
{closeMenu();}
else
{openMenu();}});}}
if($('.menu_close').length)
{var close=$('.menu_close');close.on('click',function()
{if(menuActive)
{closeMenu();}});}}
function openMenu()
{menu.addClass('active');menuActive=true;}
function closeMenu()
{menu.removeClass('active');menuActive=false;}
function initHomeSlider()
{if($('.home_slider').length)
{var homeSlider=$('.home_slider');homeSlider.owlCarousel({items:1,autoplay:false,loop:true,nav:false,dots:false,smartSpeed:1200});}}
function initScrolling()
{if($('.home_page_nav ul li a').length)
{var links=$('.home_page_nav ul li a');links.each(function()
{var ele=$(this);var target=ele.data('scroll-to');ele.on('click',function(e)
{e.preventDefault();$(window).scrollTo(target,1500,{offset:-90,easing:'easeInOutQuart'});});});}}
function initIsotope()
{if($('.item_grid').length)
{var grid=$('.item_grid').isotope({itemSelector:'.item',getSortData:{price:function(itemElement)
{var priceEle=$(itemElement).find('.destination_price').text().replace('From $','');return parseFloat(priceEle);},name:'.destination_title a'},animationOptions:{duration:750,easing:'linear',queue:false}});}}
function initTestimonialsSlider()
{if($('.testimonials_slider').length)
{var testSlider=$('.testimonials_slider');testSlider.owlCarousel({animateOut:'fadeOut',animateIn:'flipInX',items:1,autoplay:true,loop:true,smartSpeed:1200,dots:false,nav:false});}}
function initInput()
{if($('.newsletter_input').length)
{var inpt=$('.newsletter_input');inpt.each(function()
{var ele=$(this);var border=ele.next();ele.focus(function()
{border.css({'visibility':"visible",'opacity':"1"});});ele.blur(function()
{border.css({'visibility':"hidden",'opacity':"0"});});ele.on("mouseenter",function()
{border.css({'visibility':"visible",'opacity':"1"});});ele.on("mouseleave",function()
{if(!ele.is(":focus"))
{border.css({'visibility':"hidden",'opacity':"0"});}});});}}});