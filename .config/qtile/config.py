from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

terminal = guess_terminal()

#------------------------------------------------------------------------------
# keymaps
mod = "mod4"
keys = [
    Key
    (
        [mod], "H",
        lazy.layout.left(),
        desc="shift focus left"
    ),
    Key
    (
        [mod], "L",
        lazy.layout.right(),
        desc="shift focus right"
    ),
    Key
    (
        [mod], "J",
        lazy.layout.down(),
        desc="shift focus down"
    ),
    Key
    (
        [mod], "K",
        lazy.layout.up(),
        desc="shift focus up"
    ),

    Key
    (
        [mod, "Shift"], "H",
        lazy.layout.shuffle_left(),
        desc="move focused window left"
    ),
    Key
    (
        [mod, "Shift"], "L",
        lazy.layout.shuffle_right(),
        desc="move focused window right"
    ),
    Key
    (
        [mod, "Shift"], "J",
        lazy.layout.shuffle_down(),
        desc="move focused window down"
    ),
    Key
    (
        [mod, "Shift"], "K",
        lazy.layout.shuffle_up(),
        desc="move focused window up"
    ),

    Key
    (
        [mod, "Control"], "H",
        lazy.layout.grow_left(),
        desc="grow focused window left"
    ),
    Key
    (
        [mod, "Control"], "L",
        lazy.layout.grow_right(),
        desc="grow focused window right"
    ),
    Key
    (
        [mod, "Control"], "J",
        lazy.layout.grow_down(),
        desc="grow focused window down"
    ),
    Key
    (
        [mod, "Control"], "K",
        lazy.layout.grow_up(),
        desc="grow focused window up"
    ),
    Key
    (
        [mod, "Shift"], "N",
        lazy.layout.normalize(),
        desc="reset all window sizes"
    ),

    Key
    (
        [mod, "Shift"], "Z",
        lazy.window.toggle_fullscreen(),
        desc="toggle fullscreen"
    ),

    Key
    (
        [mod, "Shift"], "F",
        lazy.window.toggle_floating(),
        desc="toggle floating mode"
    ),

    Key
    (
        [mod, "Control"], "R",
        lazy.reload_config(),
        desc="reload config"
    ),
    Key
    (
        [mod, "Control"], "Q",
        lazy.shutdown(),
        desc="shutdown Qtile"
    ),

    Key
    (
        [mod], "Q",
        lazy.window.kill(),
        desc="kill focused window"
    ),
    Key
    (
        [mod], "Space",
        lazy.spawn("rofi -show"),
        desc="spawn application launcher"
    ),
    Key
    (
        [mod], "W",
        lazy.spawn(terminal),
        desc="spawn terminal"
    ),
    Key
    (
        [mod], "P",
        lazy.spawn("flameshot gui"),
        desc="spawn screenshot utility"
    ),
    Key
    (
        [mod], "M",
        lazy.spawn(("{cmd} -e btop").format(cmd=terminal)),
        desc="spawn resource monitor"
    ),
    Key
    (
        [mod], "V",
        lazy.spawn(("{cmd} -e pulsemixer").format(cmd=terminal)),
        desc="spawn volume control"
    ),
    Key
    (
        [mod], "N",
        lazy.spawn(("{cmd} -e nmtui").format(cmd=terminal)),
        desc="spawn network manager"
    ),

    Key
    (
        [mod], "F1",
        lazy.spawn("pamixer -t"),
        desc="toggle mute output audio"
    ),
    Key
    (
        [mod], "F2",
        lazy.spawn("pamixer -d 1"),
        desc="decrease volume"
    ),
    Key
    (
        [mod], "F3",
        lazy.spawn("pamixer -i 1"),
        desc="increase volume"
    ),
    Key
    (
        [mod], "F4",
        lazy.spawn("pamixer --default-source -t"),
        desc="toggle mute input audio"
    ),
    Key
    (
        [mod], "F11",
        lazy.spawn("xbacklight -dec 10"),
        desc="decrease backlight"
    ),
    Key
    (
        [mod], "F12",
        lazy.spawn("xbacklight -inc 10"),
        desc="increase backlight"
    ),
]

def go_to_group(name):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return

        if name in "12345":
            qtile.focus_screen(0)
            qtile.groups_map[name].cmd_toscreen()
        elif name in "67890":
            qtile.focus_screen(1)
            qtile.groups_map[name].cmd_toscreen()

    return _inner

groups = [Group(i, label = "") for i in "1234567890"]
for i in groups:
    keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))
    keys.append(Key([mod, "Shift"], i.name, lazy.window.togroup(i.name)))

mouse = [
    Drag
    (
        [mod], "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag
    (
        [mod], "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click
    (
        [mod], "Button2",
        lazy.window.bring_to_front()
    ),
]

# -----------------------------------------------------------------------------
# layouts

border_normal_color="#"
border_focus_color="#"

layouts = [
    layout.Columns(
        border_normal=border_normal_color,
        border_focus=border_focus_color,
        border_width=0,
        margin=[5, 5, 5, 5]
    ),
    layout.Max(),
]

floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    border_normal=border_normal_color,
    border_focus=border_focus_color,
    border_width=0,
)

# -----------------------------------------------------------------------------
# screens & widgets

wallpaper_location="~/Desktop/Pictures/Wallpapers/"
wallpaper_1="CyborgWomanInYukata.png"
wallpaper_2="SkeletonEatingHeart.png"

brightness_location="/sys/class/backlight/intel_backlight/brightness"
max_brightness_location="/sys/class/backlight/intel_backlight/max_brightness"

groupbox_active_color="#ffffff"
groupbox_inactive_color="#6c7086"
active_group_color_1="#4fb1e5"
active_group_color_2="#e49ca8"

network_color="#3b093b"
brightness_color="#974230"
battery_color="#49232e"
battery_low_color="#ff0000"
volume_color="#385e4e"
time_color="#365e8c"

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen
    (
        wallpaper=("{location}{wallpaper}").format(location=wallpaper_location, wallpaper=wallpaper_1),
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox
                (
                    visible_groups=["1", "2", "3", "4", "5"],
                    active=groupbox_active_color,
                    inactive=groupbox_inactive_color,
                    highlight_method="text",
                    this_current_screen_border=active_group_color_1,
                    fontsize=18,
                    disable_drag=True,
                ),
                widget.Spacer
                (
                    length=bar.STRETCH,
                ),
                widget.Sep
                (
                    padding=10,
                    linewidth=0,
                ),
                widget.TextBox
                (
                    text="[BRI]",
                    background=brightness_color,
                ),
                widget.Backlight
                (
                    step=1,
                    brightness_file=brightness_location,
                    max_brightness_file=max_brightness_location,
                    background=brightness_color,
                ),
                widget.Sep
                (
                    padding=10,
                    linewidth=0,
                ),
                widget.TextBox
                (
                    text="[BAT]",
                    background=battery_color,
                ),
                widget.Battery
                (
                    battery=0,
                    format="{percent:0.0%}",
                    low_percentage=0.2,
                    low_foreground=battery_low_color,
                    update_interval=60.0,
                    background=battery_color,
                ),
                widget.Sep
                (
                    padding=10,
                    linewidth=0,
                ),
                widget.TextBox
                (
                    text="[VOL]",
                    background=volume_color,
                ),
                widget.PulseVolume
                (
                    step=1,
                    update_interval=0.01,
                    limit_max_volume=True,
                    background=volume_color,
                ),
                widget.Sep
                (
                    padding=10,
                    linewidth=0,
                ),
                widget.TextBox
                (
                    text="[DAT]",
                    background=time_color,
                ),
                widget.Clock
                (
                    format="%I:%M%p %a, %b %d",
                    update_interval=60.0,
                    background=time_color
                ),
            ],
            size=28,
            margin=[5, 5, 5, 5],
            background="#00000000",
        ),
    ),
    Screen
    (
        wallpaper=("{location}{wallpaper}").format(location=wallpaper_location, wallpaper=wallpaper_2),
        wallpaper_mode="stretch",
        top=bar.Bar(
            [
                widget.GroupBox
                (
                    visible_groups=["6", "7", "8", "9", "0"],
                    active=groupbox_active_color,
                    inactive=groupbox_inactive_color,
                    highlight_method="text",
                    this_current_screen_border=active_group_color_2,
                    fontsize=18,
                    disable_drag=True,
                ),
            ],
            size=28,
            margin=[5, 5, 5, 5],
            background="#00000000",
        ),
    ),
]

# -----------------------------------------------------------------------------
# options

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
