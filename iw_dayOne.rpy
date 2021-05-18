label iw_dayOne_arriveSemyon:
    $ ty = "1"
    play ambience ambience_camp_entrance_day
    $ renpy.pause(2)
    show text "{size=+10}{font=mods/iw/menu/headingpro.ttf}{color=#fff8e7}Существует теория, что Вселенная бесконечна,\nа потому в ней должны быть копии нашей планеты.\nВы только представьте: летел космический корабль\nмиллионы световых лет в поисках другой цивилизации…\nи уткнулся в Мытищи.{/color}{/font}{/size}" at truecenter with dissolve2
    $ renpy.pause(10)
    hide text with dissolve2
    $ backdrop = "days"
    $ new_chapter(1, u"Сокровенное желание:\nПрибытие")
    $ persistent.sprite_time = "day"
    $ day_time()
    
    ### дляТЕСТОВ
    

    
    ### /дляТЕСТОВ
    
    play music music_list["no_tresspassing"]
    scene bg ext_road_day with flash
    stop ambience fadeout 3
    $ set_mode_adv()
    
    $ iw_screens()
    $ ty = "1"
    window show
    "Я вышел из автобуса и осмотрелся."
    "Небо здесь было низкое и какое-то твёрдое, без этой легкомысленной прозрачности, намекающей на бездонность космоса — настоящая библейская твердь, гладкая и непроницаемая."
    "И твердь эта несомненно опиралась на могучие плечи местного Атланта."
    "Воздух был горячий и густой, пахло пылью, старым железом, раздавленной зеленью, жизнью."
    "Трава была по пояс, неподалёку темнели заросли кустарника, торчали кое-как унылые кривоватые деревья."

    window hide
    scene bg ext_bus with dissolve
    window show
    "Автобус стоял на дне огромной котловины с пологими склонами; местность вокруг заметно поднималась к размытому неясному горизонту, и это было странно, потому что где-то рядом текла река, большая и спокойная, текла на запад, вверх по склону котловины."
    sv "Мало того, что из зимы попал в лето, так и местность ещё странная"

    window hide    
    scene bg ext_camp_entrance_day with dissolve2
    window show
    $ ty = "2"
    sv "И что это за пионерлагерь “Совёнок”?{w} Откуда здесь пережиток далёких социалистических времён?{w} И ведь не скажешь, что заброшен"

    window hide
    play ambience ambience_camp_entrance_day
    play sound sfx_scratch2
    show jd normal pioneer at center
    with hpunch
    stop music
    
    window show
    dvp "Привет!{w} Ты, наверное, новенький?"    
    "Я недолго постоял в раздумьях и решился-таки осторожно перейти к контакту четвёртой степени:"
    me "Ну… наверное."
    sv "Мало ли, куда меня занесло. Может, уже и планета совсем другая, и я тут общаюсь с некоей кремнийорганической формой жизни"
    sv "Впрочем, как раз-таки {i}форма{/i} у этой жизни весьма человеческая"
    "Взгляд непроизвольно прокатился сверху вниз."
    sv "И очень даже ничего себе форма, надо сказать"
    
    show jd grin with dissolve
    dvp "О! Это замечательно! Добро пожаловать в пионерлагерь «Совёнок»."
    dvp "От лица всего нашего дружного коллектива ребят, вожатых и обслуживающего персонала приветствую тебя!"
    
    show jd smile with dissolve
    dvp "Надеюсь, тебе у нас понравится! Моё имя Славяна!{w} Но все меня Славя зовут. И ты тоже зови."

    me "Хорошо. Буду звать."

    show jd normal with dissolve
    sv "Надеюсь, скоро я проснусь, и никого звать уже не понадобится. Как там в Винни-Пухе: как позвать Слонопотама? Идёт ли он на свист и если идёт, то зачем?"

    me "Э-э-э…{w} да…{w} а меня Семён зовут.{w} И ты тоже зови…{w} если понадоблюсь."
    
    show jd smile with dissolve
    "Я почесал затылок."
    sv "Абсурдная ситуация, абсурдные мысли. Какой-то лагерь, пионерки, Славяны…"

    show ja serious pioneer at right with hpunch
    show jd shocked:
        ease 1 xpos 0.2
        
    slp "Алиса? Что ты тут делаешь?"

    show jd surprise with dissolve
    dvp "Не слушай её! Она перепутала! Я — Славяна!"

    show ja surprise with dissolve
    slp "Что значит ты — Славяна? А я тогда кто?"
    
    show jd normal:
        ease 0.5 xpos 0.3    
    play music music_list["eat_some_trouble"] fadein 2
    stop ambience fadeout 2
    slf "Откуда я знаю? Возможно, ты — Лена."
    
    show jd laugh with dissolve
    slf "И вообще, кто первый, тот и Славяна!"

    show ja serious with dissolve
    sls "Не обращай внимания, Алиса шутит. Она у нас выдумщица и хулиганка."
    "Обратилась Славя Номер Два уже ко мне."
    
    show jd normal with dissolve
    
    show ja shy close:
        ease 1 xpos 0.6
    "Она подхватила меня под руку и прижалась так, что я почувствовал мягкость её груди."
    sls "И лучше держись от неё подальше. От таких, сам понимаешь, ничего хорошего не жди."

    show ja smile close at right with ease
    
    "Потом немного отстранилась и продолжила уже громче:"
    sls "Сейчас я провожу тебя к вожатой.{w} Как доехал?"

    sv "Что здесь творится?"

    show jd pioneer normal close at fleft with ease
    "Славя Номер Один схватила меня за другую руку и потянула к себе."
    slf "Нет, я провожу!"
    show bg:
        anchor (0.5,0.5)
        pos (0.5,0.5)
        zoom 1.2
    with hpunch

    show ja serious with dissolve
    window hide
    pause
   
    play sound sfx_prunk1
    show bg:
        ease 0.5 xpos 0.55
    show jd normal:
        ease 0.5 xpos 0.05
    show ja serious with hpunch:
        ease 0.5 xpos 0.75
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk2
    show bg:
        ease 0.5 xpos 0.45
    show jd normal:
        ease 0.5 xpos 0.25
    show ja serious with hpunch:
        ease 0.5 xpos 0.95
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk3
    show bg:
        ease 0.5 xpos 0.55
    show jd angry:
        ease 0.5 xpos 0.05
    show ja serious with hpunch:
        ease 0.5 xpos 0.75
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk1
    show bg:
        ease 0.4 xpos 0.45
    show jd angry:
        ease 0.4 xpos 0.25
    show ja serious with hpunch:
        ease 0.4 xpos 0.95
    $ renpy.pause(0.4, hard=True)
    
    play sound sfx_prunk2
    show bg:
        ease 0.4 xpos 0.55
    show jd angry:
        ease 0.4 xpos 0.05
    show ja angry with hpunch:
        ease 0.4 xpos 0.75
    $ renpy.pause(0.4, hard=True)
    
    play sound sfx_prunk3
    show bg:
        ease 0.3 xpos 0.45
    show jd angry:
        ease 0.3 xpos 0.25
    show ja angry with hpunch:
        ease 0.3 xpos 0.95
    $ renpy.pause(0.3, hard=True)
    
    play sound sfx_prunk1
    show bg:
        ease 0.3 xpos 0.55
    show jd rage:
        ease 0.3 xpos 0.05
    show ja angry with hpunch:
        ease 0.3 xpos 0.75
    $ renpy.pause(0.3, hard=True)
    
    play sound sfx_prunk2
    show bg:
        ease 0.2 xpos 0.45
    show jd rage:
        ease 0.2 xpos 0.25
    show ja rage with hpunch:
        ease 0.2 xpos 0.95
    $ renpy.pause(0.2, hard=True)
    
    play sound sfx_prunk3
    show bg:
        ease 0.1 xpos 0.55
    show jd rage:
        ease 0.1 xpos 0.05
    show ja rage with hpunch:
        ease 0.1 xpos 0.75
    $ renpy.pause(0.1, hard=True)
    
    play sound sfx_prunk1
    show bg:
        ease 0.1 xpos 0.45
    show jd rage:
        ease 0.1 xpos 0.25
    show ja rage with hpunch:
        ease 0.1 xpos 0.95
    $ renpy.pause(0.1, hard=True)
    
    play sound sfx_prunk2
    show bg:
        ease 0.1 xpos 0.55
    show jd rage:
        ease 0.1 xpos 0.05
    show ja rage with hpunch:
        ease 0.1 xpos 0.75
    $ renpy.pause(0.1, hard=True)
    
    play sound sfx_prunk3
    show bg:
        ease 0.1 xpos 0.45
    show jd rage:
        ease 0.1 xpos 0.25
    show ja rage with hpunch:
        ease 0.1 xpos 0.95
    $ renpy.pause(0.1, hard=True)
    
    play sound sfx_prunk1
    show bg:
        ease 0.1 xpos 0.55
    show jd rage:
        ease 0.1 xpos 0.05
    show ja rage with hpunch:
        ease 0.1 xpos 0.75
    $ renpy.pause(0.1, hard=True)

    play sound sfx_prunk2
    show bg:
        ease 0.1 xpos 0.45
    show jd rage:
        ease 0.1 xpos 0.25
    show ja rage with hpunch:
        ease 0.1 xpos 0.95
    $ renpy.pause(0.1, hard=True)
    
    play sound sfx_prunk3
    show bg:
        ease 0.1 xpos 0.55
    show jd rage:
        ease 0.1 xpos 0.05
    show ja rage with hpunch:
        ease 0.1 xpos 0.75
    $ renpy.pause(0.1, hard=True)

    play sound sfx_prunks
    show bg:
        parallel:
            ease 1.5 zoom 100
        parallel:
            ease 1.5 rotate 2160
    show jd:
        ease 1.5 xpos -0.5
    show ja:
        ease 1.5 xpos 1.5
    $ renpy.pause(1.5, hard=True)

    scene bg ext_camp_entrance_day with flash
    show jd angry pioneer at left
    show ja angry pioneer at right
    with ease
    window show
    "Некоторое время продолжалось молчаливое соревнование по перетягиванию Семёна."
    "Наконец поняв, что грубой силой тут ничего не решить, соперницы оставили меня в покое и перешли к переговорам."
    
    show ja dontlike at cright with ease
    sls "Ты что творишь? Совсем сбрендила или это уже белая горячка?"

    show jd angry at cleft with ease
    slf "Да сколько можно одно и то же снова и снова. Всё, надоело! Хочу быть доброй, ласковой и милой."

    show ja surprise at right with ease
    sls "Чего-о-о?"

    show jd normal with dissolve
    slf "Того!{w} Теперь твоя очередь в одиночестве бренчать на гитаре по вечерам, устраивать пакости Панамке и держать в страхе весь лагерь."
    slf "Ещё быть колючей, гордой и неприступной, но с большим любящим сердцем. Не забудь."

    show ja serious with dissolve
    sls "Вот ещё.{w} С каких это пор…"

    slf "А вот с таких. Теперь только так и никак иначе. Твоё место занято.{w} Смирись."

    show ja rage with dissolve
    sls "Знаешь, что?"
    slf "Что?"
    sls "Это уже переходит всякие границы.{w} Ты совсем распоясалась.{w} Придётся взяться и за твоё воспитание!"

    show jd grin with dissolve
    slf "Ну, попробуй…"

    scene bg ext_road_day with wipeleft
    "Я под шумок стал озираться в поисках путей отступления, чтобы просто по-тихому незаметно удалиться."

    play ambience ambience_camp_entrance_day
    stop music fadeout 2
    unv "Ой, девочки, м-может, не надо?"
    "Раздался сзади чей-то жалобный голос."

    window hide
    scene bg ext_camp_entrance_day with wiperight
    show un sad pioneer far at center with dissolve
    show ja serious pioneer:
        anchor (0.5,0.0)
        xpos -0.5
    show jd normal pioneer:
        anchor (0.5,0.0)
        xpos 1.5
    $ renpy.pause(1, hard=True)
    window show

    sv "Кажется, я окружён и бежать некуда"

    show ja:
        ease 0.3 xpos 0.15
    with hpunch
    sls "Лена!"
    
    show jd:
        ease 0.3 xpos 0.85
    with hpunch
    slf "Вот только тебя здесь не хватало.{w} Чего пришла? Скройся с глаз, а то я за себя не ручаюсь!"

    show un sad pioneer at center with dissolve
    un "Алиса… Но ведь так нельзя…"

    show jd angry with dissolve
    slf "Было нельзя, а теперь можно! Беру власть в свои руки!"

    show un surprise with dspr
    usp "Вся власть советам!"
    show us laugh sport far at cright behind un with hpunch
    usp "То есть мне!"

    "Сцена обогатилась ещё одним персонажем: маленькой рыжей девочкой лет двенадцати."
    
    show un angry2 at cleft zorder 0
    show us normal sport at center zorder 1
    with ease
    
    sls "Ульяна, ты очень вовремя!{w} Держи свою подругу на поводке и намордник на неё надень, а то покусает ещё." 
    show ja angry with dissolve
    sls "Бешеная."

    show jd rage with dissolve
    slf "Щас я кого-то укушу — мало не покажется!"
    window hide
    stop ambience
    play sound sfx_angry_ulyana
    show us surp2 with dissolve
    show jd:
        linear 0.01 xpos 0.854
        linear 0.01 xpos 0.85
        repeat
    $ renpy.pause(4, hard=True)
        
    scene anim prolog_1 at jogging
    stop ambience
    play music music_list["that_s_our_madhouse"]
    
    play sound sfx_face_slap 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_lena_hits_alisa 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_washstand
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_medium
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_piano_head_bump 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_armature_swish 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_drop_pipe 
    with hpunch
    $ renpy.pause(1.0, hard=True)
    play sound sfx_bodyfall_1 
    with vpunch    
    $ renpy.pause(0.3, hard=True)
    play sound sfx_clench2 
    with hpunch    
    $ renpy.pause(0.3, hard=True)
    play sound sfx_bush_body_fall 
    with vpunch
    $ renpy.pause(0.3, hard=True)
    play sound sfx_punch_medium 
    with hpunch
    $ renpy.pause(0.3, hard=True)
    play sound sfx_broken_dish 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_energy_door_bus 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_boat_impact
    with hpunch
    $ renpy.pause(0.3, hard=True)
    play sound sfx_fall_grass 
    with vpunch
    $ renpy.pause(0.3, hard=True)
    play sound sfx_body_bump 
    with hpunch
    $ renpy.pause(0.3, hard=True)
    play sound sfx_break_monitor 
    with hpunch
    $ renpy.pause(0.7, hard=True)
    play sound sfx_alisa_falls 
    with hpunch
    
    $ renpy.pause(1, hard=True)
    stop music fadeout 2
    stop sound
    play ambience ambience_ext_road_day

    scene bg ext_camp_entrance_day with dissolve
    show jd cry pioneer at fleft
    show ja dontlike pioneer at fright
    show us angry sport at left
    show un angry pioneer at right
    with dissolve2
    
    window show
    "Довольно быстро всё кончилось."
    "Славя Номер Один лежала на земле, и её держала каким-то хитрым захватом маленькая Ульяна, а Славю Номер Два держала Лена, выглядевшая теперь отнюдь не безобидно."

    us "Ну, и что тут происходит? Что я пропустила интересного?"

    show un angry2 at cright
    show ja sad
    with dissolve
    sls "Эта ненормальная утверждает, что теперь она Славяна."
    "Славя Номер Два кивнула на поверженную Славю Номер Один."

    show us sad at cleft with ease
    us "Алиска, поясни!"

    show jd sad with dissolve
    sls "Да чего пояснять? Хочу побыть колхозницей.{w} Надоело, знаешь ли, каждый раз одно и то же.{w} Разнообразие, все дела."

    show us smile with dissolve
    us "А что, идея мне нравится. Должно быть весело. Может, правда попробуем?"

    mtp "И правда, почему бы не попробовать?"

    window hide
    show mt normal panama pioneer far at center with vpunch
    show us surp2 sport at left
    show un surprise pioneer at right
    with ease
    show jd surprise 
    show ja surprise pioneer
    with dissolve
    window show
    chor "Ольга Дмитриевна?"
    hide mt
    show mt laugh panama pioneer at center with dissolve
    "Ольга Дмитриевна придвинулась ближе к пионеркам, на её лице сияла лучезарная, но жутковатая улыбка."
    mt "Не ждали?"
    $ renpy.pause(1, hard=True)
    show mt grin with dissolve
    mt "Что за кутерьма?{w} Кто у нас опять по эциху заскучал?"
    window hide
    $ renpy.pause(1, hard=True)
    show mt rage
    show us fear far at left
    show un scared far at right
    show jd scared far at fleft
    show ja scared far at fright
    with vpunch    
    play music music_list["doomed_to_be_defeated"]
    window show
    mt "Чего притихли?{w} Вам совсем кукушки поотшибало на жаре?!"
    "Грозно проревела вожатая, впечатывая взглядом в плавящийся вязкий воздух каждую по отдельности и всех вместе."
    "Пионерки молчали."
    window hide
    $ renpy.pause(1, hard=True)
    show mt angry close with dissolve2
    stop music fadeout 5
    window show
    mt "Так, ладно…"
    "Удовлетворившись произведённым эффектом, Ольга Дмитриевна так же резко сменила гнев на милость и приблизилась ко мне."
    mt "Что это у нас тут?"
    "Она оглядела меня с брезгливым недоумением и хмыкнула."
    show mt surprise with dissolve
    mt "Какой жалкий экземпляр…"
    window hide
    show us sad
    show un sad
    show jd sad
    show ja sad
    with dissolve
    window show
    mt "Лена, ты ещё здесь?"
    show un shy with dissolve
    show mt smile with dissolve
    mt "В расход его."
    mt "А остальным оправиться и прибыть ко мне для профилактической беседы."
    show un angry2 with dissolve
    window hide
    stop ambience
    hide mt with dissolve
    
label iw_dayOne_arriveJoshka:    
    play sound sfx_intro_bus_stop_sigh
    scene bg ext_camp_entrance_sunset with dissolve2
    $ renpy.pause(2, hard=True)
    
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    show un sad pioneer far at center with dissolve
    window show
    un "Прости, Семён…"

    play music iw_killem fadein 2
    "Девушка Лена зашагала ко мне, не сводя с меня грустного взгляда."
    "В её руке блеснул угрожающего вида кухонный нож."
    "Наверняка очень острый."
    "Впрочем, проверять его остроту на себе мне не хотелось, и я стал медленно пятиться, не выпуская из виду всю чудную компанию, собравшуюся на стоянке перед воротами пионерского лагеря «Совёнок»."

    play sound sfx_clench2
    with vpunch
    "Спина встретилась с твёрдой холодной преградой."
    "Я несколько раз толкнулся в неё не оборачиваясь, но безрезультатно."
    
    window hide
    hide un with dissolve2
    show un cry pioneer at center with dissolve
    
    window show
    "Лена тем временем подходила всё ближе и становилась всё печальнее."
    me "Лена… Леночка, ты это… ножик положь, пока не поранилась."
    $ renpy.pause(1, hard=True)
    show un cry_smile with dissolve
    $ renpy.pause(1, hard=True)
    "Но её решимость огорчить меня до невозможности ничуть не поколебалась."
    me "Сходил за хлебушком, называется…"

    window hide
    scene bg ext_camp_entrance_sunset_sur with dissolve2
    show un cry_smile pioneer close at center with dissolve2
    window show

    play sound_loop sfx_head_heartbeat
    sv "Я же просто хотел потрогать…"
    sv "Кстати, а где эта, как её там…"
    sv "По-моему, самое время ей появиться и спасти меня"
    sv "Ведь так обычно бывает во второсортном кино, когда главному герою грозит смерть"
    sv "Или это не тот фильм? Или не фильм? Или я не главный герой?"
    sv "Мать моя в коньках на босу ногу, какой же бред…"
    
    window hide
    $ renpy.pause(1, hard=True)
    window show
    
    un "Не бойся."
    "Успокоила меня Лена и занесла нож для удара."
    
    un "Я как раз недавно смотрела в библиотеке анатомический атлас, и теперь знаю, куда бить, чтобы всё прошло быстро."
    window hide
    $ renpy.pause(1, hard=True)
    stop music fadeout 3
    play sound sfx_scary_sting
    show un evil_smile
    $ renpy.pause(1, hard=True)
    play ambience ambience_camp_entrance_night fadein 3
    play sound sfx_ghost_children_laugh
    $ renpy.pause(1, hard=True)
    scene bg black with dissolve2
    stop sound_loop
    pause
    stop ambience
    
    jump iw_start