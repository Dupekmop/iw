label iw_start:
    menu:
        "Давай с самого начала":
            jump iw_prescriptum
        "День первый: прибытие":
            jump iw_dayOne_arrive

label iw_prescriptum:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание: Прескриптум")
        
    ### дляТЕСТОВ
    

    
    ### /дляТЕСТОВ

    show text "{i}{color=#f1d076}Бойтесь своих желаний — они имеют свойство сбываться{/color}{/i}" at truecenter with dissolve2
    $ renpy.pause(3)
    hide text with dissolve2
    
    play ambience ambience_cold_wind_loop fadein 3
    play music music_prologue fadein 3
    scene bg black with dissolve2
    $ set_mode_nvl()
    "Иногда случается, что вещи теряют свой смысл.{w} Вот смысл окна, например, чтобы в него смотреть, но порой смотришь в него, а смотреть там нечего.{w} Ничего интересного.{w} Или вот какой смысл умываться по утрам? Чтобы быть бодрым?{w} А какой смысл быть по утрам бодрым?{w} Какой вообще смысл быть по утрам… Непонятно."
    "И непонятно, то ли жизнь всегда была бессмысленной, а ты просто не замечал этого, то ли смысл был, но куда-то затерялся."
    window hide
    
    scene anim prolog_1 with dissolve5
    $ set_mode_adv()
            
    window show
    pvo "Не лежи на снегу, простудишься."
    
    me "Ну и что? А смысл не простужаться?"

    pvo "Чтобы не болеть."

    me "А смысл не болеть?"

    pvo "Чтобы быть здоровым! Семён, ты что, опять забыл принять таблетки?"

    "Я медленно осмотрелся. Сверху, из сумрака, с одной из веток раскинувшегося рядом клёна на меня таращились два ярко-жёлтых кошачьих глаза с тёмными узкими зрачками."

    sv "Говорящая кошка, только и всего"

    "Вспомнился анекдот."
    "{i}Учитель: «Дети, запишите предложение: “Рыба сидела на дереве”».\n{w}Ученик: «А разве рыбы сидят на деревьях?»\n{w}Учитель: «Ну… Это была сумасшедшая рыба».{/i}"

    sv "А это — сумасшедшая кошка"

    sv "Или сумасшедший я, если слышу, как она со мной разговаривает?"
    "Ведь кошки совершенно точно не могут разговаривать, у них даже нет произносительных органов артикуляции…"
    "Хотя откуда мне достоверно знать про кошачьи органы, разве я фелинолог? Куда там, я даже не зоолог.{w} Так, никчёмный хиккан-анимешник…"

    me "А смысл быть здоровым?"
    "Обратился я с новым вопросом, пристально глядя на две жёлтые точки."

    "Точки сощурились, как если бы их обладатель улыбнулся."

    pvo "Чудак, тебе что, не нравится быть здоровым?"

    me "При чём здесь нравится или не нравится… Я не хочу быть бессмысленно здоровым."

    "Точки снова округлились."

    pvo "Тебе нужен смысл?"

    me "Да."

    pvo "Во всём, во всём?"

    me "Неплохо бы."

    pvo "Тогда тебе нужна Эвристическая Машина."
    "Веско ответствовала кошка."

    me "Какая-какая машина?.."

    pvo "Эвристическая.{w} Дающая смысл."

    "Я покатал во рту это новое для меня слово. И неожиданно решил:"

    me "Да, она мне нужна…{w} Но где её искать?"

    pvo "О! Это очень далеко!"

    me "За смыслом хоть на край света.{w} Веди меня!"

    "Кошка выпрыгнула из темноты."
    "Её неестественно большая морда застыла совсем рядом"
    play sound sfx_catlaugh
    "Её неестественно большая морда застыла совсем рядом и громко расхохоталась мне в лицо."
    stop ambience fadeout 3
    stop music fadeout 3
    $ renpy.pause(3)
    window hide
        
label iw_dayOne_arrive:
    $ persistent.sprite_time = "day"
    scene bg black with dissolve2
    
    ### дляТЕСТОВ
    

    
    ### /дляТЕСТОВ
    
    show text "{i}{color=#f1d076}Существует теория, что Вселенная бесконечна,\n а потому в ней должны быть копии нашей планеты.\n Вы только представьте: летел космический корабль\n миллионы световых лет в поисках другой цивилизации…\n и уткнулся в Мытищи.{/color}{/i}" at truecenter with dissolve2
    $ renpy.pause(10)
    hide text with dissolve2
    $ day_time()
    $ backdrop = "days"
    $ new_chapter(1, u"Сокровенное желание: Прибытие")
    play music music_list["no_tresspassing"]
    scene bg ext_bus with flash
    $ set_mode_adv()
    window show
    "Я вышел из автобуса и осмотрелся."
    
    "Небо здесь было низкое и какое-то твёрдое, без этой легкомысленной прозрачности, намекающей на бездонность космоса — настоящая библейская твердь, гладкая и непроницаемая."
    "И твердь эта несомненно опиралась на могучие плечи местного Атланта."

    "Воздух был горячий и густой, пахло пылью, старым железом, раздавленной зеленью, жизнью."
    "Трава была по пояс, неподалёку темнели заросли кустарника, торчали кое-как унылые кривоватые деревья."

    "Автобус стоял на дне огромной котловины с пологими склонами; местность вокруг заметно поднималась к размытому неясному горизонту, и это было странно, потому что где-то рядом текла река, большая и спокойная, текла на запад, вверх по склону котловины."

    sv "Мало того, что из зимы попал в лето, так и местность ещё странная"

    window hide    
    scene bg ext_camp_entrance_day with dissolve2
    window show
    sv "И что это за пионерлагерь “Совёнок”?{w} Откуда здесь пережиток далёких социалистических времён?{w} И ведь не скажешь, что заброшен"

    window hide
    play ambience ambience_camp_entrance_day
    play sound sfx_suddenly
    show jd normal pioneer at center with hpunch
    stop music
    window show
    dvp "Привет!{w} Ты, наверное, новенький?"
    
    "Я недолго постоял в раздумьях и решился-таки осторожно перейти к контакту четвёртой степени:"

    me "Ну… наверное."

    sv "Мало ли, куда меня занесло. Может, уже и планета совсем другая, и я тут общаюсь с некоей кремнийорганической формой жизни"

    "Впрочем, внешне девушка ничем не отличалась от обыкновенных людей."

    show jd smile with dissolve
    dvp "О! Это замечательно! Добро пожаловать в пионерлагерь «Совёнок»."
    dvp "От лица всего нашего дружного коллектива ребят, вожатых и обслуживающего персонала приветствую тебя!"
    
    show jd grin with dissolve
    dvp "Надеюсь, тебе у нас понравится! Моё имя Славяна!{w} Но все меня Славя зовут. И ты тоже зови."

    me "Хорошо. Буду звать."

    show jd normal with dissolve
    sv "Надеюсь, вскоре я проснусь, и никого звать уже не понадобится. Как там в Винни-Пухе: как позвать Слонопотама? Идёт ли он на свист и если идёт, то зачем?"

    me "Э-э-э… да… А меня Семён зовут. И ты тоже зови… Если понадоблюсь."
    
    show jd smile with dissolve

    "Я почесал затылок."

    sv "Абсурдная ситуация, абсурдные мысли. Какой-то лагерь, пионеры, Славяны…"

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

    show ja smile pioneer at cright with ease
    
    "Потом немного отстранилась и продолжила уже громче:"
    sls "Сейчас я провожу тебя к вожатой.{w} Как доехал?"

    sv "Что здесь творится?"

    show jd normal:
        ease 0.5 xpos 0.4    
    "Славя Номер Один схватила меня за другую руку и потянула к себе."
    slf "Нет, я провожу!"

    show ja serious:
        ease 0.5 xpos 0.6
    sls "..."
    
    window hide
    show jd normal:
        ease 0.7 xpos 0.2
    show ja serious with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show ja serious:
        ease 0.7 xpos 0.8
    show jd normal with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show jd angry:
        ease 0.7 xpos 0.2
    show ja serious with hpunch:
        ease 0.7 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show ja angry:
        ease 0.6 xpos 0.8
    show jd angry with hpunch:
        ease 0.6 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show jd angry:
        ease 0.6 xpos 0.2
    show ja angry with hpunch:
        ease 0.6 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show ja angry:
        ease 0.5 xpos 0.8
    show jd rage with hpunch:
        ease 0.5 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show jd rage:
        ease 0.5 xpos 0.2
    show ja rage with hpunch:
        ease 0.5 xpos 0.5
    $ renpy.pause(0.5, hard=True)
    
    show ja rage:
        ease 0.4 xpos 0.8
    show jd rage with hpunch:
        ease 0.4 xpos 0.5
    $ renpy.pause(0.5, hard=True)

    show jd angry at left with ease
    show ja angry at right with ease

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
    slf "Ещё быть колючей, гордой и неприступной, но с большим, любящим сердцем. Не забудь."

    show ja serious with dissolve
    sls "Вот ещё.{w} С каких это пор…{w=1}{nw}"

    slf "А вот с таких. Теперь только так и никак иначе. Твоё место занято.{w} Смирись."

    show ja rage with dissolve
    sls "Знаешь, что?"
    slf "Что?"
    sls "Это уже переходит всякие границы.{w} Совсем распоясалась.{w} Придётся взяться и за твоё воспитание!"

    show jd grin with dissolve
    slf "Ну, попробуй…"

    scene bg ext_road_day with wipeleft
    "Я под шумок стал озираться в поисках путей отступления, чтобы просто по-тихому незаметно удалиться."

    stop music fadeout 2
    unv "Ой, девочки, м-может, не надо?"
    "Раздался сзади чей-то жалобный голос."

    window hide
    scene bg ext_camp_entrance_day with wiperight
    show un sad sport far at center with dissolve
    $ renpy.pause(1, hard=True)
    window show

    sv "Кажется, я окружён и бежать некуда"

    show ja serious pioneer at fleft with hpunch
    sls "Лена!"
    
    show jd normal pioneer at fright with vpunch
    slf "Вот только тебя здесь не хватало.{w} Чего пришла? Скройся с глаз, а то я за себя не ручаюсь!"

    show un sad sport at center with dissolve
    un "Алиса… Но ведь так нельзя…"

    show jd angry with dissolve
    slf "Было нельзя, а теперь можно! Беру власть в свои руки!"

    usp "Вся власть советам!"
    show us laugh sport far at cright behind un with hpunch
    show un surprise with dissolve
    usp "То есть мне!"

    "Сцена обогатилась ещё одним персонажем: маленькой рыжей девочкой лет двенадцати."
    "Она быстро подбежала к Славянам и встала между ними живым барьером."
    
    show un angry2 at cleft zorder 0
    show us normal sport at center zorder 1
    with ease
    
    sls "Ульяна, ты очень вовремя!{w} Держи свою подругу на поводке и намордник на неё надень, а то покусает ещё." 
    show ja angry with dissolve
    sls "Бешеная."

    show jd rage with dissolve
    slf "Щас я кого-то укушу — мало не покажется!"
    window hide
    show us surp1 with dissolve
    stop ambience
    play sound sfx_angry_ulyana
    $ renpy.pause(2, hard=True)
    show us surp2 with dissolve
    $ renpy.pause(2, hard=True)
        
    scene anim prolog_1
    play music music_list["that_s_our_madhouse"]
    
    play sound sfx_face_slap 
    with hpunch
    $ renpy.pause(0.1, hard=True)
    play sound sfx_lena_hits_alisa 
    with vpunch
    $ renpy.pause(0.1, hard=True)
    play sound sfx_pat_shoulder_hard 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_drop_alisa_bag 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_punch_medium 
    with hpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_broken_dish 
    with vpunch
    $ renpy.pause(0.75, hard=True)
    play sound sfx_armature_swish 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_piano_head_bump 
    with vpunch
    $ renpy.pause(1.5, hard=True)
    play sound sfx_body_bump 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_break_flashlight_alisa
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_washstand 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_break_cupboard 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_soccer_ball_kick
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_bodyfall_1 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_medium 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_bush_body_fall 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_table_hit 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_boat_impact 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_break_monitor 
    with hpunch
    $ renpy.pause(1.5, hard=True)
    play sound sfx_energy_door_bus 
    with vpunch
    $ renpy.pause(2, hard=True)
    play sound sfx_drop_pipe 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_punch_washstand 
    with hpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_fall_grass 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_fall_wood_floor 
    with vpunch
    $ renpy.pause(0.5, hard=True)
    play sound sfx_alisa_falls 
    with hpunch
    $ renpy.pause(1, hard=True)
    play sound sfx_chair_fall 
    with vpunch
    $ renpy.pause(1, hard=True)
    stop music fadeout 2
    stop sound
    play ambience ambience_ext_road_day

    scene bg ext_camp_entrance_day with dissolve
    show jd cry pioneer at fleft
    show ja dontlike pioneer at fright
    show us angry sport at left
    show un angry sport at right
    with dissolve
    
    window show
    "Довольно быстро всё кончилось."
    "Славя Номер Один лежала на земле, и её держала каким-то хитрым захватом маленькая Ульяна, а Славю Номер Два держала Лена, выглядевшая теперь отнюдь не безобидно."

    us "Ну, и что тут происходит? Что я пропустила интересного?"

    show un angry2 at cright with ease
    show ja sad with dissolve
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
    show mt normal panama pioneer at center with dspr
    show us surp2 sport at left
    show un surprise sport at right
    with ease
    
    show jd surprise 
    show ja surprise pioneer
    with dissolve
    
    window show
    chor "Ольга Дмитриевна?"

    mt "Да-да, она самая. Не ждали?"
    mt "Ну и что вы тут устроили? Совсем кукухой поехали."
    
    show mt sad close with dissolve
    mt "Лена, давай его на новый виток. А этих бракованных в расход, и сама не забудь ликвидироваться."
    
    window hide
    show us fear
    show un scared
    show jd scared
    show ja scared
    show mt smile
    with dissolve    
    window show

    mt "Отдохну наконец от вас хотя бы недельку.{w} В конце концов, должен же и у меня быть отпуск…"

    window hide
    stop ambience
    play music killem
    hide mt with dissolve
    $ renpy.pause(1, hard=True)
    hide jd
    hide ja
    hide un
    hide us
    with dissolve
    
    $ renpy.pause(2, hard=True)
    
    play sound sfx_intro_bus_stop_sigh
    scene bg ext_camp_entrance_evening with dissolve2
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    show un sad sport far at center with dissolve
    window show
    un "Прости, Семён…"

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
    show un cry sport at center with dissolve2
    
    window show
    "Лена тем временем подходила всё ближе и становилась всё печальнее."
    "Но несмотря ни на что, её решимость огорчить меня до невозможности ничуть не поколебалась."

    me "Сходил за хлебушком, называется…"

    window hide
    scene bg ext_camp_entrance_night with dissolve2
    $ persistent.sprite_time = "night"
    $ night_time()
    show un cry_smile sport close at center with dissolve2
    window show

    play sound_loop sfx_head_heartbeat
    un "Не бойся."
    "Успокоила меня Лена и занесла нож для удара."
    
    un "Я как раз недавно смотрела в библиотеке анатомический атлас, и теперь знаю, куда бить, чтобы всё прошло быстро."
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_scary_sting
    show un evil_smile
    $ renpy.pause(0.5, hard=True)
    play sound sfx_ghost_children_laugh
    $ renpy.pause(1, hard=True)
    
    scene bg black with dissolve2
    stop sound_loop
    play ambience ambience_camp_entrance_night
    stop music fadeout 3
    pause
    jump iw_start