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
    
    show ai grin1 jeans srt
    show sl normal pioneer at left
    show cs normal at right
    ai "grin1"

    scene bg ext_island_day
    show ai surprise uniformb srt
    show cs normal at left
    show el normal pioneer at right
    ai "surprise"

    scene bg int_house_of_sl_day
    show ai scary jeans lng
    show cs normal at left
    show cs normal at right
    ai "scary"

    scene bg int_clubs_male_day
    show ai sad little2 tal
    show uv normal at left
    show yo normal shirt at right
    ai "sad"

    scene bg ext_camp_entrance_day
    show ai shy1 dress tal
    show uv normal at left
    show mi normal pioneer at right
    ai "shy1"

    scene bg ext_aidpost_day
    show ai guilty dress lng
    show un normal pioneer at left
    show yo normal shirt at right
    ai "guilty"

    scene bg ext_polyana_day
    show ai evilsmile1 little1 tal
    show cs normal at left
    show yo normal shirt at right
    ai "evilsmile1"

    scene bg ext_beach_day
    show ai happy kimono tal
    show yo normal shirt at left
    show pi at right
    ai "happy"

    scene bg int_bus
    show ai laugh1 pink srt
    show un normal pioneer at left
    show yo normal shirt at right
    ai "laugh1"

    scene bg int_bus_people_day
    show ai smile1 dress srt
    show mz normal pioneer at left
    show el normal pioneer at right
    ai "smile1"

    scene bg int_library_day
    show ai normal shirt tal
    show mi normal pioneer at left
    show uv normal at right
    ai "normal"

    scene bg int_bus
    show ai serious jeans srt
    show uv normal at left
    show us normal pioneer at right
    ai "serious"

    scene bg ext_square_day_city
    show ai dontlike1 shirt lng
    show yo normal shirt at left
    show cs normal at right
    ai "dontlike1"

    scene bg int_house_of_dv_day
    show ai angry1 uniformb lng
    show mt normal pioneer at left
    show mz normal pioneer at right
    ai "angry1"

    scene bg int_dining_hall_day
    show ai rage pink lng
    show gl normal jeans at left
    show uv normal at right
    ai "rage"

    scene bg int_dining_hall_people_day
    show ai anger jeans srt
    show jd normal pioneer at left
    show mz normal pioneer at right
    ai "anger"

    scene bg int_aidpost_day
    show ai frust1 xmas srt
    show uv normal at left
    show jd normal pioneer at right
    ai "frust1"

    scene bg ext_houses_day
    show ai dontlike2 uniformb tal
    show sl normal pioneer at left
    show un normal pioneer at right
    ai "dontlike2"

    scene bg ext_house_of_sl_day
    show ai evilsmile2 uniformb lng
    show jd normal pioneer at left
    show mz normal pioneer at right
    ai "evilsmile2"

    scene bg int_library_day
    show ai grin2 xmas lng
    show jd normal pioneer at left
    show mt normal pioneer at right
    ai "grin2"

    scene bg ext_path2_day
    show ai smile2 xmas srt
    show cs normal at left
    show jd normal pioneer at right
    ai "smile2"

    scene bg ext_path2_day
    show ai shy2 uniformw srt
    show mz normal pioneer at left
    show yo normal shirt at right
    ai "shy2"

    scene bg ext_road_day
    show ai laugh2 little2 lng
    show us normal pioneer at left
    show pi at right
    ai "laugh2"

    scene bg ext_houses_day
    show ai frust2 kimono srt
    show cs normal at left
    show sh normal pioneer at right
    ai "frust2"

    scene bg int_clubs_male_day
    show ai angry2 uniformw tal
    show sl normal pioneer at left
    show pi at right
    ai "angry2"

    scene bg int_library_day
    show ai dontlike1 jeans lng
    show mt normal pioneer at left
    show dv normal pioneer at right
    ai "jeans lng"

    scene bg ext_bus
    show ai evilsmile2 pink lng
    show uv normal at left
    show sh normal pioneer at right
    ai "pink lng"

    scene bg ext_bus
    show ai rage little1 lng
    show mz normal pioneer at left
    show el normal pioneer at right
    ai "little1 lng"

    scene bg int_library_day
    show ai dontlike1 little2 lng
    show gl normal jeans at left
    show sh normal pioneer at right
    ai "little2 lng"

    scene bg ext_playground_day
    show ai guilty kimono lng
    show uv normal at left
    show yo normal shirt at right
    ai "kimono lng"

    scene bg int_bus
    show ai dontlike2 uniformw lng
    show yo normal shirt at left
    show mi normal pioneer at right
    ai "uniformw lng"

    scene bg ext_road_day
    show ai shy2 uniformb lng
    show yo normal shirt at left
    show mi normal pioneer at right
    ai "uniformb lng"

    scene bg ext_no_bus
    show ai smile2 xmas lng
    show gl normal jeans at left
    show mt normal pioneer at right
    ai "xmas lng"

    scene bg ext_clubs_day
    show ai dontlike1 shirt lng
    show el normal pioneer at left
    show el normal pioneer at right
    ai "shirt lng"

    scene bg ext_road_day
    show ai happy dress lng
    show jd normal pioneer at left
    show dv normal pioneer at right
    ai "dress lng"

    scene bg int_aidpost_day_apple
    show ai serious jeans srt
    show yo normal shirt at left
    show pi at right
    ai "jeans srt"

    scene bg ext_road_day
    show ai frust1 pink srt
    show mt normal pioneer at left
    show yo normal shirt at right
    ai "pink srt"

    scene bg ext_musclub_day
    show ai anger little1 srt
    show pi at left
    show sh normal pioneer at right
    ai "little1 srt"

    scene bg ext_washstand2_day
    show ai dontlike1 little2 srt
    show mz normal pioneer at left
    show sh normal pioneer at right
    ai "little2 srt"

    scene bg ext_island_day
    show ai angry2 kimono srt
    show cs normal at left
    show pi at right
    ai "kimono srt"

    scene bg ext_house_of_sl_day
    show ai scary uniformw srt
    show pi at left
    show mi normal pioneer at right
    ai "uniformw srt"

    scene bg int_musclub_day
    show ai normal uniformb srt
    show cs normal at left
    show mi normal pioneer at right
    ai "uniformb srt"

    scene bg ext_road_day
    show ai sad xmas srt
    show un normal pioneer at left
    show sh normal pioneer at right
    ai "xmas srt"

    scene bg ext_path2_day
    show ai frust1 shirt srt
    show mi normal pioneer at left
    show mi normal pioneer at right
    ai "shirt srt"

    scene bg int_dining_hall_day
    show ai frust1 dress srt
    show jd normal pioneer at left
    show mt normal pioneer at right
    ai "dress srt"

    scene bg ext_dining_hall_near_day
    show ai shy1 jeans tal
    show yo normal shirt at left
    show yo normal shirt at right
    ai "jeans tal"

    scene bg ext_houses_day
    show ai evilsmile2 pink tal
    show jd normal pioneer at left
    show un normal pioneer at right
    ai "pink tal"

    scene bg ext_square_day
    show ai smile2 little1 tal
    show sh normal pioneer at left
    show gl normal jeans at right
    ai "little1 tal"

    scene bg int_aidpost_day
    show ai frust2 little2 tal
    show gl normal jeans at left
    show el normal pioneer at right
    ai "little2 tal"

    scene bg ext_square_day_city
    show ai dontlike2 kimono tal
    show el normal pioneer at left
    show jd normal pioneer at right
    ai "kimono tal"

    scene bg int_musclub_day
    show ai happy uniformw tal
    show mt normal pioneer at left
    show us normal pioneer at right
    ai "uniformw tal"

    scene bg int_aidpost_day
    show ai dontlike2 uniformb tal
    show uv normal at left
    show un normal pioneer at right
    ai "uniformb tal"

    scene bg ext_path2_day
    show ai serious xmas tal
    show gl normal jeans at left
    show sh normal pioneer at right
    ai "xmas tal"

    scene bg int_bus
    show ai dontlike2 shirt tal
    show sl normal pioneer at left
    show yo normal shirt at right
    ai "shirt tal"

    scene bg ext_house_of_sl_day
    show ai smile1 dress tal
    show sh normal pioneer at left
    show el normal pioneer at right
    ai "dress tal"

    $ persistent.sprite_time = "sunset"

    scene bg ext_dining_hall_away_sunset
    show ai grin1 little1 lng
    show cs normal far at left
    show el normal pioneer far at right
    ai "grin1"

    scene bg ext_dining_hall_away_sunset
    show ai surprise uniformw lng
    show sl normal pioneer far at left
    show sl normal pioneer far at right
    ai "surprise"

    scene bg ext_dining_hall_away_sunset
    show ai scary dress srt
    show mt normal pioneer far at left
    show mz normal pioneer far at right
    ai "scary"

    scene bg ext_houses_sunset
    show ai sad little2 tal
    show uv normal far at left
    show sl normal pioneer far at right
    ai "sad"

    scene bg ext_polyana_sunset
    show ai shy1 uniformw tal
    show mi normal pioneer far at left
    show mi normal pioneer far at right
    ai "shy1"

    scene bg ext_path_sunset
    show ai guilty kimono lng
    show sl normal pioneer far at left
    show jd normal pioneer far at right
    ai "guilty"

    scene bg ext_polyana_sunset
    show ai evilsmile1 uniformw tal
    show mz normal pioneer far at left
    show mi normal pioneer far at right
    ai "evilsmile1"

    scene bg ext_square_sunset
    show ai happy shirt srt
    show mi normal pioneer far at left
    show mz normal pioneer far at right
    ai "happy"

    scene bg ext_dining_hall_near_sunset
    show ai laugh1 uniformb srt
    show uv normal far at left
    show mi normal pioneer far at right
    ai "laugh1"

    scene bg ext_dining_hall_near_sunset
    show ai smile1 little1 lng
    show el normal pioneer far at left
    show un normal pioneer far at right
    ai "smile1"

    scene bg ext_beach_sunset
    show ai normal uniformw tal
    show el normal pioneer far at left
    show us normal pioneer far at right
    ai "normal"

    scene bg ext_road_sunset
    show ai serious dress lng
    show mt normal pioneer far at left
    show sh normal pioneer far at right
    ai "serious"

    scene bg ext_houses_sunset
    show ai dontlike1 kimono tal
    show dv normal pioneer far at left
    show jd normal pioneer far at right
    ai "dontlike1"

    scene bg ext_house_of_mt_sunset
    show ai angry1 xmas tal
    show mz normal pioneer far at left
    show cs normal far at right
    ai "angry1"

    scene bg ext_road_sunset
    show ai rage uniformb srt
    show mz normal pioneer far at left
    show us normal pioneer far at right
    ai "rage"

    scene bg ext_house_of_mt_sunset
    show ai anger little1 lng
    show uv normal far at left
    show us normal pioneer far at right
    ai "anger"

    scene bg int_dining_hall_sunset
    show ai frust1 xmas srt
    show mt normal pioneer far at left
    show yo normal shirt far at right
    ai "frust1"

    scene bg ext_no_bus_sunset
    show ai dontlike2 xmas lng
    show cs normal far at left
    show pi far at right
    ai "dontlike2"

    scene bg ext_no_bus_sunset
    show ai evilsmile2 shirt tal
    show yo normal shirt far at left
    show jd normal pioneer far at right
    ai "evilsmile2"

    scene bg ext_no_bus_sunset
    show ai grin2 kimono lng
    show jd normal pioneer far at left
    show us normal pioneer far at right
    ai "grin2"

    scene bg ext_no_bus_sunset
    show ai smile2 little2 tal
    show mz normal pioneer far at left
    show sh normal pioneer far at right
    ai "smile2"

    scene bg ext_dining_hall_near_sunset
    show ai shy2 uniformw lng
    show pi far at left
    show un normal pioneer far at right
    ai "shy2"

    scene bg int_clubs_male_sunset
    show ai laugh2 little2 tal
    show un normal pioneer far at left
    show sl normal pioneer far at right
    ai "laugh2"

    scene bg ext_square_sunset
    show ai frust2 little2 srt
    show gl normal jeans far at left
    show uv normal far at right
    ai "frust2"

    scene bg int_clubs_male_sunset
    show ai angry2 little1 srt
    show yo normal shirt far at left
    show mi normal pioneer far at right
    ai "angry2"

    scene bg int_dining_hall_sunset
    show ai frust2 jeans lng
    show un normal pioneer far at left
    show jd normal pioneer far at right
    ai "jeans lng"

    scene bg ext_dining_hall_away_sunset
    show ai evilsmile1 pink lng
    show mz normal pioneer far at left
    show uv normal far at right
    ai "pink lng"

    scene bg ext_houses_sunset
    show ai anger little1 lng
    show mi normal pioneer far at left
    show jd normal pioneer far at right
    ai "little1 lng"

    scene bg ext_dining_hall_away_sunset
    show ai guilty little2 lng
    show el normal pioneer far at left
    show pi far at right
    ai "little2 lng"

    scene bg int_clubs_male_sunset
    show ai dontlike2 kimono lng
    show gl normal jeans far at left
    show un normal pioneer far at right
    ai "kimono lng"

    scene bg ext_dining_hall_away_sunset
    show ai happy uniformw lng
    show cs normal far at left
    show sh normal pioneer far at right
    ai "uniformw lng"

    scene bg int_clubs_male_sunset
    show ai dontlike1 uniformb lng
    show dv normal pioneer far at left
    show el normal pioneer far at right
    ai "uniformb lng"

    scene bg ext_dining_hall_near_sunset
    show ai frust2 xmas lng
    show us normal pioneer far at left
    show sh normal pioneer far at right
    ai "xmas lng"

    scene bg int_clubs_male_sunset
    show ai evilsmile2 shirt lng
    show uv normal far at left
    show sh normal pioneer far at right
    ai "shirt lng"

    scene bg ext_beach_sunset
    show ai angry2 dress lng
    show cs normal far at left
    show mz normal pioneer far at right
    ai "dress lng"

    scene bg ext_no_bus_sunset
    show ai evilsmile1 jeans srt
    show el normal pioneer far at left
    show mz normal pioneer far at right
    ai "jeans srt"

    scene bg ext_path_sunset
    show ai happy pink srt
    show mz normal pioneer far at left
    show yo normal shirt far at right
    ai "pink srt"

    scene bg ext_road_sunset
    show ai rage little1 srt
    show gl normal jeans far at left
    show gl normal jeans far at right
    ai "little1 srt"

    scene bg ext_polyana_sunset
    show ai frust1 little2 srt
    show yo normal shirt far at left
    show us normal pioneer far at right
    ai "little2 srt"

    scene bg ext_no_bus_sunset
    show ai frust2 kimono srt
    show sh normal pioneer far at left
    show pi far at right
    ai "kimono srt"

    scene bg ext_no_bus_sunset
    show ai surprise uniformw srt
    show mz normal pioneer far at left
    show uv normal far at right
    ai "uniformw srt"

    scene bg ext_house_of_mt_sunset
    show ai dontlike2 uniformb srt
    show mi normal pioneer far at left
    show cs normal far at right
    ai "uniformb srt"

    scene bg int_dining_hall_sunset
    show ai shy1 xmas srt
    show mt normal pioneer far at left
    show sh normal pioneer far at right
    ai "xmas srt"

    scene bg ext_polyana_sunset
    show ai laugh2 shirt srt
    show yo normal shirt far at left
    show yo normal shirt far at right
    ai "shirt srt"

    scene bg ext_square_sunset
    show ai happy dress srt
    show dv normal pioneer far at left
    show cs normal far at right
    ai "dress srt"

    scene bg ext_square_sunset
    show ai grin1 jeans tal
    show pi far at left
    show un normal pioneer far at right
    ai "jeans tal"

    scene bg int_clubs_male_sunset
    show ai rage pink tal
    show jd normal pioneer far at left
    show pi far at right
    ai "pink tal"

    scene bg int_clubs_male_sunset
    show ai smile2 little1 tal
    show un normal pioneer far at left
    show pi far at right
    ai "little1 tal"

    scene bg int_clubs_male_sunset
    show ai angry2 little2 tal
    show uv normal far at left
    show mi normal pioneer far at right
    ai "little2 tal"

    scene bg ext_dining_hall_away_sunset
    show ai frust1 kimono tal
    show sl normal pioneer far at left
    show mz normal pioneer far at right
    ai "kimono tal"

    scene bg int_house_of_mt_sunset
    show ai anger uniformw tal
    show el normal pioneer far at left
    show us normal pioneer far at right
    ai "uniformw tal"

    scene bg int_clubs_male_sunset
    show ai dontlike1 uniformb tal
    show mz normal pioneer far at left
    show yo normal shirt far at right
    ai "uniformb tal"

    scene bg ext_dining_hall_away_sunset
    show ai frust1 xmas tal
    show cs normal far at left
    show pi far at right
    ai "xmas tal"

    scene bg ext_road_sunset
    show ai anger shirt tal
    show cs normal far at left
    show un normal pioneer far at right
    ai "shirt tal"

    scene bg ext_house_of_mt_sunset
    show ai normal dress tal
    show mz normal pioneer far at left
    show pi far at right
    ai "dress tal"

    $ persistent.sprite_time = "night"

    scene bg ext_path_night
    show ai grin1 xmas lng
    show gl normal jeans close at fleft
    show sh normal pioneer close at fright
    ai "grin1"

    scene bg ext_path2_night
    show ai surprise shirt lng
    show dv normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "surprise"

    scene bg int_house_of_mt_night
    show ai scary uniformw srt
    show us normal pioneer close at fleft
    show gl normal jeans close at fright
    ai "scary"

    scene bg ext_stage_big_night
    show ai sad jeans tal
    show jd normal pioneer close at fleft
    show un normal pioneer close at fright
    ai "sad"

    scene bg ext_old_building_night_moonlight
    show ai shy1 little2 tal
    show pi close at fleft
    show mt normal pioneer close at fright
    ai "shy1"

    scene bg int_bus_night
    show ai guilty dress srt
    show gl normal jeans close at fleft
    show un normal pioneer close at fright
    ai "guilty"

    scene bg ext_house_of_dv_night
    show ai evilsmile1 little1 tal
    show pi close at fleft
    show us normal pioneer close at fright
    ai "evilsmile1"

    scene bg int_house_of_mt_noitem_night
    show ai happy pink tal
    show mi normal pioneer close at fleft
    show mt normal pioneer close at fright
    ai "happy"

    scene bg ext_no_bus_night
    show ai laugh1 pink tal
    show gl normal jeans close at fleft
    show sl normal pioneer close at fright
    ai "laugh1"

    scene bg int_old_building_night
    show ai smile1 little2 lng
    show pi close at fleft
    show sh normal pioneer close at fright
    ai "smile1"

    scene bg ext_library_night
    show ai normal dress lng
    show pi close at fleft
    show el normal pioneer close at fright
    ai "normal"

    scene bg int_house_of_mt_noitem_night
    show ai serious uniformw lng
    show us normal pioneer close at fleft
    show dv normal pioneer close at fright
    ai "serious"

    scene bg ext_bus_night
    show ai dontlike1 pink tal
    show sh normal pioneer close at fleft
    show uv normal close at fright
    ai "dontlike1"

    scene bg int_house_of_mt_night2
    show ai angry1 little1 srt
    show sh normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "angry1"

    scene bg int_dining_hall_night
    show ai rage kimono tal
    show mt normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "rage"

    scene bg ext_house_of_mt_night_without_light
    show ai anger shirt lng
    show sl normal pioneer close at fleft
    show dv normal pioneer close at fright
    ai "anger"

    scene bg int_house_of_mt_noitem_night
    show ai frust1 uniformw tal
    show uv normal close at fleft
    show mi normal pioneer close at fright
    ai "frust1"

    scene bg ext_house_of_mt_night
    show ai dontlike2 jeans tal
    show un normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "dontlike2"

    scene bg ext_house_of_dv_night
    show ai evilsmile2 uniformw lng
    show un normal pioneer close at fleft
    show dv normal pioneer close at fright
    ai "evilsmile2"

    scene bg ext_bus_night
    show ai grin2 shirt srt
    show uv normal close at fleft
    show cs normal close at fright
    ai "grin2"

    scene bg int_house_of_mt_night
    show ai smile2 uniformb tal
    show uv normal close at fleft
    show el normal pioneer close at fright
    ai "smile2"

    scene bg ext_square_night_party
    show ai shy2 little1 tal
    show mi normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "shy2"

    scene bg int_house_of_dv_night
    show ai laugh2 little1 tal
    show mi normal pioneer close at fleft
    show gl normal jeans close at fright
    ai "laugh2"

    scene bg int_aidpost_night
    show ai frust2 little1 tal
    show el normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "frust2"

    scene bg ext_island_night
    show ai angry2 pink tal
    show jd normal pioneer close at fleft
    show sl normal pioneer close at fright
    ai "angry2"

    scene bg ext_dining_hall_near_night
    show ai rage jeans lng
    show gl normal jeans close at fleft
    show uv normal close at fright
    ai "jeans lng"

    scene bg ext_island_night
    show ai evilsmile1 pink lng
    show cs normal close at fleft
    show jd normal pioneer close at fright
    ai "pink lng"

    scene bg ext_house_of_mt_night
    show ai scary little1 lng
    show cs normal close at fleft
    show un normal pioneer close at fright
    ai "little1 lng"

    scene bg ext_old_building_night
    show ai dontlike2 little2 lng
    show mz normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "little2 lng"

    scene bg ext_old_building_night_moonlight
    show ai evilsmile1 kimono lng
    show el normal pioneer close at fleft
    show dv normal pioneer close at fright
    ai "kimono lng"

    scene bg ext_dining_hall_away_night
    show ai dontlike2 uniformw lng
    show mi normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "uniformw lng"

    scene bg int_bus_night
    show ai smile1 uniformb lng
    show sl normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "uniformb lng"

    scene bg ext_boathouse_night
    show ai scary xmas lng
    show sl normal pioneer close at fleft
    show jd normal pioneer close at fright
    ai "xmas lng"

    scene bg int_house_of_dv_night
    show ai grin2 shirt lng
    show mi normal pioneer close at fleft
    show el normal pioneer close at fright
    ai "shirt lng"

    scene bg ext_path2_night
    show ai grin2 dress lng
    show mz normal pioneer close at fleft
    show jd normal pioneer close at fright
    ai "dress lng"

    scene bg ext_beach_night
    show ai smile1 jeans srt
    show mz normal pioneer close at fleft
    show mt normal pioneer close at fright
    ai "jeans srt"

    scene bg int_library_night2
    show ai angry2 pink srt
    show sh normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "pink srt"

    scene bg int_clubs_male2_night
    show ai laugh1 little1 srt
    show mi normal pioneer close at fleft
    show sl normal pioneer close at fright
    ai "little1 srt"

    scene bg ext_square_night
    show ai frust1 little2 srt
    show sh normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "little2 srt"

    scene bg int_house_of_mt_night
    show ai laugh1 kimono srt
    show sh normal pioneer close at fleft
    show sl normal pioneer close at fright
    ai "kimono srt"

    scene bg int_aidpost_night
    show ai anger uniformw srt
    show pi close at fleft
    show mt normal pioneer close at fright
    ai "uniformw srt"

    scene bg int_bus_night
    show ai shy1 uniformb srt
    show cs normal close at fleft
    show sh normal pioneer close at fright
    ai "uniformb srt"

    scene bg ext_path2_night
    show ai anger xmas srt
    show el normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "xmas srt"

    scene bg ext_playground_night
    show ai scary shirt srt
    show jd normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "shirt srt"

    scene bg ext_boathouse_night
    show ai serious dress srt
    show jd normal pioneer close at fleft
    show un normal pioneer close at fright
    ai "dress srt"

    scene bg int_house_of_mt_night
    show ai shy2 jeans tal
    show el normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "jeans tal"

    scene bg ext_playground_night
    show ai grin1 pink tal
    show mi normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "pink tal"

    scene bg ext_old_building_night_moonlight
    show ai guilty little1 tal
    show un normal pioneer close at fleft
    show mt normal pioneer close at fright
    ai "little1 tal"

    scene bg ext_path2_night
    show ai happy little2 tal
    show pi close at fleft
    show mt normal pioneer close at fright
    ai "little2 tal"

    scene bg ext_camp_entrance_night
    show ai smile1 kimono tal
    show un normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "kimono tal"

    scene bg ext_playground_night
    show ai angry1 uniformw tal
    show sl normal pioneer close at fleft
    show uv normal close at fright
    ai "uniformw tal"

    scene bg ext_library_night
    show ai normal uniformb tal
    show sl normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "uniformb tal"

    scene bg ext_library_night
    show ai frust1 xmas tal
    show mi normal pioneer close at fleft
    show el normal pioneer close at fright
    ai "xmas tal"

    scene bg ext_boathouse_night
    show ai laugh1 shirt tal
    show pi close at fleft
    show un normal pioneer close at fright
    ai "shirt tal"

    scene bg int_house_of_mt_night
    show ai serious dress tal
    show mz normal pioneer close at fleft
    show gl normal jeans close at fright
    ai "dress tal"










    
