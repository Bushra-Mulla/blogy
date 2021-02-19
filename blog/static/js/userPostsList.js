$(document).ready(function () {
  console.log('working')
  // $("nav-link a:first").click(function () {
  //   $('.nav-tabs a[href="#all"]').css({ "color": "red" });
  // });
  // $("nav-link #published").click(function () {
  //   $('div #published').tab('show');
  // });
  // $("a #notPublished").click(function () {
  //   $('.nav-tabs a[href="#notPublished"]').toggleClass(".active");
  // });
  // $("a #refused").click(function () {
  //   $('.nav-tabs a[href="#refused"]').toggleClass(".active");
  // });
  $('.nav-link').click(function (event) {
    // alert(event.target.id);
    // $('div ', event.target.id).addClass(".active");
    alert(event.target.id);
    $('a #', event.target.id).addClass(".active");
    // var x = $(event.target).text();         // active tab
    // var y = $(event.relatedTarget).text();
    // document.write(event.target.text())
    // confirm('fgbhjnklm', event.target.text()) // previous tab
  });
});
