const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, (data) => {
  $.map(data.results, (film) => {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  });
});
