 #[Testing](#testing)

## Table of contents

  1. [**Overall Peformance**](#overall-performance)
  2. [**Code Validation**](#code-validation)
  3. [**Accessibility Testing**](#accessibility-testing)
  4. [**Responsiveness & Compatability Testing**](#responsiveness--compatability-testing)
  5. [**JavaScript Testing**](#javascript-testing)
  6. [**Python Testing**](#python-testing)
        - **JS Hint**
  7. [**Bug Fixes**](#bug-fixes)
  8. [**Testing User Stories from User Experience (UX) Section**](#testing-user-stories)
        - **Project Goals**
        - **User Goals**
        - 
  9. [**Other Testing Methods**](#other-testing)
  10. [**Further Testing**](#further-testing)

  ------

## Overall Performance

The complete site was tested on the lighthouse facility in Google Developer Tools to assess the overall performance of the site. The site meets the pass criteria and you can see the results in the below table.

| Page         | Screenshot                                                      | Notes          |
|--------------|-----------------------------------------------------------------|----------------|
| Index Page |![screenshot](documents/testing/lighthouse/index_lighthouse.png)  |  Meets criteria|
| Login   |![screenshot](documents/testing/lighthouse/login_lighthouse.png) |  Meets criteria|                        
| Sign Up |![screenshot](documents/testing/lighthouse/signup_lighthouse.png) |  Meets criteria|                        
| User Dashboard |![screenshot](documents/testing/lighthouse/dashboard_lighthouse.png) |  Meets criteria |                        
| Contact |![screenshot](documents/testing/lighthouse/add_slang_lighthouse.png) |  Meets criteria |                        
| FAQ's  |![screenshot](documents/testing/lighthouse/delete_lighthouse.png)    |  Meets criteria|
| Profile |![screenshot](documents/testing/lighthouse/admin_dashboard_lighthouse.png)    |  Meets criteria |                         
|404       |![screenshot](documents/testing/lighthouse/404_lighthouse.png)       |  Meets criteria. Lower SEO but as a 404 page this is not too concerning |

------

## Responsiveness & Compatability Testing

To ensure a broad range of users can successfully use this site, I tested it across the 5 major browsers in both desktop and mobile configuration.

- Chrome *v.74*
- Edge *v.18*
- Firefox *v.67*
- Safari *v.12*
- Opera n/a
- Internet Explorer *v.11*

For testing compatibility, I created a testing matrix to test across multiple devices and browsers. The test matrix can be found seen below.

![screenshot](documents/testing/compatability_matrix.png)

------

## Code Validation

### Html Validation

The W3C Markup Validator was used to validate every html page of the project to ensure there were no syntax errors in the project. The results and screenshots are in the table below.

| Page                  | Screenshot Link                                                                       | Notes  |
|-----------------------|---------------------------------------------------------------------------------------|--------|
|base.html              |[view here](documentation/testing_images/html_validation/base_html_w3c.png)            | Passed |
|index.html             |[view here](documentation/testing_images/html_validation/index_html_w3c.png)           | Passed |
|main-nav.html          |[view here](documentation/testing_images/html_validation/products_html_w3c.png)        | Passed |
|mobile-top-header.html |[view here](documentation/testing_images/html_validation/products_html_w3c.png)        | Passed |
|products.html          |[view here](documentation/testing_images/html_validation/products_html_w3c.png)        | Passed |
|product-detail.html    |[view here](documentation/testing_images/html_validation/product_details_html_w3c.png) | Passed |
|edit-product.html      |[view here](documentation/testing_images/html_validation/)                             | Passed | 
|add-product.html       |[view here](documentation/testing_images/html_validation/)                             | Passed |
|profile.html           |[view here](documentation/testing_images/html_validation/)                             | Passed | 
|bag.html               |[view here](documentation/testing_images/html_validation/)                             | Passed |
|checkout.html          |[view here](documentation/testing_images/html_validation/)         | Passed |
|checkout-success.html  |[view here](documentation/testing_images/html_validation/)         | Passed |
|contact.html           |[view here](documentation/testing_images/html_validation/)         | Passed |
|faq_list.html          |[view here](documentation/testing_images/html_validation/)         | Passed |
|faq_form.html          |[view here](documentation/testing_images/html_validation/)         | Passed |
|faq_add.html           |[view here](documentation/testing_images/html_validation/)         | Passed |
|faq_confirm_delete.html  |[view here](documentation/testing_images/html_validation/)         | Passed |
|404.html               |[view here](documentation/testing_images/html_validation/)         | Passed |

### CSS Validation

The W3C CSS Validator Services was used to validate every css file of the project to ensure there were no syntax errors in the project. The results and screenshots are in the table below.

| Page          | Screenshot Link                                               | Notes  |
|---------------|---------------------------------------------------------------|--------|
|base.css       |[view here](documentation/testing_images/css_validation/base_css.png) | Passed | 
|profiles.css   |[view here](documentation/testing_images/html_validation/profile_css.png) | Passed |
|checkout.css   |[view here](documentation/testing_images/html_validation/checkout_css.png) | Passed |


##### back to [top](#table-of-contents)

------

## Accesibility Testing

* The complete site was tested using [Web Aim](https://wave.webaim.org/) and has passed. The links are available in the below table.


| Page                 | Screenshot                                                            | Notes  |
|----------------------|-----------------------------------------------------------------------|--------|
|index.html            |[view here](documents/testing/webaim/webaim_index_pass.png)                   | Passed | 
|login.html            |[view here](documents/testing/webaim/webaim_login.png)                        | Passed |
|signup.html           |[view here](documents/testing/webaim/webaim_signup.png) | Passed |
|add_slang.html        |[view here](documents/testing/webaim/webaim_add_slang.png)                    | Passed | 
|delete_slang.html     |[view here](documents/testing/webaim/webaim_remove_slang.png)                 | Passed |
|404.html              |[view here](documents/testing/webaim/webaim_404.png)                          | Passed - alt text query(minor)| 
|dashboard.html   |[view lighthouse testing here](documents/testing/lighthouse/dashboard_lighthouse.png) | Can only be tested in lighthouse due to login required. Not supported by webaim. |
|admin_dashboard.html  |[view lighthouse testing here](documents/testing/lighthouse/admin_dashboard_lighthouse.png) | Can only be tested in lighthouse due to login required. Not supported by webaim. |

------

## JavaScript Testing

### JS Hint

  * All JavaScript code was put though [JS Hint](https://jshint.com/) 

| Test      | Screenshot                                              | Notes                                                   |
|-----------|---------------------------------------------------------|---------------------------------------------------------|
| JS Hint   |![screenshot](documents/testing/jshint_testing.png)      | Passed - No warnings. 1 undefined variable as expected. |

### Summary

 Shows an undefined variable in the script.js file. This variable is defined in a script tag in the 404.html file. For more information see bug fix section in the [development](DEVELOPMENT.md).

------

## Python Testing

### CI Python Linter

  * All Python code files ina ll apps was put though [CI Python Linter](https://pep8ci.herokuapp.com/).
| Test      | Screenshot                                                                                   | Notes                                                |
|----------------------------|-----------------------------------------------------------------------------|------------------------------------------------------|
| CI python linter  | [Home App Python Linter Images](documentation/testing_images/python_linting/home) | Passed |
| CI python linter | [Products App Python Linter Images](documentation/testing_images/python_linting/products) | Passed | 
| CI python linter | [Bag App Python Linter Images](documentation/testing_images/python_linting/bag)  | Passed |
| CI python linter | [Checkout App Python Linter Images](documentation/testing_images/python_linting/checkout) | Passed |
| CI python linter | [Profiles App Python Linter Images](documentation/testing_images/python_linting/profiles) | Passed |
| CI python linter | [Contact App Python Linter Images](documentation/testing_images/python_linting/contact) | Passed |
| CI python linter | [FAQ App Python Linter Images](documentation/testing_images/python_linting/faq)  | Passed |
### Summary

After initially correcting the code format and it passing testing using the CI python linter it seemed that the indentation after breaking a line due to line length wasnt quite aesthetically correct, although meeting pep8 guidlines. The decision was made to use a python beautifier tool which then amended the code and changed the line lengths and indentations. To test if the beautifier tool was pep8 comliant the beautified code was re-run through the CI python linter which then logged warnings for some of the lines being too long. The app.py file was the reverted back to the tested and passed version that was verified by CI python linter, as this meant that  the beautifier tool was not pep8 compliant. As the criteria for this project is that python is to be pep8 compliant, using results and testing of the CI python linter was the most reliable approach.

##### back to [top](#table-of-contents)

------

## Fuzzywuzzy Testing

  * Initially the matching threshold was set to 80% whilst in development.
  * The function and installation was tested by entering random slang words that were stored in the database and by seeing what results were displayed as a match. 
  * At 80% threshold the user needs to be very accurate and close to the correct spelling of the slang word to get a close match. This does not align with the user stories.
  * The threshold was then reduced to 50% and tested in the same way again at 5% intervals. Between 50-65% the results were too broad and the matches were too 'fuzzy'. 
  * 70% match threshold seems to return close enough matches with enough tollerance and flexibility for spelling mistakes for all users.

## Bug Fixes

  * please see the [development](DEVELOPMENT.md) file for bug fix information.

------

## Testing User Stories from User Experience (UX) Section

The project user stories have been met with the following features;

"**_As a guest user, I would like to_** _______________"

✅  browse through the slang terms listed alphabetically so I can see all the terms that are available.

   ItScool provides:<br>
      * a bootstrap accordion of all slangs listed alphabetically on all devices. <br>
      * expandable accordion headings revealing slang words starting with the corresponding letter. <br>
      * correspoding defintions in the accordion next to each slang word.<br>

       The accordion can be seen below.

![screenshot]()


✅  click on slang terms to view their definitions and sample usage, so I can understand the meaning and context.

   ItScool provides:<br>
      * a bootstrap accordion which when clicked, reveals slang words listed with their corresponding definitions. Viewable [here]().<br>


✅  search for slang terms by typing keywords or phrases, so I can quickly find the slang term I'm interested in.

   ItScool provides:<br>
    * A search bar enabling the user to search for slang terms, that are relevance from partial matching using fuzzywuzzy. This displays partial match results due to the nature of slang spellings. This can be seen [here]().<br>
    * A search result area displaying the results of the search. Viewable [here]().


✅  browse slang terms by selecting a letter from A-Z, so I can easily find terms that start with a specific letter.

   ItScool provides:<br>
     * a bootstrap accordion of all slangs listed alphabetically on all devices. The accordion can be seen [here]().

✅  as a new user, create an account by providing a username and password, so I can log in and use additional features.

   ItScool provides:<br>
     * a signup page for users to register as a user with a signup form.<br>
     * This function is a create part of CRUD functionality for this project. It allows the user to create a profile with a username and password.

     Signup page is shown below.

![screenshot](documents/readme/signup.png)

------

"**_As a registered user, I would like to_** _______________"

✅  as a returning user, I want to log in with my username and password, so I can access my account.<br>

  ItScool provides:<br>
      * a login page for users to login with their username and password.<br>
      * a flash message letting users know they are logged in.<br>

![screenshot](documents/readme/login.png)

✅  as a logged-in user, I want to log out of my account, so I can ensure my account remains secure on shared devices.

  ItScool provides:<br>
    * a link in the navbar for both users and admin users to log out with one click. These can be seen below.<br>

![screenshot](documents/readme/logout.png)
![screenshot](documents/readme/admin_nav.png)

✅  get immediate feedback to know if I have signed up, logged in or signed out.

  ItScool provides:<br>
     * Immediate feedback via a flash message to let users know they have signd up successfully.<br>
     * Immediate feedback via a flash message to let users know they have logged in successfully.<br>
     * Immediate feedback via a flash message to let users know they have logged out successfully.<br>

    Example of a flash message is shown below.

![screenshot](documents/readme/admin_flash.png)

✅  access a user dashboard when logged in.

  ItScool provides:<br>
     * a user dashboard for logged in users accessible via the navbar as required.<br>

![screenshot](documents/readme/user_dashboard.png)

✅  request to add new slang terms and definitions, so I can expand the slang dictionary and share knowledge.

  ItScool provides:<br>
      * A navigation link to a add slang word request form in the navbar<br>
      * A add slang page with a add slang word request for for logged in users.<br>

![screenshot](documents/readme/add_slang.png)

✅  request to edit slang terms I’ve added to correct or improve definitions, ensuring the information stays accurate and up-to-date.

  ItScool provides:<br>
      * A add slang form where any slang or revision of slang will be reviewed by admin to update appropriately.<br>
      * This is the update functionality within the CRUD functionality. This can be seen [here](documents/readme/add_slang.png).<br>


✅  request to delete slang terms that are no longer relevant or are duplicates, so the dictionary remains clean and useful.

  ItScool provides:<br>
      * A delete slang page for logged in users which can be navigated to in the navbar.<br>
      * Delete slang form on the delete slang page that once submitted is subject to review by admin. This is part of the delete functionality within CRUD. 
     
![screenshot](documents/readme/delete_slang.png)

✅   be able to save my favourite slang words to a favourites list in my user dashboard.

    ItScool provides:<br>
      * A heart shaped favourite button that allows users to add favourite slang words to be added to a favourites list in their user profile dashboard page.<br>
      * Favourite buttons located in both the accordion and search results sections, next to slang words. These can be seen below.<br>
     
![screenshot](documents/readme/result_favourite.png)
![screenshot](documents/readme/favourite_accordion.png)

------

"**_As an student user, I would like to_** _______________"

✅  Learn About Common School Slang:
    As a student, I want to browse slang terminology so I can understand the informal language and slang used by peers in the school environment and elsewhere.

  ItScool provides:<br>
      * A bootstrap accordion where students can browse slang words and their corresponding terminology, seen [here](documents/readme/accordion.png).<br>
      * A search bar enabling the user to search for slang terms, that are benefot from partial matching using fuzzywuzzy. This displays partial match results due to the nature of slang spellings. This can be seen [here](documents/readme/search_function.png).<br>
      * A search result area displaying the results of the search. Viewable [here](documents/readme/search_results.png).
     

![screenshot](documents/readme/favourite_accordion.png)

✅  Contribute School-Specific Slang:
    As a student, I want to contribute slang that’s specific to my age, school type or region, so I can share it with other students who may find it relevant or interesting.<br>

  ItScool provides:<br>
    * A add slang page where users can add slang words that, pending approval, will be added to the dictionary allowing users to contribute, making the concept user centric. This can be seen [here](documents/readme/add_slang.png).<br>
    
✅  See Slang Organized Alphabetically:
    As a student, I want to see slang words organized by their first letter, so I can easily find terms that I hear frequently.<br>

  ItScool provides:<br>
      * A bootstrap accordion where students can browse slang words and their corresponding terminology grouped by the letter they begin with. This can be seen [here](documents/readme/accordion.png).<br>

✅   Report Incorrect or Inappropriate Content:
    As a student, I want to report slang entries that are incorrect, outdated, or inappropriate, so I can help maintain a positive and accurate dictionary.<br>

  ItScool provides:<br>
      * A delete slang word page where users can request a slang word and its related fields to be deleted from the dictionary if a users feels it is incorrect or innapropriate for the user groups.<br>
      * A clearly labelled delete slang page which can be navigated to from the nav bar.<br>
      * A simple, clear delete slang form that takes the slang word to be deleted and submits it to admin for approval.<br>
     
![screenshot](documents/readme/delete_nav.png)

✅  Save Favourite Slang:
   As a student, I want to be able to save my favourite slang words to a favourites list in my user dashboard.<br>

  ItScool provides:<br>
      * A heart shaped favourite button that allows users to add favourite slang words to be added to a favourites list in their user profile dashboard page.<br>
      * Favourite buttons located in both the accordion and search results sections, next to slang words. These can be seen below.<br>
     
![screenshot](documents/readme/result_favourite.png)
![screenshot](documents/readme/favourite_accordion.png)


##### back to [top](#table-of-contents)

------

"**_As a teacher or parent, I would like to_** _______________"

✅  Understand Student Language:
    As a teacher or parent, I want to look up slang terms and definitions, so I can understand the language students are using in social and school settings.<br>

  ItScool provides:<br>
    * A search bar enabling the user to search for slang terms, that are benefot from partial matching using fuzzywuzzy. This displays partial match results due to the nature of slang spellings. This can be seen [here](documents/readme/search_function.png).<br>
    * A search result area displaying the results of the search. Viewable [here](documents/readme/search_results.png).<br>
    * A bootstrap accordion enabling the user to browse slang terms that they may find relevant or may be looking for. This can be seen [here](documents/readme/accordion.png).<br>


✅  View Related Terms and Meanings:
    As a teacher or parent, I want to be able to search for slang words that i have heard and want to find out their corresponding definition and appropriateness.

  ItScool provides:<br>
    * A search bar enabling the user to search for slang terms, that are benefot from partial matching using fuzzywuzzy. This displays partial match results due to the nature of slang spellings. This can be seen [here](documents/readme/search_function.png).<br>
    * A search result area displaying the results of the search. Viewable [here](documents/readme/search_results.png).<br>
     

✅  Browse by Letter or Category:
    As a teacher or parent, I want to browse slang by letter to find terms more easily and understand common slang patterns.

  ItScool provides:<br>
     * a bootstrap accordion of all slangs listed alphabetically on all devices. The accordion can be seen [here](documents/readme/accordion.png).


✅  Save Relevant Slang:
    As a teacher or parent, I want to be able to save slang words to a favourites list in my user dashboard that i can come back to as a reference point.

  ItScool provides:<br>
    * a favourites list for logged in and registered users available in the user dashboard.<br>
    * favourite buttons to allow logged in and registered users to add favourite slangs to their favourites list.<br>
     
![screenshot](documents/readme/favourite_list.png)

##### back to [top](#table-of-contents)

------

"**_As an administrator, I would like to_** _______________"

✅  review slang terms submitted by users before they are published, so I can ensure quality and appropriateness.

  ItScool provides:<br>
    * a pending slang list where users have submitted request for slangs to be added to the dictionary by submitting the add slang form for users.
    * Action button allowing the admin user to take appropriate action.
     
![screenshot](documents/readme/action_buttons.png)

✅  delete any slang term to correct inaccuracies, enforce content guidelines, and remove inappropriate entries.

  ItScool provides:<br>
    * an admin search function allowing admin to search slang words they wish to remove from the dictionary. This can be seen below.<br>
    * a confirmation modal to ensure admin confirm that they want to delete the slang entry, minimising mistakes. This can be seen [here](documents/readme/delete_nav.png).<br>
     

![screenshot](documents/readme/admin_dashboard.png)

✅  edit, delete or approve pending approval requests from users requesting a slang word to be added to the app via an admin dashboard.

  ItScool provides:<br>
    * action buttons allowing the admin user to add, delete or edit a pending slang.<br>
    * an edit button that triggers an edit modal enabling the admin user to edit the pending slang before approval. This can be seen [here](documents/readme/edit_modal.png).<br>
     
![screenshot](documents/readme/action_buttons.png)


✅  use a form to add new slang words to the app.

  ItScool provides:<br>
    * an add slang form located in the admin dashboard where the admin can add a slang term and its corresponding fields without having to submit it for approval, streamlining the process for admin.
     

![screenshot](documents/readme/add_slang_admin.png)

✅  navigate easily to the admin dashboard via a navbar.

  ItScool provides:<br>
    * a navbar specifically for admin users, which can be seen below.<br>
     
![screenshot](documents/readme/admin_nav.png)

##### back to [top](#table-of-contents)

------

## Other Testing Methods

### Manual Testing

Behaviour driven Development (BDD) is where a project or product is tested to the user stories and by the user. This has also been done in responsiveness and compatability testing section above. 
This form of testing although useful in terms of user story testing can be subject to bias and sometimes things can get missed due to fatigue and is costly in time and resources. BDD is more user-centric and revolves around system behaviour. This is an Agile software development methodology.
It is particuarly useful as it can encompass a wide range of input from stakeholders to managers and is good for planning a project and monitoring throughout its entirety. Goals can be set along the projects way to delivery and measured.

- Below is a table of the manual user testing carried for home.

| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |
| ItScool Nav Link | Click to redirect to index page | Links to start page, except when modal displayed | Pass |
| Signup Nav Link | Click to direct to signup page | Links to signup page, except when modal displayed or logged in| Pass |
| Login Nav Link | Click to direct to Login page | Links to login page, except when modal displayed and currently logged in | Pass |
| Logout Nav Link | Click to logout | Logs out unless already logged out. redirects to login page | Pass |
| User Dashboard nav link | Click to direct to user dashboard | Links to user dashboard, visible when logged in as user | Pass |
| Add Slang Nav Link | Click to direct to add slang page| Links to add slang, visible when logged in as user | Pass |
| Remove Slang Nav Link | Click to direct to remove slang page| Links to remove slang, visible when logged in as user | Pass |
| Admin Dashboard Nav Link | Click to direct to admin dashboard | Links to admin dashboard, visible when logged in as admin | Pass |
| Sign Up & Login Link | Click links to direct to relevant page | Links to relevant page | Pass |
| Sign Up | create user name and password, attempt login | Creates username and password. Logs in | Pass |
| Auto date change in footer | Check year is present and correct on loading | Shows current year in span in footer | Pass |
| 404 Page | Type unknown url extention in browser | Page loads when a page cannot be found or error occurs | Pass |
| 404 take me home button | Click take me home button | Redirects to index and links to index.html page on click | Pass |
| 404 redirect | Check redirect after 10 seconds of inactivity | Redirects to index after 10 seconds | Pass |

- Below is a table of the manual user testing carried for products.

| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |

- Below is a table of the manual user testing carried for bag.

| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |

- Below is a table of the manual user testing carried for checkout.

| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |

- Below is a table of the manual user testing carried for profiles.

| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |
| Admin Dashboard | Navigate to admin dashboard, check for flash message | Flash message appears in dashboard when navigated to | Pass |
| User Dashboard Profile | Login as user and navigate to userdashboard | User dashboard displays username in the profile card | Pass |
| Sign Up | Create user name and password, attempt login | Creates username and password. Logs in | Pass |
| Log In | Attempt login with username and password used for signup | Logs in with registered credentials | Pass |
| Logout | Click link in admin and user navbar | Logs user out and redirects to login page | Pass |

- Below is a table of the manual user testing carried for contact.
| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |

- Below is a table of the manual user testing carried for FAQ's.
| **Feature**          | **Test Details**           | **Expected results**                      | **Pass/Fail** |                                             
| :-- | :-- | :-- | :-- |
| Admin Delete Slang | Input slang to delete, select from results and use confirmation modal to confirm. Re-search for deleted slang | Returns close matches, modal shows when delete button is clicked and removes from app, verified on re search | Pass |
| Admin Pending Slangs | Add slang as user, log in as admin to check updated list | Request is shown in the pending slangs list and updates | Pass |
| Admin Action Button (Approve) | Click approval button, check success by searching for approved slang. | Flash message appears with success. Slang is added to database | Pass |
| Admin Action Button (Delete) | Click delete button, confirm in modal. | Confirming deletion removes slang from pending list and database | Pass |
| Admin Action Button (Edit) | Click edit button |  Edit modal triggered and shows | Pass |
| Admin Edit Modal | Enter input to edit pending slang, confirm or cancel | Pending slang is updated with edits upon saving changes, modal shuts upon clicking close button | Pass |
| Add Slang Admin | Enter input to add slang | Search for new slang added using search bar | Pass |

##### back to [top](#table-of-contents)

------

### Automated Testing

Various language specific frameworks are available to run automated testing. One of the most popular is Jest for testing JavaScript. 

It is best to combine manual and automated testing. Automated tests will not test user experience and tests will only ever be as good as the questions we ask it to perform.

#### Bag App Test (BagViewTest)
The BagViewTests class is designed to comprehensively test the main features and user interactions of the bag (shopping cart) functionality in the application. It uses Django’s built-in test client to simulate user actions and verify that the bag behaves as expected.

Test Coverage
The tests cover the following core features:

Viewing the Bag
Adding Items to the Bag
Adjusting Item Quantities
Removing Items from the Bag
1. Viewing the Bag
Test: test_view_bag_get
Purpose: Ensures that the bag page is accessible and renders correctly.
How:
The test sends a GET request to the bag page using the URL pattern 'view_bag'.
It asserts that the response status code is 200 (OK) and that the correct template is used.
Why:
This confirms that users can always access their bag and that the view and template are set up correctly.
2. Adding Items to the Bag
Test: test_add_to_bag
Purpose: Verifies that a user can add a product to their bag.
How:
The test simulates a POST request to the add_to_bag view, sending the product ID, quantity, and a redirect URL.
It checks that the response redirects to the correct page and that the session data contains the correct product and quantity.
Why:
This ensures that the add-to-bag functionality works, the session is updated, and the user receives appropriate feedback.
3. Adjusting Item Quantities
Test: test_adjust_bag
Purpose: Ensures that users can change the quantity of an item already in their bag.
How:
The test first adds a product to the bag, then simulates a POST request to the adjust_bag view with a new quantity.
It asserts that the session data reflects the updated quantity (not the sum of old and new, but the new value).
Why:
This test checks that the adjust functionality sets the quantity as expected, matching user intent and preventing accidental over-adding.
4. Removing Items from the Bag
Test: test_remove_from_bag
Purpose: Verifies that users can remove items from their bag.
How:
The test adds a product to the bag, then simulates a POST request to the remove_from_bag view.
It checks that the product is no longer present in the session bag data.
Why:
This ensures that the remove functionality works and that users can manage their bag contents as expected.
Why These Tests Matter
Reliability: They ensure the bag’s core features work as intended after every code change.
User Experience: They help guarantee that users can add, adjust, and remove products without unexpected behavior.
Regression Prevention: They catch bugs early, especially after refactoring or adding new features.

On the first test the app failed. The image of the terminal can be seen below.

![screenshot](documentation/testing_images/automated_testing/bag_auto_test_fail.png)


What Was Wrong
Previously, the adjust_bag view was adding the new quantity to the existing quantity in the bag.
For example, if the bag already had 2 of an item in the bag and you tried to "adjust" it to 5, the code would add 5 to 2, resulting in 7.
This is not the expected behavior for an "adjust" action—users expect the quantity to be set to the new value, not increased by it.

What the Fix Does:
The fix changes the logic so that when you adjust the quantity of an item in the bag, it sets the quantity to the new value provided by the user, rather than adding to the existing quantity.

Key Line Changed:
Before (incorrect): bag[item_id] += quantity

![screenshot](documentation/testing_images/automated_testing/bag_fail_code_snippet.png)

After (correct): bag[item_id] = quantity

![screenshot](documentation/testing_images/automated_testing/bag_fixed_snippet.png)
 
How the Fixed Code Works
Retrieve the Bag:
The bag is fetched from the session. If it doesn’t exist, an empty dictionary is used.

Check for Product Size:
If the product has sizes (like S, M, L), the code adjusts the quantity for the specific size.

Adjust Quantity (No Size):

If the item is already in the bag, its quantity is set to the new value (bag[item_id] = quantity).
If the item is not in the bag, it is added with the specified quantity.
Save the Bag:
The updated bag is saved back to the session.

Redirect:
The user is redirected to the appropriate page.

Why This Fix Is Important
Correct User Experience:
When users adjust the quantity of an item in their bag, they expect the number to be exactly what they set, not the sum of the old and new values.

Test Consistency:
The automated tests expect the quantity to be set, not added. This fix ensures your tests pass and your app behaves as users expect.

Prevents Over-Adding:
Without this fix, users could accidentally end up with more items in their bag than intended.

In summary:
The fix ensures that "adjusting" a bag item sets its quantity to the user’s chosen value, matching both user expectations and your test logic.
The test pass returning a print to the terminal of 'ok' can be seen below

![screenshot](documentation/testing_images/automated_testing/auto_test_bag_pass.png)

#### Contact App Test (ContactViewTest)
Contact App Automated Test Summary
The automated tests for the contact app ensure both the accessibility and functionality of the contact form:
Below is an image of the test file followed by the summary.<br>
![screenshot](documentation/testing_images/automated_testing/contact_app_auto_test_file.png)<br>

1. GET Request Test
Purpose:
Verifies that the contact page loads successfully when accessed by a user.
How it works:
The test sends a GET request to the contact page URL and checks that the server responds with a status code 200 (OK).
It also confirms that the correct template (contact/contact.html) is used to render the page.
Why it matters:
This ensures that users can reach the contact form without errors and that the page is set up correctly in the Django project.

2. POST Request Test
Purpose:
Simulates a user submitting the contact form and verifies that the form data is processed correctly.
How it works:
The test sends a POST request with sample form data (name and email) to the contact page.
It then checks that:
The response status is 200, indicating the page reloads successfully.
The submitted data is saved in the database (i.e., a new Contact object is created).
The response contains a success indicator, confirming that the user receives feedback after submitting the form.
Why it matters:
This test ensures that the contact form works end-to-end: users can submit their information, the backend processes and stores the data, and users receive confirmation that their message was sent.
In summary:
These tests provide confidence that the contact page is always accessible and that the contact form reliably accepts and stores user submissions, helping to catch issues early in development or after changes.
The confirmation that the test passed with aan output of 'ok' is shown below in the terminal.
<br>


![screenshot](documentation/testing_images/automated_testing/contact_app_auto_test_terminal.png)<br>

## Further Testing

 * A large amount of testing was carried out to ensure that all pages, buttons, feedback and functions were working correctly.

 * Friends and family members were asked to review the site and documentation to point out any bugs and/or user 
      experience issues.

##### back to [top](#table-of-contents)