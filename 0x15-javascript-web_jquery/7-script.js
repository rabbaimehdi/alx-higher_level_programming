// $.ajax({
//     type:'GET',
//     url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
//     success: function(data){
//         $("DIV#character").html(data["name"])
//     }
// })

$.get("https://swapi-api.alx-tools.com/api/people/5/?format=json", function(data){
    $("DIV#character").html(data["name"])
})