window.addEventListener("load", function() {
  $(".toggle-sidebar-left").click(function () {
    $("#sidebar-left").toggleClass("collapsed");
  });

  $(".toggle-sidebar-right").click(function () {
    $("#sidebar-right").toggleClass("collapsed");
  });
}, false);
