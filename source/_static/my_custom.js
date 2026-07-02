$(document).ready(function(){
    let div_logo = document.getElementsByClassName("wy-side-nav-search")[0];
    let a_logo = div_logo.getElementsByTagName("a");
    a_logo[0].href = "https://tnlearn-documentation.readthedocs.io/en/latest/index.html";
    a_logo[0].target = "_blank";
});