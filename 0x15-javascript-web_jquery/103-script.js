const url = 'https://hellosalut.stefanbohacek.dev/'
$( () => {
    function hello() {
        lang_code = $('#language_code').val()
        $.getJSON(url, {'lang': lang_code}, (data) => {
            console.log(data)
            $('#hello').text(data.hello)
        })
    }
    
    $('#btn_translate').click(() => {
        hello()
    })

    $('#language_code').on('keypress', (e) => {
        if (e.which === 13)
            hello()
    })
})