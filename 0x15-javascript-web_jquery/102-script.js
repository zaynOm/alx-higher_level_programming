const url = 'https://hellosalut.stefanbohacek.dev/';
$(() => {
  $('#btn_translate').click(() => {
    langCode = $('#language_code').val();
    $.getJSON(url, { lang: langCode }, (data) => {
      $('#hello').text(data.hello);
    });
  });
});
