function setBookImg(obj, isbn){
    var url='https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn;
    $.ajax({
    dataType: "json",
    url: url,
    success: (data) => {
        if (0 < data.totalItems){
            console.log(data);
            data.items.forEach(item => {
                item.volumeInfo.industryIdentifiers.forEach(id => {
                console.log(id['identifier'] == isbn);
                console.log(id['identifier']);
                console.log(isbn);
                if (id['identifier'] == isbn){
                    obj.fadeOut(300, function() {
                        obj.attr('src',item.volumeInfo.imageLinks.thumbnail);
                    })
                    .fadeIn(350);
                }});
            });
        }
    }});
}