HyperlinkHelper Service is a version of the TextMate / SublimeText 2 link creator
in the format used by [This Service](http://wafflesoftware.net/thisservice/).

The [Sublime Text 2 implementation](https://github.com/sentience/HyperlinkHelper)
 from which the basic functionality is lifted is far more comprehensive, but 
 I just needed the basic ability to create a link using the selection as the anchor
 text and the clipboard contents as the URL, if any.
 
 Like the TextMate and ST2 implementations, the script will look up the link 
 destination and attempt to read the title out of the page, adding it as an
 attribute of the link.
 
 
 ###Requirements
 
 Python  
 chardet module (`pip install chardet`)