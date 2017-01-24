import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")

edge_of_tomorrow = media.Movie("Edge of Tomorrow",
                               "A story of Major William Cage who has to save Planet Earth from an alien species, after being caught in a time loop.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/Edge_of_Tomorrow_Poster.jpg/220px-Edge_of_Tomorrow_Poster.jpg",
                               "https://www.youtube.com/watch?v=vw61gCe2oqI")

gravity = media.Movie("Gravity",
                      "Story about Dr. Ryan Stone, an engineer on her first time on a space mission, and Matt Kowalski, an astronaut on his final expedition, who have to survive in space after they are hit by debris while spacewalking.",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Gravity_Poster.jpg/220px-Gravity_Poster.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

rustom = media.Movie("Rustom",
                     "A story about Rustom, a naval officer, and Cynthia, his wife, who are happily married. However, their lives change when he discovers her affair and is accused of murdering Vikram, her lover.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Akshay_Kumar%27s-Rustom_poster.jpg/220px-Akshay_Kumar%27s-Rustom_poster.jpg",
                     "https://www.youtube.com/watch?v=L83qMnbJ198")

baaghi = media.Movie("Baaghi",
                     "Baaghi is a Indian martial arts film about Ronny (Tiger Shroff), a rebellious 23-year-old from Delhi who shortly after arriving at a martial arts academy. The troubled young man falls for the girl being wooed by his rival.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/0/07/Baaghi_Hindi_film_poster.jpg/220px-Baaghi_Hindi_film_poster.jpg",
                     "https://www.youtube.com/watch?v=8HQIKJBUsQk")

kick = media.Movie("Kick",
                   "A story about Devi Lal Singh, a typical youth with an anomalous standard of living, who tries to find pleasure in whatever he does. He eventually becomes a thief and dons a new name, Devil.",
                   "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Kick_%282014_film%29_Official_release_poster.jpg/220px-Kick_%282014_film%29_Official_release_poster.jpg",
                   "https://www.youtube.com/watch?v=kNEpMpbmayU")

jatt_and_juliet_2 = media.Movie("Jatt & Juliet 2",
                              "A story about a jatt, Fateh Singh who flies to Canada to retrieve his boss's daughter, Pooja, but things change when he mistakes Pooja's friend who is working in a parlour as Pooja.",
                              "https://upload.wikimedia.org/wikipedia/en/thumb/6/6f/Jatt_and_Juliet_2.jpg/220px-Jatt_and_Juliet_2.jpg",
                              "https://www.youtube.com/watch?v=FtGrababuKo")

barbie_princess_charm_school = media.Movie("Barbie: Princess Charm School",
                                           "A story about Barbie as Blair Willows, a kind-hearted girl who must find an enchanted crown to prove her true identity in this charming and magical princess story!",
                                           "https://upload.wikimedia.org/wikipedia/en/c/c0/Barbie_Princess_Charm_School.jpg",
                                           "https://www.youtube.com/watch?v=FjN4Fh9bOVg")

movies = [toy_story, avatar, edge_of_tomorrow, gravity, rustom, baaghi, kick, jatt_and_juliet_2, barbie_princess_charm_school]

fresh_tomatoes.open_movies_page(movies)

