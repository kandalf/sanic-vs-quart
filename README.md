## Sanic vs Quart

This is a Proof of Concept to evaluate the similarities and differences betwen two asynchronous Python frameworks, [Sanic](https://sanic.readthedocs.io/en/latest/index.html) and [Quart](https://pgjones.gitlab.io/quart/index.html).

For its purpose it defines an API with two endpoints to create and list a resource:

* `GET /apps`
* `POST /apps`

For simplicity's sake it doesn't include any authentication layer.

Both frameworks have a [Flask](http://flask.pocoo.org/)-like style, [Quart](https://pgjones.gitlab.io/quart/index.html) even defines itself as a _superset_ of [Flask](http://flask.pocoo.org/) and you can even use a few [supported Flask extensions](https://pgjones.gitlab.io/quart/flask_extensions.html)


### Things in common

The codebase is pretty much the same for both versions the main differences have to do with asynchronous behaviour which Quart kind of enforces a bit more.

Database access for both variations is handled by [Gino](https://python-gino.readthedocs.io/en/latest/index.html) which supports Sanic and Quart, and database migrations are handling with Alembic which works the same for both frameworks.

Also testing was made with pytest which seems to be the recommended option by both frameworks.

The tests code is mostly the same with some small differences regarding to the `Response` object that has some variations between the two frameworks.

### Conclusion

TL;DR This was by no means an in-depth analysis, its goal was to compare both variations on the most basic tasks and, for this, I found Sanic slightly more intuitive and predictable.

One of the reasons for this opinion is based in how responses are sent to the client. Sanic provides an out of the box JSON helper which makes it easier to send the response with its status and headers, with Quart, for example, I had to add a hook to `after_request` event in order to specify the JSON content type, otherwise it will return a `text/html` response.

The other main reason was testing. With Sanic was more straight forward while with Quart I had a bunch of problems for DB engine initialization for it being run in a separate loop. I even had to skip a test to not avoid wasting more time on this.

Maybe I'll keep playing with this until I resolve it and update this review, but for the purpose of this app it was enough. The `GET` endpoint was tested with an actual request and it works, so there was no point on spending more time dealing with this.

It's worth noting that both frameworks are under active development, so probably the rough edges will be polished soon.

Even I'm feeling slightly leaned to Sanic, it's fair to say that both options are equivalent and my feeling is that deciding for one option or another for a given project might depend on matters of personal preference rather than on technical factors.

This is my humble opinion and I would love to hear other opinions so feel free to discuss in the PR or to reach me out directly!
