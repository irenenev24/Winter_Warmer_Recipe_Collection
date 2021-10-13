/* jQuery for  sidenav functionality */

$(document).ready(function(){
    $('.sidenav').sidenav({edge: "right"});
  });

/* jQuery for dropdown menu for category selection */

$(document).ready(function(){
  $('select').formSelect();
});
/*For call to action button */
document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.fixed-action-btn');
  var instances = M.FloatingActionButton.init(elems, {
    direction: 'left'
  });
});