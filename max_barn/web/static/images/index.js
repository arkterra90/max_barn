document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#index').addEventListener('click', () =>  disp_page('home'));
    document.querySelector('#about').addEventListener('click', () => disp_page('about'));
    document.querySelector('#process').addEventListener('click', () => disp_page('process'));
    document.querySelector('#contact').addEventListener('click', () => disp_page('contact'));

    disp_page('home');

});

function disp_page(pageId) {

    const home =  document.querySelector('#home-view');
    const about = document.querySelector('#about-view');
    const process = document.querySelector('#process-view');
    const contact = document.querySelector('#contact-view');

    // Hide all views
    home.style.display = 'none';
    about.style.display = 'none';
    process.style.display = 'none';
    contact.style.display = 'none';

    // Show the selected view
    const page = document.querySelector(`#${pageId}-view`);
    if (page) {
        page.style.display = 'block';
    }
}
