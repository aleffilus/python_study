import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                         "A story of a boy and his toys that come to life",
                         "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://youtube.com/watch?v=5PSNL1qE6VY")

senhor_dos_aneis = media.Movie("O Senhor dos Anéis – A Sociedade do Anel",
                               "Numa terra fantástica e única, chamada Terra-Média, um hobbit (seres de estatura entre 80 cm e 1,20 m, com pés peludos e bochechas um pouco avermelhadas) recebe de presente de seu tio o Um Anel, um anel mágico e maligno que precisa ser destruído antes que caia nas mãos do mal. Para isso o hobbit Frodo (Elijah Woods) terá um caminho árduo pela frente, onde encontrará perigo, medo e personagens bizarros. Ao seu lado para o cumprimento desta jornada aos poucos ele poderá contar com outros hobbits, um elfo, um anão, dois humanos e um mago, totalizando 9 pessoas que formarão a Sociedade do Anel.",
                               "http://megafilmes.org/wp-content/uploads/2016/04/o-senhor-dos-aneis-a-sociedade-do-anel.jpg",
                               "https://www.youtube.com/watch?v=IUerKBZHnBs")

school_of_rock = media.Movie("School of Rock", "Storyline",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "Storyline",
                             "https://upload.wikimedia.org/wikipedia/pt/8/82/Ratatouille_p%C3%B4ster.jpg",
                             "https://www.youtube.com/watch?v=4XAFYbIxkcA")

midnight_in_paris = media.Movie("Meia noite em Paris", "Storyline",
                             "https://upload.wikimedia.org/wikipedia/pt/b/be/Meia-noite-em-paris-poster1.jpg",
                             "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Jogos Vorazes", "Storyline",
                             "https://upload.wikimedia.org/wikipedia/pt/d/dc/The_Hunger_Games.jpg",
                             "https://www.youtube.com/watch?v=4S9a5V9ODuY")

#print(avatar.storyline)
#avatar.show_trailer()
#print(toy_story.storyline)
#print(senhor_dos_aneis.storyline)
#senhor_dos_aneis.show_trailer();

movies = [toy_story, avatar, senhor_dos_aneis, school_of_rock, ratatouille, midnight_in_paris]
movies.append(hunger_games)

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
