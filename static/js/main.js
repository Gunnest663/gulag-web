// sticky header
$(window).scroll(() => {
    var header = document.getElementById("navbar");
    var sticky = header.offsetTop;

    if (window.pageYOffset > sticky) {
        header.classList.add("minimized");
    } else {
        header.classList.remove("minimized");
    }
});

//toggle navbar for mobile
function togglenavbar() {
    document.getElementById('navbar').classList.toggle("is-active");
    document.getElementById('navbar-burger').classList.toggle("is-active");
}

var modal = document.querySelector('.modal');  // assuming you have only 1
modal.querySelector('.modal-background').addEventListener('click', function (e) {
    e.preventDefault();
    modal.classList.remove('is-active');
});