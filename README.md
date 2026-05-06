# various scripts for Thai workflow in Robofont

Hi all, I have customized my Thai workflow in Robofont, and I recommend you do the same. So it's easier to follow through.

### install startup scripts:

* `contextual_filters.py` https://gist.github.com/frankrolf/07d09be24d22413e55ba2a9b4d12a2c8
* `ramsayController.py` https://gist.github.com/frankrolf/d15bf1d1dff97d455238100817e1833a

[How to set up a start up script](https://robofont.com/documentation/tutorials/setting-up-a-startup-script/)


### install RF extensions
Through Extension -> "Mechanic"

* RamsaySt
* Adjust Anchors
* Mark Feature Helper
* Mark Positioning tool


### install RF scripts

Put the whole `Thai Workshop` folder in your Robofont scripts directory.

Various scripts are contained:
* a script to clear anchors from selected glyphs (or current glyph)
* scripts to select Thai glyphs based on category
* scripts to drop approximate anchors per-category (in selected glyphs or current glyph). Please note: the anchors may need to be adjusted manually after dropping. Also, the scripts will not delete anchors for you, so make sure you take care of that first.


## manual intervention:

Change the Thai-specific BOR_HEIGHT variable in `modules/settings.py` to correspond to your specific setup.

## How to
In Thai, we need anchors in both consonant + tonemark. See more in [PDF explanation](https://www.dropbox.com/scl/fi/xdby9ucbn51j1ugky4x95/Thai-MarktoMark.pdf?rlkey=0ebf29qk8isn9gdfy9lotl7vy&dl=0) 

### Set up during the drawing process
1. Open “settings.py” Scripts -> Thai Workshop -> modules -> settings.py
2. Change the BOR_HEIGHT value, it’s the Thai height value 
3. To see/preview the position of the tonemark using plug-in : 
    1. Mark Positioning Tool 
    2. Adjust Anchors

Note: If No.2 is not set properly, the anchors will positioning wrongly, so please make sure to do this step.

### Set up for generating the font file
**Please make sure that the anchors were set on both consonant and tonemark. 
1. Open plug-in “mark feature helper” 
2. Click “Filter Eligible Glyphs” -> you will see the tonemark or / and diacritics show in the overall font view.
3. Then click “Build Group From Selection" -> this will create "COMBINING_MARKS" group
![Screenshot of Robofont's group view](https://github.com/boomwooq/Thai-Workshop/blob/main/images/CleanShot%202026-05-06%20at%2012.50.42%402x.png)


