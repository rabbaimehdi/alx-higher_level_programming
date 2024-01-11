$(function () {

    $("#btn_translate").click(function () {
        let language = $("#language_code").val()
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, function (data) {
            $("#hello").html(data.hello);
        })
    })
})