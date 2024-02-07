const url = 'https://hellosalut.stefanbohacek.dev/'
$( () => {
    $('#btn_translate').click(() => {
        lang_code = $('#language_code').val()
        $.getJSON(url, {'lang': lang_code}, (data) => {
            console.log(data)
            $('#hello').text(data.hello)
        })
    })
})