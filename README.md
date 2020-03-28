# 2 plus 2 Equals 5

* [Description](#description)
* [Manual](#manual)
  * [Status Bar](#status-bar)
  * [Creating Shares](#creating-shares)
  * [Combining Shares](#combining-shares)
  * [Encryption Level](#encryption-level)
  * [GPG Presettings](#gpg-presettings)
    * [Public Key](#public-key)
    * [Signing Key](#signing-key)
  * [Best Practice](#best-practice)
  * [Wikipedia](#wikipedia)
  * [Languages](#languages)
  * [File Formats](#file-formats)
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

### Status Bar

The status bar is the bar on the botton of the GUI.
There will be the output for diagnostic and error messages.

### Creating Shares

To create shares from a file of your choice, first click on the "Create" tab and choose the file you want to split into shares with the Load button.

![Load File](https://github.com/Ned84/2plus2eq5/blob/master/Screenshots/twotwofive_load_file_GUI.png)

Choose the encryption level of your choice.
If you leave it on Default, the lowest possible encryption level will be chosen.
More information on the encryption level [here.](#encryption-level)

Increase or decrease the Minimum Shares and Total Shares as you wish.
The Total Shares are the amount of shares youll create in total.
The Minimum Shares are the amount of shares youll need at least to reconstruct your file e.g:

```If you want to split a secret into 10 parts but want to be able to reconstruct it from only 5 or more of this parts```
```the correct input would be:```

```Total shares: 10 ```

```Minimum Shares: 5```

When you are done choosing the above, you can start the share creation with the Start button.

If you chose to use GPG it will create a .asc file in the same directory as your chosen file with the signed, encrypted or signed/encrypted data.
More on how to enable GPG encryption/signing [here.](#gpg-presettings)

After the Shares are created the status bar will show "Shares successfully created".

The creation of the shares will create a folder in the same directory as your chosen file with the name "Shares".
In it you will find the shares and a Overview.txt which contains important information on how to reconstruct the file again.

**You should keep this file as safe as your shares and/or hand it out to people you want to be able to reconstruct it with their shares.**

After the creation is done, the File explorer will pop up and show you the newly created folder.


### Combining Shares
To combine the shares again you first need to check the Overview.txt you hopefully kept safely.
The important information written there are the encryption level used to create the shares (which we will use to combine them again), the minimum amount of shares you need to reconstruct and finally the original file name of the splitted file.

![Combine_GUI](https://github.com/Ned84/2plus2eq5/blob/master/Screenshots/twotwofive_Combine_Gui.png)

First click on the "Combine" tab and choose the Minimum Shares as written in the Overview.txt.

Next choose the shares for reconstruction with the Load button.
The amount of shares have to be at least as many as the minimum shares chosen.

![Load Shares](https://github.com/Ned84/2plus2eq5/blob/master/Screenshots/twotwofive_load_shares_GUI.png)

As you can see youre able to (and have to) choose multiple shares at once.
To be able to do this save all your shares in one location.

Next choose the encryption level as written in the Overview.txt.
More information on the encryption level [here.](#encryption-level)
If you choose another encryption level or less "minimum shares" than used to create the shares, it wont be able to reconstruct the file or the file will be broken.

When you are done to choose the settings as written in the Overview.txt and loaded your shares you are able to start the reconstruction with the Start button.

This will create a "Combined_Shares.txt" in the directory of your previously loaded shares.
If the reconstructed file is gpg encrypted it will create a "Combined_Shares.txt.asc".
More on how to enable GPG encryption/signing [here.](#gpg-presettings)

Next rename the file to the original filename written in the Overview.txt.

Voilà you reconstructed your file.


### Encryption Level

The encryption level is a Mersenne primenumber wich will be chosen on the size (bitlength) file you want to split into shares.
You are able to increase it but going lower than the minimum needed will break the splitted files.

Be aware that increasing the encryption level can dramasticly add to the time it will take to create the shares.
The time is dependent on the encryption level, the minimum shares chosen and the size of the file you want to split itself.
If you try to split a .zip with a many files inside, with a high encryption level and a high minimum shares needed it can take very long to create the shares (even if it will finish eventually).

The minimum available encryption level i chose to be 521 which should be sufficient for smaller files.


### GPG Presettings


#### Public Key


#### Signing Key

### Best Practice

### Wikipedia


### Languages
* English

### File Formats
* *.gpg
* *.zip
* *.7z
* *.asc
* *.txt


### Linux Versions

OnionSwitch is tested in **Ubuntu, Debian and Fedora**.

## Download

Download the newest release [here](https://github.com/Ned84/2plus2eq5/releases).

## Dependencies

### Windows

Newest Python from [here](https://www.python.org/downloads/).

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip install PyQt5```

Python-GnuPG from [here.](https://pypi.org/project/python-gnupg/)

```pip install python-gnupg```

Optional Pyinstaller. Infos are [here](https://www.pyinstaller.org/downloads.html).

```pip install pyinstaller```


### Linux

Newest Python from [here](https://www.python.org/downloads/).

PYQT5 information at [this link](https://pypi.org/project/PyQt5/).

```pip3 install PyQt5```

Python-GnuPG from [here.](https://pypi.org/project/python-gnupg/)

```pip3 install python-gnupg```


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

```pip install python-gnupg```


Use Pyinstaller from within the twotwofive_GUI folder.

```pyinstaller --windowed --icon=Icon/twotwofive_wo_bg.ico --clean --name TwoTwoFive twotwofive_GUI.py```

### Linux

#### Build .app GUI Version from .py

```pip3 install pyinstaller```

```pip3 install PyQt5```

```pip3 install python-gnupg```

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
