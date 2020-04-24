function setBookImg(obj, isbn10){
    var url='https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn10;
    $.ajax({
    dataType: "json",
    url: url,
    success: (data) => {
        data.items.forEach(item => {
            item.volumeInfo.industryIdentifiers.forEach(id => {
            if (id['type'] == 'ISBN_10' && id['identifier'] == isbn10){
                console.log(id);
                obj.fadeOut(400, function() {
                    obj.attr('src',item.volumeInfo.imageLinks.thumbnail);
                })
                .fadeIn(400);
            } 
            });
        });
    }});
}