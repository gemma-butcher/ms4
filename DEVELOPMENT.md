### Javascript
- During development of js code and using JS Hint to verify the code, there were a few errors coming up. However this is due to Django syntax being used within the script which js hint doesnt recognise or
take into consideration. However with this considered the js code does pass criteria.
The JS errors are shown below.
![screenshot](documentation\development_images\js_development.png)


### Contrast
#### Logo Text
- During development and testing with webaim a persistant contrast issue arose. It was on the nav bar logo text. The purple hyphen was shwoing as not meeting contrast criteria. 
- Although it is text designed to look like a logo, and could be argues that it could be dismissed, the text will still need to be accessible which it was not.
- The original contrast was a background of #000000 with the hyphen being #7719a1.
![screenshot](documentation\development_images\hyphen_contrast_fail.png)
- The updated contrast is a background of #000000 with the hyphen being #ff6b6b. This is now consistent with the site footer which makes the branding more consistent.
![screenshot](documentation\development_images\hyphen_contrast_pass.png)