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

function set_menu_color(menu_item) {
    menu_item.css({
        "color": cdarkblue
    });
}

function set_lang_en() {
    window.localStorage.setItem('language', 'en');
    //console.log("en clicked")
}

function set_lang_cs() {
    window.localStorage.setItem('language', 'cs');
   // console.log("cs clicked")
}


function make_sure_lang_is_set() {
    var language = window.localStorage.getItem('language');
    console.log("making sure fns")
    console.log(language);

    if (language == null) {
        window.localStorage.setItem('language', 'cs');
        var language = window.localStorage.getItem('language');
        console.log('making sure, variable was null now is');
        console.log(language);
    }
}

function menu_hover_dropdowns() {
    var screen_size = 'small';
    $(window).on("load resize", function () {
        if (window.innerWidth > 767) {
            $(".children_menu").removeClass('dropdown-toggle')
            //$("#children_drop_link_en").removeClass('dropdown-toggle')
            $(".language_menu").removeClass('dropdown-toggle')
            //$("#language_drop_link_en").removeClass('dropdown-toggle')

            screen_size = 'large';
            var is_children_hovered = false;
            var $children_menu = $('#children-menu');
            $children_menu.on('click', function () {
                window.location.href = "/deti";
            });
            $children_menu.on('mouseleave', function () {
                is_children_hovered = false
                $children_menu.children('.dropdown-menu').css({'display': 'block'});
                setTimeout(function () {
                    if (is_children_hovered == false) {
                        $children_menu.children('.dropdown-menu').css({'display': 'none'});
                    }
                }, 300);
            });
            $children_menu.on('mouseenter', function () {
                is_children_hovered = true;
                $(this).children('.dropdown-menu').css({'display': 'block'})
            })


            var is_user_nav_item_hovered = false;
            var $user_nav_item = $('#user-nav-item');
            var $user_dropdown_menu = $('#user-dropdown-menu')
            $user_nav_item.on('mouseleave', function () {
                is_user_nav_item_hovered = false;
                $user_dropdown_menu.css({'display': 'block'});
                setTimeout(function () {
                    if (is_user_nav_item_hovered == false) {
                        $user_dropdown_menu.css({'display': 'none'});
                    }
                }, 300);
            });
            $user_nav_item.on('mouseenter', function () {
                is_user_nav_item_hovered = true;
                $user_dropdown_menu.css({'display': 'block'})
            });

            var is_language_hovered = false;
            var $language_nav_item = $('#language_drop-li');
            var $language_dropdown_menu = $('#language-dropdown')
            $language_nav_item.on('mouseleave', function () {
                is_language_hovered = false;
                $language_dropdown_menu.css({'display': 'block'});
                setTimeout(function () {
                    if (is_language_hovered == false) {
                        $language_dropdown_menu.css({'display': 'none'});
                    }
                }, 300);
            });
            $language_nav_item.on('mouseenter', function () {
                is_language_hovered = true;
                $language_dropdown_menu.css({'display': 'block'})
            })
        } else {
            if (screen_size === 'large') {
                screen_size = 'small';
                location.reload();
                $(".children_menu").addClass('dropdown-toggle');
                //$("#children_drop_link_en").addClass('dropdown-toggle')
                $(".language_menu").addClass('dropdown-toggle');
                //$("#language_drop_link_en").addClass('dropdown-toggle');

            }
        }
    });
}



function manage_user_dropdown(userName) {

    var language = window.localStorage.getItem('language');
    //console.log(language);
    if (language == null) {
        language = 'cs'
        //console.log('variable was null now is');
        //console.log(language);
    }
    console.log(userName);
    if (userName === "") {
        $('.user-dropdown-item').each(function (index, item) {
            var $drop_item = $(item);
            $drop_item.css("display", "none");
        });

        $('.no-user-dropdown-item').each(function (index, item) {
            var $drop_item = $(item);
            $drop_item.css("display", "block");
            console.log($drop_item.text());
            console.log(language);

            if (language === 'en') {
                if ($drop_item.hasClass('cs-lang')) {
                    $drop_item.css("display", "none");
                }
            }
            if (language === 'cs') {
                if ($drop_item.hasClass('en-lang')) {
                    $drop_item.css("display", "none");
                }
            }

        });
    } else {
        $('.user-dropdown-item').each(function (index, item) {
            var $drop_item = $(item);
            $drop_item.css("display", "block");
            if (language === 'en') {
                if ($drop_item.hasClass('cs-lang')) {
                    $drop_item.css("display", "none");
                }
            }
            if (language === 'cs') {
                if ($drop_item.hasClass('en-lang')) {
                    $drop_item.css("display", "none");
                }
            }

        });
        $('.no-user-dropdown-item').each(function (index, item) {
            var $drop_item = $(item);
            $drop_item.css("display", "none");
        });
    }
}

