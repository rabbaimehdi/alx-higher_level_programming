
$(function () {
    $("DIV#add_item").click(function () {
        $("UL.my_list").append("<li>Item</li>");
    })
});

$(function () {
    $("DIV#remove_item").click(function () {
        $("UL.my_list").children().last().remove();
    })
});

$(function () {
    $("DIV#clear_list").click(function () {
        $("UL.my_list").empty();
    })
});
