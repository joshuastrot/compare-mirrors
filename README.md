# compare-mirrors

Compare-Mirrors is a program to compare package differences between Manjaro and Arch mirrors. It downloads the databases from the supplied mirrors, and then checks for package changes between the mirrors.


# Installation

First, install the needed dependencies. 
```
sudo pacman -S libyaml
```
Then install compare-mirrors, clone it from the git and then run the installer. 
```
git clone https://github.com/joshuastrot/compare-mirrors.git
cd compare-mirrors
chmod +x install.sh
sudo bash install.sh
```


# Usage

To display the help for compare-mirrors, simply run it with no flags.
```
compare-mirrors
```
To use compare-mirrors, open a terminal and run:
```
compare-mirrors -u
```
You can also dry-run it without redownloading the databases by running it with the `-c` flag.
```
compare-mirrors -c
```
You can at any time clear the cache's as well with the `--clear` flag.
```
compare-mirrors --clear
```
or
```
compare-mirrors -u --clear
```
If you would like it to output in YAML format, then pass the -y flag as well.
```
compare-mirrors -y
```
You can capture the YAML format in a file, or pipe it into another program to process.
```
compare-mirrors -y > packages.yaml
```

## Configuration

There are many different configuration options in the config file. You can configure which mirrors to compare, which repositories to use, and which Manjaro branch to compare. The configuration file is by default located in `/usr/share/compare-mirrors/compare-mirrors.yaml`. To customize the settings, you can copy the configuration file to your `$XDG_CONFIG_HOME`, or `~/.config/compare-mirrors`.

```
mkdir -p ~/.config/compare-mirrors
cp /usr/share/compare-mirrors/compare-mirrors.yaml ~/.config/compare-mirrors
```

You can then edit it with the editor of your choice. You can, for example, comment out certain repositories that you do not wish to compare, change the branch, etc.
