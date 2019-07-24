# Windows Login Wallpaper Scraper
This simple python script illustrates exporting windows login wallpaper images.
It enforces certain requirements to filter out other content that exists in the same directory. Images are sorted for desktop and mobile devices.

**Requires Pillow (Python Imaging Library):** *(Used to get image dimensions)*
```
pip install Pillow
```
## Variables to edit
```
# Min size in bytes
minbytes = 100000
```
The minimum file size in bytes for a file to be copied

```
# Max days old
maxdays = 10
```
The maximum age of the file from today for the file to be copied

```
# Path to logon images
# Replace rob53 with your user folder name to fix the directory path.
imagespath = "C:\\Users\\rob53\\AppData\\Local\\Packages\\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\\LocalState\\Assets"
```
The path to the content. Replace "rob53" in the string to match your username. Check this in the Users folder.
