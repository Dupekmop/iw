init -1000:
    $ normal = "mods/iw/sprites/normal/"
    $ far = "mods/iw/sprites/far/"
    $ close = "mods/iw/sprites/close/"
#РАСШИРЕНИЕ ВАНИЛЬНЫХ СПРАЙТОВ
#ВИОЛА

#НОВЫЕ СПРАЙТЫ
#ИСКИН
#normal
    image ai grin1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 shirt lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai surprise dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai scary dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai sad dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai shy1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai guilty dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai evilsmile1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai happy dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai laugh1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai smile1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai normal dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai serious dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai dontlike1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai angry1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai rage dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai anger dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai frust1 dress lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai grin1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai surprise kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai scary kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai sad kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai shy1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai guilty kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai evilsmile1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai happy kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai laugh1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai smile1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai normal kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai serious kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai dontlike1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai angry1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai rage kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai anger kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai frust1 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai grin1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai surprise uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai scary uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai sad uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai shy1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai guilty uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai evilsmile1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai happy uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai laugh1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai smile1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai normal uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai serious uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai dontlike1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai angry1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai rage uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai anger uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai frust1 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai grin1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai surprise uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai scary uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai sad uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai shy1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai guilty uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai evilsmile1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai happy uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai laugh1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai smile1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai normal uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai serious uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai angry1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai rage uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai anger uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai frust1 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1lng.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 jeans lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 pink lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 kimono lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 little2 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai evilsmile2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai grin2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai smile2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai shy2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai laugh2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai frust2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai angry2 little1 lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai dontlike2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai evilsmile2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai grin2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai smile2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai shy2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai laugh2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai frust2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai angry2 xmas lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai dontlike2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai evilsmile2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai grin2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai smile2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai shy2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai laugh2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai frust2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai angry2 uniformb lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai dontlike2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai evilsmile2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai grin2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai smile2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai shy2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai laugh2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai frust2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai angry2 uniformw lng = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2lng.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai grin1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 shirt srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai surprise dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai scary dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai sad dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai shy1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai guilty dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai evilsmile1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai happy dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai laugh1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai smile1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai normal dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai serious dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai dontlike1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai angry1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai rage dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai anger dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai frust1 dress srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai grin1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai surprise kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai scary kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai sad kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai shy1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai guilty kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai evilsmile1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai happy kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai laugh1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai smile1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai normal kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai serious kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai dontlike1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai angry1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai rage kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai anger kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai frust1 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai grin1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai surprise uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai scary uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai sad uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai shy1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai guilty uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai evilsmile1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai happy uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai laugh1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai smile1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai normal uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai serious uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai dontlike1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai angry1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai rage uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai anger uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai frust1 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai grin1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai surprise uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai scary uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai sad uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai shy1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai guilty uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai evilsmile1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai happy uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai laugh1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai smile1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai normal uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai serious uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai angry1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai rage uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai anger uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai frust1 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1srt.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 jeans srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 pink srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 kimono srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 little2 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai evilsmile2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai grin2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai smile2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai shy2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai laugh2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai frust2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai angry2 little1 srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai dontlike2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai evilsmile2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai grin2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai smile2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai shy2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai laugh2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai frust2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai angry2 xmas srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai dontlike2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai evilsmile2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai grin2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai smile2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai shy2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai laugh2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai frust2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai angry2 uniformb srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai dontlike2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai evilsmile2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai grin2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai smile2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai shy2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai laugh2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai frust2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai angry2 uniformw srt = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2srt.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai grin1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/jeans_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/pink_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little1_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/little2_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 shirt tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/shirt_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/grin1.png"))
    image ai surprise xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/surprise.png"))
    image ai scary xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/scary.png"))
    image ai sad xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/sad.png"))
    image ai shy1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/shy1.png"))
    image ai guilty xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/guilty.png"))
    image ai evilsmile1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/evilsmile1.png"))
    image ai happy xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/happy.png"))
    image ai laugh1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/laugh1.png"))
    image ai smile1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/smile1.png"))
    image ai normal xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/normal.png"))
    image ai serious xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/serious.png"))
    image ai dontlike1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/dontlike1.png"))
    image ai angry1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/angry1.png"))
    image ai rage xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/rage.png"))
    image ai anger xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/anger.png"))
    image ai frust1 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/xmas_1.png", (0, 0), normal+"ai/frust1.png"))
    image ai grin1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai surprise dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai scary dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai sad dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai shy1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai guilty dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai evilsmile1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai happy dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai laugh1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai smile1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai normal dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai serious dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai dontlike1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai angry1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai rage dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai anger dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai frust1 dress tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/dress_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_dress_1.png"))
    image ai grin1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai surprise kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai scary kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai sad kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai shy1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai guilty kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai evilsmile1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai happy kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai laugh1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai smile1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai normal kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai serious kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai dontlike1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai angry1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai rage kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai anger kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai frust1 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/kimono_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_kimono_1.png"))
    image ai grin1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai surprise uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai scary uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai sad uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai shy1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai guilty uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai evilsmile1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai happy uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai laugh1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai smile1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai normal uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai serious uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai dontlike1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai angry1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai rage uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai anger uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai frust1 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformb_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_ub_1.png"))
    image ai grin1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/grin1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai surprise uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/surprise.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai scary uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/scary.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai sad uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/sad.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai shy1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/shy1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai guilty uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/guilty.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai evilsmile1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/evilsmile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai happy uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/happy.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai laugh1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/laugh1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai smile1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/smile1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai normal uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/normal.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai serious uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/serious.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/dontlike1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai angry1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/angry1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai rage uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/rage.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai anger uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/anger.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai frust1 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_1tal.png", (0, 0), normal+"ai/uniformw_1.png", (0, 0), normal+"ai/frust1.png", (0, 0), normal+"ai/acs_uw_1.png"))
    image ai dontlike2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 jeans tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/jeans_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 pink tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/pink_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 kimono tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/kimono_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/dontlike2.png"))
    image ai evilsmile2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/evilsmile2.png"))
    image ai grin2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/grin2.png"))
    image ai smile2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/smile2.png"))
    image ai shy2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/shy2.png"))
    image ai laugh2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/laugh2.png"))
    image ai frust2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/frust2.png"))
    image ai angry2 little2 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little2_2.png", (0, 0), normal+"ai/angry2.png"))
    image ai dontlike2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai evilsmile2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai grin2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai smile2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai shy2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai laugh2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai frust2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai angry2 little1 tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/little1_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_little_2.png"))
    image ai dontlike2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai evilsmile2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai grin2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai smile2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai shy2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai laugh2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai frust2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai angry2 xmas tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/xmas_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_xmas_2.png"))
    image ai dontlike2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai evilsmile2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai grin2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai smile2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai shy2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai laugh2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai frust2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai angry2 uniformb tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformb_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_ub_2.png"))
    image ai dontlike2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/dontlike2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai evilsmile2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/evilsmile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai grin2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/grin2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai smile2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/smile2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai shy2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/shy2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai laugh2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/laugh2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai frust2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/frust2.png", (0, 0), normal+"ai/acs_uw_2.png"))
    image ai angry2 uniformw tal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"), im.matrix.tint(0.78, 0.93, 0.97)),
        True, im.Composite((900, 1080), (0, 0), normal+"ai/body_2tal.png", (0, 0), normal+"ai/uniformw_2.png", (0, 0), normal+"ai/angry2.png", (0, 0), normal+"ai/acs_uw_2.png"))

#ГЛАША
# normal
    image gl grin1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png"))
    image gl surprise = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png"))
    image gl scary = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png"))
    image gl sad = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png"))
    image gl shy1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png"))
    image gl guilty = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png"))
    image gl evilsmile1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png"))
    image gl happy = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png"))
    image gl laugh1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png"))
    image gl smile1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png"))
    image gl normal = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png"))
    image gl serious = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png"))
    image gl dontlike1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png"))
    image gl angry1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png"))
    image gl rage = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png"))
    image gl anger = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png"))
    image gl frust1 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png"))
    image gl dontlike2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png"))
    image gl evilsmile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png"))
    image gl grin2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png"))
    image gl smile2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png"))
    image gl shy2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png"))
    image gl laugh2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png"))
    image gl frust2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png"))
    image gl angry2 = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png"))
    image gl grin1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/grin1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl surprise ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/surprise.png", (0, 0), normal+"gl/ears_1.png"))
    image gl scary ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/scary.png", (0, 0), normal+"gl/ears_1.png"))
    image gl sad ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/sad.png", (0, 0), normal+"gl/ears_1.png"))
    image gl shy1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/shy1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl guilty ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/guilty.png", (0, 0), normal+"gl/ears_1.png"))
    image gl evilsmile1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/evilsmile1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl happy ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/happy.png", (0, 0), normal+"gl/ears_1.png"))
    image gl laugh1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/laugh1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl smile1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/smile1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl normal ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/normal.png", (0, 0), normal+"gl/ears_1.png"))
    image gl serious ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/serious.png", (0, 0), normal+"gl/ears_1.png"))
    image gl dontlike1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/dontlike1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl angry1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/angry1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl rage ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/rage.png", (0, 0), normal+"gl/ears_1.png"))
    image gl anger ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/anger.png", (0, 0), normal+"gl/ears_1.png"))
    image gl frust1 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png", (0, 0), normal+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_1.png", (0, 0), normal+"gl/jeans_1.png", (0, 0), normal+"gl/frust1.png", (0, 0), normal+"gl/ears_1.png"))
    image gl dontlike2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/dontlike2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl evilsmile2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/evilsmile2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl grin2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/grin2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl smile2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/smile2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl shy2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/shy2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl laugh2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/laugh2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl frust2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/frust2.png", (0, 0), normal+"gl/ears_2.png"))
    image gl angry2 ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png", (0, 0), normal+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), normal+"gl/body_2.png", (0, 0), normal+"gl/jeans_2.png", (0, 0), normal+"gl/angry2.png", (0, 0), normal+"gl/ears_2.png"))

# far
    image gl grin1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png"))
    image gl surprise far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png"))
    image gl scary far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png"))
    image gl sad far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png"))
    image gl shy1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png"))
    image gl guilty far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png"))
    image gl evilsmile1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png"))
    image gl happy far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png"))
    image gl laugh1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png"))
    image gl smile1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png"))
    image gl normal far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png"))
    image gl serious far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png"))
    image gl dontlike1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png"))
    image gl angry1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png"))
    image gl rage far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png"))
    image gl anger far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png"))
    image gl frust1 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png"))
    image gl dontlike2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png"))
    image gl evilsmile2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png"))
    image gl grin2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png"))
    image gl smile2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png"))
    image gl shy2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png"))
    image gl laugh2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png"))
    image gl frust2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png"))
    image gl angry2 far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png"))
    image gl grin1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/grin1.png", (0, 0), far+"gl/ears_1.png"))
    image gl surprise ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/surprise.png", (0, 0), far+"gl/ears_1.png"))
    image gl scary ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/scary.png", (0, 0), far+"gl/ears_1.png"))
    image gl sad ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/sad.png", (0, 0), far+"gl/ears_1.png"))
    image gl shy1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/shy1.png", (0, 0), far+"gl/ears_1.png"))
    image gl guilty ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/guilty.png", (0, 0), far+"gl/ears_1.png"))
    image gl evilsmile1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/evilsmile1.png", (0, 0), far+"gl/ears_1.png"))
    image gl happy ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/happy.png", (0, 0), far+"gl/ears_1.png"))
    image gl laugh1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/laugh1.png", (0, 0), far+"gl/ears_1.png"))
    image gl smile1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/smile1.png", (0, 0), far+"gl/ears_1.png"))
    image gl normal ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/normal.png", (0, 0), far+"gl/ears_1.png"))
    image gl serious ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/serious.png", (0, 0), far+"gl/ears_1.png"))
    image gl dontlike1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/dontlike1.png", (0, 0), far+"gl/ears_1.png"))
    image gl angry1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/angry1.png", (0, 0), far+"gl/ears_1.png"))
    image gl rage ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/rage.png", (0, 0), far+"gl/ears_1.png"))
    image gl anger ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/anger.png", (0, 0), far+"gl/ears_1.png"))
    image gl frust1 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png", (0, 0), far+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_1.png", (0, 0), far+"gl/jeans_1.png", (0, 0), far+"gl/frust1.png", (0, 0), far+"gl/ears_1.png"))
    image gl dontlike2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/dontlike2.png", (0, 0), far+"gl/ears_2.png"))
    image gl evilsmile2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/evilsmile2.png", (0, 0), far+"gl/ears_2.png"))
    image gl grin2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/grin2.png", (0, 0), far+"gl/ears_2.png"))
    image gl smile2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/smile2.png", (0, 0), far+"gl/ears_2.png"))
    image gl shy2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/shy2.png", (0, 0), far+"gl/ears_2.png"))
    image gl laugh2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/laugh2.png", (0, 0), far+"gl/ears_2.png"))
    image gl frust2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/frust2.png", (0, 0), far+"gl/ears_2.png"))
    image gl angry2 ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png", (0, 0), far+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), far+"gl/body_2.png", (0, 0), far+"gl/jeans_2.png", (0, 0), far+"gl/angry2.png", (0, 0), far+"gl/ears_2.png"))

# close
    image gl grin1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png"))
    image gl surprise close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png"))
    image gl scary close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png"))
    image gl sad close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png"))
    image gl shy1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png"))
    image gl guilty close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png"))
    image gl evilsmile1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png"))
    image gl happy close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png"))
    image gl laugh1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png"))
    image gl smile1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png"))
    image gl normal close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png"))
    image gl serious close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png"))
    image gl dontlike1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png"))
    image gl angry1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png"))
    image gl rage close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png"))
    image gl anger close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png"))
    image gl frust1 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png"))
    image gl grin1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/grin1.png", (0, 0), close+"gl/ears_1.png"))
    image gl surprise ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/surprise.png", (0, 0), close+"gl/ears_1.png"))
    image gl scary ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/scary.png", (0, 0), close+"gl/ears_1.png"))
    image gl sad ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/sad.png", (0, 0), close+"gl/ears_1.png"))
    image gl shy1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/shy1.png", (0, 0), close+"gl/ears_1.png"))
    image gl guilty ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/guilty.png", (0, 0), close+"gl/ears_1.png"))
    image gl evilsmile1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/evilsmile1.png", (0, 0), close+"gl/ears_1.png"))
    image gl happy ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/happy.png", (0, 0), close+"gl/ears_1.png"))
    image gl laugh1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/laugh1.png", (0, 0), close+"gl/ears_1.png"))
    image gl smile1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/smile1.png", (0, 0), close+"gl/ears_1.png"))
    image gl normal ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/normal.png", (0, 0), close+"gl/ears_1.png"))
    image gl serious ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/serious.png", (0, 0), close+"gl/ears_1.png"))
    image gl dontlike1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/dontlike1.png", (0, 0), close+"gl/ears_1.png"))
    image gl angry1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/angry1.png", (0, 0), close+"gl/ears_1.png"))
    image gl rage ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/rage.png", (0, 0), close+"gl/ears_1.png"))
    image gl anger ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/anger.png", (0, 0), close+"gl/ears_1.png"))
    image gl frust1 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png", (0, 0), close+"gl/ears_1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_1.png", (0, 0), close+"gl/jeans_1.png", (0, 0), close+"gl/frust1.png", (0, 0), close+"gl/ears_1.png"))
    image gl dontlike2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png"))
    image gl evilsmile2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png"))
    image gl grin2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png"))
    image gl smile2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png"))
    image gl shy2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png"))
    image gl laugh2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png"))
    image gl frust2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png"))
    image gl angry2 close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png"))
    image gl dontlike2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/dontlike2.png", (0, 0), close+"gl/ears_2.png"))
    image gl evilsmile2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/evilsmile2.png", (0, 0), close+"gl/ears_2.png"))
    image gl grin2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/grin2.png", (0, 0), close+"gl/ears_2.png"))
    image gl smile2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/smile2.png", (0, 0), close+"gl/ears_2.png"))
    image gl shy2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/shy2.png", (0, 0), close+"gl/ears_2.png"))
    image gl laugh2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/laugh2.png", (0, 0), close+"gl/ears_2.png"))
    image gl frust2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/frust2.png", (0, 0), close+"gl/ears_2.png"))
    image gl angry2 ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png", (0, 0), close+"gl/ears_2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), close+"gl/body_2.png", (0, 0), close+"gl/jeans_2.png", (0, 0), close+"gl/angry2.png", (0, 0), close+"gl/ears_2.png"))









































