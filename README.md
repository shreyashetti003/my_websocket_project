# WebSocket Backend

## Overview
This WebSocket backend performs the following actions:
1. Echoes whatever message is sent in a streaming format with a 0.1-second delay.
2. Echoes the message in reverse in a streaming format with a 0.1-second delay.
3. Counts the number of times the last character is repeated in the message (excluding the last character) and returns this count.

### Example
- *Message*: "The quick brown fox jumped over the lazy dog o"
- *Last Character*: o
- *Occurrences of 'o' (excluding the last character)*: 4

## Requirements
- Python 3.7+
- websockets library

## Setup and Run Locally

### Server

1. *Install Dependencies*:
   ```bash
   pip install websockets

2.Run the server
   # WebSocket Backend
   python server.py

3.client
Install Dependencies :
pip install websockets
Run the Client:
python client.py   

## Overview
This WebSocket backend performs the following actions:
1. Echoes whatever message is sent in a streaming format with a 0.1-second delay.
2. Echoes the message in reverse in a streaming format with a 0.1-second delay.
3. Counts the number of times the last character is repeated in the message (excluding the last character) and returns this count.

### Example
- *Message*: "The quick brown fox jumped over the lazy dog o"
- *Last Character*: o
- *Occurrences of 'o' (excluding the last character)*: 4

## Requirements
- Python 3.7+
- websockets library

## output
When you run the client.py, it should connect to the WebSocket server, send the message "The quick brown fox jumped over the lazy dog o", and print the responses as they are received. For example:
Streamed echo: T
Streamed echo: h
Streamed echo: e
Streamed echo:  
Streamed echo: q
Streamed echo: u
Streamed echo: i
Streamed echo: c
Streamed echo: k
Streamed echo:  
Streamed echo: b
Streamed echo: r
Streamed echo: o
Streamed echo: w
Streamed echo: n
Streamed echo:  
Streamed echo: f
Streamed echo: o
Streamed echo: x
Streamed echo:  
Streamed echo: j
Streamed echo: u
Streamed echo: m
Streamed echo: p
Streamed echo: e
Streamed echo: d
Streamed echo:  
Streamed echo: o
Streamed echo: v
Streamed echo: e
Streamed echo: r
Streamed echo:  
Streamed echo: t
Streamed echo: h
Streamed echo: e
Streamed echo:  
Streamed echo: l
Streamed echo: a
Streamed echo: z
Streamed echo: y
Streamed echo:  
Streamed echo: d
Streamed echo: o
Streamed echo: g
Streamed echo:  
Streamed echo: o
Streamed reverse echo: o
Streamed reverse echo:  
Streamed reverse echo: g
Streamed reverse echo: o
Streamed reverse echo: d
Streamed reverse echo:  
Streamed reverse echo: y
Streamed reverse echo: z
Streamed reverse echo: a
Streamed reverse echo: l
Streamed reverse echo:  
Streamed reverse echo: e
Streamed reverse echo: h
Streamed reverse echo: t
Streamed reverse echo:  
Streamed reverse echo: r
Streamed reverse echo: e
Streamed reverse echo: v
Streamed reverse echo: o
Streamed reverse echo:  
Streamed reverse echo: d
Streamed reverse echo: e
Streamed reverse echo: p
Streamed reverse echo: m
Streamed reverse echo: u
Streamed reverse echo: j
Streamed reverse echo:  
Streamed reverse echo: x
Streamed reverse echo: o
Streamed reverse echo: f
Streamed reverse echo:  
Streamed reverse echo: n
Streamed reverse echo: w
Streamed reverse echo: o
Streamed reverse echo: r
Streamed reverse echo: b
Streamed reverse echo:  
Streamed reverse echo: k
Streamed reverse echo: c
Streamed reverse echo: i
Streamed reverse echo: u
Streamed reverse echo: q
Streamed reverse echo:  
Streamed reverse echo: e
Streamed reverse echo: h
Streamed reverse echo: T
Last char 'o' count: 4



