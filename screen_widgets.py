from libqtile import widget

FOREGROUND = "#f7fbfe"
ROSE = " இڿڰۣ-ڰۣ—{}"
ROSE_COL = "#6c2e2c"

screen_widgets = [
    widget.GroupBox(
        active="#6c2e2c",
        block_highlight_text_color="#E9EAEC",
        highlight_method="border",
        highlight_color="#fcbb6c",
        this_current_screen_border="#DCAE96",
        borderwidth=1,
    ),
    widget.Prompt(),
    widget.WindowName(foreground=FOREGROUND),
    widget.Chord(
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Systray(),
    widget.CPU(foreground=FOREGROUND),
    widget.ThermalZone(),
    widget.Image(
        filename=r"/home/denny/.config/qtile/icons/rose.png",
        scale="True",
        background=FOREGROUND,
    ),
    widget.TextBox(fmt=ROSE, foreground=ROSE_COL),
    widget.Memory(foreground=FOREGROUND),
    widget.TextBox(fmt=ROSE, foreground=ROSE_COL),
    widget.NvidiaSensors(foreground=FOREGROUND, fmt="GPU: {}"),
    widget.TextBox(fmt=ROSE, foreground=ROSE_COL),
    widget.Clock(foreground=FOREGROUND, format="%Y-%m-%d %a %I:%M %p"),
]
