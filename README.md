# Uzumaki Transform

A python program that uses computer vision techniques to change an image into a swirling gif that resembles the Uzumaki manga by Junji Ito

### Screenshots

<p align="center">
  <img src="https://github.com/connorjchen/uzumaki_transform/blob/master/background_removal/data/connorScared.jpg" width="500" />
  <img src="https://github.com/connorjchen/uzumaki_transform/blob/master/background_removal/data/connorScared_out_swirl.gif" width="500" />
</p>

## Note

Program and README was created for MacBook Pro M1 Ventura 13.1

## Code Reference

- https://github.com/pythonlessons/background_removal
- https://stackoverflow.com/questions/74977491/how-can-i-apply-effects-like-a-swirl-to-a-webcam-stream-using-python-and-opencv

## How to Get Setup

1. Install pyenv

   1. brew install pyenv
   2. nano ~/.zshrc
   3. Copy paste at bottom of .zshrc
      ```
      export PYENV_ROOT="$HOME/.pyenv"
      command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
      eval "$(pyenv init -)"
      ```
   4. Reload terminal

2. pyenv install 3.11.0

3. sh setup.sh

## How to Run

1. sh run_main.sh
