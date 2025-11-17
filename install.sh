#!/bin/bash
mkdir ~/.local/share/pybuild
cp -r * ~/.local/share/pybuild

chmod +x ~/.local/share/pybuild/main

echo "alias pybuild='~/.local/share/pybuild/main'" >> ~/.zshrc
echo "alias pybuild='~/.local/share/pybuild/main'" >> ~/.bashrc
