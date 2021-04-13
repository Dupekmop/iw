init:

    $ mods["iw_start"]=u"{font=mods/iw/menu/slimamif.ttf}{color=#131357}Сокровенное желание{/color}{/font}"
    
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
    
    $ dissolve5 = Dissolve(5.0)
    $ pixellate3 = Pixellate(3,3)

#sfx
    $ sfx_suddenly = "mods/iw/audio/sfx/suddenly.ogg"
    $ sfx_scratch1 = "mods/iw/audio/sfx/scratch1.mp3"
    $ sfx_magic = "mods/iw/audio/sfx/magic.ogg"
    $ sfx_catlaugh = "mods/iw/audio/sfx/catlaugh.ogg"
    $ sfx_click = "mods/iw/audio/sfx/click.mp3"
    $ sfx_ding = "mods/iw/audio/sfx/ding.mp3"
    $ sfx_ding_in = "mods/iw/audio/sfx/ding_in.mp3"
    $ sfx_ding_out = "mods/iw/audio/sfx/ding_out.mp3"
    $ sfx_blop = "mods/iw/audio/sfx/blop.ogg"
    $ sfx_prunk1 = "mods/iw/audio/sfx/prunk1.ogg"
    $ sfx_prunk2 = "mods/iw/audio/sfx/prunk2.ogg"
    $ sfx_prunk3 = "mods/iw/audio/sfx/prunk3.ogg"
    $ sfx_smoke = "mods/iw/audio/sfx/smoke.ogg"
    

#music
    $ music_prologue = "mods/iw/audio/music/reverance.mp3"
    $ christmas_met = "mods/iw/audio/music/christmas_met_7dl.ogg"
    $ killem = "mods/iw/audio/music/killem.mp3"
    
#bg 
    image bg ext_park_dream = "mods/iw/img/bg/ext_park_dream.png"
    image bg semen_room_pc = "mods/iw/img/bg/semen_room_pc.png"
    image bg semen_room_pc_alt = "mods/iw/img/bg/semen_room_pc_alt.png"
    image bg semen_room_pc_altt = "mods/iw/img/bg/semen_room_pc_altt.png"
    image bg semen_room_alt = "mods/iw/img/bg/semen_room_alt.png"
    image bg ext_camp_entrance_evening = "mods/iw/img/bg/ext_camp_entrance_evening.jpg"
    image bg ext_camp_entrance_sunset_sur = "mods/iw/img/bg/ext_camp_entrance_sunset_sur.jpg"
    image bg ext_camp_entrance_sunset = "mods/iw/img/bg/ext_camp_entrance_sunset.png"

#image
    image snowblossom1 = SnowBlossom("mods/iw/img/i/snowflake1.png", count=50, border=200, xspeed=(30, 70), yspeed=(75, 175), start=2, fast=True, horizontal=False)
    image snowblossom2 = SnowBlossom("mods/iw/img/i/snowflake2.png", count=60, border=200, xspeed=(20, 60), yspeed=(50, 150), start=3, fast=True, horizontal=False)
    image snowblossom3 = SnowBlossom("mods/iw/img/i/snowflake3.png", count=70, border=200, xspeed=(10, 50), yspeed=(25, 125), start=4, fast=True, horizontal=False)
    image snowblossom4 = SnowBlossom("mods/iw/img/i/snowflake4.png", count=80, border=200, xspeed=(5, 40), yspeed=(12, 112), start=5, fast=True, horizontal=False)
    image fireflies0 = SnowBlossom("mods/iw/img/i/firefly0.png", count=15, border=50, xspeed=(30, 90), yspeed=(-50, -150), start=2, fast=False, horizontal=False)
    image fireflies1 = SnowBlossom("mods/iw/img/i/firefly1.png", count=15, border=50, xspeed=(30, 90), yspeed=(-37, -100), start=2, fast=False, horizontal=False)
    image fireflies2 = SnowBlossom("mods/iw/img/i/firefly2.png", count=15, border=50, xspeed=(25, 75), yspeed=(-27, -70), start=2, fast=False, horizontal=False)
    image fireflies3 = SnowBlossom("mods/iw/img/i/firefly3.png", count=15, border=50, xspeed=(20, 60), yspeed=(-16, -45), start=2, fast=False, horizontal=False)
    image fireflies4 = SnowBlossom("mods/iw/img/i/firefly4.png", count=30, border=50, xspeed=(15, 45), yspeed=(-8, -20), start=2, fast=False, horizontal=False)
    image fireflies5 = SnowBlossom("mods/iw/img/i/firefly5.png", count=30, border=50, xspeed=(10, 30), yspeed=(-2, -8), start=2, fast=False, horizontal=False)
    image dreamgirl = "mods/iw/img/i/dreamgirl.png"
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