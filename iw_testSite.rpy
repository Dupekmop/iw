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
    
    show ai grin1 uniformb lng
    show yo normal shirt at fleft
    show el normal pioneer at fright
    ai "ai grin1 uniformb lng"

    scene bg int_bus_people_day
    show ai surprise shirt lng
    show mi normal pioneer at fleft
    show uv normal at fright
    ai "ai surprise shirt lng"

    scene bg ext_path2_day
    show ai scary xmas srt
    show un normal pioneer at fleft
    show dv normal pioneer at fright
    ai "ai scary xmas srt"

    scene bg ext_island_day
    show ai sad uniformw tal
    show un normal pioneer at fleft
    show us normal pioneer at fright
    ai "ai sad uniformw tal"

    scene bg ext_washstand_day
    show ai shy1 kimono srt
    show uv normal at fleft
    show el normal pioneer at fright
    ai "ai shy1 kimono srt"

    scene bg int_library_day
    show ai guilty shirt srt
    show yo normal shirt at fleft
    show mz normal pioneer at fright
    ai "ai guilty shirt srt"

    scene bg int_house_of_un_day
    show ai evilsmile1 pink srt
    show yo normal shirt at fleft
    show uv normal at fright
    ai "ai evilsmile1 pink srt"

    scene bg ext_bus
    show ai happy little2 lng
    show mz normal pioneer at fleft
    show pi at fright
    ai "ai happy little2 lng"

    scene bg ext_house_of_mt_day
    show ai laugh1 xmas tal
    show sl normal pioneer at fleft
    show yo normal shirt at fright
    ai "ai laugh1 xmas tal"

    scene bg int_aidpost_day_apple
    show ai smile1 kimono tal
    show jd normal pioneer at fleft
    show uv normal at fright
    ai "ai smile1 kimono tal"

    scene bg int_aidpost_day_apple
    show ai normal jeans tal
    show sl normal pioneer at fleft
    show uv normal at fright
    ai "ai normal jeans tal"

    scene bg ext_library_day
    show ai serious pink srt
    show yo normal shirt at fleft
    show gl normal at fright
    ai "ai serious pink srt"

    scene bg ext_house_of_mt_day
    show ai dontlike1 uniformw lng
    show yo normal shirt at fleft
    show uv normal at fright
    ai "ai dontlike1 uniformw lng"

    scene bg ext_house_of_un_day
    show ai angry1 uniformb srt
    show mz normal pioneer at fleft
    show el normal pioneer at fright
    ai "ai angry1 uniformb srt"

    scene bg ext_house_of_mt_day
    show ai rage xmas srt
    show mz normal pioneer at fleft
    show sh normal pioneer at fright
    ai "ai rage xmas srt"

    scene bg ext_playground_day
    show ai anger uniformw srt
    show mt normal pioneer at fleft
    show sh normal pioneer at fright
    ai "ai anger uniformw srt"

    scene bg ext_house_of_un_day
    show ai frust1 xmas tal
    show mt normal pioneer at fleft
    show uv normal at fright
    ai "ai frust1 xmas tal"

    scene bg ext_camp_entrance_day
    show ai dontlike2 little1 tal
    show jd normal pioneer at fleft
    show uv normal at fright
    ai "ai dontlike2 little1 tal"

    scene bg ext_boathouse_day
    show ai evilsmile2 little1 tal
    show sl normal pioneer at fleft
    show sh normal pioneer at fright
    ai "ai evilsmile2 little1 tal"

    scene bg ext_road_day
    show ai grin2 pink lng
    show pi at fleft
    show el normal pioneer at fright
    ai "ai grin2 pink lng"

    scene bg int_house_of_mt_day
    show ai smile2 jeans srt
    show pi at fleft
    show cs normal at fright
    ai "ai smile2 jeans srt"

    scene bg ext_polyana_day
    show ai shy2 xmas srt
    show el normal pioneer at fleft
    show sl normal pioneer at fright
    ai "ai shy2 xmas srt"

    scene bg int_aidpost_day_apple
    show ai laugh2 little1 tal
    show mi normal pioneer at fleft
    show mi normal pioneer at fright
    ai "ai laugh2 little1 tal"

    scene bg ext_dining_hall_away_day
    show ai frust2 kimono lng
    show sh normal pioneer at fleft
    show un normal pioneer at fright
    ai "ai frust2 kimono lng"

    scene bg int_bus
    show ai angry2 xmas srt
    show gl normal at fleft
    show yo normal shirt at fright
    ai "ai angry2 xmas srt"

    scene bg int_house_of_un_day
    show ai grin2 jeans tal
    show mz normal pioneer at fleft
    show mi normal pioneer at fright
    ai "ai grin2 jeans tal"

    scene bg int_house_of_sl_day
    show ai normal pink tal
    show jd normal pioneer at fleft
    show mt normal pioneer at fright
    ai "ai normal pink tal"

    scene bg ext_camp_entrance_day
    show ai smile2 little1 tal
    show uv normal at fleft
    show mz normal pioneer at fright
    ai "ai smile2 little1 tal"

    scene bg ext_washstand_day
    show ai dontlike1 little2 lng
    show dv normal pioneer at fleft
    show us normal pioneer at fright
    ai "ai dontlike1 little2 lng"

    scene bg ext_square_day_city
    show ai grin2 shirt srt
    show sh normal pioneer at fleft
    show el normal pioneer at fright
    ai "ai grin2 shirt srt"

    scene bg ext_square_day_city
    show ai evilsmile2 xmas tal
    show uv normal at fleft
    show el normal pioneer at fright
    ai "ai evilsmile2 xmas tal"

    scene bg ext_camp_entrance_day
    show ai evilsmile1 dress srt
    show jd normal pioneer at fleft
    show dv normal pioneer at fright
    ai "ai evilsmile1 dress srt"

    scene bg ext_houses_day
    show ai evilsmile1 kimono tal
    show uv normal at fleft
    show uv normal at fright
    ai "ai evilsmile1 kimono tal"

    scene bg int_musclub_day
    show ai dontlike2 uniformb tal
    show pi at fleft
    show us normal pioneer at fright
    ai "ai dontlike2 uniformb tal"

    scene bg ext_path2_day
    show ai dontlike1 uniformw lng
    show un normal pioneer at fleft
    show sl normal pioneer at fright
    ai "ai dontlike1 uniformw lng"

    $ persistent.sprite_time = "sunset"

    scene bg ext_dining_hall_away_sunset
    show ai grin1 uniformb lng far
    show pi far at fleft
    show us normal pioneer far at fright
    ai "ai grin1 uniformb lng"

    scene bg ext_beach_sunset
    show ai surprise shirt lng far
    show el normal pioneer far at fleft
    show cs normal far at fright
    ai "ai surprise shirt lng"

    scene bg int_house_of_mt_sunset
    show ai scary xmas srt far
    show yo normal shirt far at fleft
    show cs normal far at fright
    ai "ai scary xmas srt"

    scene bg int_dining_hall_sunset
    show ai sad uniformw tal far
    show mt normal pioneer far at fleft
    show el normal pioneer far at fright
    ai "ai sad uniformw tal"

    scene bg ext_house_of_mt_sunset
    show ai shy1 kimono srt far
    show sl normal pioneer far at fleft
    show us normal pioneer far at fright
    ai "ai shy1 kimono srt"

    scene bg ext_path_sunset
    show ai guilty shirt srt far
    show jd normal pioneer far at fleft
    show uv normal far at fright
    ai "ai guilty shirt srt"

    scene bg int_clubs_male_sunset
    show ai evilsmile1 pink srt far
    show pi far at fleft
    show yo normal shirt far at fright
    ai "ai evilsmile1 pink srt"

    scene bg ext_path_sunset
    show ai happy little2 lng far
    show el normal pioneer far at fleft
    show jd normal pioneer far at fright
    ai "ai happy little2 lng"

    scene bg ext_no_bus_sunset
    show ai laugh1 xmas tal far
    show jd normal pioneer far at fleft
    show cs normal far at fright
    ai "ai laugh1 xmas tal"

    scene bg ext_beach_sunset
    show ai smile1 kimono tal far
    show un normal pioneer far at fleft
    show mt normal pioneer far at fright
    ai "ai smile1 kimono tal"

    scene bg ext_dining_hall_near_sunset
    show ai normal jeans tal far
    show un normal pioneer far at fleft
    show us normal pioneer far at fright
    ai "ai normal jeans tal"

    scene bg int_dining_hall_sunset
    show ai serious pink srt far
    show sh normal pioneer far at fleft
    show sh normal pioneer far at fright
    ai "ai serious pink srt"

    scene bg ext_houses_sunset
    show ai dontlike1 uniformw lng far
    show us normal pioneer far at fleft
    show sl normal pioneer far at fright
    ai "ai dontlike1 uniformw lng"

    scene bg ext_houses_sunset
    show ai angry1 uniformb srt far
    show mz normal pioneer far at fleft
    show uv normal far at fright
    ai "ai angry1 uniformb srt"

    scene bg int_clubs_male_sunset
    show ai rage xmas srt far
    show gl normal far at fleft
    show gl normal far at fright
    ai "ai rage xmas srt"

    scene bg ext_polyana_sunset
    show ai anger uniformw srt far
    show gl normal far at fleft
    show gl normal far at fright
    ai "ai anger uniformw srt"

    scene bg ext_no_bus_sunset
    show ai frust1 xmas tal far
    show mz normal pioneer far at fleft
    show mz normal pioneer far at fright
    ai "ai frust1 xmas tal"

    scene bg int_dining_hall_sunset
    show ai dontlike2 little1 tal far
    show us normal pioneer far at fleft
    show dv normal pioneer far at fright
    ai "ai dontlike2 little1 tal"

    scene bg ext_dining_hall_away_sunset
    show ai evilsmile2 little1 tal far
    show mz normal pioneer far at fleft
    show pi far at fright
    ai "ai evilsmile2 little1 tal"

    scene bg ext_dining_hall_away_sunset
    show ai grin2 pink lng far
    show yo normal shirt far at fleft
    show un normal pioneer far at fright
    ai "ai grin2 pink lng"

    scene bg ext_no_bus_sunset
    show ai smile2 jeans srt far
    show sh normal pioneer far at fleft
    show cs normal far at fright
    ai "ai smile2 jeans srt"

    scene bg ext_house_of_mt_sunset
    show ai shy2 xmas srt far
    show uv normal far at fleft
    show sl normal pioneer far at fright
    ai "ai shy2 xmas srt"

    scene bg ext_dining_hall_near_sunset
    show ai laugh2 little1 tal far
    show yo normal shirt far at fleft
    show un normal pioneer far at fright
    ai "ai laugh2 little1 tal"

    scene bg int_clubs_male_sunset
    show ai frust2 kimono lng far
    show mi normal pioneer far at fleft
    show dv normal pioneer far at fright
    ai "ai frust2 kimono lng"

    scene bg ext_square_sunset
    show ai angry2 xmas srt far
    show dv normal pioneer far at fleft
    show mt normal pioneer far at fright
    ai "ai angry2 xmas srt"

    scene bg ext_no_bus_sunset
    show ai grin2 jeans tal far
    show sl normal pioneer far at fleft
    show jd normal pioneer far at fright
    ai "ai grin2 jeans tal"

    scene bg int_clubs_male_sunset
    show ai normal pink tal far
    show cs normal far at fleft
    show el normal pioneer far at fright
    ai "ai normal pink tal"

    scene bg ext_square_sunset
    show ai smile2 little1 tal far
    show us normal pioneer far at fleft
    show el normal pioneer far at fright
    ai "ai smile2 little1 tal"

    scene bg ext_houses_sunset
    show ai dontlike1 little2 lng far
    show dv normal pioneer far at fleft
    show mt normal pioneer far at fright
    ai "ai dontlike1 little2 lng"

    scene bg ext_path_sunset
    show ai grin2 shirt srt far
    show el normal pioneer far at fleft
    show cs normal far at fright
    ai "ai grin2 shirt srt"

    scene bg ext_path_sunset
    show ai evilsmile2 xmas tal far
    show sh normal pioneer far at fleft
    show cs normal far at fright
    ai "ai evilsmile2 xmas tal"

    scene bg ext_road_sunset
    show ai evilsmile1 dress srt far
    show mi normal pioneer far at fleft
    show sh normal pioneer far at fright
    ai "ai evilsmile1 dress srt"

    scene bg ext_road_sunset
    show ai evilsmile1 kimono tal far
    show us normal pioneer far at fleft
    show yo normal shirt far at fright
    ai "ai evilsmile1 kimono tal"

    scene bg ext_no_bus_sunset
    show ai dontlike2 uniformb tal far
    show cs normal far at fleft
    show uv normal far at fright
    ai "ai dontlike2 uniformb tal"

    scene bg ext_houses_sunset
    show ai dontlike1 uniformw lng far
    show uv normal far at fleft
    show dv normal pioneer far at fright
    ai "ai dontlike1 uniformw lng"

    $ persistent.sprite_time = "night"

    scene bg int_old_building_night
    show ai grin1 uniformb lng close
    show mz normal pioneer close at fleft
    show cs normal close at fright
    ai "ai grin1 uniformb lng"

    scene bg int_house_of_mt_night2
    show ai surprise shirt lng close
    show sl normal pioneer close at fleft
    show el normal pioneer close at fright
    ai "ai surprise shirt lng"

    scene bg int_dining_hall_night
    show ai scary xmas srt close
    show pi close at fleft
    show mz normal pioneer close at fright
    ai "ai scary xmas srt"

    scene bg ext_library_night
    show ai sad uniformw tal close
    show dv normal pioneer close at fleft
    show gl normal close at fright
    ai "ai sad uniformw tal"

    scene bg ext_square_night_party
    show ai shy1 kimono srt close
    show mt normal pioneer close at fleft
    show mt normal pioneer close at fright
    ai "ai shy1 kimono srt"

    scene bg ext_square_night
    show ai guilty shirt srt close
    show un normal pioneer close at fleft
    show un normal pioneer close at fright
    ai "ai guilty shirt srt"

    scene bg ext_old_building_night
    show ai evilsmile1 pink srt close
    show mt normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "ai evilsmile1 pink srt"

    scene bg ext_camp_entrance_night
    show ai happy little2 lng close
    show un normal pioneer close at fleft
    show un normal pioneer close at fright
    ai "ai happy little2 lng"

    scene bg int_house_of_mt_night2
    show ai laugh1 xmas tal close
    show un normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "ai laugh1 xmas tal"

    scene bg ext_playground_night
    show ai smile1 kimono tal close
    show mz normal pioneer close at fleft
    show gl normal close at fright
    ai "ai smile1 kimono tal"

    scene bg int_bus_night
    show ai normal jeans tal close
    show yo normal shirt close at fleft
    show us normal pioneer close at fright
    ai "ai normal jeans tal"

    scene bg ext_stage_normal_night
    show ai serious pink srt close
    show sh normal pioneer close at fleft
    show sl normal pioneer close at fright
    ai "ai serious pink srt"

    scene bg ext_stage_normal_night
    show ai dontlike1 uniformw lng close
    show mt normal pioneer close at fleft
    show sl normal pioneer close at fright
    ai "ai dontlike1 uniformw lng"

    scene bg ext_boathouse_night
    show ai angry1 uniformb srt close
    show uv normal close at fleft
    show el normal pioneer close at fright
    ai "ai angry1 uniformb srt"

    scene bg int_old_building_night
    show ai rage xmas srt close
    show jd normal pioneer close at fleft
    show jd normal pioneer close at fright
    ai "ai rage xmas srt"

    scene bg ext_path2_night
    show ai anger uniformw srt close
    show us normal pioneer close at fleft
    show uv normal close at fright
    ai "ai anger uniformw srt"

    scene bg ext_square_night_party2
    show ai frust1 xmas tal close
    show yo normal shirt close at fleft
    show jd normal pioneer close at fright
    ai "ai frust1 xmas tal"

    scene bg ext_camp_entrance_night
    show ai dontlike2 little1 tal close
    show sl normal pioneer close at fleft
    show cs normal close at fright
    ai "ai dontlike2 little1 tal"

    scene bg int_clubs_male2_night
    show ai evilsmile2 little1 tal close
    show jd normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "ai evilsmile2 little1 tal"

    scene bg ext_house_of_dv_night
    show ai grin2 pink lng close
    show sh normal pioneer close at fleft
    show cs normal close at fright
    ai "ai grin2 pink lng"

    scene bg int_house_of_un_night
    show ai smile2 jeans srt close
    show sh normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "ai smile2 jeans srt"

    scene bg ext_square_night
    show ai shy2 xmas srt close
    show cs normal close at fleft
    show sh normal pioneer close at fright
    ai "ai shy2 xmas srt"

    scene bg int_bus_night
    show ai laugh2 little1 tal close
    show mz normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "ai laugh2 little1 tal"

    scene bg int_old_building_night
    show ai frust2 kimono lng close
    show sh normal pioneer close at fleft
    show el normal pioneer close at fright
    ai "ai frust2 kimono lng"

    scene bg ext_beach_night
    show ai angry2 xmas srt close
    show mz normal pioneer close at fleft
    show jd normal pioneer close at fright
    ai "ai angry2 xmas srt"

    scene bg ext_polyana_night
    show ai grin2 jeans tal close
    show us normal pioneer close at fleft
    show uv normal close at fright
    ai "ai grin2 jeans tal"

    scene bg ext_stage_normal_night
    show ai normal pink tal close
    show uv normal close at fleft
    show jd normal pioneer close at fright
    ai "ai normal pink tal"

    scene bg int_old_building_night
    show ai smile2 little1 tal close
    show us normal pioneer close at fleft
    show cs normal close at fright
    ai "ai smile2 little1 tal"

    scene bg int_library_night
    show ai dontlike1 little2 lng close
    show sl normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "ai dontlike1 little2 lng"

    scene bg ext_beach_night
    show ai grin2 shirt srt close
    show gl normal close at fleft
    show pi close at fright
    ai "ai grin2 shirt srt"

    scene bg ext_aidpost_night
    show ai evilsmile2 xmas tal close
    show mz normal pioneer close at fleft
    show pi close at fright
    ai "ai evilsmile2 xmas tal"

    scene bg int_library_night2
    show ai evilsmile1 dress srt close
    show sl normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "ai evilsmile1 dress srt"

    scene bg ext_playground_night
    show ai evilsmile1 kimono tal close
    show cs normal close at fleft
    show us normal pioneer close at fright
    ai "ai evilsmile1 kimono tal"

    scene bg int_house_of_un_night
    show ai dontlike2 uniformb tal close
    show yo normal shirt close at fleft
    show mt normal pioneer close at fright
    ai "ai dontlike2 uniformb tal"

    scene bg ext_road_night2
    show ai dontlike1 uniformw lng close
    show mi normal pioneer close at fleft
    show cs normal close at fright
    ai "ai dontlike1 uniformw lng"
















    
