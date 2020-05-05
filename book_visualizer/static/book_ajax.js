function switchImage(img, target){
    img.fadeOut(300, function() {
        img.attr('src', target);
    })
    .fadeIn(350);
}

function searchIsbn(isbn){
    return 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn;
}

function restPath(){
    return window.location.origin + '/api/comments/';
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function postComent(comment, onSuccess, onFail){
    comment['csrfmiddlewaretoken'] = window.CSRF_TOKEN;
    console.log(restPath());
    $.ajax({
        type: "POST",
        dataType: "json",
        url: restPath(),
        data: comment,
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        success: onSuccess,
        error: onFail
    });
}

function setBookDetails(img, price, isbn){
    var url = searchIsbn(isbn);
    $.ajax({
    dataType: "json",
    url: url,
    success: (data) => {
        if (0 < data.totalItems){
            data.items.forEach(item => {
                item.volumeInfo.industryIdentifiers.forEach(id => {
                if (id['identifier'] == isbn){
                    switchImage(img, item.volumeInfo.imageLinks.thumbnail);
                    if (item.saleInfo.listPrice != undefined){
                        price.find('span').html(item.saleInfo.listPrice.amount);
                    }
                    return;
                }});
            });
        }
    }});
}

function setBookImg(obj, isbn){
    var url = searchIsbn(isbn);
    $.ajax({
    dataType: "json",
    url: url,
    success: (data) => {
        if (0 < data.totalItems){
            data.items.forEach(item => {
                item.volumeInfo.industryIdentifiers.forEach(id => {
                if (id['identifier'] == isbn){
                    switchImage(obj, item.volumeInfo.imageLinks.thumbnail);
                    return;
                }});
            });
        }
    }});
}