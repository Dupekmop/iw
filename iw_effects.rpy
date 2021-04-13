init:
#noise effect
    $ config.layers = [ 'master', 'texture', 'transient', 'screens', 'overlay' ]
    image noise:
        "mods/iw/img/i/noise1.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/i/noise2.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/i/noise3.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/i/noise4.png" with Dissolve(0.2, alpha=True)
        0.05
        "mods/iw/img/i/noise5.png" with Dissolve(0.2, alpha=True)
        0.05
        repeat