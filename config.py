import os
import subprocess

from libqtile import bar, hook, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

from key_bindings import keys
from screen_widgets import screen_widgets

MOD = "MOD4"

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

wmname = "LG3D"


# Keybindings
def keybinding(*args):
    """Keybindings --> key_bindings.py"""
    bindings = args

    return bindings


def init_groups():
    """Initialize & name groups"""
    group = [Group(i) for i in "123456789"]
    return group


# Cycle/swap through screens
for i in init_groups():
    keys.extend(
        [
            # MOD + group number = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"switch to group {i.name}",
            ),
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                desc=f"move window to group {i.name}",
            ),
        ]
    )


def init_layouts():
    """List of layouts"""
    lay_outs = [
        layout.MonadTall(
            border_focus=["#DCAE96", "#2f1111"],
            border_width=1,
            border_normal="#222224",
            margin=4,
        ),
    ]
    return lay_outs


def init_screens(*args):
    """Initialize bar/wdigets"""

    current_screen = [
        Screen(
            top=bar.Bar(
                [*args],
                24,
                border_width=[0, 0, 0, 0],
                border_color=["#DCAE96", "#DCAE96", "#DCAE96", "#DCAE96"],
                background="#FFFFFF00",
            ),
        ),
    ]
    return current_screen


def init_mouse():
    """Mouse Drag Options"""
    imouse = [
        Drag(
            [MOD],
            "Button1",
            lazy.window.set_position_floating(),
            start=lazy.window.get_position(),
        ),
        Drag(
            [MOD],
            "Button3",
            lazy.window.set_size_floating(),
            start=lazy.window.get_size(),
        ),
        Click([MOD], "Button2", lazy.window.bring_to_front()),
    ]

    return imouse


@hook.subscribe.startup_once
def autostart():
    """Run start up script picom/wallpaper"""
    home = os.path.expanduser("~/.config/qtile/scripts/auto_start.sh")
    subprocess.Popen([home])


def floating():

    floating_layout = layout.Floating(
        float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class="confirmreset"),  # gitk
            Match(wm_class="makebranch"),  # gitk
            Match(wm_class="maketag"),  # gitk
            Match(wm_class="ssh-askpass"),  # ssh-askpass
            Match(title="branchdialog"),  # gitk
            Match(title="pinentry"),  # GPG key password entry
        ]
    )
    return floating_layout


if __name__ in ["config", "__main__"]:
    keys = keybinding(*keys)
    groups = init_groups()
    layouts = init_layouts()
    screens = init_screens(*screen_widgets)
    mouse = init_mouse()
    floating_layout = floating()
