init:
#transitions
    $ dissolve5 = Dissolve(5.0)
    $ pixellate3 = Pixellate(3,4)
    
#noise effect
    $ config.layers = [ 'master', 'texture', 'transient', 'screens', 'overlay' ]
    image noise:
        "mods/iw/img/sfx/noise1.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/sfx/noise2.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/sfx/noise3.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/sfx/noise4.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/sfx/noise5.png" with Dissolve(0.2, alpha=True)
        0.05
        repeat
        
#клубящийся фон в прологе
    image drm_bg:
        "mods/iw/img/bg/ext_dream_prologue_0.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_1.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_2.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_3.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_4.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_5.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_6.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_7.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_8.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_9.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_10.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_11.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_12.png" with Dissolve(5.0, alpha=True)
        5.0
        "mods/iw/img/bg/ext_dream_prologue_13.png" with Dissolve(5.0, alpha=True)
        5.0
        repeat

#снегопад
    image snowblossom1 = SnowBlossom(Animation("mods/iw/img/sfx/snowflake0.png", 0.25, "mods/iw/img/sfx/snowflake1.png", 0.25, "mods/iw/img/sfx/snowflake2.png", 0.25), count=50, border=200, xspeed=(100, 150), yspeed=(100, 200), start=2, fast=True, horizontal=False)
    image snowblossom2 = SnowBlossom(Animation("mods/iw/img/sfx/snowflake3.png", 0.25, "mods/iw/img/sfx/snowflake4.png", 0.25, "mods/iw/img/sfx/snowflake5.png", 0.25), count=75, border=200, xspeed=(75, 125), yspeed=(50, 100), start=3, fast=True, horizontal=False)
    image snowblossom3 = SnowBlossom(Animation("mods/iw/img/sfx/snowflake6.png", 0.25, "mods/iw/img/sfx/snowflake7.png", 0.25, "mods/iw/img/sfx/snowflake8.png", 0.25), count=100, border=200, xspeed=(50, 100), yspeed=(25, 50), start=4, fast=True, horizontal=False)
    

    
#светлячки
    image fireflies0 = SnowBlossom("mods/iw/img/sfx/firefly0.png", count=15, border=50, xspeed=(30, 90), yspeed=(-50, -150), start=2, fast=False, horizontal=False)
    image fireflies1 = SnowBlossom("mods/iw/img/sfx/firefly1.png", count=15, border=50, xspeed=(30, 90), yspeed=(-37, -100), start=2, fast=False, horizontal=False)
    image fireflies2 = SnowBlossom("mods/iw/img/sfx/firefly2.png", count=15, border=50, xspeed=(25, 75), yspeed=(-27, -70), start=2, fast=False, horizontal=False)
    image fireflies3 = SnowBlossom("mods/iw/img/sfx/firefly3.png", count=15, border=50, xspeed=(20, 60), yspeed=(-16, -45), start=2, fast=False, horizontal=False)
    image fireflies4 = SnowBlossom("mods/iw/img/sfx/firefly4.png", count=30, border=50, xspeed=(15, 45), yspeed=(-8, -20), start=2, fast=False, horizontal=False)
    image fireflies5 = SnowBlossom("mods/iw/img/sfx/firefly5.png", count=30, border=50, xspeed=(10, 30), yspeed=(-2, -8), start=2, fast=False, horizontal=False)