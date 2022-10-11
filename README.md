# UnpackOSZ
![UnpackOSZ](https://cdn-icons-png.flaticon.com/512/5132/5132856.png)
A simple decompressor for .osz files (OSU)

# Why Use?
> If you want to get some data from Chart, like: `Music`, `Images` and etc, just run the code and it will unpack everything for you.

# How to Use
> To use it is very simple, you will put the code in your project and then you will import it:
**Example**
```py
from unpackosz import unpack
```
> To unpack, just inform the path where your .osz file is.
```py
unpack("Bad Apple") # In (Bad Apple) obviously put your .osz file name
```
> **Warning**<br/>
> You don't need to put the file format at the end, for example: `Example.osz`, just put the name of the file: `Example` and obviously the path where it is located.

## Parameters (Optionals)
- **Create Folder**: By default it comes as true, which as the name suggests, will create a folder to add the assets of the chart, very good for organizing.

- **Prevent File**: By default it also comes true, what this does is create a copy of the file and then extract it, after all it will delete and leave the original file intact with no changes. If disabled, the original file will be deleted.
