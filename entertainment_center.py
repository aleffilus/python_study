import media

toy_story = media.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://pt.wikipedia.org/wiki/Avatar_(filme)#/media/File:Avatar-Teaser-Poster.jpg",
                     "https://youtube.com/watch?v=5PSNL1qE6VY")

print(avatar.storyline)
avatar.show_trailer()