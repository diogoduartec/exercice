# Apollo Back-End Engineering Challenge

This challenge is designed to evaluate several things:
 - How well you know Python
 - How effectively you can work with the Django framework
 - How well you understand different data serialization formats, which is important for working with the diverse APIs Apollo integrates with
 - Your ability to work with connected Django pages
 - Your ability to work with Django Rest Framework

It is intended to take 2-4 hours. After you submit your solution (either by emailing us a .tar or .zip file, or uploading to GitHub), we will schedule a call to talk through your solution and how it could be extended to accomplish further goals.

## Setting Up

Install Python 3.7 or later if it is not already installed. Then, set up and enter a virtual environment and run `pip install -r requirements.txt` to install the dependencies. You should then be able to run the project from the `exercise` directory by running `python manage.py runserver`.

To verify that the server is running correctly, visit `http:127.0.0.1:8000` in your browser.

## Challenge Guidelines

This Django project consists of two parts:
1. A very simple HTML page at `/connected/`.
2. A stubbed out API endpoint at `/api/converter/convert/`

Your tasks are to:
1. Add a file input to the HTML page and modify the view so that, when a file is submitted, convert it to JSON and return that to the user
2. Add the same functionality to the API endpoint, returning the converted JSON as an `application/json` response.

To test your solution, you can run `python manage.py test`. This will execute 3 tests, which attempt to submit a file and check the response.

A good solution will not only pass the tests, but also work on any user-submitted XML file.

### JSON Conversion

For the purposes of this exercise, you may ignore any XML attributes. We are only interested in converting the XML node tags and any text values into JSON.

Leaf nodes should be converted into a JSON object with the node tag as the key and the node's text value as the value. For example, `<Foo>Bar</Foo>` should be converted to `{"Foo": "Bar"}`.

Non-leaf nodes should be converted into a JSON object with the node name as the key and an array of the node's children as the value. For example:
```
<Foo>
    <Bar>Baz</Bar>
</Foo>
```
should be converted to
```javascript
{
    "Foo": [
        {"Bar": "Baz"}
    ]
}
```

The tests provide additional examples of more complex conversions.


### Candidate notes
How I've solved this problem: First, I've researched if there were some lib to help do the job. I've found a lib that solves all the problem called `xmltodict`, but I've decided to not use it and show you my abilities in programming and problem solving. I've decided to use the native tool `xml.etree.ElementTree` with which I can manipulate the XML as a tree, so I could do my own algorithm to convert a simple XML to a dictionary (and later return it as a JSON).