const getAlbum = () => {
  console.log('button clicked!')
  fetch('/album')
    .then(res => res.json())
    .then(body => {
      console.log(body)
      const el = document.getElementById('album-info')
      el.src = body.image.urls.regular
    })
    .catch(err => console.log(err))
}

console.log('script loaded')