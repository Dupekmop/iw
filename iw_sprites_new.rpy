init -1000:
#РАСШИРЕНИЕ ВАНИЛЬНЫХ СПРАЙТОВ
#ВИОЛА

#НОВЫЕ СПРАЙТЫ
#ГЛАША
#normal
    image gl grin1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"))
    image gl surprise jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"))
    image gl scary jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"))
    image gl sad jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"))
    image gl shy1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"))
    image gl guilty jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"))
    image gl evilsmile1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"))
    image gl happy jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"))
    image gl laugh1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"))
    image gl smile1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"))
    image gl normal jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"))
    image gl serious jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"))
    image gl dontlike1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"))
    image gl angry1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"))
    image gl rage jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"))
    image gl anger jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"))
    image gl frust1 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"))
    image gl dontlike2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"))
    image gl evilsmile2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"))
    image gl grin2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"))
    image gl smile2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"))
    image gl shy2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"))
    image gl laugh2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"))
    image gl frust2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"))
    image gl angry2 jeans = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"))

#Добавление кошачьих ушек

    image gl grin1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/grin1.png"))
    image gl surprise jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/surprise.png"))
    image gl scary jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/scary.png"))
    image gl sad jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/sad.png"))
    image gl shy1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/shy1.png"))
    image gl guilty jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/guilty.png"))
    image gl evilsmile1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile1.png"))
    image gl happy jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/happy.png"))
    image gl laugh1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/laugh1.png"))
    image gl smile1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/smile1.png"))
    image gl normal jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/normal.png"))
    image gl serious jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/serious.png"))
    image gl dontlike1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike1.png"))
    image gl angry1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/angry1.png"))
    image gl rage jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/rage.png"))
    image gl anger jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/anger.png"))
    image gl frust1 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_1.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_1.png", (0, 0), "mods/iw/sprites/normal/gl/ears_1.png", (0, 0), "mods/iw/sprites/normal/gl/frust1.png"))
    image gl dontlike2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/dontlike2.png"))
    image gl evilsmile2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/evilsmile2.png"))
    image gl grin2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/grin2.png"))
    image gl smile2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/smile2.png"))
    image gl shy2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/shy2.png"))
    image gl laugh2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/laugh2.png"))
    image gl frust2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/frust2.png"))
    image gl angry2 jeans ears = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/gl/body_2.png", (0, 0), "mods/iw/sprites/normal/gl/jeans_2.png", (0, 0), "mods/iw/sprites/normal/gl/ears_2.png", (0, 0), "mods/iw/sprites/normal/gl/angry2.png"))

#far

    image gl grin1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"))
    image gl surprise jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"))
    image gl scary jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"))
    image gl sad jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"))
    image gl shy1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"))
    image gl guilty jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"))
    image gl evilsmile1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"))
    image gl happy jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"))
    image gl laugh1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"))
    image gl smile1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"))
    image gl normal jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"))
    image gl serious jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"))
    image gl dontlike1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"))
    image gl angry1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"))
    image gl rage jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"))
    image gl anger jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"))
    image gl frust1 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"))
    image gl dontlike2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"))
    image gl evilsmile2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"))
    image gl grin2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"))
    image gl smile2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"))
    image gl shy2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"))
    image gl laugh2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"))
    image gl frust2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"))
    image gl angry2 jeans far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"))

#Добавление кошачьих ушек


    image gl grin1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/grin1.png"))
    image gl surprise jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/surprise.png"))
    image gl scary jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/scary.png"))
    image gl sad jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/sad.png"))
    image gl shy1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/shy1.png"))
    image gl guilty jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/guilty.png"))
    image gl evilsmile1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile1.png"))
    image gl happy jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/happy.png"))
    image gl laugh1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/laugh1.png"))
    image gl smile1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/smile1.png"))
    image gl normal jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/normal.png"))
    image gl serious jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/serious.png"))
    image gl dontlike1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/dontlike1.png"))
    image gl angry1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/angry1.png"))
    image gl rage jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/rage.png"))
    image gl anger jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/anger.png"))
    image gl frust1 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_1.png", (0, 0), "mods/iw/sprites/far/gl/jeans_1.png", (0, 0), "mods/iw/sprites/far/gl/ears_1.png", (0, 0), "mods/iw/sprites/far/gl/frust1.png"))
    image gl dontlike2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/dontlike2.png"))
    image gl evilsmile2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/evilsmile2.png"))
    image gl grin2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/grin2.png"))
    image gl smile2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/smile2.png"))
    image gl shy2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/shy2.png"))
    image gl laugh2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/laugh2.png"))
    image gl frust2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/frust2.png"))
    image gl angry2 jeans ears far = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((675, 1080), (0, 0), "mods/iw/sprites/far/gl/body_2.png", (0, 0), "mods/iw/sprites/far/gl/jeans_2.png", (0, 0), "mods/iw/sprites/far/gl/ears_2.png", (0, 0), "mods/iw/sprites/far/gl/angry2.png"))

#close

    image gl grin1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"))
    image gl surprise jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"))
    image gl scary jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"))
    image gl sad jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"))
    image gl shy1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"))
    image gl guilty jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"))
    image gl evilsmile1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"))
    image gl happy jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"))
    image gl laugh1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"))
    image gl smile1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"))
    image gl normal jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"))
    image gl serious jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"))
    image gl dontlike1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"))
    image gl angry1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"))
    image gl rage jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"))
    image gl anger jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"))
    image gl frust1 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"))
    image gl dontlike2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"))
    image gl evilsmile2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"))
    image gl grin2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"))
    image gl smile2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"))
    image gl shy2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"))
    image gl laugh2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"))
    image gl frust2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"))
    image gl angry2 jeans close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"))

#Добавление кошачьих ушек

    image gl grin1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/grin1.png"))
    image gl surprise jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/surprise.png"))
    image gl scary jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/scary.png"))
    image gl sad jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/sad.png"))
    image gl shy1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/shy1.png"))
    image gl guilty jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/guilty.png"))
    image gl evilsmile1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile1.png"))
    image gl happy jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/happy.png"))
    image gl laugh1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/laugh1.png"))
    image gl smile1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/smile1.png"))
    image gl normal jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/normal.png"))
    image gl serious jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/serious.png"))
    image gl dontlike1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/dontlike1.png"))
    image gl angry1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/angry1.png"))
    image gl rage jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/rage.png"))
    image gl anger jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/anger.png"))
    image gl frust1 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_1.png", (0, 0), "mods/iw/sprites/close/gl/jeans_1.png", (0, 0), "mods/iw/sprites/close/gl/ears_1.png", (0, 0), "mods/iw/sprites/close/gl/frust1.png"))
    image gl dontlike2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/dontlike2.png"))
    image gl evilsmile2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/evilsmile2.png"))
    image gl grin2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/grin2.png"))
    image gl smile2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/smile2.png"))
    image gl shy2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/shy2.png"))
    image gl laugh2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/laugh2.png"))
    image gl frust2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/frust2.png"))
    image gl angry2 jeans ears close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/gl/body_2.png", (0, 0), "mods/iw/sprites/close/gl/jeans_2.png", (0, 0), "mods/iw/sprites/close/gl/ears_2.png", (0, 0), "mods/iw/sprites/close/gl/angry2.png"))









































