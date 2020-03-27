# OnionSwitch

* [Description](#description)
* [Manual](#manual)
  * [Creating Shares](#creating-shares)
  * [Combining Shares](#combining-shares)
  * [GPG Presettings](#gpg-presettings)
    * [Public Key](#public-key)
    * [Signing Key](#signing-key)
  * [Wikipedia](#wikipedia)
  * [Languages](#languages)
  * [Linux Versions](#linux-versions)
* [Download](#download)
* [Dependencies](#dependencies)
  * [Windows](#windows)
  * [Linux](#linux)
* [License](#license)
* [Install](#install)
  * [Windows](#windows)
    * [Build executable GUI Version from .py](#build-executable-gui-version-from-py)
  * [Linux](#linux)
    * [Build .app GUI Version from .py](#build-app-gui-version-from-py)
* [Support](#support)
* [Verify Signatures](#verify-signatures)
  * [Windows](#windows)
  * [Linux](#linux)
* [Get my Public Key](#get-my-public-key)

## Description

Easily share secrets in parts and reconstruct them again from
an minimum amount of parts.
GUI Copyright (C) 2020  Ned84 ned84@protonmail.com
The Shares are created using Shamir's Secret Sharing Scheme.
Optional it is possible to use GPG encryption and signing.
For further information on Shamirs Secret Sharing visit:
https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

## Manual



### Creating Shares


### Combining Shares


### GPG Presettings


#### Public Key


#### Signing Key

### Wikipedia


### Languages
* English


### Linux Versions

OnionSwitch is tested in **Ubuntu, Debian and Fedora**.

## Download

Download the newest release [here](https://github.com/Ned84/2plus2eq5/releases).

## Dependencies

### Windows

Newest Python from [here](https://www.python.org/downloads/).

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip install PyQt5```

Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

```pip install pyinstaller```


### Linux

Newest Python from [here](https://www.python.org/downloads/).

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip3 install PyQt5```


Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

```pip3 install pyinstaller```

## License

>Copyright (C) 2020  Ned84 ned84@protonmail.com
>This program is free software: you can redistribute it and/or modify
>it under the terms of the GNU General Public License as published by
>the Free Software Foundation, either version 3 of the License, or
>(at your option) any later version.
>This program is distributed in the hope that it will be useful,
>but WITHOUT ANY WARRANTY; without even the implied warranty of
>MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
>GNU General Public License for more details.
>You should have received a copy of the GNU General Public License
>along with this program.  If not, see <https://www.gnu.org/licenses/>.

## Install

### Windows

#### Build executable GUI Version from .py

```pip install pyinstaller```

```pip install PyQt5```


Use Pyinstaller from within the twotwofive_GUI folder.

```pyinstaller --windowed --icon=Icon/twotwofive_wo_bg.ico --clean --name TwoTwoFive twotwofive_GUI.py```

### Linux

#### Build .app GUI Version from .py

```pip3 install pyinstaller```

```pip3 install PyQt5```

```pip3 install Stem```

```pip3 install tor```

```pyinstaller --windowed --icon=Icon/twotwofive_wo_bg.ico --clean --name TwoTwoFive.app twotwofive_GUI.py```

## Support

If you require help or if you have suggestions please refer to the [Issue section](https://github.com/Ned84/2plus2eq5/issues).

## Verify Signatures

### Windows

Download the sha256sum.txt and the .asc for your TwoTwoFive version.

#### Basic checksum verification

In Powershell:

```(Get-FileHash .\TwoTwoFive*.*_setup.exe).Hash -eq (Get-Content .\sha256sum.txt).split(" ")[0].ToUpper()```

should show:

```True```

#### Signature verification

The programm is signed with my signature which windows checks when you run the TwoTwoFive setup.

It should state **"Open Source Developer, Rene Mario Baumgartner"** as Verified Publisher.

### Linux

Download the sha256sum.txt and the .asc for your TwoTwoFive version.

#### Basic checksum verification:

```shasum -a 256 -c sha256sum.txt```

should show:

```TwoTwoFive_V*.*.tar.xz: OK```

#### GPG verification

```curl https://keybase.io/ned84/pgp_keys.asc | gpg --import```

and verify with:

```gpg --verify TwoTwoFive_V*.*.tar.xz.asc```

should show:

```Good signature from "Ned84 <ned84@protonmail.com>"```

## Get my Public Key

Get my public key at [Keybase](https://keybase.io/ned84).
