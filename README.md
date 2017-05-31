# compare-mirrors

Compare-Mirrors is a program to compare package differences between Manjaro and Arch mirrors. It downloads the databases from the supplied mirrors, and then checks for package additions on the Arch mirror, and package upgrades


# Installation

To install compare-mirrors, clone it from the git and then run the installer. 
```
git clone https://github.com/joshuastrot/compare-mirrors.git
cd compare-mirrors
chmod +x install.sh
sudo bash install.sh
```


# Usage

To use compare-mirrors, simply open a terminal and run:
```
compare-mirrors -u
```
You can also dry-run it without redownloading the databases by running it with the `-c` flag.
```
compare-mirrors -c
```
If you would like to view packages added in Arch and not yet in Manjaro yet, use the `-a` flag.
```
compare-mirrors -u -a
```

## Configuration

If the mirrors in the configuration file are not fully synced yet, or not fast enough, you can configure them in the configuration file, located in `~/.compare-mirrors/compare-mirrors.conf`

You can also change which branch to compare to the Arch repositories. Currently this will only compare against the stable Arch branch, but the configuration setting will change which Manjaro branch is compared. 
