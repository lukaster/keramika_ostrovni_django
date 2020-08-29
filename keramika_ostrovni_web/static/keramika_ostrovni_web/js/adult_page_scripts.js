function add_time_table() {
    var language = window.localStorage.getItem('language');
    console.log("language");
    console.log(language);
    if (language == null) {
        language = 'cs';
        //console.log('variable was null now is');
        //console.log(language);
    }
    var table_filepath = '';
    //console.log(language);
    if (language === 'en') {
        table_filepath = '../templates/time_table_adults_en.html';
    }
    if (language === 'cs') {
        table_filepath = '../templates/time_table_adults_cs.html';
    }
    $.get(table_filepath, function (data, status) {
        var $data = $(data);

        $('#time_table').html($data.unwrap());
    });
    //console.log("table loaded")
}


function switch_page_language() {
    //console.log('in adults switch');

    var language = window.localStorage.getItem('language');
    //console.log(language);
    //add_time_table();
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
