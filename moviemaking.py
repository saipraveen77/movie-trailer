import fresh_tomatoes
import title
taxiwala=title.Tollywood("Taxiwala",
                         "Move about gost in car",
                         "https://www.25cineframes.com/images/gallery/2018/05/vijay-deverakonda-taxiwala-movie-first-look-ultra-hd-posters/05-Vijay-Deverakonda-TaxiWala-Movie-First-Look-ULTRA-HD-Posters-WallPapers.jpg",
                         "https://www.youtube.com/watch?v=9KN3dbZVRwQ")
geetha_govindam=title.Tollywood("Geetha govindam",
                                "Vijay Govind a young lecturer in a college.",
                                "http://t3.gstatic.com/images?q=tbn:ANd9GcTCOb0CxymxS_oHTVE9RnRqyd3iwF3XXHa9PmWVdxkoA8cQe3SA",
                                "https://www.youtube.com/watch?v=OYK2eJ0oeg8")
Pokiri=title.Tollywood("Pokiri",
                       "Meanwhile, he falls in love with Shruti, an aerobics teacher.",
                       "https://upload.wikimedia.org/wikipedia/en/b/b2/Pokiri_movie_poster.jpg",
                       "https://www.youtube.com/watch?v=rdIwjSBIW4w")

pelli_choopulu=title.Tollywood("Pelli choopulu",
                               "Vijay's father, who is fed up with Vijay's carefree life",
                               "https://upload.wikimedia.org/wikipedia/en/b/b3/Pelli_Choopulu_poster.jpg",
                               "https://www.youtube.com/watch?v=zHO7BuWCHK8")
arjun_reddy=title.Tollywood("Arjun Reddy",
                            "Arjun Reddy is a successful young medical surgeon",
                            "https://cdn-images-1.medium.com/max/1200/1*lKQHFB3b_bxN3lLhIm-RJw.jpeg",
                            "https://www.youtube.com/watch?v=Wcw90XCrgjo")
Mahanati=title.Tollywood("Mahanati",
                         "Savitri, an energetic and jubilant child, grows up to become an actress.",
                         "https://upload.wikimedia.org/wikipedia/en/1/1d/Mahanati_poster.jpg",
                         "https://www.youtube.com/watch?v=eO2EFdOlafI")

movies=[taxiwala,geetha_govindam,Pokiri,arjun_reddy,pelli_choopulu,Mahanati]
fresh_tomatoes.open_movies_page(movies)
