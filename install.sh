#!/bin/bash
mkdir ~/.local/share/pybuild
cp -r * ~/.local/share/pybuild

echo "alias pybuild='python3 ~/.local/share/pybuild/builder.py'" >> ~/.zshrc
echo "alias pybuild='python3 ~/.local/share/pybuild/builder.py'" >> ~/.bashrc