# generate-thunderbird-filter

It's a python script that generates thunderbird filter files to be imported

## How to use

### Step 1: Gather your rules
- gather your rules
- store them into an inputfile
- **tweak the script if you have different needs**

#### example
- I filter incoming emails into folders if the sender address contains any keywords
- I create a `json` file as follows:
```json
{
    "protocol": "imap",
    "email": "me@proton.me",
    "server": "127.0.0.1",
    "folderdir": "Folders/Notifications",
    "filters": {
        "Tech": [
            "apple.com",
            "live.com",
            "google.com",
            "proton.me"
        ],
        "Streaming": [
            "youtube.com",
            "netflix.com"
        ]
    }
}
```
- Running the script would result in the following:
```dat
version="9"
logging="yes"
name="Streaming"
enabled="yes"
type="17"
action="Move to folder"
actionValue="imap://me%40proton.me@127.0.0.1/Folders/Notifications/Streaming"
condition="OR (from,contains,youtube.com) OR (from,contains,netflix.com)"
name="Tech"
enabled="yes"
type="17"
action="Move to folder"
actionValue="imap://me%40proton.me@127.0.0.1/Folders/Notifications/Tech"
condition="OR (from,contains,apple.com) OR (from,contains,live.com) OR (from,contains,google.com) OR (from,contains,proton.me)"
```

### Step 2: Run the script
- run `python3 generate.py -i inputfile -o msgFilterRules.dat`

### Step 3: Import the generate rule file
- if you are filtering emails into folders, check if the target folders exist
- locate where Thunderbird puts the rules
    - on MacOS: `~/Library/Thunderbird/Profiles/<something>.default-esr/<protocal>/<server>`
- verify it's the correct location
    - you should be able to see `msgFilterRules.dat` there
    - better create some random rules to see if it is the exact file
- quit Thunderbird
- **back up** the old msgFilterRules.dat if there are any rules that you have been using
- copy the generated `msgFilterRules.dat` there
- reopen Thunderbird

### Step 4: Verify that the rules are properly imported
- open Thunderbird
- open rules, see if they are properly imported
- move some **unimportant** emails into the inbox folder to see if the rules work as intended
