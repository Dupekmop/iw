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
    $ persistent.sprite_time = "day"
        
    ### дляТЕСТОВ
    

    
    ### /дляТЕСТОВ

    show text "{i}{color=#f1d076}Бойтесь своих желаний — они имеют свойство сбываться{/color}{/i}" at truecenter with dissolve2
    $ renpy.pause(3)
    hide text with dissolve2
    
    play ambience ambience_cold_wind_loop fadein 3
    play music music_prologue fadein 3
    scene bg black with dissolve2
    $ set_mode_nvl()
    "Иногда случается, что вещи теряют свой смысл.{w} Вот смысл окна, например, чтобы в него смотреть, но порой смотришь в него, а смотреть там нечего.{w} Ничего интересного.{w} Или вот какой смысл умываться по утрам? Чтобы быть бодрым?{w} А какой смысл быть по утрам бодрым?{w} Какой вообще смысл быть по утрам…{w} Непонятно."
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

    "Я покатал во рту это новое для меня слово. И неожиданно решил:"
    me "Да, она мне нужна…{w} Но где её искать?"

    pvo "О!{w=0.5} Это очень далеко!"

    me "За смыслом хоть на край света.{w} Веди меня!"

    "Неожиданно точки погасли, и кошка бесшумно выпрыгнула из темноты."
    "Её неестественно большая морда застыла совсем рядом…"
    
    window hide
    play sound sfx_catlaugh
    $ renpy.pause(0.5, hard=True)
    play ambience ambience_medstation_inside_night
    stop music
    scene bg semen_room
    window show
    
    "Я проснулся."
    "На панели задач мерцал значок мессенджера, а из болтающихся на шее наушников тускло пищало, требуя моего внимания."
    "Рука протянулась к мышке."
    
    window hide
    $ renpy.pause(1, hard=True)
    play sound sfx_click_3
    $ renpy.pause(1, hard=True)
    $ set_mode_nvl()
    window show
    
    "Посреди тёмных обоев рабочего стола резко вспыхнул белый прямоугольник, ударив по глазам ярким светом. Виски сдавило ноющей болью."

    uvp "{i}«Семён, привет! Помнишь меня?»{/i}"
    "Я вгляделся в незнакомый никнейм «ЮВАО» и весьма миловидное лицо девушки с кавайными кошачьими ушками на аватаре. Не придумав ничего лучше, написал в ответ:{nw}"
    me "{i}«Ты кто?»{/i}"
    uvp "{i}«Опять всё забыл?»{/i}"
    me "{i}«А что я должен помнить?»{/i}"
    uvp "{i}«Как что?!»{w=1}\n«Ведь мы…»{w=1}\n«Ты же меня…»{w=0.75}\n«А, я поняла, забей»{/i}"

    $ set_mode_adv()
    "Окно мессенджера несколько минут не подавало признаков жизни, и я решил, что неизвестная мне ЮВАО просто ошиблась номером."
    "Говоря начистоту, симпатичные молодые девушки только так и могут наткнуться на меня: в темноте и по ошибке."
    "Да и несимпатичные тоже.{w} И даже совсем немолодые и несимпатичные…"
    "Я бы ещё долго углублялся в степени некрасивости девушек, с которыми мне теоретически светит хоть что-то, но поток угрюмых мыслей прервало новое сообщение от незнакомки."

    $ set_mode_nvl()
    uvp "{i}«410 автобус. Собирайся прямо сейчас!»{/i}"
    "Я несколько раз перечитал короткую строчку из пяти слов, но так и не нашёлся, что ответить.{w} Вдогонку прилетело следующее:{nw}"
    uvp "{i}«Если не хочешь на автобусе, можешь просто выброситься из окна. Только надо тщательно это сделать, чтоб в лепёшку, а иначе ничего не получится!»{/i}"
    "Теперь я уже твёрдо уверился, что меня с кем-то перепутали, и написал:{nw}"
    me "{i}«Ты ошиблась, я тебя не знаю»{/i}"
    uvp "{i}«И про Машину тоже не знаешь?»{/i}"
    me "{i}«Какую Машину?»{/i}"
    uvp "{i}«Эвристическую»{/i}"
    
    window hide
    $ renpy.pause(3, hard=True)
    $ set_mode_adv()
    window show
    
    "Экран монитора расплылся перед глазами, строчки сообщений разъехались в разные стороны.{w} Из памяти выпрыгнула где-то услышанная недавно фраза."
    "{i}«Вот смысл окна, например, чтобы в него выброситься, но порой бросаешься в него, а бросаться там некуда».{/i}"
    "Нет, не эта…{w} Про Эвристическую Машину."
    
    $ set_mode_nvl()
    "Неумолимым свинцовым кирпичом по мозгам ударило следующее сообщение:{nw}"
    uvp "{i}«Вспомнил?»{/i}"
    me "Вспомнил."
    "Произнёс я вслух и закурил."
    uvp "{i}«Раз так, собирайся, у тебя мало времени!»{/i}"
    me "А ты-то кто такая ваще?"
    uvp "https://vtentakle.com/xram_uvao{w=1}{nw}"
    uvp "{i}«Какой же ты сегодня непонятливый! Ну, кто твоя вайфу? Кто посещает Храм богини Юли и делает щедрые подношения мне там?»{/i}"
    me "Стебёшься? Это же просто картинки с вымышленным персонажем визуальной новеллы. Даже я это понимаю."
    uvp "{i}«Не знаю, кто там у вас вымышленный, а я — настоящая!»{/i}"
    me "Чем докажешь?"
    uvp "{i}«Приходи и потрогай…»{/i}"
    "Спустя секунду сообщение дополнилось кокетливым смайликом."
    me "А почему именно я?{w} Нас же там тысячи."
    uvp "{i}«Фейспалм.жпг»{/i}{w=0.5}{nw}"
    uvp "{i}«Теперь я понимаю, почему у тебя нет девушки»{/i}{w=0.5}{nw}"
    uvp "{i}«ТЫ ЖЕ ТОРМОЗ!»{/i}{w=1}{nw}"
    uvp "{i}«Совсем уже овощем стал от картинок с голыми задницами»{/i}"
    me "Эй, давай-ка повежливей."
    uvp "{i}«Тогда прекрати задавать глупые вопросы и собирайся, пока и вправду не пошла искать более сообразительного поклонника»{/i}{w=1}{nw}"
    uvp "{i}«И более симпатичного»{/i}"
    me "Слыш, вот это уже обидно было!"

    window hide
    scene bg black with flash
    $ renpy.pause(3, hard=True)
    scene bg semen_room with dissolve
    $ set_mode_adv()

    "Прыгая на одной ноге посреди комнаты и натягивая поверх домашних трико зимние джинсы, я не переставал задаваться множеством вопросов."
    "Кто она такая и как нашла меня, не зарегистрированного под настоящим именем ни в одной соцсети."
    "Откуда знает, что мне снилось?"
    "Или, например, каким образом слышит то, что я говорю вслух в пустой квартире?"
    "Так или иначе, выходило, что пойти на улицу проветрить мозги и правда будет полезно."
    "И почему бы не подыграть своим галлюцинациям и не совместить это с поездкой на…{w=1} каком там…{w=1} автобусе."
    "Хоть какое-то приключение…"
    "{i}«Приходи и потрогай…»{/i} — эти слова стояли у меня перед глазами и будоражили воображение."
    sv "О да, я приду…"
    
    me "Куда мне, говоришь, ехать надо?"
    "Окно мессенджера тут же мигнуло новым сообщением. Я затянул ремень на худосочном теле и подошёл к монитору."

    $ set_mode_nvl()
    uvp "{i}«Садись на автобус 410 и приезжай»{/i}"
    me "И всё, так просто?"
    uvp "{i}«Да»{/i}"
    me "Типа больше ничего делать не надо? Просто сесть на автобус, и я приеду к тебе?"
    uvp "{i}«Да. А что не так?»{/i}"
    me "Ничего. Кроме того, что я еду на встречу с кошкодевочкой, которая ни с того ни с сего свалилась на меня, как снег на голову, и теперь общается со мной посредством…{w} э-э…{w} а как ты это делаешь?"
    "В ответ прилетел бьющийся головой о стену смайлик."
    uvp "{i}«Пока ещё не свалилась!»{/i}{w=1}{nw}"
    uvp "{i}«Но ты прав, кое-что сделать придётся, когда будешь на месте. Чтобы я почувствовала твоё присутствие и нашла тебя, тебе придётся совершить ритуал призыва»{/i}"
    "Когда пауза затянулась, я осторожно поинтересовался:"
    me "Ну? И какой?"
    uvp "{i}«Короче, там будет площадь. Выйди на неё голышом рано-рано утром, встань лицом строго на юго-юго-восток и с первыми лучами солнца громко три раза крикни: “Юля, приди!”»{/i}{w=1}{nw}"
    uvp "{i}«Да, самая главная деталь — трусы! Тебе надо будет кричать, держа их как можно выше над головой. А в оконцове обязательно сожги их и развей пепел по ветру»{/i}{w=1}{nw}"
    uvp "{i}«Это самое важное, иначе я не найду дорогу к тебе. Трусы подойдут любые, но лучше женские»{/i}"
    
    window hide
    scene bg black with flash
    $ renpy.pause(3, hard=True)
    scene bg semen_room with dissolve
    $ set_mode_adv()
    
    me "Сегодня, должно быть, четверг…{w} По четвергам у меня вечно все наперекосяк."
    scene bg black with dissolve5
    $ renpy.pause(5, hard=True)
    stop ambience


label iw_dayOne_arrive:
    show text "{i}{color=#f1d076}Существует теория, что Вселенная бесконечна,\nа потому в ней должны быть копии нашей планеты.\nВы только представьте: летел космический корабль\nмиллионы световых лет в поисках другой цивилизации…\nи уткнулся в Мытищи.{/color}{/i}" at truecenter with dissolve2
    $ renpy.pause(10)
    hide text with dissolve2
    $ backdrop = "days"
    $ new_chapter(1, u"Сокровенное желание: Прибытие")
    $ persistent.sprite_time = "day"
    $ day_time()
    
    ### дляТЕСТОВ
    

    
    ### /дляТЕСТОВ
    
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
    show entrance_day
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
    show entrance_day:
        zoom 1.1
    with vpunch

    show ja serious with dissolve
    sls "..."
    
    window hide
    play sound sfx_prunk1
    show entrance_day:
        anchor (0.5,1)
        ease 0.5 pos (0.55,1)
    show jd normal:
        ease 0.5 xpos 0.05
    show ja serious with hpunch:
        ease 0.5 xpos 0.75
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk2
    show entrance_day:
        ease 0.5 pos (0.45,1)
    show jd normal:
        ease 0.5 xpos 0.25
    show ja serious with hpunch:
        ease 0.5 xpos 0.95
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk3
    show entrance_day:
        ease 0.5 pos (0.55,1)
    show jd angry:
        ease 0.5 xpos 0.05
    show ja serious with hpunch:
        ease 0.5 xpos 0.75
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk1
    show entrance_day:
        ease 0.5 pos (0.45,1)
    show jd angry:
        ease 0.5 xpos 0.25
    show ja serious with hpunch:
        ease 0.5 xpos 0.95
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk2
    show entrance_day:
        ease 0.5 pos (0.55,1)
    show jd angry:
        ease 0.5 xpos 0.05
    show ja angry with hpunch:
        ease 0.5 xpos 0.75
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk3
    show entrance_day:
        ease 0.5 pos (0.45,1)
    show jd angry:
        ease 0.4 xpos 0.25
    show ja angry with hpunch:
        ease 0.4 xpos 0.95
    $ renpy.pause(0.5, hard=True)
    
    play sound sfx_prunk1
    show entrance_day:
        ease 0.5 pos (0.55,1)
    show jd rage:
        ease 0.4 xpos 0.05
    show ja angry with hpunch:
        ease 0.4 xpos 0.75
    $ renpy.pause(0.4, hard=True)
    
    play sound sfx_prunk2
    show entrance_day:
        ease 0.5 pos (0.45,1)
    show jd rage:
        ease 0.3 xpos 0.25
    show ja rage with hpunch:
        ease 0.3 xpos 0.95
    $ renpy.pause(0.3, hard=True)
    
    play sound sfx_prunk3
    show entrance_day:
        ease 0.5 pos (0.55,1)
    show jd rage:
        ease 0.3 xpos 0.05
    show ja rage with hpunch:
        ease 0.3 xpos 0.75
    $ renpy.pause(0.3, hard=True)

    window show
    "Некоторое время продолжалось молчаливое соревнование по перетягиванию Семёна."

    show jd angry pioneer at left with ease
    show ja angry pioneer at right with ease

    "Наконец поняв, что грубой силой тут ничего не решить, соперницы оставили меня в покое и перешли к переговорам."

    hide entrance_day with vpunch
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
    with dissolve2
    
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
    hide mt with dissolve
    play music killem fadein 2
    $ renpy.pause(1, hard=True)
    hide jd
    hide ja
    hide un
    hide us
    with dissolve2
    
    $ renpy.pause(2, hard=True)
    
    play sound sfx_intro_bus_stop_sigh
    scene bg ext_camp_entrance_sunset with dissolve2
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
    show un cry sport at center with dissolve
    
    window show
    "Лена тем временем подходила всё ближе и становилась всё печальнее."
    me "Лена… Леночка, ты это… ножик положь, пока не поранилась."
    show un cry_smile with dissolve
    $ renpy.pause(1, hard=True)
    "Но её решимость огорчить меня до невозможности ничуть не поколебалась."
    me "Сходил за хлебушком, называется…"

    window hide
    scene bg ext_camp_entrance_sunset_sur with dissolve2
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
    $ renpy.pause(1, hard=True)
    play sound sfx_ghost_children_laugh
    $ renpy.pause(1, hard=True)
    
    scene bg black with dissolve2
    stop sound_loop
    play ambience ambience_camp_entrance_night
    stop music fadeout 3
    pause
    jump iw_start