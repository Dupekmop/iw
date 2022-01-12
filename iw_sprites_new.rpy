init -1000:
#РАСШИРЕНИЕ ВАНИЛЬНЫХ СПРАЙТОВ
#ВИОЛА

#НОВЫЕ СПРАЙТЫ
#АНТОНИНА
#normal
    image ri bored dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_bored.png"))
    image ri bored everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_bored.png"))
    image ri bored sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_bored.png"))
    image ri bored swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_bored.png"))
    image ri bored top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_bored.png"))
    image ri smile2 dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile2.png"))
    image ri smile2 everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile2.png"))
    image ri smile2 sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile2.png"))
    image ri smile2 swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile2.png"))
    image ri smile2 top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile2.png"))
    image ri sad dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_sad.png"))
    image ri sad everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_sad.png"))
    image ri sad sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_sad.png"))
    image ri sad swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_sad.png"))
    image ri sad top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_sad.png"))
    image ri smile dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_smile.png"))
    image ri smile everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_smile.png"))
    image ri smile sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_smile.png"))
    image ri smile swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_smile.png"))
    image ri smile top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_smile.png"))
    image ri dontlike dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_dontlike.png"))
    image ri dontlike everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_dontlike.png"))
    image ri dontlike sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_dontlike.png"))
    image ri dontlike swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_dontlike.png"))
    image ri dontlike top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_dontlike.png"))
    image ri pensive dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_pensive.png"))
    image ri pensive everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_pensive.png"))
    image ri pensive sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_pensive.png"))
    image ri pensive swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_pensive.png"))
    image ri pensive top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_pensive.png"))
    image ri surprise dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_surprise.png"))
    image ri surprise everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_surprise.png"))
    image ri surprise sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_surprise.png"))
    image ri surprise swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_surprise.png"))
    image ri surprise top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_surprise.png"))
    image ri angry dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_angry.png"))
    image ri angry everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_angry.png"))
    image ri angry sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_angry.png"))
    image ri angry swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_angry.png"))
    image ri angry top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_angry.png"))
    image ri nope dress = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_dress_nope.png"))
    image ri nope everyday = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_everyday_nope.png"))
    image ri nope sport = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_sport_nope.png"))
    image ri nope swim = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_swim_nope.png"))
    image ri nope top = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((900, 1080), (0, 0), "mods/iw/sprites/normal/ri/ri_top_nope.png"))

#close

    image ri bored dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"))
    image ri bored everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"))
    image ri bored sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"))
    image ri bored swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"))
    image ri bored top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_bored.png"))
    image ri smile2 dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"))
    image ri smile2 everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"))
    image ri smile2 sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"))
    image ri smile2 swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"))
    image ri smile2 top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile2.png"))
    image ri sad dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"))
    image ri sad everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"))
    image ri sad sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"))
    image ri sad swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"))
    image ri sad top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_sad.png"))
    image ri smile dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"))
    image ri smile everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"))
    image ri smile sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"))
    image ri smile swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"))
    image ri smile top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_smile.png"))
    image ri dontlike dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"))
    image ri dontlike everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"))
    image ri dontlike sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"))
    image ri dontlike swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"))
    image ri dontlike top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_dontlike.png"))
    image ri pensive dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"))
    image ri pensive everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"))
    image ri pensive sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"))
    image ri pensive swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"))
    image ri pensive top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_pensive.png"))
    image ri surprise dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"))
    image ri surprise everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"))
    image ri surprise sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"))
    image ri surprise swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"))
    image ri surprise top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_surprise.png"))
    image ri angry dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"))
    image ri angry everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"))
    image ri angry sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"))
    image ri angry swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"))
    image ri angry top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_angry.png"))
    image ri nope dress close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_dress.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"))
    image ri nope everyday close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_everyday.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"))
    image ri nope sport close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_sport.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"))
    image ri nope swim close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_swim.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"))
    image ri nope top close = ConditionSwitch(
        "persistent.sprite_time == 'sunset'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.94, 0.82, 1.0)),
        "persistent.sprite_time == 'night'", im.MatrixColor(im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"), im.matrix.tint(0.63, 0.78, 0.82)),
        True, im.Composite((1125, 1080), (0, 0), "mods/iw/sprites/close/ri/ri_top.png", (0, 0), "mods/iw/sprites/close/ri/ri_nope.png"))

