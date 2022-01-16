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
    
    show gl grin1 jeans
    show un normal pioneer at left
    show mz normal pioneer at right
    gl "grin1"

    scene bg ext_path_day
    show gl surprise jeans
    show sh normal pioneer at left
    show sl normal pioneer at right
    gl "surprise"

    scene bg ext_house_of_mt_day
    show gl scary jeans
    show mt normal pioneer at left
    show ai normal lng_pink at right
    gl "scary"

    scene bg ext_house_of_un_day
    show gl sad jeans
    show mz normal pioneer at left
    show yo normal shirt at right
    gl "sad"

    scene bg ext_path_day
    show gl shy1 jeans
    show el normal pioneer at left
    show el normal pioneer at right
    gl "shy1"

    scene bg ext_beach_day
    show gl guilty jeans
    show yo normal shirt at left
    show sl normal pioneer at right
    gl "guilty"

    scene bg ext_dining_hall_away_day
    show gl evilsmile1 jeans
    show cs normal at left
    show sh normal pioneer at right
    gl "evilsmile1"

    scene bg ext_boathouse_day
    show gl happy jeans
    show yo normal shirt at left
    show mz normal pioneer at right
    gl "happy"

    scene bg ext_path_day
    show gl laugh1 jeans
    show sl normal pioneer at left
    show mi normal pioneer at right
    gl "laugh1"

    scene bg int_house_of_dv_day
    show gl smile1 jeans
    show el normal pioneer at left
    show mz normal pioneer at right
    gl "smile1"

    scene bg ext_polyana_day
    show gl normal jeans
    show cs normal at left
    show uv normal at right
    gl "normal"

    scene bg ext_stage_normal_day
    show gl serious jeans
    show mz normal pioneer at left
    show jd normal pioneer at right
    gl "serious"

    scene bg ext_playground_day
    show gl dontlike1 jeans
    show un normal pioneer at left
    show cs normal at right
    gl "dontlike1"

    scene bg ext_road_day
    show gl angry1 jeans
    show yo normal shirt at left
    show ai normal lng_pink at right
    gl "angry1"

    scene bg ext_polyana_day
    show gl rage jeans
    show ai normal lng_pink at left
    show pi at right
    gl "rage"

    scene bg ext_no_bus
    show gl anger jeans
    show yo normal shirt at left
    show cs normal at right
    gl "anger"

    scene bg int_house_of_mt_day
    show gl frust1 jeans
    show uv normal at left
    show pi at right
    gl "frust1"

    scene bg ext_path2_day
    show gl dontlike2 jeans
    show dv normal pioneer at left
    show un normal pioneer at right
    gl "dontlike2"

    scene bg ext_bus
    show gl evilsmile2 jeans
    show mt normal pioneer at left
    show sl normal pioneer at right
    gl "evilsmile2"

    scene bg ext_stage_normal_day
    show gl grin2 jeans
    show mi normal pioneer at left
    show uv normal at right
    gl "grin2"

    scene bg ext_house_of_un_day
    show gl smile2 jeans
    show mz normal pioneer at left
    show us normal pioneer at right
    gl "smile2"

    scene bg ext_house_of_dv_day
    show gl shy2 jeans
    show yo normal shirt at left
    show cs normal at right
    gl "shy2"

    scene bg ext_playground_day
    show gl laugh2 jeans
    show cs normal at left
    show pi at right
    gl "laugh2"

    scene bg ext_house_of_un_day
    show gl frust2 jeans
    show mt normal pioneer at left
    show uv normal at right
    gl "frust2"

    scene bg ext_road_day
    show gl angry2 jeans
    show jd normal pioneer at left
    show un normal pioneer at right
    gl "angry2"

    $ persistent.sprite_time = "sunset"

    scene bg ext_road_sunset
    show gl grin1 jeans far
    show el normal pioneer far at left
    show pi far at right
    gl "grin1"

    scene bg int_clubs_male_sunset
    show gl surprise jeans far
    show ai normal lng_pink far at left
    show sl normal pioneer far at right
    gl "surprise"

    scene bg ext_houses_sunset
    show gl scary jeans far
    show ai normal lng_pink far at left
    show cs normal far at right
    gl "scary"

    scene bg ext_path_sunset
    show gl sad jeans far
    show us normal pioneer far at left
    show mi normal pioneer far at right
    gl "sad"

    scene bg ext_no_bus_sunset
    show gl shy1 jeans far
    show pi far at left
    show jd normal pioneer far at right
    gl "shy1"

    scene bg ext_beach_sunset
    show gl guilty jeans far
    show el normal pioneer far at left
    show sh normal pioneer far at right
    gl "guilty"

    scene bg ext_houses_sunset
    show gl evilsmile1 jeans far
    show sh normal pioneer far at left
    show jd normal pioneer far at right
    gl "evilsmile1"

    scene bg int_clubs_male_sunset
    show gl happy jeans far
    show mi normal pioneer far at left
    show us normal pioneer far at right
    gl "happy"

    scene bg ext_houses_sunset
    show gl laugh1 jeans far
    show ai normal lng_pink far at left
    show ai normal lng_pink far at right
    gl "laugh1"

    scene bg ext_path_sunset
    show gl smile1 jeans far
    show pi far at left
    show sl normal pioneer far at right
    gl "smile1"

    scene bg int_dining_hall_sunset
    show gl normal jeans far
    show sl normal pioneer far at left
    show mi normal pioneer far at right
    gl "normal"

    scene bg ext_path_sunset
    show gl serious jeans far
    show mt normal pioneer far at left
    show mt normal pioneer far at right
    gl "serious"

    scene bg int_dining_hall_sunset
    show gl dontlike1 jeans far
    show pi far at left
    show mz normal pioneer far at right
    gl "dontlike1"

    scene bg ext_dining_hall_near_sunset
    show gl angry1 jeans far
    show yo normal shirt far at left
    show mz normal pioneer far at right
    gl "angry1"

    scene bg ext_square_sunset
    show gl rage jeans far
    show uv normal far at left
    show dv normal pioneer far at right
    gl "rage"

    scene bg ext_no_bus_sunset
    show gl anger jeans far
    show yo normal shirt far at left
    show sl normal pioneer far at right
    gl "anger"

    scene bg ext_square_sunset
    show gl frust1 jeans far
    show mi normal pioneer far at left
    show sh normal pioneer far at right
    gl "frust1"

    scene bg int_dining_hall_sunset
    show gl dontlike2 jeans far
    show sl normal pioneer far at left
    show sl normal pioneer far at right
    gl "dontlike2"

    scene bg ext_road_sunset
    show gl evilsmile2 jeans far
    show mi normal pioneer far at left
    show ai normal lng_pink far at right
    gl "evilsmile2"

    scene bg ext_dining_hall_away_sunset
    show gl grin2 jeans far
    show el normal pioneer far at left
    show sh normal pioneer far at right
    gl "grin2"

    scene bg ext_road_sunset
    show gl smile2 jeans far
    show uv normal far at left
    show dv normal pioneer far at right
    gl "smile2"

    scene bg ext_polyana_sunset
    show gl shy2 jeans far
    show pi far at left
    show mz normal pioneer far at right
    gl "shy2"

    scene bg ext_square_sunset
    show gl laugh2 jeans far
    show sl normal pioneer far at left
    show un normal pioneer far at right
    gl "laugh2"

    scene bg ext_square_sunset
    show gl frust2 jeans far
    show yo normal shirt far at left
    show uv normal far at right
    gl "frust2"

    scene bg int_dining_hall_sunset
    show gl angry2 jeans far
    show mt normal pioneer far at left
    show pi far at right
    gl "angry2"

    $ persistent.sprite_time = "night"

    scene bg ext_camp_entrance_night
    show gl grin1 jeans close
    show mi normal pioneer close at fleft
    show yo normal shirt close at fright
    gl "grin1"

    scene bg ext_square_night_party
    show gl surprise jeans close
    show us normal pioneer close at fleft
    show el normal pioneer close at fright
    gl "surprise"

    scene bg int_bus_people_night
    show gl scary jeans close
    show us normal pioneer close at fleft
    show dv normal pioneer close at fright
    gl "scary"

    scene bg ext_camp_entrance_night
    show gl sad jeans close
    show cs normal close at fleft
    show un normal pioneer close at fright
    gl "sad"

    scene bg int_old_building_night
    show gl shy1 jeans close
    show uv normal close at fleft
    show sl normal pioneer close at fright
    gl "shy1"

    scene bg ext_polyana_night
    show gl guilty jeans close
    show mz normal pioneer close at fleft
    show pi close at fright
    gl "guilty"

    scene bg int_library_night2
    show gl evilsmile1 jeans close
    show pi close at fleft
    show ai normal lng_pink close at fright
    gl "evilsmile1"

    scene bg int_bus_night
    show gl happy jeans close
    show sl normal pioneer close at fleft
    show sh normal pioneer close at fright
    gl "happy"

    scene bg int_clubs_male2_night_nolight
    show gl laugh1 jeans close
    show uv normal close at fleft
    show un normal pioneer close at fright
    gl "laugh1"

    scene bg ext_square_night_party
    show gl smile1 jeans close
    show mt normal pioneer close at fleft
    show us normal pioneer close at fright
    gl "smile1"

    scene bg ext_library_night
    show gl normal jeans close
    show us normal pioneer close at fleft
    show ai normal lng_pink close at fright
    gl "normal"

    scene bg ext_house_of_mt_night_without_light
    show gl serious jeans close
    show jd normal pioneer close at fleft
    show ai normal lng_pink close at fright
    gl "serious"

    scene bg int_house_of_un_night
    show gl dontlike1 jeans close
    show yo normal shirt close at fleft
    show mz normal pioneer close at fright
    gl "dontlike1"

    scene bg ext_boathouse_night
    show gl angry1 jeans close
    show ai normal lng_pink close at fleft
    show mt normal pioneer close at fright
    gl "angry1"

    scene bg ext_playground_night
    show gl rage jeans close
    show mi normal pioneer close at fleft
    show mz normal pioneer close at fright
    gl "rage"

    scene bg ext_house_of_mt_night
    show gl anger jeans close
    show sh normal pioneer close at fleft
    show mz normal pioneer close at fright
    gl "anger"

    scene bg int_bus_night
    show gl frust1 jeans close
    show un normal pioneer close at fleft
    show cs normal close at fright
    gl "frust1"

    scene bg ext_old_building_night
    show gl dontlike2 jeans close
    show pi close at fleft
    show sh normal pioneer close at fright
    gl "dontlike2"

    scene bg ext_aidpost_night
    show gl evilsmile2 jeans close
    show sh normal pioneer close at fleft
    show us normal pioneer close at fright
    gl "evilsmile2"

    scene bg int_bus_night
    show gl grin2 jeans close
    show el normal pioneer close at fleft
    show pi close at fright
    gl "grin2"

    scene bg ext_camp_entrance_night
    show gl smile2 jeans close
    show pi close at fleft
    show yo normal shirt close at fright
    gl "smile2"

    scene bg ext_old_building_night
    show gl shy2 jeans close
    show cs normal close at fleft
    show mi normal pioneer close at fright
    gl "shy2"

    scene bg ext_polyana_night
    show gl laugh2 jeans close
    show ai normal lng_pink close at fleft
    show jd normal pioneer close at fright
    gl "laugh2"

    scene bg ext_square_night_party
    show gl frust2 jeans close
    show un normal pioneer close at fleft
    show us normal pioneer close at fright
    gl "frust2"

    scene bg ext_house_of_mt_night
    show gl angry2 jeans close
    show sl normal pioneer close at fleft
    show uv normal close at fright
    gl "angry2"






    
