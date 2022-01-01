init:

    $ mods["iw_start"]=u"{font=mods/iw/menu/headingpro.ttf}{color=#011}Сокровенное желание{/color}{/font}"

    $ wotl = [(0,"#000000",2,2)]
    $ wclr = "#fff8e7"
    $ pvo = Character(u"Голос из темноты",     color="#000000", what_color=wclr, what_outlines=wotl) # Голос во сне в прологе
    $ sv = Character(u"...",                   color="#fff8e7", what_color=wclr, what_outlines=wotl, what_prefix=u"«", what_suffix=u"»") # мысли Семёна
    $ slf = Character(u"Славя Номер Один",     color="#ffaa00", what_color=wclr, what_outlines=wotl) # Алиса на остановке
    $ sls = Character(u"Славя Номер Два",      color="#ffd200", what_color=wclr, what_outlines=wotl) # Славя на остановке
    $ unv = Character(u"...",                  color="#b956ff", what_color=wclr, what_outlines=wotl) # голос Лены
    $ chor = Character(u"Пионерки",            color="#02de90", what_color=wclr, what_outlines=wotl) # все пионерки говорят хором
    $ yo = Character(u"Йошка",                 color="#e60000", what_color=wclr, what_outlines=wotl) # Йошка
    $ yop = Character(u"Пилот пепелаца",       color="#e60000", what_color=wclr, what_outlines=wotl) # Йошка до представления
    $ ai = Character(u"Искин",                 color="#fff8e7", what_color=wclr, what_outlines=wotl) # Искин
    $ aip = Character(u"Голографическая нэко", color="#fff8e7", what_color=wclr, what_outlines=wotl) # Искин до представления
    $ ri = Character(u"Антонина",              color="#f750b6", what_color=wclr, what_outlines=wotl) # Антонина
    $ rip = Character(u"Розоволосая тян",      color="#f750b6", what_color=wclr, what_outlines=wotl) # Антонина до представления

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
    $ sfx_prunks = "mods/iw/audio/sfx/prunks.ogg"
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
    image cg prologue_cat = "mods/iw/img/cg/prologue_cat.png"

#image
    image dreamgirl = "mods/iw/img/i/dreamgirl.png"
    image dreamgirl_bubble = "mods/iw/img/i/dreamgirl_bubble.png"
    image dreamgirl_creepy = "mods/iw/img/i/dreamgirl_creepy.png"
    image chat = "mods/iw/img/i/chat.png"
    image msngr = "mods/iw/img/i/msngr.png"


#===========================
#Новый текстбокс
init -1 python:

    style.default.font = "mods/iw/menu/arsenal.ttf"
    
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

            add "mods/iw/gui/dialogue_box/dialogue_box_large.png" xpos 0 ypos 850

            imagebutton auto "mods/iw/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 883 action HideInterface()
            imagebutton auto "mods/iw/gui/dialogue_box/save_%s.png" xpos 1567 ypos 883 action ShowMenu('save')
            imagebutton auto "mods/iw/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 883 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/iw/gui/dialogue_box/load_%s.png" xpos 1682 ypos 883 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/iw/gui/dialogue_box/forward_%s.png" xpos 1735 ypos 924 action Skip()
            else:
                imagebutton auto "mods/iw/gui/dialogue_box/fast_forward_%s.png" xpos 1735 ypos 924 action Skip()

            text what id "what" xpos 194 ypos 914 xmaximum 1550 size 35 line_spacing 1 font 'mods/iw/menu/arsenal.ttf' color '#fff8e7'
            if who:
                text who id "who" xpos 194 ypos 877 size 35 line_spacing 1 font 'mods/iw/menu/arsenal.ttf'

        elif persistent.font_size == "small":

            add "mods/iw/gui/dialogue_box/dialogue_box.png" xpos -5 ypos 900

            imagebutton auto "mods/iw/gui/dialogue_box/" + ty + "_backward_%s.png" xpos 30 ypos 950 action ShowMenu("text_history")

            imagebutton auto "mods/iw/gui/dialogue_box/hide_%s.png" xpos 1508 ypos 910 action HideInterface()
            imagebutton auto "mods/iw/gui/dialogue_box/save_%s.png" xpos 1567 ypos 910 action ShowMenu('save')
            imagebutton auto "mods/iw/gui/dialogue_box/menu_%s.png" xpos 1625 ypos 910 action ShowMenu('game_menu_selector')
            imagebutton auto "mods/iw/gui/dialogue_box/load_%s.png" xpos 1682 ypos 910 action ShowMenu('load')

            if not config.skipping:
                imagebutton auto "mods/iw/gui/dialogue_box/forward_%s.png" xpos 1800 ypos 950 action Skip()
            else:
                imagebutton auto "mods/iw/gui/dialogue_box/fast_forward_%s.png" xpos 1800 ypos 950 action Skip()

            text what id "what" xpos 184 ypos 950 xmaximum 1550 size 28 line_spacing 2 font 'mods/iw/menu/arsenal.ttf' color '#fff8e7'
            if who:
                text who id "who" xpos 184 ypos 910 size 28 line_spacing 2 font 'mods/iw/menu/arsenal.ttf'
                
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
