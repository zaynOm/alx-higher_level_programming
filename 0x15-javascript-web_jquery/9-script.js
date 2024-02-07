const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$.getJSON(url, (data) => {
    $('div#hello').text(data.hello)
})