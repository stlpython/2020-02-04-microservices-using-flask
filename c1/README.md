# C1

This is the client service that is available to external clients.  The only API endpoint is the root eg. http://host:5000 and only POST requests are allowed.

_The following example uses HTTPie_

```
http POST localhost:5000 name=TestCar
```