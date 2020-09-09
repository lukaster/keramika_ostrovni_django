function set_main_picture_background_for_screen_size(window) {
    $(window).on("load resize", function () {
        if (window.innerWidth > 589) {

            if (window.innerHeight < 500) {
                $(".fill-screen").css("height", "500px"); //mobile sideways, table does not overflow background
            } else {

                $(".fill-screen").css("height", window.innerHeight); // big screen, background exactly matches window
            }
        } else {
            $(".fill-screen").css("height", "1150px");//mobile view, table longer than one screen height
        }

        if (window.innerWidth > 751) {
            var display_curr = $('#navbar-template-section').css("display")
            if (display_curr === "none") {
                $('#navbar-template-section').css("display", "flex");
            }
        }
    });

}

function switch_page_language() {
    //console.log('in children switch');

    var language = window.localStorage.getItem('language');
    //console.log(language);

    if (language === 'en') {
        $('.cs-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "none");
        });
        $('.en-lang').each(function (index, item) {
            var $text = $(item);
            $text.css("display", "block");
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

    }

}


