# Testing

Return to [README.md](README.md) file

## Code Validation

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
| admin.py |  | --- | No errors |
| apps.py |  | --- | No errors |
| forms.py |  | --- | No errors |
| models.py |  | --- | No errors |
| urls.py |  | --- | No errors |
| views.py |  |  | White space and line length errors. Fixed |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) |  | Works as expected |
| Tablet (DevTools) |  | Works as expected |
| Desktop (DevTools) |  | Works as expected |
| XL Monitor |  | Works as expected |
| Samsung Galaxy A52s (my own phone) |  | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| --- | --- | --- | --- |


