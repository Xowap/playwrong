# PlayWrong

A simple reproduction of the asyncio/pytest-playwright issue.

Basically, if you have a single test which depends on the `playwright` fixture,
then all tests using asyncio will fail with the following error:

```
self = <_UnixSelectorEventLoop running=True closed=False debug=False>

    def _check_running(self):
        if self.is_running():
>           raise RuntimeError('This event loop is already running')
E           RuntimeError: This event loop is already running

../../.pyenv/versions/3.10.10/lib/python3.10/asyncio/base_events.py:584: RuntimeError
```

To run the tests, first install the virtual environment:

```bash
uv venv
uv pip install -r requirements.txt
```

Then run the tests:

```bash
.venv/bin/pytest -m "not playwright"  # don't activate the playwright fixture
.venv/bin/pytest  # activate the playwright fixture
```

You'll see that if you don't have a dependency on `playwright`, then all tests
pass, but if you don't exclude it then all the tests that require some asyncio
will fail.
