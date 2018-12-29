layui.define(['layer', 'element'], function(exports){

  var $ = layui.jquery
  ,layer = layui.layer
  ,element = layui.element
  ,device = layui.device();

  //阻止IE7以下访问
  if(device.ie && device.ie < 10){
    layer.alert('如果您非得使用 IE 浏览器,那么请使用 IE10+');
  }

  //搜索区域固定在上
  var topbar = $('.search-nav'),fixTop = function(){
    var top = $(window).scrollTop();
    if(top > 60){
      topbar.addClass('scroll');
    } else {
      topbar.removeClass('scroll');
    }
  };

  fixTop(), $(window).on('scroll', fixTop);


});

