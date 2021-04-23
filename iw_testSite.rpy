label iw_test:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание:\nТестовый полигон")
    $ persistent.sprite_time = "day"

    scene bg ext_camp_entrance_day
    "..."
    
# ТЕСТИРОВАНИЕ КОДА    
    
    show dv normal pioneer
    show un normal pioneer at fright
    show ai normal lng_pink at fleft
    pause
    show ai smile1 srt_pink at fleft
    pause
    show ai smile2 tai_pink at fleft
    pause
    show ai laugh1 lng_pink at fleft
    pause
    show ai laugh2 srt_pink at fleft
    pause
    show ai happy tai_pink at fleft
    pause

    $ persistent.sprite_time = "sunset"

    scene bg ext_camp_entrance_sunset
    show sl normal pioneer at fleft
    show mi normal pioneer at fright
    show ai shy1 lng_pink
    pause
    show ai shy2 srt_pink
    pause
    show ai sad tai_pink
    pause
    show ai guilty lng_pink
    pause
    show ai surprise srt_pink
    pause
    show ai scary tai_pink
    pause

    $ persistent.sprite_time = "night"

    scene bg ext_camp_entrance_night
    show us normal pioneer at fleft
    show uv normal
    show ai cry lng_pink at fright
    pause
    show ai serious srt_pink at fright
    pause
    show ai dontlike tai_pink at fright
    pause
    show ai angry1 lng_pink at fright
    pause
    show ai angry2 srt_pink at fright
    pause
    show ai rage tai_pink at fright
    pause
    
    $ persistent.sprite_time = "day"
    
    scene bg ext_camp_entrance_day
    show dv normal pioneer
    show un normal pioneer at fright
    show ai anger lng_pink at fleft
    pause
    show ai frust1 srt_pink at fleft
    pause
    show ai frust2 tai_pink at fleft
    pause
