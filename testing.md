# Testing

Return to [README.md](README.md) file

## Code Validation

In this document I have detailed all the testing that I have performed.  Where bugs have been found they have been documented and the fix has been outlined
### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2F) | ![Home before](axiom/documentation/testing/w3c_home_before.png) | ![Home after](axiom/documentation/testing/w3c_home_after.png) | Some trailing slash info message. Fixed |
| Jobs | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fpostings%2F) | ![Jobs before](axiom/documentation/testing/w3c_jobs_before.png) | --- | No errors |
| Services | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fservices%2F) | ![Services before](axiom/documentation/testing/w3c_services_before.png) | --- | No errors |
| Contact | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fcontact%2F) | ![Contact before](axiom/documentation/testing/w3c_contact_before.png) | ![Contact after](axiom/documentation/testing/w3c_contact_after.png) | Some trailing slash info message. Fixed |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fregister%2F) | ![Register](axiom/documentation/testing/w3c_register_before.png) | --- | No errors |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Flogin%2F) | ![Login](axiom/documentation/testing/w3c_login_before.png) | --- | No errors |
| Logout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Flogout%2F) | ![Logout](axiom/documentation/testing/w3c_logout_before.png) | --- | No errors |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fprofile%2F) | ![Profile](axiom/documentation/testing/w3c_profile_before.png) | --- | No errors |
| Job Detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fjob%2F13%2F) | ![Detail](axiom/documentation/testing/w3c_detail_before.png) | --- | No errors |
| Job Update | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fjob%2F13%2Fupdate%2F) | ![Update](axiom/documentation/testing/w3c_update_before.png) | --- | No errors |
| Job Delete | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Faxiom-recruitment-f7943c5e25ff.herokuapp.com%2Fjob%2F13%2Fdelete%2F) | ![Delete](axiom/documentation/testing/w3c_delete_before.png) | --- | No errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | ![style.css before](axiom/documentation/testing/style.css_before.png) | --- | No errors |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

#### Application level
| File | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | ![settings before](axiom/documentation/testing/ci_settings.before.png) | ![Alt text](axiom/documentation/testing/ci_settings.after.png) | indent and line length errors. Fixed |

#### Jobs app
| File | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | ![admin](axiom/documentation/testing/ci_jobs_admin_before.png) | --- | No errors |
| apps.py | ![apps](axiom/documentation/testing/ci_jobs_apps_before.png) | --- | No errors |
| forms.py | ![forms](axiom/documentation/testing/ci_jobs_forms_before.png) | --- | No errors |
| models.py | ![models](axiom/documentation/testing/ci_jobs_models_before.png) | --- | No errors |
| urls.py | ![urls](axiom/documentation/testing/ci_jobs_urls_before.png) | --- | No errors |
| views.py | ![views before](axiom/documentation/testing/ci_jobs_views_before.png) | ![views after](axiom/documentation/testing/ci_jobs_views_after.png) | White space and line length errors. Fixed |

#### Users app
| File | Before Screenshot | After Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | ![admin](axiom/documentation/testing/ci_users_admin_before.png) | --- | No errors |
| apps.py | ![apps](axiom/documentation/testing/ci_users_apps_before.png) | --- | No errors |
| forms.py | ![forms](axiom/documentation/testing/ci_users_forms_before.png) | --- | No errors |
| models.py | ![models](axiom/documentation/testing/ci_users_models_before.png) | --- | No errors |
| signals.py | ![signals](axiom/documentation/testing/ci_users_signals_before.png) | --- | No errors |
| urls.py | ![urls](axiom/documentation/testing/ci_users_urls.before.png) | --- | No errors |
| views.py | ![views before](axiom/documentation/testing/ci_users_views_before.png) | ![views after](axiom/documentation/testing/ci_users_views_after.png) | Line length & indentation errors. Fixed |

## Browser Compatibility

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![Chrome](axiom/documentation/testing/Chrome.png) | Works as expected |
| Edge | ![Edge](axiom/documentation/testing/microsoft_edge.png) | Works as expected |
| Firefox | ![Firefox](axiom/documentation/testing/firefox.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![samsung](axiom/documentation/testing/devtools_samsung.png) | Works as expected |
| Tablet (DevTools) | ![ipad](axiom/documentation/testing/devtoold_ipad.png) | Works as expected |
| XL Monitor | ![monitor](<axiom/documentation/testing/Large Screen.png>) | Works as expected |
| iPhone 11 (Chrome) | ![iphone](axiom/documentation/testing/iphone.png) | Works as expected |



## User Story Testing

| User Story | Acceptance | Status |
| --- | --- | --- |
| As a **site owner** I want to **create a base template** so that I can **create and maintain core functions such as navigation and messaging in one place and not repeat them on every page** | template is successfully passing navigation, messaging and footer components to all relevant teamplates (home, jobs, services, contact) | Passed |
| As a **User** I want to **engage with navigation bar** so that I can **easily move from page to page** | All navigation buttons take to correct page. Post job only appears after login, Function on mobile device | Passed |
| As a **User or staff member** I want to **view a list of jobs** so that I can **decide which jobs I want to engage with** | To successfully view a list of jobs. To be able to click on any of the jobs. To have usable pagination to look at further jobs | Passed |
| As a **user or staff member** I want to **add new job postings** so that I can **add new jobs for others to view** | User with staff permission will be able to post new job. Format the text in the description and skills fields in form. Job will appear in list of jobs and display correct data when viewed | Passed |
| As a **User or staff member** I want to **be able to edit the content of a job post** so that I can **display the most up to date information** | User can open a post have the ability to edit and repost. Check that post data has been updated as expected | Passed |
| As a **User or staff member** I want to **be able to delete a job post** so that I can **remove job posts that are no longer valid** | Only user or staff can see delete button and complete the task. Post is removed from list of jobs/database | Passed |
| As a **User** I want to **be able to register for the site** so that I can **login in and create job posts** | A new user can register with username, password, email, profile picture and name details. | Passed |
| As a **User** I want to **be able to log in to site** so that I can **create and edit job posts** | A registered user can log in and edit their own job posts.. Only correct credentials allow this. User cannot edit other users job posts | Passed |
| As a **User** I want to **log out from site** so that I can **others cannot edit my information** | User can logout and there cannot edit posts or profile until logged back in | Passed |
| As a **User** I want to **be able to amend my profile details** so that I can **have the most recent profile information** | User can access and amend only their own profile | Passed |
| As a **User** I want to **view and engaging image on the home page** so that I **find the page interesting and be introduced to what the site is about** | User can view hero image and more info button takes them to services page | Passed |
| As a **User** I want to **see some short messages explaining the company service** so that I can **decide which service are relevant to me** | User can view each service description with appropriate image and click on button that take them to more detail description on services page. | Passed |
| As a **User** I want to **enter my details into a form and submit** so that I can **be contact for further information on a topic** | User can enter details into form and when submitted and email is sent to the site owners inbox | Passed |
| As a **User** I want to **view an interesting page heading within an engaging image** so that I **can clearly identify what page I am on** | Image appears at top of contact page with contact page heading | Passed |
| As a **User** I want to **view services descriptions** so that I can **understand what the company can do for me** | User can navigate to page and read all of the individual service descriptions | Passed |
| As a **User** I want to **view an interesting page heading within an engaging image** so that I can **clearly identify what page I am on** | Image appears at top of services page with services page heading | Passed |
| As a **User** I want to **see some feedback messaging when I update posts or profile** so that I can **know whether or not the action was successful** | User can see colour coded message during CRUD events at top of page | Passed |
| As a **User** I want to **additional information at the foot of the page** so that I can **access navigation etc without having to scroll back to the top of pages** | User has same navigation functionality at base of each page. Can click on company social links. Can view additional company information. | Passed |


## Bugs

### Fixed

| Location | Description | Notes |
| --- | --- | --- |
| Contact Page | Emails would not sent on submission of form, eventually timed out with 500 error | Discovered GitPod blocked the ports, works on deployed version |
| Entire deployed site | Styling lost on deployed (heroku) version of site | Had to set up new location for STATIC files in settings.py |
| Job Post form | Summernote rich text editing not functioning on desired fields | had to build forms.py and expand the form model to asign summernote widgets to specific fields |


### Unfixed

| Location | Description | Notes |
| --- | --- | --- |
| Profile page | Not finding a default.jpg since migrating media to cloudinary | Have been unable to resolve this at the point of project submission |