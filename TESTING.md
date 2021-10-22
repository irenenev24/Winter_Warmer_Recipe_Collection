# Manual Testing

## Navigation

- Navigation was taken from MaterializeCSS.com. Will automatically adjust to a hamburger icon after 780px.
- This will result in the menu becoming a side nav that comes from the right when the hamburger icon is activated.
- The nav bar logo will bring you back to the home page and is located in the center of the nav bar on a small screen.

## CRUD

- All users can create/read/edit/delete recipes but I have only allowed admin to create/read/edit/delete catergories.
- In the future I aim to only allow users to delete recipes that they have created themselves.

## Front end Validation

- This application currently only uses front-end data validation via the formfield attributes for example:
(max and min of characters, only accepting valid url using a pattern pattern="https://.*" to verify images, all form fields are required).
- In the future I will aim to validaate through the back-end code.
- The text fields for the recipes can only except a certain amount of characters so as not to overload the site.

## Home Page

- Carousel taken from w3schools.
- ( Working )

- Fonts from google font.
- ( Working )

## Profile Page

- Used jinga to have users name shown on the profile page after login. 
- (  Failed to work due to comma instead of : in profile view )
- Added link to add recipe page
- (  At first did not work due to using href="add_recipe.html" replaced with jinga {{ url_for('add_recipe') }} )

## Recipe Page

- Added search bar. 
- (  Worked )

- Added recipes as a test through the data base which worked I then removed these and wired up the add recipe
 page following the video in the mini project. 
- I also wired up the view recipe view following the video and found them to be working.
 I had some issues with the image sizes which I could not target using CSS but found I could target in the img tag on the HTML

## View Recipe Page

- At first this page would not show recipes as I had incorrect tried to link to each recipe without using 
(  the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})   )
- When I corrected this I found the recipe to show. I was originally using a card to display it but found that it looked much batter with out the card.
- Used width/height in the image tag to control the picture size.
- Included an edit button here which redirects to a page to edit the recipe with a form that is prepopulated using jinga and recipe.recipe id.
- After a few edits of images and such I found that the category box no longer prepopulated on the edit page and the edit button stopped working.
- This was also found to be because of a , instead of a :. Tutor support assisted me with this.

## Add recipe page

- Add recipe page that ha a category box that requires a selection. All form items are required.
- Found that the submit button did not work but when I added type="submit" this worked.

## Category create/read/update/delete
- These page are only available to admin.
- Created using videos from CI and found to be working.

## Login/Logout/Register
 
- These were added using CI videos and found to be working.
- All icons across these pages and the site are from font-awesome.

## Delete Recipe/Categories Pages

- Used JS to alert users/admin to the decision to delete these items.

## User stories test

### First time customer

1. Is this site trusthworthy and easy to navigate?
1. Can I add to the infomation provided?
1. Can I look at recipes on this site?
1. Is the information provided relevant to my needs?
1. Is the purpose of this site clear?
1. Am I able to make a profile for my own recipes?
1. Is it easy to create an account?
1. Do I understand the aim of this site?
1. Can I use this site on all my devices?

 #### Results

1. Yes I find it to be trustworthy and easy to navigate.
1. Yes a user can add to the information.
1. Yes a user can look at recipes on the site.
1. I find the information to be relevant.
1. Yes I find the purpose to be clear.
1. Yes a user can make their own profile.
1. Yes an account is easy to create.
1. Yes it is easy to understand the use of the site.
1. Yes it is responsive on all devices.

### Repeat customers

1. If I see a recipe I wish to use in the future 
am I able to access the site again to use it?
1. Can I add to this site?
1. Will I be able to use this on all my devices?
1. Is this site easy to navigate to save time?
(eg: navigation bar, search bar, categories)

 #### Results

1. Yes a user can reacces recipes.
1. Yes a user can add to the site.
1. Yes it is responsive on all devices.
1. Yes it is easy to navigate.


### Friends/Family

- Friends, family and slack peer review used.
-  Devices and browsers were HP Pavilion 17, iphone XS Max: Safari, iphone 6: Chrome, iphone XR: safari, iphone 11 Pro: Safari, 
iphone 10: Safari, Samsung S20 FE: Chrome, Samsung S10 and Sony Xperia I3: Chrome. Smasung Galaxy Tab2, Samsung A50. Xperia.
- I used Chrome devtoolsto test the responsiveness throughout the development process.
- I viewed all pages on all of the available devices at the end of the project and was happy with the results.

## Wireframes

- All images for wireframes and validators/lighthouse also stored in the image file.

- [Mobile-form](/static/images/mobile-form.png)
- [Mobile-home](/static/images/mobile-home-page.png)
- [View-recipe](/static/images/view-recipe.png)

## For all code I used JS/HTML/CSS Validators and Lighthouse on DevTools

- [HTML](/static/images/TESTING.md.images/Screenshot(114).png)
- [HTML](/static/images/TESTING.md.images/screenshot(115).png)
- [HTML](/static/images/TESTING.md.images/screenshot(116).png)
- [CSS](/static/images/TESTING.md.images/screenshot(117).png)
- [PEP8](/static/images/TESTING.md.images/screenshot(126).png)
- [Lighthouse](/static/images/TESTING.md.images/screenshot(121).png)
- [Lighthouse](/static/images/TESTING.md.images/screenshot(122).png)
- [Lighthouse](/static/images/TESTING.md.images/screenshot(123).png)
- [Lighthouse](/static/images/TESTING.md.images/screenshot(124).png)
- [Lighthouse](/static/images/TESTING.md.images/screenshot(115).png)

- I found that the HTML on all pages flagged the jinga templates {{}} as an error but these were essential for my project.
- I corrected various stray divs and such like. I ran them again and the only errors were the jinga templates.
- CSS came back clear as seen above.
- PEP8 came back with one indent error whish I coorected.

## Beautifier

- I also used an Online Beautifier for all code used in my project.



