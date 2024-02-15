# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# enable powerlevel10k instant prompt. should stay close to the top of ~/.zshrc.
# initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${xdg_cache_home:-$home/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${xdg_cache_home:-$home/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme

source $ZSH/oh-my-zsh.sh

plugins=(git)

# to customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

autoload -Uz compinit; compinit

eval $(thefuck --alias)
export term=xterm-256color
export editor=nvim

alias k=kubectl
alias kx=kubectx
alias n=nvim
alias c=~/Coding
