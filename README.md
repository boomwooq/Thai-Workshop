# various scripts for Thai workflow in Robofont

Hi all, I have customized my Thai workflow in Robofont, and I recommend you do the same. So it's easier to follow through.

### install startup scripts:

* `contextual_filters.py` https://gist.github.com/frankrolf/07d09be24d22413e55ba2a9b4d12a2c8
* `ramsayController.py` https://gist.github.com/frankrolf/d15bf1d1dff97d455238100817e1833a


### install RF extensions

* RamsaySt
* Adjust Anchors
* Mark Feature Helper


### install RF scripts

Put the whole `Thai Workshop` folder in your Robofont scripts directory.

Various scripts are contained:
* a script to clear anchors from selected glyphs (or current glyph)
* scripts to select Thai glyphs based on category
* scripts to drop approximate anchors per-category (in selected glyphs or current glyph). Please note: the anchors may need to be adjusted manually after dropping. Also, the scripts will not delete anchors for you, so make sure you take care of that first.


## manual intervention:

Change the Thai-specific BOR_HEIGHT variable in `modules/settings.py` to correspond to your specific setup.
