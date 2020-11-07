# literotica_dl
A tool to download stories from Literotica.

# Installation
I highly recommend you use pipx
```sh
pipx install literotica_dl
```
otherwise you can use pip
```sh
pipx install literotica_dl
```
PyPI: https://github.com/fuzzyfiend/literotica_dl

# Details
You must specify whether to download stories (-s) or author works (-a).
* Stories are identified as the url stub following the /s/ directory in the url
    * https://www.literotica.com/s/a-my-name-is-alice
    * story flag is a-my-name-is-alice
* Authors are identified as the memberuid
    * https://www.literotica.com/stories/memberpage.php?uid=36374
    * author flag is 36374

This program will attempt to resolve the author uid or story id for you.
By default this program will write stories to a new folder called output. This can be overridden by specifying the -o flag.

# Examples
```sh
# Downloading an authors works via the author stub
literotica_dl -a 36374

# Downloading an authors works via member url
literotica_dl -a "https://www.literotica.com/stories/memberpage.php?uid=36374"

# Downloading an story via the story stub
literotica_dl -s a-my-name-is-alice

# Downloading an story via the story stub
literotica_dl -s "https://www.literotica.com/s/a-my-name-is-alice"

# Mirroring the author to a specific directory
literotica_dl -a "https://www.literotica.com/stories/memberpage.php?uid=36374" -o "archive"
```

# Credits

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [fuzzyfiend/pythoncookie](https://github.com/fuzzyfiend/pythoncookie) project template.
