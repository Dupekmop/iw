init:

    $ mods["iw_start"]=u"{font=mods/iw/menu/slimamif.ttf}{color=#000}Сокровенное желание{/color}{/font}"
    
    $ pvo = Character(u"Голос из темноты", color="#000000", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Голос во сне в прологе
    $ sv = Character(u"...",               color="#fff8e7", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )], what_prefix=u"«", what_suffix=u"»") # мысли Семёна
    $ slf = Character(u"Славя Номер Один", color="#ffaa00", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Алиса на остановке
    $ sls = Character(u"Славя Номер Два",  color="#ffd200", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Славя на остановке
    $ unv = Character(u"Голос",            color="#b956ff", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # голос Лены
    $ chor = Character(u"Пионерки",        color="#02de90", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # все пионерки говорят хором
    $ jo = Character(u"Йошка",             color="#e60000", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Йошка
    $ jop = Character(u"Пришелец",         color="#e60000", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Йошка до представления
    $ ai = Character(u"Искин",             color="#fff8e7", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Искин
    $ aip = Character(u"Голограмма",       color="#fff8e7", what_color="#f1d076", what_outlines=[( 0, "#000000", 2, 2 )]) # Искин до представления
    
    define dreamgirl2 = Character(u"ЮВАО", color="#467722", what_color="#f1d076")
    define d1 = Character(u"Девушка 1", what_color="#f1d076")
    define d2 = Character(u"Девушка 2", what_color="#f1d076")
    define girl_A = Character(u"Какая-то девочка", what_color="#f1d076")
    define girl_B = Character(u"Юннатка", what_color="#f1d076")
    define boy_A = Character(u"Какой-то мальчик", what_color="#f1d076")
    define al1 = Character(u"Девчачий голосок", color="#364ac5", what_color="#f1d076")
    define al2 = Character(u"Странная девочка", color="#364ac5", what_color="#f1d076")
    define al_e3 = Character(u"Алёна", color="#364ac5", what_color="#f1d076")
    define ci = Character(u"Саша", color="#59d80c", what_color="#f1d076")
    define iie = Character(u"Инна", color="#0ae5f3", what_color="#f1d076")
    define hai = Character(u"Аня", color="#ec8312", what_color="#f1d076")
    define hai1 = Character(u"Незнакомка", color="#ec8312", what_color="#f1d076")
    define iie1 = Character(u"Опять незнакомка", color="#0ae5f3", what_color="#f1d076")
    define tok1 = Character(u"Какой-то пионер", color="#d4620e", what_color="#f1d076")
    define tok = Character(u"Вилли", color="#d4620e", what_color="#f1d076")
    define nat1 = Character(u"Повар", color="#fbfe04", what_color="#f1d076")
    define uv1 = Character(u"Странная пионерка", color="#467722", what_color="#f1d076")
    
#sfx
    $ sfx_vzhux = "mods/iw/audio/sfx/vzhux.ogg"
    $ sfx_scratch1 = "mods/iw/audio/sfx/scratch1.mp3"
    $ sfx_scratch2 = "mods/iw/audio/sfx/scratch2.ogg"
    $ sfx_magic = "mods/iw/audio/sfx/magic.ogg"
    $ sfx_catlaugh = "mods/iw/audio/sfx/catlaugh.ogg"
    $ sfx_click = "mods/iw/audio/sfx/click.mp3"
    $ sfx_ding_short = "mods/iw/audio/sfx/ding_short.ogg"
    $ sfx_ding = "mods/iw/audio/sfx/ding.mp3"
    $ sfx_ding_in = "mods/iw/audio/sfx/ding_in.mp3"
    $ sfx_ding_out = "mods/iw/audio/sfx/ding_out.mp3"
    $ sfx_blop = "mods/iw/audio/sfx/blop.ogg"
    $ sfx_prunk1 = "mods/iw/audio/sfx/prunk1.ogg"
    $ sfx_prunk2 = "mods/iw/audio/sfx/prunk2.ogg"
    $ sfx_prunk3 = "mods/iw/audio/sfx/prunk3.ogg"
    $ sfx_smoke = "mods/iw/audio/sfx/smoke.ogg"
    

#music
    $ iw_reverance = "mods/iw/audio/music/reverance.mp3"
    $ iw_story = "mods/iw/audio/music/story.ogg"
    $ iw_killem = "mods/iw/audio/music/killem.mp3"
    
#bg 
    image bg ext_dream_prologue = "mods/iw/img/bg/ext_dream_prologue.png"
    image bg semen_room_iw_1 = "mods/iw/img/bg/semen_room_iw_1.png"
    image bg semen_room_iw_2 = "mods/iw/img/bg/semen_room_iw_2.png"
    image bg semen_room_pc = "mods/iw/img/bg/semen_room_pc.png"
    image bg semen_room_pc_alt = "mods/iw/img/bg/semen_room_pc_alt.png"
    image bg ext_camp_entrance_evening = "mods/iw/img/bg/ext_camp_entrance_evening.jpg"
    image bg ext_camp_entrance_sunset_sur = "mods/iw/img/bg/ext_camp_entrance_sunset_sur.jpg"
    image bg ext_camp_entrance_sunset = "mods/iw/img/bg/ext_camp_entrance_sunset.png"
    
#cg
    image cg prologue_cat =  "mods/iw/img/cg/prologue_cat.png"

#image
    image dreamgirl = "mods/iw/img/i/dreamgirl.png"
    image dreamgirl_bubble = "mods/iw/img/i/dreamgirl_bubble.png"
    image dreamgirl_creepy = "mods/iw/img/i/dreamgirl_creepy.png"
    image chat = "mods/iw/img/i/chat.png"
    image msngr = "mods/iw/img/i/msngr.png"
        

#=====================================
#День 1
    $ d1_keys_e3 = False
    $ d1_un_zn_e3 = False #true если заговорил с Леной вечером когда она на лавочке читала книгу
    $ d1_sl_zn_e3 = False #true если ответил Славе при знакомстве
    $ lp_us_e3 = 0
    $ lp_un_e3 = 0
    $ lp_sl_e3 = 0
    $ lp_mi_e3 = 0
    $ lp_dv_e3 = 0
    $ lp_mt_e3 = 0
    $ lp_sh_e3 = 0
    
#BG    
    image bg int_dining_hall_people_day_e3 = "mods/2020miku/bg/int_dining_hall_people_day_e3.jpg"
    
#CG    
    image cg d1_sl_dinner_e3 = "mods/2020miku/cg/d1_sl_dinner_e3.jpg"
    image cg d1_sl_dinner_0_e3 = "mods/2020miku/cg/d1_sl_dinner_0_e3.jpg"
#IMAGE
            
#Музыка
    $ koster1_e3 = "mods/2020miku/music/koster1_e3.mp3"
    $ bremen_dr_e3 = "mods/2020miku/music/bremen_dr_e3.mp3" #вечер с мику
    $ rigim_e3 = "mods/2020miku/music/rigim_e3.mp3" #душевые с двач
    $ vinni_puh_e3 = "mods/2020miku/music/vinni_puh_e3.mp3" #украшение с Ульяной 2
    $ visota_e3 = "mods/2020miku/music/visota_e3.mp3" #перед душем
    $ grustn_pesn_e3 = "mods/2020miku/music/grustn_pesn_e3.mp3" #переноска колонок с Леной
    $ polet_e3 = "mods/2020miku/music/polet_e3.mp3" #отбор музыки с Мику
    $ ch_zakata_e3 = "mods/2020miku/music/ch_zakata_e3.mp3" #вечер с мику
    $ tolpa_e3 = "mods/2020miku/music/tolpa_e3.mp3" #шум толпы на площади
    
  
#Амбиенсы
    $ veter_e3 = "mods/2020miku/music/veter_e3.mp3"
    $ dogd3_e3 = "mods/2020miku/music/dogd3_e3.mp3"
    $ dogd_gr_e3 = "mods/2020miku/music/dogd_gr_e3.mp3"    