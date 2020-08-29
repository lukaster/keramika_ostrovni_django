function switch_page_language() {
    var language = window.localStorage.getItem('language');
    console.log("language");
    console.log(language);
    if (language == null) {
        language = 'cs'
        alert('variable was null now is');
        console.log(language);
    }
    if (language === 'en') {
        $('.cs-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "none");
        });
        $('.en-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "block");
        });
        $('.more-info-button').each(function (index, item) {
            var $button = $(item);
            $button.text('More information');
        });
    }
    if (language === 'cs') {
        $('.cs-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "block");
        });
        $('.en-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "none");
        });
        $('.more-info-button').each(function (index, item) {
            var $button = $(item);
            $button.text('Více informací');
        });
    }
}

function make_sure_lang_is_set() {
    var language = window.localStorage.getItem('language');
    console.log("making sure fns")
    console.log(language);

    if (language == null) {
        window.localStorage.setItem('language', 'cs');
        var language = window.localStorage.getItem('language');
        alert('making sure, variable was null now is');
        console.log(language);
    }
}

function resize_index_page() {
    $fill_screen = $('.fill-screen');
    var fill_screen_width = $fill_screen.css('width');//
    var fill_screen_height_int = parseInt(fill_screen_width.replace(/px/, "")) * 0.82;
    var fill_screen_height = (fill_screen_height_int) + "px";
    $fill_screen.css("height", fill_screen_height);
    if (window.innerWidth < 768) { //so each screen of mobile device has one section at the time shown
        var total_window_height = window.innerHeight;
        //console.log(total_window_height);
        var navbar_height_int = parseInt($('#navbar-template-section').css('height').replace(/px/, ""));
        //console.log(navbar_height_int);

        $('.text-bubble-col').each(function (index, item) {
            var $text_bubble = $(item);
            //console.log('-----------------------------')
            //console.log($text_bubble)
            //console.log($text_bubble.children('.inside-text-container'));
            var inside_text_container_height_int = parseInt($text_bubble.children('.inside-text-container').css('height').replace(/px/, ""));
            //console.log(inside_text_container_height_int);
            // console.log($text_bubble.css('padding-top'));
            var leftover_window_height = ((total_window_height - navbar_height_int - fill_screen_height_int - inside_text_container_height_int) / 2) + 2;
            //console.log(leftover_window_height);
            if (leftover_window_height > 0) {
                var text_padding = leftover_window_height + "px";
                $text_bubble.css({
                    "padding-top": text_padding,
                    "padding-bottom": text_padding
                });
            }
        });
    }
}
