Summit Tech Help Committee
==========================
STHC is a simple tech support ticketing system running on Google App Engine. Here's the general program flow, to get an idea. 

User logs into Google account -> Fills out Ticket -> Ticket is emailed to Google Groups -> Google Groups dispatches ticket to committee members

Make STHC your own!
-------------------

It's easy to implement STHC at your own school and organization!

* Fork this repo
* Create an instance on Google App Engine for Python (it's free!)
* Edit the `app.yaml` file accordingly
* Change the email senders found in the Python code
* Deploy!

app.yaml
--------

    'application: s-t-h-c'
Change this to the name of your own Appspot instance

    - url: /.*
      script: s-t-h-c.application
      
Change this to the name of your own Python script, after forking (optional, but keeps things organized)

s-t-h-c.py
----------

    sender_address ="Summit Tech Help Bot <aramesh.sj@mysummitps.org>"
    reciever_address="Summit Tech Help Google Group <summit-tech-help@googlegroups.com>"
    
    
Change the `sender_address` and `receiver_address` to your own organization. Please, please, please, remember to do this! 

License
-------

The MIT License (MIT)

Copyright (c) 2013 Ajay Ramesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

