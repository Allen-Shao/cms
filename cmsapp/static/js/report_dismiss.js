// this function is to get the csrf token for sending patch request
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrf_token = getCookie("csrftoken");
console.log(csrf_token);

function dismissReport(reportID) {
    $.ajax({
        url: "http://localhost:8888/api/reports/"+reportID+"/",
        headers: {"X-CSRFToken": csrf_token},
        data: '{"status": false}',
        method: "PATCH",
        contentType: 'application/json',
        dataType: "json",
        success: function(data) {
            console.log(data);
        }
    });

    $("#row" + reportID).remove();
}
