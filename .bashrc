[[ $- != *i* ]] && return

# alias ls='ls -lhvAF --color=auto'
alias ls='exa -lag --group-directories-first --time=changed --time-style=long-iso --color=auto --icons --git'
alias ls-tree='exa -laTg --level=3 --group-directories-first --time=changed --time-style=long-iso --color=auto --icons --git'

PS1='[\w] '
