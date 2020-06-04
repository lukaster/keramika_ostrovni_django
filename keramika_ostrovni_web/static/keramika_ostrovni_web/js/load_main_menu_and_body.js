const main_bg_color = '#fcfaf2';
const cdarkblue = '#031740';
var language = window.localStorage.getItem('language');


function set_bg_color() {
    $('body').css({
        "background-color": main_bg_color,
        "border-left-style": "solid",
        "border-left-color": cdarkblue,
        "border-right-style": "solid",
        "border-right-color": cdarkblue,
        "border-bottom-style": "solid",
        "border-bottom-color": cdarkblue
    });
}


function set_lang_en() {
    window.localStorage.setItem('language', 'en');
    console.log("en clicked")
}

function set_lang_cs() {
    window.localStorage.setItem('language', 'cs');
    console.log("cs clicked")
}




