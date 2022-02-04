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
    
    show gl grin1
    show pi normal at fleft
    show pi normal at fright
    gl "gl grin1"

    scene bg int_house_of_sl_day
    show gl surprise
    show mz normal pioneer at fleft
    show us normal pioneer at fright
    gl "gl surprise"

    scene bg ext_clubs_day
    show gl scary neko
    show sh normal pioneer at fleft
    show mz normal pioneer at fright
    gl "gl scary neko"

    scene bg ext_boathouse_day
    show gl sad
    show us normal pioneer at fleft
    show cs normal at fright
    gl "gl sad"

    scene bg ext_path2_day
    show gl shy1
    show uv normal at fleft
    show ai normal pink at fright
    gl "gl shy1"

    scene bg ext_house_of_un_day
    show gl guilty
    show un normal pioneer at fleft
    show sh normal pioneer at fright
    gl "gl guilty"

    scene bg ext_dining_hall_near_day
    show gl evilsmile1 neko
    show sh normal pioneer at fleft
    show ai normal pink at fright
    gl "gl evilsmile1 neko"

    scene bg ext_path2_day
    show gl happy
    show un normal pioneer at fleft
    show un normal pioneer at fright
    gl "gl happy"

    scene bg ext_no_bus
    show gl laugh1 neko
    show sl normal pioneer at fleft
    show uv normal at fright
    gl "gl laugh1 neko"

    scene bg ext_dining_hall_away_day
    show gl smile1
    show mi normal pioneer at fleft
    show mt normal pioneer at fright
    gl "gl smile1"

    scene bg ext_square_day_city
    show gl normal
    show mi normal pioneer at fleft
    show sh normal pioneer at fright
    gl "gl normal"

    scene bg ext_dining_hall_near_day
    show gl serious
    show uv normal at fleft
    show mt normal pioneer at fright
    gl "gl serious"

    scene bg int_bus_people_day
    show gl dontlike1
    show mz normal pioneer at fleft
    show mz normal pioneer at fright
    gl "gl dontlike1"

    scene bg ext_playground_day
    show gl angry1
    show el normal pioneer at fleft
    show yo normal shirt at fright
    gl "gl angry1"

    scene bg int_aidpost_day_apple
    show gl rage
    show uv normal at fleft
    show sh normal pioneer at fright
    gl "gl rage"

    scene bg ext_bus
    show gl anger neko
    show yo normal shirt at fleft
    show yo normal shirt at fright
    gl "gl anger neko"

    scene bg int_house_of_un_day
    show gl frust1
    show mi normal pioneer at fleft
    show ai normal pink at fright
    gl "gl frust1"

    scene bg ext_dining_hall_away_day
    show gl dontlike2 neko
    show un normal pioneer at fleft
    show uv normal at fright
    gl "gl dontlike2 neko"

    scene bg ext_path2_day
    show gl evilsmile2
    show sh normal pioneer at fleft
    show dv normal pioneer at fright
    gl "gl evilsmile2"

    scene bg ext_clubs_day
    show gl grin2
    show mi normal pioneer at fleft
    show jd normal pioneer at fright
    gl "gl grin2"

    scene bg ext_polyana_day
    show gl smile2 neko
    show un normal pioneer at fleft
    show mz normal pioneer at fright
    gl "gl smile2 neko"

    scene bg int_clubs_male_day
    show gl shy2 neko
    show dv normal pioneer at fleft
    show yo normal shirt at fright
    gl "gl shy2 neko"

    scene bg int_bus
    show gl laugh2
    show el normal pioneer at fleft
    show mz normal pioneer at fright
    gl "gl laugh2"

    scene bg int_bus_people_day
    show gl frust2
    show mi normal pioneer at fleft
    show un normal pioneer at fright
    gl "gl frust2"

    scene bg ext_boathouse_day
    show gl angry2 neko
    show dv normal pioneer at fleft
    show dv normal pioneer at fright
    gl "gl angry2 neko"

    scene bg ext_aidpost_day
    show gl evilsmile1 neko
    show pi normal at fleft
    show mi normal pioneer at fright
    gl "gl evilsmile1 neko"

    $ persistent.sprite_time = "sunset"

    scene bg ext_polyana_sunset
    show gl grin1 far
    show us normal pioneer far at fleft
    show sl normal pioneer far at fright
    gl "gl grin1"

    scene bg ext_house_of_mt_sunset
    show gl surprise far
    show yo normal shirt far at fleft
    show mt normal pioneer far at fright
    gl "gl surprise"

    scene bg ext_no_bus_sunset
    show gl scary neko far
    show sl normal pioneer far at fleft
    show us normal pioneer far at fright
    gl "gl scary neko"

    scene bg ext_house_of_mt_sunset
    show gl sad far
    show mi normal pioneer far at fleft
    show sh normal pioneer far at fright
    gl "gl sad"

    scene bg int_clubs_male_sunset
    show gl shy1 far
    show yo normal shirt far at fleft
    show uv normal far at fright
    gl "gl shy1"

    scene bg int_dining_hall_sunset
    show gl guilty far
    show pi normal far at fleft
    show ai normal pink far at fright
    gl "gl guilty"

    scene bg int_dining_hall_sunset
    show gl evilsmile1 neko far
    show mz normal pioneer far at fleft
    show sh normal pioneer far at fright
    gl "gl evilsmile1 neko"

    scene bg ext_no_bus_sunset
    show gl happy far
    show uv normal far at fleft
    show yo normal shirt far at fright
    gl "gl happy"

    scene bg ext_path_sunset
    show gl laugh1 neko far
    show jd normal pioneer far at fleft
    show mi normal pioneer far at fright
    gl "gl laugh1 neko"

    scene bg ext_no_bus_sunset
    show gl smile1 far
    show el normal pioneer far at fleft
    show yo normal shirt far at fright
    gl "gl smile1"

    scene bg ext_house_of_mt_sunset
    show gl normal far
    show us normal pioneer far at fleft
    show jd normal pioneer far at fright
    gl "gl normal"

    scene bg ext_dining_hall_away_sunset
    show gl serious far
    show mi normal pioneer far at fleft
    show ai normal pink far at fright
    gl "gl serious"

    scene bg ext_beach_sunset
    show gl dontlike1 far
    show pi normal far at fleft
    show uv normal far at fright
    gl "gl dontlike1"

    scene bg ext_polyana_sunset
    show gl angry1 far
    show mz normal pioneer far at fleft
    show mz normal pioneer far at fright
    gl "gl angry1"

    scene bg ext_beach_sunset
    show gl rage far
    show sl normal pioneer far at fleft
    show us normal pioneer far at fright
    gl "gl rage"

    scene bg ext_road_sunset
    show gl anger neko far
    show cs normal far at fleft
    show dv normal pioneer far at fright
    gl "gl anger neko"

    scene bg int_clubs_male_sunset
    show gl frust1 far
    show mi normal pioneer far at fleft
    show jd normal pioneer far at fright
    gl "gl frust1"

    scene bg ext_dining_hall_near_sunset
    show gl dontlike2 neko far
    show uv normal far at fleft
    show mt normal pioneer far at fright
    gl "gl dontlike2 neko"

    scene bg ext_beach_sunset
    show gl evilsmile2 far
    show sh normal pioneer far at fleft
    show pi normal far at fright
    gl "gl evilsmile2"

    scene bg ext_dining_hall_near_sunset
    show gl grin2 far
    show el normal pioneer far at fleft
    show sl normal pioneer far at fright
    gl "gl grin2"

    scene bg ext_dining_hall_away_sunset
    show gl smile2 neko far
    show uv normal far at fleft
    show pi normal far at fright
    gl "gl smile2 neko"

    scene bg ext_beach_sunset
    show gl shy2 neko far
    show sh normal pioneer far at fleft
    show sl normal pioneer far at fright
    gl "gl shy2 neko"

    scene bg ext_polyana_sunset
    show gl laugh2 far
    show uv normal far at fleft
    show mz normal pioneer far at fright
    gl "gl laugh2"

    scene bg ext_polyana_sunset
    show gl frust2 far
    show cs normal far at fleft
    show mz normal pioneer far at fright
    gl "gl frust2"

    scene bg ext_polyana_sunset
    show gl angry2 neko far
    show yo normal shirt far at fleft
    show us normal pioneer far at fright
    gl "gl angry2 neko"

    scene bg ext_dining_hall_near_sunset
    show gl evilsmile1 neko far
    show dv normal pioneer far at fleft
    show jd normal pioneer far at fright
    gl "gl evilsmile1 neko"

    $ persistent.sprite_time = "night"

    scene bg ext_clubs_night
    show gl grin1 vclose
    show cs normal close at fleft
    show us normal pioneer close at fright
    gl "gl grin1"

    scene bg ext_square_night_party2
    show gl surprise close
    show sl normal pioneer close at fleft
    show pi normal close at fright
    gl "gl surprise"

    scene bg ext_house_of_dv_night
    show gl scary neko close
    show mi normal pioneer close at fleft
    show mz normal pioneer close at fright
    gl "gl scary neko"

    scene bg int_bus_night
    show gl sad vclose
    show mt normal pioneer close at fleft
    show mt normal pioneer close at fright
    gl "gl sad"

    scene bg ext_dining_hall_away_night
    show gl shy1 close
    show yo normal shirt close at fleft
    show sl normal pioneer close at fright
    gl "gl shy1"

    scene bg ext_aidpost_night
    show gl guilty close
    show sl normal pioneer close at fleft
    show el normal pioneer close at fright
    gl "gl guilty"

    scene bg ext_square_night
    show gl evilsmile1 neko vclose
    show cs normal close at fleft
    show mt normal pioneer close at fright
    gl "gl evilsmile1 neko"

    scene bg ext_clubs_night
    show gl happy close
    show mz normal pioneer close at fleft
    show sh normal pioneer close at fright
    gl "gl happy"

    scene bg ext_dining_hall_away_night
    show gl laugh1 neko close
    show cs normal close at fleft
    show un normal pioneer close at fright
    gl "gl laugh1 neko"

    scene bg ext_dining_hall_near_night
    show gl smile1 vclose
    show ai normal pink close at fleft
    show pi normal close at fright
    gl "gl smile1"

    scene bg ext_aidpost_night
    show gl normal close
    show yo normal shirt close at fleft
    show jd normal pioneer close at fright
    gl "gl normal"

    scene bg ext_dining_hall_near_night
    show gl serious close
    show ai normal pink close at fleft
    show dv normal pioneer close at fright
    gl "gl serious"

    scene bg ext_aidpost_night
    show gl dontlike1 vclose
    show el normal pioneer close at fleft
    show sl normal pioneer close at fright
    gl "gl dontlike1"

    scene bg ext_polyana_night
    show gl angry1 close
    show jd normal pioneer close at fleft
    show mi normal pioneer close at fright
    gl "gl angry1"

    scene bg ext_library_night
    show gl rage close
    show pi normal close at fleft
    show sl normal pioneer close at fright
    gl "gl rage"

    scene bg ext_square_night
    show gl anger neko vclose
    show uv normal close at fleft
    show mz normal pioneer close at fright
    gl "gl anger neko"

    scene bg int_house_of_mt_noitem_night
    show gl frust1 close
    show jd normal pioneer close at fleft
    show sl normal pioneer close at fright
    gl "gl frust1"

    scene bg ext_boathouse_night
    show gl dontlike2 neko close
    show pi normal close at fleft
    show sl normal pioneer close at fright
    gl "gl dontlike2 neko"

    scene bg ext_road_night2
    show gl evilsmile2 vclose
    show jd normal pioneer close at fleft
    show el normal pioneer close at fright
    gl "gl evilsmile2"

    scene bg ext_old_building_night_moonlight
    show gl grin2 close
    show mt normal pioneer close at fleft
    show jd normal pioneer close at fright
    gl "gl grin2"

    scene bg ext_dining_hall_near_night
    show gl smile2 neko close
    show ai normal pink close at fleft
    show dv normal pioneer close at fright
    gl "gl smile2 neko"

    scene bg ext_old_building_night
    show gl shy2 neko vclose
    show sl normal pioneer close at fleft
    show jd normal pioneer close at fright
    gl "gl shy2 neko"

    scene bg ext_bus_night
    show gl laugh2 close
    show yo normal shirt close at fleft
    show el normal pioneer close at fright
    gl "gl laugh2"

    scene bg ext_library_night
    show gl frust2 close
    show pi normal close at fleft
    show el normal pioneer close at fright
    gl "gl frust2"

    scene bg ext_aidpost_night
    show gl angry2 neko vclose
    show pi normal close at fleft
    show mt normal pioneer close at fright
    gl "gl angry2 neko"

    scene bg int_library_night2
    show gl evilsmile1 neko close
    show mt normal pioneer close at fleft
    show yo normal shirt close at fright
    gl "gl evilsmile1 neko"




















    
