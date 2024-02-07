const url = 'https://hellosalut.stefanbohacek.dev/';
$(() => {
  function hello () {
    const langCode = $('#language_code').val();
    $.getJSON(url, { lang: langCode }, (data) => {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(() => {
    hello();
  });

  $('#language_code').on('keypress', (e) => {
    if (e.which === 13) {
      hello();
    }
  });
});
