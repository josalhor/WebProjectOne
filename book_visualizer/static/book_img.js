function switchImage(img, target){
    img.fadeOut(300, function() {
        img.attr('src', target);
    })
    .fadeIn(350);
}

function searchIsbn(isbn){
    return 'https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn;
}

function setBookDetails(img, price, isbn){
    var url = searchIsbn(isbn);
    $.ajax({
    dataType: "json",
    url: url,
    success: (data) => {
        if (0 < data.totalItems){
            console.log(data);
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
            console.log(data);
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