label iw_test:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание:\nТестовый полигон")
    $ persistent.sprite_time = "day"

    scene bg int_bus
    "..."
    
# ТЕСТИРОВАНИЕ КОДА    
    scene bg black with dissolve2
    play ambience ambience_camp_center_day
    play music iw_feelgood
    $ renpy.pause(2)
    scene bg ext_camp_entrance_day with dissolve:
        promenad
    $ renpy.pause(3)
    scene bg ext_clubs_day with dissolve:
        promenad
    $ renpy.pause(3)
    scene bg ext_square_day with dissolve:
        promenad
    $ renpy.pause(3)
    scene bg ext_dining_hall_away_day with dissolve:
        promenad
    $ renpy.pause(3)
    scene bg ext_beach_day with dissolve
    play ambience ambience_lake_shore_day
    $ renpy.pause(2)
    
    show ai grin1 jeans tal
    show sh normal pioneer at left
    show mt normal pioneer at right
    ai "grin1"

    scene bg ext_camp_entrance_day
    show ai surprise uniformb srt
    show mi normal pioneer at left
    show yo normal shirt at right
    ai "surprise"

    scene bg ext_square_day_city
    show ai scary little1 lng
    show uv normal at left
    show gl normal jeans at right
    ai "scary"

    scene bg ext_washstand_day
    show ai sad uniformw srt
    show un normal pioneer at left
    show sl normal pioneer at right
    ai "sad"

    scene bg int_dining_hall_people_day
    show ai shy1 jeans srt
    show pi at left
    show uv normal at right
    ai "shy1"

    scene bg ext_path2_day
    show ai guilty little1 tal
    show el normal pioneer at left
    show pi at right
    ai "guilty"

    scene bg ext_square_day_city
    show ai evilsmile1 uniformw lng
    show mi normal pioneer at left
    show sh normal pioneer at right
    ai "evilsmile1"

    scene bg ext_washstand_day
    show ai happy jeans srt
    show mz normal pioneer at left
    show el normal pioneer at right
    ai "happy"

    scene bg int_musclub_day
    show ai laugh1 pink srt
    show mz normal pioneer at left
    show mi normal pioneer at right
    ai "laugh1"

    scene bg int_bus
    show ai smile1 pink lng
    show mt normal pioneer at left
    show un normal pioneer at right
    ai "smile1"

    scene bg int_aidpost_day
    show ai normal jeans srt
    show mi normal pioneer at left
    show us normal pioneer at right
    ai "normal"

    scene bg ext_musclub_day
    show ai serious pink lng
    show mz normal pioneer at left
    show el normal pioneer at right
    ai "serious"

    scene bg int_aidpost_day_apple
    show ai dontlike1 little2 tal
    show yo normal shirt at left
    show el normal pioneer at right
    ai "dontlike1"

    scene bg int_house_of_mt_day
    show ai angry1 uniformb tal
    show un normal pioneer at left
    show un normal pioneer at right
    ai "angry1"

    scene bg ext_house_of_mt_day
    show ai rage uniformb srt
    show yo normal shirt at left
    show pi at right
    ai "rage"

    scene bg ext_house_of_dv_day
    show ai anger jeans lng
    show gl normal jeans at left
    show mz normal pioneer at right
    ai "anger"

    scene bg ext_beach_day
    show ai frust1 kimono srt
    show mt normal pioneer at left
    show yo normal shirt at right
    ai "frust1"

    scene bg ext_no_bus
    show ai dontlike2 xmas tal
    show el normal pioneer at left
    show un normal pioneer at right
    ai "dontlike2"

    scene bg ext_house_of_un_day
    show ai evilsmile2 pink tal
    show cs normal at left
    show mt normal pioneer at right
    ai "evilsmile2"

    scene bg ext_houses_day
    show ai grin2 little2 tal
    show sh normal pioneer at left
    show cs normal at right
    ai "grin2"

    scene bg ext_house_of_un_day
    show ai smile2 uniformb lng
    show sl normal pioneer at left
    show un normal pioneer at right
    ai "smile2"

    scene bg ext_house_of_un_day
    show ai shy2 uniformb srt
    show mz normal pioneer at left
    show uv normal at right
    ai "shy2"

    scene bg int_musclub_day
    show ai laugh2 little2 lng
    show pi at left
    show un normal pioneer at right
    ai "laugh2"

    scene bg int_house_of_sl_day
    show ai frust2 little1 lng
    show mz normal pioneer at left
    show sh normal pioneer at right
    ai "frust2"

    scene bg ext_washstand2_day
    show ai angry2 little1 lng
    show mi normal pioneer at left
    show mz normal pioneer at right
    ai "angry2"

    scene bg int_house_of_mt_day
    show ai surprise jeans lng
    show pi at left
    show mt normal pioneer at right
    ai "jeans lng"

    scene bg ext_bus
    show ai laugh1 pink lng
    show yo normal shirt at left
    show jd normal pioneer at right
    ai "pink lng"

    scene bg int_dining_hall_day
    show ai serious little1 lng
    show dv normal pioneer at left
    show jd normal pioneer at right
    ai "little1 lng"

    scene bg ext_house_of_mt_day
    show ai evilsmile1 little2 lng
    show us normal pioneer at left
    show sh normal pioneer at right
    ai "little2 lng"

    scene bg ext_dining_hall_away_day
    show ai rage kimono lng
    show us normal pioneer at left
    show us normal pioneer at right
    ai "kimono lng"

    scene bg ext_square_day
    show ai laugh2 uniformw lng
    show jd normal pioneer at left
    show mz normal pioneer at right
    ai "uniformw lng"

    scene bg ext_island_day
    show ai guilty uniformb lng
    show el normal pioneer at left
    show sl normal pioneer at right
    ai "uniformb lng"

    scene bg ext_clubs_day
    show ai surprise xmas lng
    show mi normal pioneer at left
    show un normal pioneer at right
    ai "xmas lng"

    scene bg ext_beach_day
    show ai frust1 jeans srt
    show pi at left
    show yo normal shirt at right
    ai "jeans srt"

    scene bg ext_no_bus
    show ai scary pink srt
    show mt normal pioneer at left
    show gl normal jeans at right
    ai "pink srt"

    scene bg ext_clubs_day
    show ai shy1 little1 srt
    show mi normal pioneer at left
    show mz normal pioneer at right
    ai "little1 srt"

    scene bg ext_island_day
    show ai shy2 little2 srt
    show cs normal at left
    show sh normal pioneer at right
    ai "little2 srt"

    scene bg ext_no_bus
    show ai grin2 kimono srt
    show cs normal at left
    show el normal pioneer at right
    ai "kimono srt"

    scene bg ext_playground_day
    show ai smile2 uniformw srt
    show pi at left
    show us normal pioneer at right
    ai "uniformw srt"

    scene bg ext_polyana_day
    show ai surprise uniformb srt
    show mt normal pioneer at left
    show un normal pioneer at right
    ai "uniformb srt"

    scene bg ext_house_of_un_day
    show ai frust1 xmas srt
    show pi at left
    show uv normal at right
    ai "xmas srt"

    scene bg ext_stage_normal_day
    show ai happy jeans tal
    show sh normal pioneer at left
    show yo normal shirt at right
    ai "jeans tal"

    scene bg int_house_of_sl_day
    show ai frust1 pink tal
    show mi normal pioneer at left
    show sl normal pioneer at right
    ai "pink tal"

    scene bg ext_island_day
    show ai evilsmile2 little1 tal
    show gl normal jeans at left
    show mz normal pioneer at right
    ai "little1 tal"

    scene bg ext_square_day_city
    show ai angry2 little2 tal
    show yo normal shirt at left
    show us normal pioneer at right
    ai "little2 tal"

    scene bg int_aidpost_day
    show ai serious kimono tal
    show uv normal at left
    show mz normal pioneer at right
    ai "kimono tal"

    scene bg int_aidpost_day_apple
    show ai smile1 uniformw tal
    show mt normal pioneer at left
    show yo normal shirt at right
    ai "uniformw tal"

    scene bg int_library_day
    show ai guilty uniformb tal
    show us normal pioneer at left
    show mt normal pioneer at right
    ai "uniformb tal"

    scene bg ext_path2_day
    show ai anger xmas tal
    show jd normal pioneer at left
    show uv normal at right
    ai "xmas tal"

    $ persistent.sprite_time = "sunset"

    scene bg ext_beach_sunset
    show ai grin1 kimono lng
    show sh normal pioneer at left
    show el normal pioneer at right
    ai "grin1"

    scene bg int_house_of_mt_sunset
    show ai surprise xmas srt
    show el normal pioneer at left
    show mt normal pioneer at right
    ai "surprise"

    scene bg ext_polyana_sunset
    show ai scary xmas lng
    show sh normal pioneer at left
    show sh normal pioneer at right
    ai "scary"

    scene bg ext_road_sunset
    show ai sad little1 srt
    show sh normal pioneer at left
    show gl normal jeans at right
    ai "sad"

    scene bg ext_path_sunset
    show ai shy1 little2 srt
    show el normal pioneer at left
    show gl normal jeans at right
    ai "shy1"

    scene bg int_house_of_mt_sunset
    show ai guilty kimono srt
    show mz normal pioneer at left
    show pi at right
    ai "guilty"

    scene bg ext_dining_hall_away_sunset
    show ai evilsmile1 jeans srt
    show mt normal pioneer at left
    show sh normal pioneer at right
    ai "evilsmile1"

    scene bg ext_path_sunset
    show ai happy jeans tal
    show mz normal pioneer at left
    show jd normal pioneer at right
    ai "happy"

    scene bg ext_dining_hall_near_sunset
    show ai laugh1 kimono tal
    show uv normal at left
    show mz normal pioneer at right
    ai "laugh1"

    scene bg int_clubs_male_sunset
    show ai smile1 little2 tal
    show mz normal pioneer at left
    show dv normal pioneer at right
    ai "smile1"

    scene bg int_dining_hall_sunset
    show ai normal jeans lng
    show sh normal pioneer at left
    show sh normal pioneer at right
    ai "normal"

    scene bg ext_house_of_mt_sunset
    show ai serious xmas lng
    show sl normal pioneer at left
    show el normal pioneer at right
    ai "serious"

    scene bg ext_no_bus_sunset
    show ai dontlike1 jeans srt
    show un normal pioneer at left
    show mt normal pioneer at right
    ai "dontlike1"

    scene bg ext_house_of_mt_sunset
    show ai angry1 kimono srt
    show sh normal pioneer at left
    show gl normal jeans at right
    ai "angry1"

    scene bg ext_road_sunset
    show ai rage xmas lng
    show uv normal at left
    show dv normal pioneer at right
    ai "rage"

    scene bg ext_square_sunset
    show ai anger uniformb lng
    show gl normal jeans at left
    show el normal pioneer at right
    ai "anger"

    scene bg ext_square_sunset
    show ai frust1 pink tal
    show pi at left
    show yo normal shirt at right
    ai "frust1"

    scene bg ext_square_sunset
    show ai dontlike2 uniformw tal
    show mz normal pioneer at left
    show pi at right
    ai "dontlike2"

    scene bg ext_no_bus_sunset
    show ai evilsmile2 kimono srt
    show pi at left
    show jd normal pioneer at right
    ai "evilsmile2"

    scene bg ext_road_sunset
    show ai grin2 pink tal
    show yo normal shirt at left
    show sh normal pioneer at right
    ai "grin2"

    scene bg ext_dining_hall_away_sunset
    show ai smile2 kimono srt
    show mz normal pioneer at left
    show mi normal pioneer at right
    ai "smile2"

    scene bg ext_dining_hall_near_sunset
    show ai shy2 jeans tal
    show uv normal at left
    show pi at right
    ai "shy2"

    scene bg ext_polyana_sunset
    show ai laugh2 kimono lng
    show yo normal shirt at left
    show el normal pioneer at right
    ai "laugh2"

    scene bg ext_dining_hall_near_sunset
    show ai frust2 pink lng
    show mt normal pioneer at left
    show sl normal pioneer at right
    ai "frust2"

    scene bg ext_house_of_mt_sunset
    show ai angry2 pink lng
    show mi normal pioneer at left
    show us normal pioneer at right
    ai "angry2"

    scene bg ext_dining_hall_away_sunset
    show ai evilsmile1 jeans lng
    show mt normal pioneer at left
    show cs normal at right
    ai "jeans lng"

    scene bg ext_path_sunset
    show ai smile1 pink lng
    show mz normal pioneer at left
    show yo normal shirt at right
    ai "pink lng"

    scene bg ext_houses_sunset
    show ai laugh2 little1 lng
    show mi normal pioneer at left
    show sl normal pioneer at right
    ai "little1 lng"

    scene bg ext_house_of_mt_sunset
    show ai evilsmile1 little2 lng
    show sl normal pioneer at left
    show us normal pioneer at right
    ai "little2 lng"

    scene bg ext_dining_hall_away_sunset
    show ai dontlike1 kimono lng
    show cs normal at left
    show us normal pioneer at right
    ai "kimono lng"

    scene bg int_clubs_male_sunset
    show ai dontlike2 uniformw lng
    show sh normal pioneer at left
    show gl normal jeans at right
    ai "uniformw lng"

    scene bg ext_path_sunset
    show ai grin2 uniformb lng
    show cs normal at left
    show uv normal at right
    ai "uniformb lng"

    scene bg ext_no_bus_sunset
    show ai serious xmas lng
    show pi at left
    show dv normal pioneer at right
    ai "xmas lng"

    scene bg int_dining_hall_sunset
    show ai evilsmile1 jeans srt
    show mz normal pioneer at left
    show uv normal at right
    ai "jeans srt"

    scene bg ext_beach_sunset
    show ai frust2 pink srt
    show mt normal pioneer at left
    show cs normal at right
    ai "pink srt"

    scene bg ext_beach_sunset
    show ai shy2 little1 srt
    show mz normal pioneer at left
    show un normal pioneer at right
    ai "little1 srt"

    scene bg ext_no_bus_sunset
    show ai normal little2 srt
    show us normal pioneer at left
    show mt normal pioneer at right
    ai "little2 srt"

    scene bg int_house_of_mt_sunset
    show ai smile2 kimono srt
    show cs normal at left
    show yo normal shirt at right
    ai "kimono srt"

    scene bg int_clubs_male_sunset
    show ai guilty uniformw srt
    show sh normal pioneer at left
    show mi normal pioneer at right
    ai "uniformw srt"

    scene bg ext_path_sunset
    show ai scary uniformb srt
    show mt normal pioneer at left
    show gl normal jeans at right
    ai "uniformb srt"

    scene bg ext_no_bus_sunset
    show ai dontlike1 xmas srt
    show sl normal pioneer at left
    show uv normal at right
    ai "xmas srt"

    scene bg int_clubs_male_sunset
    show ai dontlike1 jeans tal
    show jd normal pioneer at left
    show sl normal pioneer at right
    ai "jeans tal"

    scene bg ext_path_sunset
    show ai laugh1 pink tal
    show cs normal at left
    show mz normal pioneer at right
    ai "pink tal"

    scene bg ext_house_of_mt_sunset
    show ai smile1 little1 tal
    show mi normal pioneer at left
    show cs normal at right
    ai "little1 tal"

    scene bg ext_polyana_sunset
    show ai grin2 little2 tal
    show yo normal shirt at left
    show sl normal pioneer at right
    ai "little2 tal"

    scene bg ext_no_bus_sunset
    show ai grin1 kimono tal
    show jd normal pioneer at left
    show mt normal pioneer at right
    ai "kimono tal"

    scene bg ext_square_sunset
    show ai scary uniformw tal
    show sl normal pioneer at left
    show pi at right
    ai "uniformw tal"

    scene bg ext_no_bus_sunset
    show ai happy uniformb tal
    show sl normal pioneer at left
    show dv normal pioneer at right
    ai "uniformb tal"

    scene bg ext_no_bus_sunset
    show ai dontlike2 xmas tal
    show el normal pioneer at left
    show sh normal pioneer at right
    ai "xmas tal"

    $ persistent.sprite_time = "night"

    scene bg ext_path_night
    show ai grin1 uniformw tal
    show un normal pioneer at fleft
    show mz normal pioneer at fright
    ai "grin1"

    scene bg int_dining_hall_night
    show ai surprise jeans srt
    show un normal pioneer at fleft
    show mt normal pioneer at fright
    ai "surprise"

    scene bg int_library_night
    show ai scary jeans tal
    show uv normal at fleft
    show el normal pioneer at fright
    ai "scary"

    scene bg int_liaz
    show ai sad pink lng
    show uv normal at fleft
    show pi at fright
    ai "sad"

    scene bg ext_bus_night
    show ai shy1 xmas srt
    show sl normal pioneer at fleft
    show un normal pioneer at fright
    ai "shy1"

    scene bg ext_dining_hall_away_night
    show ai guilty little2 tal
    show gl normal jeans at fleft
    show us normal pioneer at fright
    ai "guilty"

    scene bg ext_house_of_dv_night
    show ai evilsmile1 uniformb tal
    show sh normal pioneer at fleft
    show cs normal at fright
    ai "evilsmile1"

    scene bg ext_bus_night
    show ai happy jeans lng
    show mt normal pioneer at fleft
    show un normal pioneer at fright
    ai "happy"

    scene bg ext_polyana_night
    show ai laugh1 jeans srt
    show un normal pioneer at fleft
    show yo normal shirt at fright
    ai "laugh1"

    scene bg int_liaz
    show ai smile1 uniformb tal
    show jd normal pioneer at fleft
    show mt normal pioneer at fright
    ai "smile1"

    scene bg int_bus_people_night
    show ai normal uniformb srt
    show mi normal pioneer at fleft
    show uv normal at fright
    ai "normal"

    scene bg ext_old_building_night
    show ai serious uniformb tal
    show jd normal pioneer at fleft
    show us normal pioneer at fright
    ai "serious"

    scene bg ext_square_night_party2
    show ai dontlike1 uniformb lng
    show mi normal pioneer at fleft
    show mi normal pioneer at fright
    ai "dontlike1"

    scene bg int_house_of_mt_night
    show ai angry1 kimono lng
    show sl normal pioneer at fleft
    show uv normal at fright
    ai "angry1"

    scene bg ext_stage_big_night
    show ai rage pink lng
    show sl normal pioneer at fleft
    show sl normal pioneer at fright
    ai "rage"

    scene bg int_dining_hall_night
    show ai anger xmas srt
    show sh normal pioneer at fleft
    show un normal pioneer at fright
    ai "anger"

    scene bg ext_house_of_mt_night_without_light
    show ai frust1 kimono lng
    show gl normal jeans at fleft
    show dv normal pioneer at fright
    ai "frust1"

    scene bg int_house_of_mt_night
    show ai dontlike2 pink lng
    show us normal pioneer at fleft
    show un normal pioneer at fright
    ai "dontlike2"

    scene bg ext_stage_big_night
    show ai evilsmile2 xmas lng
    show jd normal pioneer at fleft
    show jd normal pioneer at fright
    ai "evilsmile2"

    scene bg int_library_night2
    show ai grin2 kimono tal
    show us normal pioneer at fleft
    show cs normal at fright
    ai "grin2"

    scene bg ext_square_night_party2
    show ai smile2 kimono tal
    show el normal pioneer at fleft
    show mt normal pioneer at fright
    ai "smile2"

    scene bg int_clubs_male2_night_nolight
    show ai shy2 uniformw srt
    show mz normal pioneer at fleft
    show sh normal pioneer at fright
    ai "shy2"

    scene bg ext_square_night_party
    show ai laugh2 xmas srt
    show cs normal at fleft
    show pi at fright
    ai "laugh2"

    scene bg ext_island_night
    show ai frust2 kimono lng
    show sh normal pioneer at fleft
    show cs normal at fright
    ai "frust2"

    scene bg int_aidpost_night
    show ai angry2 little2 tal
    show sl normal pioneer at fleft
    show us normal pioneer at fright
    ai "angry2"

    scene bg ext_no_bus_night
    show ai evilsmile2 jeans lng
    show un normal pioneer at fleft
    show mi normal pioneer at fright
    ai "jeans lng"

    scene bg int_liaz
    show ai laugh1 pink lng
    show un normal pioneer at fleft
    show el normal pioneer at fright
    ai "pink lng"

    scene bg int_clubs_male2_night
    show ai angry1 little1 lng
    show pi at fleft
    show mz normal pioneer at fright
    ai "little1 lng"

    scene bg ext_stage_normal_night
    show ai sad little2 lng
    show un normal pioneer at fleft
    show us normal pioneer at fright
    ai "little2 lng"

    scene bg ext_beach_night
    show ai shy1 kimono lng
    show pi at fleft
    show us normal pioneer at fright
    ai "kimono lng"

    scene bg ext_square_night
    show ai serious uniformw lng
    show sl normal pioneer at fleft
    show us normal pioneer at fright
    ai "uniformw lng"

    scene bg ext_dining_hall_away_night
    show ai anger uniformb lng
    show jd normal pioneer at fleft
    show mt normal pioneer at fright
    ai "uniformb lng"

    scene bg ext_dining_hall_near_night
    show ai scary xmas lng
    show uv normal at fleft
    show jd normal pioneer at fright
    ai "xmas lng"

    scene bg int_house_of_un_night
    show ai dontlike2 jeans srt
    show yo normal shirt at fleft
    show sh normal pioneer at fright
    ai "jeans srt"

    scene bg int_house_of_mt_noitem_night
    show ai guilty pink srt
    show mt normal pioneer at fleft
    show un normal pioneer at fright
    ai "pink srt"

    scene bg ext_path2_night
    show ai rage little1 srt
    show el normal pioneer at fleft
    show cs normal at fright
    ai "little1 srt"

    scene bg ext_bathhouse_night
    show ai shy1 little2 srt
    show el normal pioneer at fleft
    show mz normal pioneer at fright
    ai "little2 srt"

    scene bg ext_boathouse_night
    show ai grin2 kimono srt
    show el normal pioneer at fleft
    show us normal pioneer at fright
    ai "kimono srt"

    scene bg ext_path_night
    show ai laugh1 uniformw srt
    show el normal pioneer at fleft
    show gl normal jeans at fright
    ai "uniformw srt"

    scene bg ext_stage_normal_night
    show ai laugh1 uniformb srt
    show el normal pioneer at fleft
    show dv normal pioneer at fright
    ai "uniformb srt"

    scene bg ext_no_bus_night
    show ai evilsmile2 xmas srt
    show sl normal pioneer at fleft
    show jd normal pioneer at fright
    ai "xmas srt"

    scene bg ext_clubs_night
    show ai shy2 jeans tal
    show sh normal pioneer at fleft
    show sl normal pioneer at fright
    ai "jeans tal"

    scene bg int_house_of_un_night
    show ai guilty pink tal
    show sh normal pioneer at fleft
    show mt normal pioneer at fright
    ai "pink tal"

    scene bg ext_bathhouse_night
    show ai grin1 little1 tal
    show mi normal pioneer at fleft
    show us normal pioneer at fright
    ai "little1 tal"

    scene bg ext_path_night
    show ai angry2 little2 tal
    show sh normal pioneer at fleft
    show us normal pioneer at fright
    ai "little2 tal"

    scene bg int_house_of_mt_night
    show ai anger kimono tal
    show uv normal at fleft
    show gl normal jeans at fright
    ai "kimono tal"

    scene bg ext_stage_big_night
    show ai scary uniformw tal
    show pi at fleft
    show un normal pioneer at fright
    ai "uniformw tal"

    scene bg int_bus_people_night
    show ai smile2 uniformb tal
    show jd normal pioneer at fleft
    show el normal pioneer at fright
    ai "uniformb tal"

    scene bg int_house_of_dv_night
    show ai angry2 xmas tal
    show pi at fleft
    show sh normal pioneer at fright
    ai "xmas tal"










    
