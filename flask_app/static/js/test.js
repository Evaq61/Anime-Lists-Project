var anime = document.querySelector(".anime")
var anime_id = anime.getAttribute("anime_id")
console.log(anime_id);


fetch(`https://api.jikan.moe/v3/anime/${anime_id}`)
.then(response => response.json())
.then(data => {
    console.log(data);
    anime.innerText = data["title"]
    let synopsis = document.querySelector('.synopsis')
    synopsis.innerText = data["synopsis"]
    let episode_count = document.querySelector('.episode_count')
    episode_count.innerText = "Number of episodes: " + data['episodes'] 
    let status = document.querySelector('.status')
    status.innerText = data['status']
    let span = document.querySelector(".anime_img")
    span.innerHTML = `<img src="${data['image_url']}" alt="Test">`
})