# Event Documentation

This page will lead you through all dispatched events from the websocket.

## How to listen for events

Generally, you can listen to an event like this:

```py
import ordr

client = ordr.OrdrClient()

@client.socket.event()
def on_(data):
    pass #do something

client.connect()
```

For the `OrdrAsyncClient`, handlers can be regular functions as above, or can also be coroutines:

```py
import ordr
import asyncio

client = ordr.AsyncClient()

@client.socket.event()
async def render_data_json(data):
    pass #do something

asyncio.run(await client.connect())
```

## Events

There are different events:
>
> - connect
> - connect_error
> - disconnect
> - render_added_json
> - render_progress_json
> - render_done_json
> - render_failed_json

Lets now have a look at those events in detail:

### **Event: connect**

This event fires when the client connected to the websocket.

### **Event: connect_error**

This event fires when the client having issue connecting to the websocket.

### **Event: disconnect**

This event fires when the client disconnected from the websocket.

### **Event: render_added_json**

This event fires when the a render is added to the list.

### **Event: render_progress_json**

This event fires when a render in the list gets a progress update.

### **Event: render_done_json**

This event fires when a render in the list is completed.

### **Event: render_failed_json**

This event fires when a render in the list failed.
