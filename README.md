important pacman commands
  * pacman -Syu [package]
    * sync the repo and install package
  * pacman -Rns [package]
    * removes a package and all unused dependancies
  * pacman -Qm
    * list all installed packages not found in the official repo

[programs]
  * acplight (laptop backlight control)
    * in ~/.config/qtile/config.py, change brightness_location & max_brightness_location to the locations of brightness files on your local machine
    * add your user to the video group: groupadd ${USER}
  * alacritty (terminal emulator)
  * btop (resource monitor)
  * pamixer & pulsemixer (volume control)
  * xorg-xinit (starts xorg)
  * qtile (window manager)
  * picom (compositor)
  * rofi (application launcer)
  * neovim (text editor)

[configurations]
  * localectl set-x11-keymap us '' '' caps:swapescape
    * swaps capslock and escape
