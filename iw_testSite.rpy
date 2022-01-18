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
    show mt normal pioneer at left
    show mi normal pioneer at right
    ai "grin1"

    scene bg ext_house_of_mt_day
    show gl grin1 
    show uv normal at left
    show yo normal shirt at right
    ai "grin1"

    scene bg ext_dining_hall_near_day
    show gl surprise ears
    show mt normal pioneer at left
    show un normal pioneer at right
    ai "surprise"

    scene bg int_dining_hall_day
    show gl scary 
    show un normal pioneer at left
    show pi at right
    ai "scary"

    scene bg ext_dining_hall_near_day
    show gl sad 
    show mi normal pioneer at left
    show mt normal pioneer at right
    ai "sad"

    scene bg int_dining_hall_day
    show gl shy1 
    show yo normal shirt at left
    show uv normal at right
    ai "shy1"

    scene bg ext_dining_hall_near_day
    show gl guilty 
    show mt normal pioneer at left
    show sl normal pioneer at right
    ai "guilty"

    scene bg ext_road_day
    show gl evilsmile1 
    show pi at left
    show sh normal pioneer at right
    ai "evilsmile1"

    scene bg ext_dining_hall_near_day
    show gl happy 
    show un normal pioneer at left
    show us normal pioneer at right
    ai "happy"

    scene bg ext_camp_entrance_day
    show gl laugh1 
    show sl normal pioneer at left
    show dv normal pioneer at right
    ai "laugh1"

    scene bg ext_square_day_city
    show gl smile1 
    show mz normal pioneer at left
    show sh normal pioneer at right
    ai "smile1"

    scene bg ext_bus
    show gl normal 
    show sh normal pioneer at left
    show jd normal pioneer at right
    ai "normal"

    scene bg ext_musclub_day
    show gl serious ears
    show cs normal at left
    show dv normal pioneer at right
    ai "serious"

    scene bg int_bus_people_day
    show gl dontlike1 
    show jd normal pioneer at left
    show pi at right
    ai "dontlike1"

    scene bg ext_washstand_day
    show gl angry1 
    show mi normal pioneer at left
    show pi at right
    ai "angry1"

    scene bg int_house_of_sl_day
    show gl rage 
    show mt normal pioneer at left
    show pi at right
    ai "rage"

    scene bg int_house_of_sl_day
    show gl anger 
    show us normal pioneer at left
    show el normal pioneer at right
    ai "anger"

    scene bg ext_playground_day
    show gl frust1 
    show uv normal at left
    show cs normal at right
    ai "frust1"

    scene bg ext_washstand2_day
    show gl dontlike2 
    show el normal pioneer at left
    show sh normal pioneer at right
    ai "dontlike2"

    scene bg int_aidpost_day_apple
    show gl evilsmile2 
    show cs normal at left
    show mz normal pioneer at right
    ai "evilsmile2"

    scene bg ext_polyana_day
    show gl grin2 
    show uv normal at left
    show mi normal pioneer at right
    ai "grin2"

    scene bg ext_musclub_day
    show gl smile2 
    show sh normal pioneer at left
    show us normal pioneer at right
    ai "smile2"

    scene bg ext_musclub_day
    show gl shy2 
    show pi at left
    show us normal pioneer at right
    ai "shy2"

    scene bg ext_road_day
    show gl laugh2 
    show us normal pioneer at left
    show mt normal pioneer at right
    ai "laugh2"

    scene bg ext_washstand_day
    show gl frust2 
    show mi normal pioneer at left
    show el normal pioneer at right
    ai "frust2"

    scene bg ext_house_of_sl_day
    show gl angry2 
    show yo normal shirt at left
    show us normal pioneer at right
    ai "angry2"

    scene bg ext_clubs_day
    show gl angry2 ears
    show el normal pioneer at left
    show pi at right
    ai ""

    $ persistent.sprite_time = "sunset"

    scene bg ext_polyana_sunset
    show gl grin1  far
    show us normal pioneer far at left
    show pi far at right
    ai "grin1"

    scene bg ext_house_of_mt_sunset
    show gl surprise  far
    show un normal pioneer far at left
    show sl normal pioneer far at right
    ai "surprise"

    scene bg ext_polyana_sunset
    show gl scary  far
    show el normal pioneer far at left
    show pi far at right
    ai "scary"

    scene bg int_dining_hall_sunset
    show gl sad  far
    show sh normal pioneer far at left
    show mt normal pioneer far at right
    ai "sad"

    scene bg ext_path_sunset
    show gl shy1  far
    show mt normal pioneer far at left
    show yo normal shirt far at right
    ai "shy1"

    scene bg ext_square_sunset
    show gl guilty  far
    show yo normal shirt far at left
    show uv normal far at right
    ai "guilty"

    scene bg int_dining_hall_sunset
    show gl evilsmile1 ears far
    show un normal pioneer far at left
    show uv normal far at right
    ai "evilsmile1"

    scene bg int_dining_hall_sunset
    show gl happy  far
    show mt normal pioneer far at left
    show yo normal shirt far at right
    ai "happy"

    scene bg ext_no_bus_sunset
    show gl laugh1  far
    show uv normal far at left
    show mi normal pioneer far at right
    ai "laugh1"

    scene bg ext_polyana_sunset
    show gl smile1  far
    show dv normal pioneer far at left
    show cs normal far at right
    ai "smile1"

    scene bg ext_beach_sunset
    show gl normal  far
    show us normal pioneer far at left
    show el normal pioneer far at right
    ai "normal"

    scene bg ext_no_bus_sunset
    show gl serious  far
    show us normal pioneer far at left
    show mt normal pioneer far at right
    ai "serious"

    scene bg ext_path_sunset
    show gl dontlike1  far
    show yo normal shirt far at left
    show sl normal pioneer far at right
    ai "dontlike1"

    scene bg ext_dining_hall_away_sunset
    show gl angry1 ears far
    show mi normal pioneer far at left
    show sh normal pioneer far at right
    ai "angry1"

    scene bg ext_dining_hall_away_sunset
    show gl rage  far
    show sl normal pioneer far at left
    show yo normal shirt far at right
    ai "rage"

    scene bg int_clubs_male_sunset
    show gl anger  far
    show cs normal far at left
    show uv normal far at right
    ai "anger"

    scene bg ext_road_sunset
    show gl frust1  far
    show cs normal far at left
    show mz normal pioneer far at right
    ai "frust1"

    scene bg ext_square_sunset
    show gl dontlike2  far
    show sh normal pioneer far at left
    show cs normal far at right
    ai "dontlike2"

    scene bg ext_dining_hall_away_sunset
    show gl evilsmile2  far
    show un normal pioneer far at left
    show jd normal pioneer far at right
    ai "evilsmile2"

    scene bg ext_no_bus_sunset
    show gl grin2  far
    show yo normal shirt far at left
    show pi far at right
    ai "grin2"

    scene bg ext_dining_hall_near_sunset
    show gl smile2  far
    show pi far at left
    show mi normal pioneer far at right
    ai "smile2"

    scene bg ext_no_bus_sunset
    show gl shy2  far
    show un normal pioneer far at left
    show mz normal pioneer far at right
    ai "shy2"

    scene bg ext_road_sunset
    show gl laugh2 ears far
    show uv normal far at left
    show sl normal pioneer far at right
    ai "laugh2"

    scene bg ext_no_bus_sunset
    show gl frust2  far
    show yo normal shirt far at left
    show mi normal pioneer far at right
    ai "frust2"

    scene bg ext_path_sunset
    show gl angry2  far
    show sh normal pioneer far at left
    show yo normal shirt far at right
    ai "angry2"

    scene bg ext_beach_sunset
    show gl dontlike2  far
    show uv normal far at left
    show sl normal pioneer far at right
    ai ""

    $ persistent.sprite_time = "night"

    scene bg ext_old_building_night
    show gl grin1  close
    show uv normal close at fleft
    show mt normal pioneer close at fright
    ai "grin1"

    scene bg ext_camp_entrance_night
    show gl surprise  close
    show dv normal pioneer close at fleft
    show uv normal close at fright
    ai "surprise"

    scene bg ext_camp_entrance_night
    show gl scary  close
    show dv normal pioneer close at fleft
    show el normal pioneer close at fright
    ai "scary"

    scene bg ext_house_of_mt_night
    show gl sad  close
    show uv normal close at fleft
    show cs normal close at fright
    ai "sad"

    scene bg ext_playground_night
    show gl shy1  close
    show uv normal close at fleft
    show pi close at fright
    ai "shy1"

    scene bg int_house_of_dv_night
    show gl guilty  close
    show cs normal close at fleft
    show cs normal close at fright
    ai "guilty"

    scene bg int_bus_black
    show gl evilsmile1 ears close
    show cs normal close at fleft
    show yo normal shirt close at fright
    ai "evilsmile1"

    scene bg int_house_of_mt_noitem_night
    show gl happy  close
    show un normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "happy"

    scene bg int_clubs_male2_night_nolight
    show gl laugh1  close
    show pi close at fleft
    show un normal pioneer close at fright
    ai "laugh1"

    scene bg int_clubs_male2_night_nolight
    show gl smile1  close
    show uv normal close at fleft
    show sl normal pioneer close at fright
    ai "smile1"

    scene bg ext_bathhouse_night
    show gl normal  close
    show uv normal close at fleft
    show un normal pioneer close at fright
    ai "normal"

    scene bg int_dining_hall_night
    show gl serious  close
    show mi normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "serious"

    scene bg ext_playground_night
    show gl dontlike1  close
    show mz normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "dontlike1"

    scene bg ext_old_building_night
    show gl angry1  close
    show mi normal pioneer close at fleft
    show sh normal pioneer close at fright
    ai "angry1"

    scene bg ext_no_bus_night
    show gl rage  close
    show sh normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "rage"

    scene bg int_liaz
    show gl anger ears close
    show mi normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "anger"

    scene bg int_liaz
    show gl frust1  close
    show yo normal shirt close at fleft
    show cs normal close at fright
    ai "frust1"

    scene bg ext_island_night
    show gl dontlike2  close
    show jd normal pioneer close at fleft
    show un normal pioneer close at fright
    ai "dontlike2"

    scene bg ext_road_night
    show gl evilsmile2  close
    show pi close at fleft
    show yo normal shirt close at fright
    ai "evilsmile2"

    scene bg ext_road_night2
    show gl grin2 ears close
    show sh normal pioneer close at fleft
    show cs normal close at fright
    ai "grin2"

    scene bg ext_bathhouse_night
    show gl smile2  close
    show mz normal pioneer close at fleft
    show mi normal pioneer close at fright
    ai "smile2"

    scene bg ext_house_of_mt_night_without_light
    show gl shy2  close
    show jd normal pioneer close at fleft
    show mz normal pioneer close at fright
    ai "shy2"

    scene bg int_dining_hall_night
    show gl laugh2  close
    show mz normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "laugh2"

    scene bg int_library_night
    show gl frust2  close
    show un normal pioneer close at fleft
    show yo normal shirt close at fright
    ai "frust2"

    scene bg ext_camp_entrance_night
    show gl angry2  close
    show sh normal pioneer close at fleft
    show us normal pioneer close at fright
    ai "angry2"

    scene bg int_clubs_male2_night_nolight
    show gl normal  close
    show sl normal pioneer close at fleft
    show dv normal pioneer close at fright
    ai ""










    
