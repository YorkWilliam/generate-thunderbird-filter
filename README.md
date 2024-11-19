# generate-thunderbird-filter

It's a python script that generates thunderbird filter files to be imported

## How to use

### Step 1: Gather your rules
I filter incoming emails
- into folders
- according to keywords in sender addresses
- using "OR"

I gather the filters like the following example.
```json
{
    "protocal": "imap",
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
```
**You can treak the script to suit your need.**

### Step 2: Run the script
`python3 generate.py -i inputfile -o msgFilterRules.dat`

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
