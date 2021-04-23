init:

    $ mods["iw_start"]=u"{font=mods/iw/menu/headingpro.ttf}{color=#011}Сокровенное желание{/color}{/font}"
    $ fnt = "mods/iw/menu/arsenal.ttf"
    $ otl = [(0,"#000000",2,2)]
    $ pvo = Character(u"Голос из темноты", color="#000000", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Голос во сне в прологе
    $ sv = Character(u"...",               color="#fff8e7", what_color="#fff8e7", what_outlines=otl, what_prefix=u"«", what_suffix=u"»", what_font=fnt, who_font=fnt) # мысли Семёна
    $ slf = Character(u"Славя Номер Один", color="#ffaa00", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Алиса на остановке
    $ sls = Character(u"Славя Номер Два",  color="#ffd200", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Славя на остановке
    $ unv = Character(u"Голос",            color="#b956ff", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # голос Лены
    $ chor = Character(u"Пионерки",        color="#02de90", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # все пионерки говорят хором
    $ jo = Character(u"Йошка",             color="#e60000", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Йошка
    $ jop = Character(u"Пришелец",         color="#e60000", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Йошка до представления
    $ ai = Character(u"Искин",             color="#fff8e7", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Искин
    $ aip = Character(u"Голограмма",       color="#fff8e7", what_color="#fff8e7", what_outlines=otl, what_font=fnt, who_font=fnt) # Искин до представления
    $ narrator = Character (what_color="#fff8e7", what_font=fnt, who_font=fnt)

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

    
#===========================
#Новый текстбокс
init -1 python:

    style.default.font = "mods/iw/menu/arsenal.ttf"
    style.say_dialogue.font = "mods/iw/menu/arsenal.ttf"
    style.say_thought.font = "mods/iw/menu/arsenal.ttf"

    
    def iw_screens():
        renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("iw_say", None)]
        renpy.display.screen.screens[("nvl", None)] = renpy.display.screen.screens[("iw_nvl", None)]
        
    def iw__screens_diact():
        renpy.display.screen.screens[("say", None)] 
        renpy.display.screen.screens[("nvl", None)]


screen iw_say:
    window background None id "window":

            #$ timeofday = persistent.timeofday
            
        #$ ty = "1"

        if persistent.font_size == "large":

            imagebutton auto "mods/iw/gui/dialogue_box/" + ty + "_backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

            add "mods/iw/gui/dialogue_box/dialogue_box_large.png" xpos 174 ypos 866

            imagebutton auto "mods/iw/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 883 action HideInterface()
            imagebutton auto "mods/iw/gui/dialogue_box/save_%s.png" xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto "mods/iw/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/iw/gui/dialogue_box/load_%s.png" xpos 1682 ypos 883 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/iw/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 924 action Skip()
            else:
                imagebutton auto "mods/iw/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1541 size 35 line_spacing 1 # font 'mods/iw/fonts/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1

        elif persistent.font_size == "small":

            imagebutton auto "mods/iw/gui/dialogue_box/" + ty + "_backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

            add "mods/iw/gui/dialogue_box/dialogue_box.png" xpos 174 ypos 916

            imagebutton auto "mods/iw/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 933 action HideInterface()
            imagebutton auto "mods/iw/gui/dialogue_box/save_%s.png" xpos 1567 ypos 933 action ShowMenu('save')
            imagebutton auto "mods/iw/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 933 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/iw/gui/dialogue_box/load_%s.png" xpos 1682 ypos 933 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/iw/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 949 action Skip()
            else:
                imagebutton auto "mods/iw/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 949 action Skip()

            text what id "what" xpos 194 ypos 964 xmaximum 1541 size 28 line_spacing 2 # font 'mods/iw/fonts/Caveat.ttf'
            if who:
                text who id "who" xpos 194 ypos 931 size 28 line_spacing 2
                
screen iw_nvl:

    $ timeofday = persistent.timeofday


    window background Frame("mods/iw/gui/choice_box.png",50,50) xfill True yfill True yalign 0.5 left_padding 175 right_padding 175 bottom_padding 150 top_padding 150:
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if persistent.font_size == "large":
                    if who is not None:
                        text who id who_id size 35
                    text what id what_id size 35
                elif persistent.font_size == "small":
                    if who is not None:
                        text who id who_id size 28
                    text what id what_id size 28
        if items:
            vbox:
                id "menu"
                for caption, action, chosen in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption style "nvl_menu_choice"
                    else:
                        text caption style "nvl_dialogue"

    imagebutton auto "mods/iw/gui/dialogue_box/backward_%s.png" xpos 38 ypos 924 action ShowMenu("text_history")

    if not config.skipping:
        imagebutton auto "mods/iw/gui/dialogue_box/forward_%s.png" xpos 1768 ypos 949 action Skip()
    else:
        imagebutton auto "mods/iw/gui/dialogue_box/fast_forward_%s.png" xpos 1768 ypos 949 action Skip()
