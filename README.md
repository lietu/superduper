# SuperDuper

Find dupes - duplicate files.

Requires: [Python 3.11+](https://www.python.org/downloads/)

Ensure you "Add python.exe to PATH" and then disable "App execution aliases" for Python in Windows settings.

Usage:

```shell
python superduper.py searchPath
```

So e.g.

```shell
python superduper.py "C:\"
```

Please keep in mind that this utility is simple and collects hashes of all your files in-memory before letting
you know the results. This means it is more than likely it will both 1) take a while to scan your drive's
contents to do the comparison, 2) consume a good bit of memory to remember all the unique hashes.

## License

The code is released under the BSD 3-Clause license. Details in the [LICENSE.md](./LICENSE.md) file.

# Financial support

This project has been made possible thanks to [Cocreators](https://cocreators.ee) and
[Lietu](https://lietu.net). You can help us continue our open source work by supporting us on
[Buy me a coffee](https://www.buymeacoffee.com/cocreators).

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/cocreators)
