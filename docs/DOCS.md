# ordr.py Documentation

## Where do I start?

Please look at the pages below to find out where to go.

- [Quickstart](#installing)
- [API Reference](/docs/API.md)
- [Event Documentation](/docs/EVENTS.md)
- [Frequently Asked Questions](/docs/FAQ.md)

## Installing

**ordr.py** is a python library for o!rdr API and Websocket. A library in Python has to be installed with pip. Run the following in your terminal/command line to install the library.

```py
pip install -U ordr.py
```

## Running a Client

### First, let's run the client

```py
import ordr

client = ordr.OrdrClient()

client.connect()
```

And that's it! The client should be connected to the websocket.

Let's take a look at what is happening:

- `import ordr` - This is the import line. If this returns a `ModuleNotFoundError`, please look at the section on how to install [here](#installing).
- `client = ordr.OrdrClient()` - This is the `client` variable that holds the client.
- `client.connect()` - This tells the client to connect to the websocket.
