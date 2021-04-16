label iw_start:
    menu:
        "Давай с самого начала":
            jump iw_prescriptum
        "День первый: прибытие Семёна":
            jump iw_dayOne_arriveSemyon
        "День первый: прибытие Йошки":
            jump iw_dayOne_arriveJoshka


label iw_prescriptum:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание: Прескриптум")
    $ persistent.sprite_time = "day"
    show text "{size=+20}{font=mods/iw/menu/slimamif.ttf}{color=#fff8e7}Бойтесь своих желаний — они имеют свойство сбываться{/color}{/font}{/size}" at truecenter with dissolve2
    $ renpy.pause(4)
    hide text with dissolve2
    
    play ambience ambience_cold_wind_loop fadein 3
    play music iw_reverance fadein 3
    scene bg black

    $ set_mode_nvl()
    "Иногда случается, что вещи теряют свой смысл.{w} Вот смысл окна, например, чтобы в него смотреть, но порой смотришь в него, а смотреть там нечего.{w} Ничего интересного.{w} Или вот какой смысл умываться по утрам? Чтобы быть бодрым?{w} А какой смысл быть по утрам бодрым?{w} Какой вообще смысл быть по утрам…{w} Непонятно."
    "И непонятно, то ли жизнь всегда была бессмысленной, а ты просто не замечал этого, то ли смысл был, но куда-то затерялся."
    window hide
    
    $ set_mode_adv()
            
    pvo "Не лежи на снегу, простудишься."
    
    me "Ну и что? А смысл не простужаться?"

    pvo "Чтобы не болеть."

    me "А смысл не болеть?"

    pvo "Чтобы быть здоровым! Семён, ты что, опять забыл принять таблетки?"
    
    window hide
    $ renpy.pause(1)
    scene bg drm_bg
    show snowblossom1
    show snowblossom2
    show snowblossom3
    with dissolve5
    window show

    "Я из последних сил напряг зрение.{w} Сверху, из сумрака, с одной из веток раскинувшегося рядом клёна на меня таращились два ярко-жёлтых глаза с узкими вертикальными зрачками."
    sv "Говорящая кошка, только и всего"

    "Вспомнился анекдот."
    "{i}Учитель: «Дети, запишите предложение: “Рыба сидела на дереве”».\n{w}Ученик: «А разве рыбы сидят на деревьях?»\n{w}Учитель: «Ну… Это была сумасшедшая рыба».{/i}"

    sv "А это — сумасшедшая кошка"
    sv "Или сумасшедший я, если слышу, как она со мной разговаривает?"
    "Ведь кошки совершенно точно не могут разговаривать, у них даже нет произносительных органов артикуляции…"
    "Хотя откуда мне достоверно знать про кошачьи органы, разве я фелинолог? Куда там, я даже не зоолог.{w} Так, никчёмный хиккан-анимешник…"

    me "А смысл быть здоровым?"
    "Обратился я с новым вопросом, пристально глядя на жёлтые точки."

    "Точки сощурились, как если бы их обладатель улыбнулся."
    pvo "Чудак, тебе что, не нравится быть здоровым?"

    me "При чём здесь нравится или не нравится…{w} Я не хочу быть бессмысленно здоровым."

    "Точки снова округлились."
    pvo "Тебе нужен смысл?"

    me "Да."

    pvo "Во всём, во всём?"

    me "Неплохо бы."

    pvo "Тогда тебе нужна Эвристическая Машина."
    "Веско ответствовала кошка."

    me "Какая-какая машина?.."

    pvo "Эвристическая.{w} Дающая смысл."

    "Я покатал во рту новое для меня слово. И неожиданно решил:"
    me "Да, она мне нужна…{w} Но где её искать?"

    pvo "О!{w=0.5} Это очень далеко!"

    me "За смыслом хоть на край света.{w} Веди меня!"
    
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_vzhux
    scene bg ext_dream_prologue with dissolve2
    $ renpy.pause(2, hard=True)
    play sound sfx_uliana_jumps_down
    $ renpy.pause(0.5, hard=True)
    scene cg prologue_cat with zoomin
    window show
    
    "Точки погасли, и кошка практически бесшумно выпрыгнула из темноты."
    "Её неестественно большая морда застыла совсем рядом…"
    
    window hide
    play sound sfx_catlaugh
    show cg:
        anchor (0.5,0.5)
        pos (0.5,0.5)
        parallel:
            ease 1.5 zoom 5
        parallel:
            ease 1.5 rotate 1440
    $ renpy.pause(1, hard=True)
    play ambience ambience_medstation_inside_night
    stop music
    scene bg semen_room_iw_1
    window show
    
    sv "Бывает же, приснится такое…{w} Вроде бы и не кошмар, но явно что-то не особо нормальное"
    
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_ding
    scene bg semen_room_pc with dissolve
    play sound_loop sfx_computer_noise
    window show
    
    "На панели задач замерцал значок мессенджера, а из болтающихся на шее наушников пискнуло, требуя моего внимания."
    "Рука протянулась к мышке."
    
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_click
    scene bg semen_room_pc_alt
    show chat:                           # Привет
        anchor (0.5,0.0)
        pos (0.54,0.525)
    show msngr
    with flash
    $ renpy.pause(1, hard=True)
    
    window show
    "Посреди тёмных обоев рабочего стола резко вспыхнул белый прямоугольник, ударив по глазам ярким светом. Виски сдавило ноющей болью."
    "В информации о контакте было совершенно пусто, только фотография весьма миловидной девушки с кавайными кошачьими ушками на аватаре."
    "Типичный спам-бот."
    "Даже вместо ника стоял всего лишь номер телефона. Но по номеру же нельзя узнать, что за человек на другом конце сетевого кабеля, ведь так?"
    "Хотя, конечно, когда-нибудь всё будет по-другому. Унифицированные числовые идентификаторы вместо имён, набор символов в биографии, несколько байт характера и три с половиной бита чувств…"
    
    play sound sfx_ding_in
    show chat:                           # Как поживаешь?
        ease 0.1 ypos 0.4806
    
    $ renpy.pause(2, hard=True)
    sv "Какой настойчивый спам-бот…"
    window hide
    $ renpy.pause(1, hard=True)
    
    play sound sfx_ding_out
    show chat:                           # Ты кто?
        ease 0.1 ypos 0.4148
        
    $ renpy.pause(2, hard=True)
    
    play sound sfx_ding_in
    show chat:                           # Опять всё забыл?
        ease 0.1 ypos 0.3463
    pause
    play sound sfx_ding_out
    show chat:                           # А что я должен помнить?
        ease 0.1 ypos 0.2806
    
    $ renpy.pause(2, hard=True)
    
    play sound sfx_ding_in
    show chat:                           # Как что?!
        ease 0.1 ypos 0.2148
    $ renpy.pause(1, hard=True)
    play sound sfx_ding_in
    show chat:                           # Ведь мы, ты же меня...
        ease 0.1 ypos 0.1694
    $ renpy.pause(2, hard=True)
    play sound sfx_ding_in
    show chat:                           # А, я поняла, забей 
        ease 0.1 ypos 0.1241

    pause
    window show
    "Окно мессенджера перестало подавать признаки жизни, и я решил, что девушка просто ошиблась номером."
    "Говоря начистоту, симпатичные молодые девушки только так и могут наткнуться на меня: в темноте и по ошибке."
    "Да и несимпатичные тоже.{w} И даже совсем немолодые и несимпатичные…"
    
    play sound sfx_ding_in
    show chat:                           # 410 автобус. Собирайся прямо сейчас!
        ease 0.1 ypos 0.0806
    
    "Я бы ещё долго углублялся в степени некрасивости девушек, с которыми мне теоретически светит хоть что-то, но поток угрюмых мыслей прервало новое сообщение от незнакомки."
    "Я несколько раз перечитал короткую строчку из пяти слов, но так и не нашёлся, что ответить."
    
    play sound sfx_ding_in
    show chat:                           # Если не хочешь на автобусе, можешь просто выброситься из окна
        ease 0.1 ypos -0.0102
    
    pause
    "Теперь я уже твёрдо уверился, что меня с кем-то перепутали, и написал:"
    window hide
    $ renpy.pause(2, hard=True)
    
    play sound sfx_ding_out
    show chat:                           # Ты ошиблась, я тебя не знаю
        ease 0.1 ypos -0.075
    
    $ renpy.pause(2, hard=True)
    
    play sound sfx_ding_in
    show chat:                           # И про Машину тоже не знаешь?
        ease 0.1 ypos -0.1435
    pause
    play sound sfx_ding_out
    show chat:                           # Какую Машину?
        ease 0.1 ypos -0.2083
    
    $ renpy.pause(2, hard=True)
    
    play sound sfx_ding_in
    show chat:                           # Эвристическую
        ease 0.1 ypos -0.2750
    $ renpy.pause(1, hard=True)
    play sound sfx_ding_in
    show chat:                           # хД
        ease 0.1 ypos -0.3250
    
    window show
    "Смайлик в конце показался мне исчадием ада, разверзающим свою безобразную пасть, чтобы поглотить меня."
    window hide
    
    show image "noise" onlayer texture with dissolve5
    window show
    play sound sfx_inhale
    play sound_loop sfx_head_heartbeat fadein 3
    stop ambience fadeout 3
    "Всё вокруг поплыло, потеряло чёткость.{w} Голова закружилась.{w} Я почувствовал, как само моё естество вырывается из физической оболочки.{w} Из глубин небытия медленно всплыла услышанная недавно фраза…"
    window hide
    play sound sfx_intro_bus_transition
    show text u"{size=+40}{font=mods/iw/menu/ustroke.ttf}{color=#ac0000}вот смысл окна, например,\nчтобы в него выброситься...\nно порой бросаешься в него,\nа бросаться там некуда{/color}{/font}{/size}" onlayer texture:
        alpha 0
        anchor (0.5,0.5)
        pos (0.5,0.5)
        pause 3.5
        ease 1 alpha 1
    pause
    
    window show
    sv "Нет, не эта…"
    hide text onlayer texture with dissolve2
    sv "Про Эвристическую Машину"
    
    play sound sfx_ding_in
    show chat:                           # Вспомнил?
        ease 0.1 ypos -0.3648
    hide image "noise" onlayer texture with dissolve5
    
    "Холодно мигнуло сообщение."
    me "Вспомнил."
    play ambience ambience_medstation_inside_night fadein 5
    play sound sfx_smoke
    $ renpy.pause(1, hard=True)
    stop sound_loop fadeout 5
    play sound_loop sfx_computer_noise fadein 5
    "Произнёс я вслух и закурил."
    play sound sfx_ding_in
    show chat:                           # Раз так, собирайся, у тебя мало времени!
        ease 0.1 ypos -0.4093
    pause
    
    me "А ты-то кто такой…{w} такая…{w} такое ваще?"
    
    play sound sfx_ding_in
    show chat:                           # https://vtentakle.com/xram_uvao 
        ease 0.1 ypos -0.4546
    $ renpy.pause(2, hard=True)

    play sound sfx_ding_in
    show chat:                           # Какой же ты сегодня непонятливый! 
        ease 0.1 ypos -0.5185
    pause
    
    me "Стебёшься? Это же просто картинки с вымышленным персонажем визуальной новеллы. Даже я это понимаю."
    
    play sound sfx_ding_in
    show chat:                           # Не знаю, кто там у вас вымышленный, а я — настоящая! 
        ease 0.1 ypos -0.5676
    pause
    
    me "Чем докажешь?"
    
    play sound sfx_ding_in
    show chat:                           # Приходи и потрогай…
        ease 0.1 ypos -0.6093
    $ renpy.pause(1, hard=True)

    play sound sfx_ding_in
    show chat:                           # ;)
        ease 0.1 ypos -0.6593
    pause
    
    sv "Да ну, бред какой…"
    me "А с чего вдруг именно я?{w} Нас же там сотни… тысячи."
    
    $ renpy.pause(3, hard=True)
    play sound sfx_ding_in
    show chat:                           # Фейспалм.жпг 
        ease 0.1 ypos -0.8704
    $ renpy.pause(2, hard=True)

    play sound sfx_ding_in
    show chat:                           # Теперь я понимаю, почему у тебя нет девушки
        ease 0.1 ypos -0.9213
    $ renpy.pause(1, hard=True)

    play sound sfx_ding_in
    show chat:                           # ТЫ ЖЕ ТОРМОЗ! 
        ease 0.1 ypos -0.9657
    $ renpy.pause(2, hard=True)

    play sound sfx_ding_in
    show chat:                           # Совсем уже овощем стал от картинок с голыми задницами
        ease 0.1 ypos -1.0111
    pause
    
    me "Эй, полегче!{w} Богиня, блин."
    
    play sound sfx_ding_in
    show chat:                           # Тогда прекрати задавать глупые вопросы
        ease 0.1 ypos -1.0759
    $ renpy.pause(2, hard=True)

    play sound sfx_ding_in
    show chat:                           # И более симпатичного
        ease 0.1 ypos -1.1204
    pause
    
    me "Слыш, вот это уже реально обидно было!"
    
    window hide
    play music iw_story fadein 3
    stop sound_loop fadeout 3
    scene bg semen_room_iw_2 with dissolve5
    
    play sound sfx_wood_floor_squeak
    pause 0.5
    play sound sfx_drop_alisa_bag 
    with vpunch
    pause 0.5
    play sound sfx_drop_alisa_bag 
    with vpunch
    pause 1
    play sound sfx_bus_window_hit 
    with vpunch
    pause 0.5
    play sound sfx_door_squeak_light
    pause 0.5
    play sound sfx_wood_floor_squeak
    pause 0.5
    
    "Прыгая на одной ноге посреди комнаты и натягивая поверх домашних трико зимние джинсы, я не переставал задаваться множеством вопросов."
    "Кто она такая и как нашла меня, не зарегистрированного под настоящим именем ни в одной соцсети?"
    "Откуда знает, что мне снилось?"
    "Или, например, каким образом слышит то, что я говорю вслух в пустой квартире?"
    "Так или иначе, выходило, что пойти на улицу проветрить мозги и правда будет полезно."
    "И почему бы не подыграть своим галлюцинациям и не совместить это с поездкой на…{w=1} каком там…{w=1} автобусе."
    "Хоть какое-то приключение…"
    
    window hide
    $ renpy.pause(1, hard=True)
    show blink
    show fireflies0 zorder 10
    show fireflies1 zorder 9
    show fireflies2 zorder 8
    show fireflies3 zorder 7
    show fireflies4 zorder 6
    show fireflies5 zorder 5
    $ renpy.pause(6, hard=True)
    play sound sfx_magic
    show dreamgirl zorder 1:
        anchor (0.5,0.5)
        pos (0.55,0.8)
    with pixellate3
    $ renpy.pause(1, hard=True)
    show dreamgirl_bubble zorder 1:
        anchor (0.5,0.5)
        pos (0.67,0.5)
    play sound sfx_ding_short
    $ renpy.pause(2, hard=True)
    
    show dreamgirl:
        parallel:
            ease 3 zoom 1.3
        parallel:
            ease 3 ypos 0.95
    show dreamgirl_bubble:
        parallel:
            ease 4 zoom 1.4
        parallel:
            ease 3 xpos 0.67
        parallel:
            ease 3.5 ypos 0.55

    $ renpy.pause(4.5, hard=True)
   
    window show
    sv "О да, я приду…"
    window hide
    
    hide blink
    hide dreamgirl
    hide dreamgirl_bubble
    with dissolve5
    
    hide fireflies0 with dissolve
    hide fireflies1 with dissolve
    hide fireflies2 with dissolve
    hide fireflies3 with dissolve
    hide fireflies4 with dissolve
    hide fireflies5 with dissolve
    $ renpy.pause(2, hard=True)
    
    window show
    me "Куда мне, говоришь, ехать надо?"
    window hide
    
    $ renpy.pause(1, hard=True)
    play sound sfx_ding_in
    $ renpy.pause(1, hard=True)
    scene bg semen_room_pc_alt
    play sound_loop sfx_computer_noise fadein 3
    show chat:                           # Садись на автобус 410 и приезжай 
        anchor (0.5,0.0)
        pos (0.54,-1.1648)
    show msngr
    with dissolve
    pause
    
    window show
    me "И всё, так просто?"

    play sound sfx_ding_in
    show chat:                           # Да
        ease 0.1 ypos -1.2102
    pause
    
    me "Типа больше ничего делать не надо? Просто сесть на автобус, и я приеду к тебе?"
    
    play sound sfx_ding_in
    show chat:                           # Да. А что не так? 
        ease 0.1 ypos -1.2537
    pause
    
    me "Ничего. Кроме того, что я еду на встречу с кошкодевочкой, которая ни с того ни с сего свалилась на меня, как снег на голову, и теперь общается со мной посредством…{w} э-э…{w} а как ты это делаешь?"
    window hide 
    
    $ renpy.pause(2, hard=True)
    play sound sfx_ding_in
    show chat:                           # :killmeplease:
        ease 0.1 ypos -1.3028
    $ renpy.pause(1, hard=True)

    play sound sfx_ding_in
    show chat:                           # Пока ещё не свалилась!
        ease 0.1 ypos -1.3426
    $ renpy.pause(2, hard=True)

    play sound sfx_ding_in
    show chat:                           # Но ты прав, кое-что сделать придётся, когда будешь на месте 
        ease 0.1 ypos -1.4315
    $ renpy.pause(8, hard=True)
    
    window show
    me "Ну? И какой?"
    window hide
    
    play sound sfx_ding_in
    show chat:                           # Короче, там будет площадь. Выйди на неё голышом рано-рано утром 
        ease 0.1 ypos -1.5222
    pause

    play sound sfx_ding_in
    show chat:                           # Да, самая главная деталь — трусы!
        ease 0.1 ypos -1.6102
    $ renpy.pause(2, hard=True)
    stop music
    play sound sfx_scratch1
    $ renpy.pause(3, hard=True)

    play sound sfx_ding_in
    show chat:                           # Это самое важное, иначе я не найду дорогу к тебе 
        ease 0.1 ypos -1.6769
    pause
    
    stop sound_loop
    stop ambience
    scene bg black with flash
    $ renpy.pause(2, hard=True)
    me "Сегодня, должно быть, четверг…{w} По четвергам у меня вечно все наперекосяк."
    
    jump iw_dayOne_arriveSemyon
    return