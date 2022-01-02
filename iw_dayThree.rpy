label iw_dayThree_maze:
    $ prolog_time()
    $ backdrop = "prologue"
    $ new_chapter(0, u"Сокровенное желание:\nКатакомбы")
    $ persistent.sprite_time = "night"
    play ambience ambience_catacombs fadein 3

    $ path = 0
    $ passage = 0
    $ battery = 77
    
label iw_maze_enter:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_crossroad with dissolve        
    if path == 0:
        "Вход в катакомбы. Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A
            "Прямо":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Направо":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C
            
    elif path == 1:
        "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
        "Справа в свете фонаря видна дверь, значит, мы вернулись в начало пути."
        "Ходы ведут налево и прямо."    
        menu:
            "Налево":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Прямо":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C
            "Вернуться назад":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A

    elif path == 2:
        "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
        "Перед нами в свете фонаря видна дверь, значит, мы вернулись в начало пути."
        "Ходы ведут налево и направо."    
        menu:
            "Налево":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C
            "Направо":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A
            "Вернуться назад":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B

    elif path == 3:
        "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
        "Слева в свете фонаря видна дверь, значит, мы вернулись в начало пути."
        "Ходы ведут прямо и направо."    
        menu:
            "Прямо":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A
            "Направо":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Вернуться назад":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C

label iw_maze_A:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_halt with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 1:
        "Туннель уходит направо."
    
        menu:
            "Направо":
                $ path = 4
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D
            "Вернуться назад":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter

    elif path == 4:
        "Туннель уходит налево."
    
        menu:
            "Налево":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter
            "Вернуться назад":
                $ path = 1
                $ passage = 1
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D

label iw_maze_B:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_crossroad with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 2:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D
            "Прямо":
                $ path = 7
                $ passage = 10
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE1
            "Направо":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E
            "Вернуться назад":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter

    elif path == 6:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 7
                $ passage = 10
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE1
            "Прямо":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E
            "Направо":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter
            "Вернуться назад":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D

    elif path == 7:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E
            "Прямо":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter
            "Направо":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D
            "Вернуться назад":
                $ path = 7
                $ passage = 10
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE1

    elif path == 8:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 2
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter
            "Прямо":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D
            "Направо":
                $ path = 7
                $ passage = 10
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE1
            "Вернуться назад":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E

label iw_maze_C:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_halt with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 3:
        "Туннель уходит налево."
    
        menu:
            "Налево":
                $ path = 5
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E
            "Вернуться назад":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter

    elif path == 4:
        "Туннель уходит направо."
    
        menu:
            "Направо":
                $ path = 3
                $ passage = 2
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_enter
            "Вернуться назад":
                $ path = 5
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E

label iw_maze_D:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_crossroad with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 4:
        "Ходы ведут прямо и направо."
        menu:
            "Прямо":
                $ path = 9
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F
            "Направо":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Вернуться назад":
                $ path = 4
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A

    elif path == 9:
        "Ходы ведут налево и прямо."
        menu:
            "Налево":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Прямо":
                $ path = 4
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A
            "Вернуться назад":
                $ path = 9
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F

    elif path == 6:
        "Ходы ведут налево и направо."
        menu:
            "Налево":
                $ path = 4
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_A
            "Направо":
                $ path = 9
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F
            "Вернуться назад":
                $ path = 6
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B

label iw_maze_E:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_crossroad with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 11:
        "Ходы ведут прямо и направо."
        menu:
            "Прямо":
                $ path = 5
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C
            "Направо":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Вернуться назад":
                $ path = 11
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H

    elif path == 5:
        "Ходы ведут налево и прямо."
        menu:
            "Налево":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B
            "Прямо":
                $ path = 11
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H
            "Вернуться назад":
                $ path = 5
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C

    elif path == 8:
        "Ходы ведут налево и направо."
        menu:
            "Налево":
                $ path = 11
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H
            "Направо":
                $ path = 5
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_C
            "Вернуться назад":
                $ path = 8
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_B

label iw_maze_DE1:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_coalface with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    "Дальше пути нет. Похоже, это тупик."
    "Возвращаемся назад."
    $ path = 7
    $ passage = 10
    $ battery -= passage
    scene bg black with dissolve
    jump iw_maze_B

label iw_maze_F:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_halt with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 9:
        "Туннель уходит направо."    
        menu:
            "Направо":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_G
            "Вернуться назад":
                $ path = 9
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D

    elif path == 12:
        "Туннель уходит налево."    
        menu:
            "Налево":
                $ path = 9
                $ passage = 4
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_D
            "Вернуться назад":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_G

label iw_maze_G:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_crossroad with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 12:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 14
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE2
            "Прямо":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H
            "Направо":
                $ path = 10
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_exit
            "Вернуться назад":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F

    elif path == 13:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 10
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_exit
            "Прямо":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F
            "Направо":
                $ path = 14
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE2
            "Вернуться назад":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H

    elif path == 14:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H
            "Прямо":
                $ path = 10
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_exit
            "Направо":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F
            "Вернуться назад":
                $ path = 14
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE2

    elif path == 10:
        "Ходы ведут налево, прямо и направо."
        menu:
            "Налево":
                $ path = 12
                $ passage = 5
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_F
            "Прямо":
                $ path = 14
                $ passage = 3
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_DE2
            "Направо":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_H
            "Вернуться назад":
                $ path = 10
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_exit

label iw_maze_H:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_halt with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    if path == 13:
        "Туннель уходит направо."    
        menu:
            "Направо":
                $ path = 11
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E
            "Вернуться назад":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_G

    elif path == 11:
        "Туннель уходит налево."    
        menu:
            "Налево":
                $ path = 13
                $ passage = 7
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_G
            "Вернуться назад":
                $ path = 11
                $ passage = 6
                $ battery -= passage
                scene bg black with dissolve
                jump iw_maze_E

label iw_maze_DE2:
    $ renpy.pause(passage)
    if battery <= 0:
        jump iw_maze_youaredead

    scene bg int_mine_coalface with dissolve
    "Переход израсходовал [passage]\%, от заряда батарейки осталось [battery]\%."
    "Дальше пути нет. Похоже, это тупик."
    "Возвращаемся назад."
    $ path = 14
    $ passage = 3
    $ battery -= passage
    scene bg black with dissolve
    jump iw_maze_G

label iw_maze_exit:
    $ renpy.pause(passage)
    scene bg int_mine_door with dissolve
    "Вы нашли выход!"
    "Ура!"
    return
    
label iw_maze_youaredead:
    "Тусклый свет фонарика совсем померк."
    "Лампочка несколько раз моргнула и окончательно погасла."
    "Запасных батареек не было."
    "Вы попытались найти выход на ощупь, но ничего не получилось."
    "Это конец."
    jump iw_dayThree_maze
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    