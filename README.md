# Recipe-Flask
A static site generator suitable for storing recipes under version control

**Todo**
- append tag to recipe links so sidebar can show only recipes for selected tag.
- implement google search
- add ingredients list to recipe meta info
- add an image to recipe meta info

**Application webserver**

install deps and run
    
    $ sitebuilder.py

**Static Webserver**

    $ sitebuilder.py build

Now you can copy the contents of the `build/` folder to a webserver of choice.

An example deploy can be found on http://www.renedohmen.nl/recepten
