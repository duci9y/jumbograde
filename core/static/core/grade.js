window.addEventListener("load", function() {
  function toggleSidebar(side) {
    if (side !== "left" && side !== "right") {
      return false;
    }

    var left = $("#sidebar-left"),
        right = $("#sidebar-right"),
        content = $("#content"),
        openSidebarsCount = 0,
        contentClass = "";
    
    // toggle sidebar
    if (side === "left") {
      left.toggleClass("collapsed");
    } else if (side === "right") {
      right.toggleClass("collapsed");
    }
    
    // determine number of open sidebars
    if (!left.hasClass("collapsed")) {
      openSidebarsCount += 1;
    }
    
    if (!right.hasClass("collapsed")) {
      openSidebarsCount += 1;
    }
    
    // determine appropriate content class
    if (openSidebarsCount === 0) {
      contentClass = "col-md-12";
    } else if (openSidebarsCount === 1) {
      contentClass = "col-md-10";
    } else {
      contentClass = "col-md-8";
    }
    
    // apply class to content
    content.removeClass("col-md-12 col-md-10 col-md-8").addClass(contentClass);
  }

  $(".toggle-sidebar-left").click(function () {
    toggleSidebar("left");
  });

  $(".toggle-sidebar-right").click(function () {
    toggleSidebar("right");
  });
}, false);
