$(function () {

    var myFunction = function () {
        let language = $("INPUT#language_code").val()
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, function (data) {
            $("DIV#hello").html(data.hello);
        })
    }
    $("INPUT#btn_translate").click(myFunction)
    $("INPUT#language_code").keydown((ev)=>{
        if(ev.key == 'Enter') myFunction();
    })
})