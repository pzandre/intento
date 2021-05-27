$("#institute").change(function () {
    const url1 = $("#discipline").attr("discipline-queries-url");  // get the url of the `load_cities` view#}
    const url2 = $("#teacher").attr("teacher-queries-url");  // get the url of the `load_cities` view#}
    const instituteId = $(this).val();  // get the selected institute ID from the HTML input
    $.ajax({                                  // initialize an AJAX request
        url: url1,                    // set the url of the request (= ajax/load-discipline-details/ )
        data: { 'institute_id': instituteId },       // add the institute id to the GET parameters
        success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#discipline").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });
    $.ajax({
        url: url2,
        data: { 'institute_id': instituteId },
        success: function (data) {
            $("#teacher").html(data);
        }
    })
});

$("#discipline").change(function () {
    const url = $("#macro_content").attr("macro-queries-url");  // get the url of the `load_cities` view#}
    const disciplineID = $(this).val();  // get the selected institute ID from the HTML input
    $.ajax({                                  // initialize an AJAX request
        url: url,                    // set the url of the request (= ajax/load-discipline-details/ )
        data: { 'discipline_id': disciplineID },       // add the institute id to the GET parameters
        success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#macro_content").html(data);  // replace the contents of the city input with the data that came from the server
            // $("#macro-content").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });
});

$("#macro_content").change(function () {
    const url = $("#micro_content").attr("micro-queries-url");  // get the url of the `load_cities` view#}
    const macro_contentID = $(this).val();  // get the selected institute ID from the HTML input
    $.ajax({                                  // initialize an AJAX request
        url: url,                    // set the url of the request (= ajax/load-discipline-details/ )
        data: { 'disciplinemacrocontent_id': macro_contentID },       // add the institute id to the GET parameters
        success: function (data) {   // `data` is the return of the `load_cities` view function
            $("#micro_content").html(data);  // replace the contents of the city input with the data that came from the server
        }
    });
});
