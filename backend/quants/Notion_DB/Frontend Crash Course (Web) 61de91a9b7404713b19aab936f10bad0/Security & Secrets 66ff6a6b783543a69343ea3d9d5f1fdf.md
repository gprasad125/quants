# Security & Secrets

> I can find your private API keys 😈
> 

---

# Intro

One of the main pains of frontend is that all code and assets are sent to the user for the browser to stitch together. This means that all JS, HTML, CSS, and other assets that makeup your website can be seen by your user. This means that any secret passwords, API keys, etc. you put in your frontend code can and will be found by malicious users. This means that malicious users can trick user’s browsers into running malicious code to steal their data. 

# Handling Secrets

If you have any secrets, remember to **never** store it in frontend code unless it’s somehow permitted for some weird reason (some APIs have private keys that you use by storing in frontend code. I don’t know why they think it’s reasonable). If you do need to use a private key for a third-party API for example, ideally use it in the backend (as an environment variable of course) and have a API route that fetches the data for the frontend. The frontend would then ping the backend API instead of directly pinging the third-party API, where the key will be used on the server instead of on the user’s browser. It’s an extra in-between step, but you won’t need to worry as much about somebody finding your key and stealing it for their own purposes. 

Note that this is limited to secrets. If you have some basic values that don’t need to be hidden away from the public, it’s fine to have them stored in the code. 

Also slightly unrelated but deserves mention, remember to **********never********** store secrets in code that you commit to Github as well. Use them as environment variables. 

# Basic Security

There are numerous ways to improve the security of your application and the sections below only covers a small portion of it that has some relation to the frontend. There is much more to say about backend security. 

Security will likely not be as necessary if your application does not interact with any critical personal information, but if it does, definitely do more research into security practices. The probability of a hacker targeting your project will likely be small, but if the consequences would be exceptionally severe, then implementing good security would be the right thing to do. 

### XSS (Cross-site scripting)

XSS attacks are when someone manages to get malicious code to run with the app code. The most common example is when user input is rendered directly into HTML. Imagine you have an app where users have their own profile page and can enter in a custom description. In the code, you directly embed whatever they enter as the description into the HTML without any validation. 

With this, a malicious user can simply set their profile description as an HTML `script` tag so that whenever another user visits their profile, their browser parses the description, sees the `script` tag as HTML, and executes whatever code the malicious user put inside. Since the code is run on the victim user’s browser, the malicious user has full access to their login session or tokens. Obviously, the damage can be extremely serious depending on the privileges of the hacked user. 

A basic way to protect against this is to clean all user input to prevent any code from being secretly embedded inside of it and to never directly embed user input into HTML templates. You will need to implement backend validation for the former, and UI frameworks like React have built-in protections for the latter to a certain extent. 

You can also setup a [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) via the appropriate headers that dictate what urls and locations that the browser can get assets and run code from. This blocks the user’s browser from running code or loading assets that you did not allow, preventing otherwise malicious code and assets from being loaded. 

For cookies that you do not need to interact with using Javascript, it would also be good to set the `[HttpOnly` cookie attribute](https://owasp.org/www-community/HttpOnly) to block malicious scripts from accessing critical cookies. This will not however block them from sending requests masquerading as the user and wrecking havoc. The bottom line is that the best way to protect against XSS is to prevent it from happening because there is practically no way of limiting the attack when it does succeed.

If you aren’t storing any user input and displaying it elsewhere however, then you won’t need to worry about XSS attacks as much. 

### CSRF (Cross-site request forgery)

CSRF attacks take advantage of default browser behavior where cookies for a certain site are sent along with requests to the certain site regardless of what code initiated the request. This means that if you are currently logged in to `www.pancakes.com`, you visit `www.toast.com`, and `www.toast.com` has javascript code that sends a request to `www.pancakes.com`, the browser will send the request to `www.pancakes.com` with your authentication cookies. This means that `www.toast.com` can initiate actions on your behalf (like deleting your account) simply because it can initiate requests, and your browser will automatically attach whatever cookies are related. 

CSRF is mainly an issue for cookie-session authentication, where authentication sessions are tracked using unique session strings that are stored in the browser’s cookies. CSRF is not an issue for non-automatic authentication systems such as Json Web Token authentication, where the authentication token string must be passed along in the request itself or via custom authentication headers, stuff that `www.toast.com` would not be able to do since it doesn’t have access to the token. 

To combat CSRF, websites gave unique strings called CSRF tokens to users and required that the token to be passed along with requests to verify that the request was done by the user. The idea is that `www.toast.com` would be unable to access that token and therefore unable to exploit the browser. Some server frameworks like Django have built-in CSRF systems that simplify setting something like this up. 

In recognition of this blatant vulnerability, modern browsers have gradually moved towards implementing the `[SameSite` cookie attribute](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite), where setting it to `lax` or `strict` prevents the browser from automatically sending cookies along with requests. If your website mainly targets modern browsers, then likely setting `SameSite` to `lax` or `strict`will be enough to protect from CSRF, and you won’t really need to setup CSRF token protection. If you reasonably expect a significant portion of users to be using older browsers like Internet Explorer for example, then having CSRF tokens would be necessary since they might not support the `SameSite` attribute. 

### DDOS (Distributed denial of service)

DDOS attacks are simply when a malicious actor overloads your servers with mountains of requests. This prevents actual users from accessing your site since the servers are busy dealing with malicious requests. Of course, this attack requires a lot of puppets to execute, so the likelihood of experiencing such an attack is small if your project isn’t very popular. 

If you’re curious however, one way to combat this issue is to use an external service like Cloudflare, which can act as a proxy that verifies valid requests and protects your application from bot swarms. Another approach is to simply have the scaling and capacity to handle such a load. For example, your app may have a server-less deployment or have automatic horizontal scaling so it can dynamically adjust to heavier loads without shutting down. Of course, you’ll be paying for all the fake requests coming in.