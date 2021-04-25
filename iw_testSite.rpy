label iw_test:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание:\nТестовый полигон")
    $ persistent.sprite_time = "day"

    scene bg int_bus
    "..."
    
# ТЕСТИРОВАНИЕ КОДА    
    
    scene bg ext_camp_entrance_day
    show ai normal lng_dress
    pause
    
    scene bg ext_stage_normal_day
    show ai angry1 tai_dress
    pause
    
    scene bg ext_aidpost_day
    show ai smile2 srt_dress
    pause
    
    scene bg ext_beach_day
    show ai rage lng_kimono
    pause
    
    scene bg ext_boathouse_day
    show ai happy tai_kimono
    pause
    
    scene bg ext_no_bus
    show ai normal srt_kimono
    pause
    
    scene bg ext_camp_entrance_day
    show ai angry1 lng_uniformb
    pause
    
    scene bg ext_dining_hall_away_day
    show ai smile2 tai_uniformb
    pause
    
    scene bg ext_house_of_mt_day
    show ai rage srt_uniformb
    pause
    
    scene bg ext_houses_day
    show ai happy lng_uniformw
    pause
    
    scene bg ext_island_day
    show ai normal tai_uniformw
    pause
    
    scene bg ext_musclub_day
    show ai angry1 srt_uniformw
    pause
    
    scene bg ext_path_day
    show ai smile2 lng_shirt
    pause
    
    scene bg ext_playground_day
    show ai rage tai_shirt
    pause
    
    scene bg ext_square_day
    show ai happy srt_shirt
    pause
    
    scene bg ext_washstand_day
    show ai normal lng_jeans
    pause
    

    $ persistent.sprite_time = "sunset"

    scene bg ext_camp_entrance_sunset
    show ai angry1 tai_jeans
    pause
    
    scene bg ext_beach_sunset
    show ai smile2 srt_jeans
    pause
    
    scene bg int_clubs_male_sunset
    show ai rage lng_xmas
    pause
    
    scene bg ext_beach_sunset
    show ai happy tai_xmas
    pause
    
    scene bg ext_dining_hall_away_sunset
    show ai normal srt_xmas
    pause
    
    scene bg int_dining_hall_sunset
    show ai angry1 lng_infant1
    pause
    
    scene bg ext_no_bus_sunset
    show ai smile2 tai_infant1
    pause
    
    scene bg ext_path_sunset
    show ai rage srt_infant1
    pause
    
    scene bg int_house_of_mt_sunset
    show ai happy lng_infant2
    pause
    
    scene bg ext_houses_sunset
    show ai normal tai_infant2
    pause
    
    scene bg ext_square_sunset
    show ai angry1 srt_infant2
    pause

    $ persistent.sprite_time = "night"

    scene bg ext_camp_entrance_night
    show ai smile2 lng_pink
    pause
    
    scene bg ext_aidpost_night
    show ai rage tai_pink
    pause
    
    scene bg ext_bathhouse_night
    show ai happy srt_pink
    pause
    
    scene bg int_aidpost_night
    show ai normal lng_pink
    pause
    
    scene bg ext_beach_night
    show ai angry1 tai_pink
    pause
    
    scene bg ext_boathouse_night
    show ai smile2 srt_pink
    pause
    
    scene bg int_clubs_male2_night_nolight
    show ai rage lng_pink
    pause
    
    scene bg ext_camp_entrance_night
    show ai happy tai_pink
    pause
    
    scene bg ext_clubs_night
    show ai normal srt_pink
    pause
    
    scene bg int_dining_hall_night
    show ai angry1 lng_pink
    pause
    
    scene bg ext_dining_hall_near_night
    show ai smile2 tai_pink
    pause
    
    scene bg ext_house_of_dv_night
    show ai rage srt_pink
    pause
    
    scene bg int_house_of_dv_night
    show ai happy lng_pink
    pause
    
    scene bg ext_path_night
    show ai normal tai_pink
    pause
    
    scene bg ext_playground_night
    show ai angry1 srt_pink
    pause
    
    scene bg int_library_night
    show ai smile2 lng_pink
    pause
    
    scene bg ext_square_night
    show ai rage tai_pink
    pause
    
    scene bg ext_stage_big_night
    show ai happy srt_pink
    pause
    
    scene bg int_old_building_night
    show ai normal lng_pink
    "ФСЁ!"
    
