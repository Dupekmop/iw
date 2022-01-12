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
    
    show ri bored dress at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_aidpost_day
    show ri smile2 dress at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_boathouse_day
    show ri sad everyday at center
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_no_bus
    show ri smile everyday at center
    show mi normal pioneer at right
    show el normal pioneer at left
    pause
    
    scene bg ext_clubs_day
    show ri smile sport at center
    show sh normal pioneer at right
    show yo happy2 hati_gadget jerkin at left
    pause

    scene bg ext_dining_hall_near_day
    show ri dontlike sport at center
    show uv normal at right
    show ai happy tai_infant2 at left
    pause

    scene bg ext_houses_day
    show ri pensive swim at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_musclub_day
    show ri surprise swim at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_square_day
    show ri angry top
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_washstand_day
    show ri nope top
    show mi normal pioneer at right
    show el normal pioneer at left
    pause

    scene bg ext_beach_sunset
    $ persistent.sprite_time = "sunset"
    show ri bored dress at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_dining_hall_away_sunset
    show ri smile2 dress at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_house_of_mt_sunset
    show ri sad everyday at center
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_path_sunset
    show ri smile everyday at center
    show mi normal pioneer at right
    show el normal pioneer at left
    pause
    
    scene bg ext_road_sunset
    show ri smile sport at center
    show sh normal pioneer at right
    show yo happy2 hati_gadget jerkin at left
    pause

    scene bg ext_dining_hall_near_sunset
    show ri dontlike sport at center
    show uv normal at right
    show ai happy tai_infant2 at left
    pause

    scene bg ext_houses_sunset
    show ri pensive swim at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_no_bus_sunset
    show ri surprise swim at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_square_sunset
    show ri angry top
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_polyana_sunset
    show ri nope top
    show mi normal pioneer at right
    show el normal pioneer at left
    pause

    scene bg ext_aidpost_night
    $ persistent.sprite_time = "night"
    show ri bored dress at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_beach_night
    show ri smile2 dress at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_camp_entrance_night
    show ri sad everyday at center
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_clubs_night
    show ri smile everyday at center
    show mi normal pioneer at right
    show el normal pioneer at left
    pause
    
    scene bg ext_library_night
    show ri smile sport at center
    show sh normal pioneer at right
    show yo happy2 hati_gadget jerkin at left
    pause

    scene bg ext_playground_night
    show ri dontlike sport at center
    show uv normal at right
    show ai happy tai_infant2 at left
    pause

    scene bg ext_square_night
    show ri pensive swim at center
    show sl normal pioneer at right
    show dv normal pioneer at left
    pause
    
    scene bg ext_stage_big_night
    show ri surprise swim at center
    show un normal pioneer at right
    show us normal pioneer at left
    pause

    scene bg ext_house_of_dv_night
    show ri angry top
    show mt normal pioneer at right
    show cs normal at left
    pause
    
    scene bg ext_path_night
    show ri nope top
    show mi normal pioneer at right
    show el normal pioneer at left
    pause


    
