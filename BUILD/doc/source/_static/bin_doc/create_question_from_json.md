Create Question From JSON Readme
===========================

---------------------------
<a name='toc'>Table of contents:</a>

  * [Help for Create Question From JSON](#user-content-help-for-create-question-from-json)
  * [Export question id 1 as JSON](#user-content-export-question-id-1-as-json)
  * [Change name or url_regex in the JSON](#user-content-change-name-or-url_regex-in-the-json)
  * [Create a new question from the modified JSON file](#user-content-create-a-new-question-from-the-modified-json-file)

---------------------------

# Help for Create Question From JSON

  * Print the help for create_question_from_json.py
  * All scripts in bin/ will supply help if -h is on the command line
  * If passing in a parameter with a space or a special character, you need to surround it with quotes properly. On Windows this means double quotes. On Linux/Mac, this means single or double quotes, depending on what kind of character escaping you need.
  * If running this script on Linux or Mac, use the python scripts directly as the bin/create_question_from_json.py
  * If running this script on Windows, use the batch script in the winbin/create_question_from_json.bat so that python is called correctly.

```bash
create_question_from_json.py -h
```

```
usage: create_question_from_json.py [-h] [-u USERNAME] [-p PASSWORD]
                                    [--session_id SESSION_ID] [--host HOST]
                                    [--port PORT] [-l LOGLEVEL]
                                    [--debugformat] [--debug_method_locals]
                                    [--record_all_requests]
                                    [--stats_loop_enabled] [--http_auth_retry]
                                    [--http_retry_count HTTP_RETRY_COUNT]
                                    [--pytan_user_config PYTAN_USER_CONFIG]
                                    [--force_server_version FORCE_SERVER_VERSION]
                                    -j JSON_FILE

Create an object of type: question from a JSON file

optional arguments:
  -h, --help            show this help message and exit

Handler Authentication:
  -u USERNAME, --username USERNAME
                        Name of user (default: None)
  -p PASSWORD, --password PASSWORD
                        Password of user (default: None)
  --session_id SESSION_ID
                        Session ID to authenticate with instead of
                        username/password (default: None)
  --host HOST           Hostname/ip of SOAP Server (default: None)
  --port PORT           Port to use when connecting to SOAP Server (default:
                        443)

Handler Options:
  -l LOGLEVEL, --loglevel LOGLEVEL
                        Logging level to use, increase for more verbosity
                        (default: 0)
  --debugformat         Enable debug format for logging (default: False)
  --debug_method_locals
                        Enable debug logging for each methods local variables
                        (default: False)
  --record_all_requests
                        Record all requests in
                        handler.session.ALL_REQUESTS_RESPONSES (default:
                        False)
  --stats_loop_enabled  Enable the statistics loop (default: False)
  --http_auth_retry     Disable retry on HTTP authentication failures
                        (default: True)
  --http_retry_count HTTP_RETRY_COUNT
                        Retry count for HTTP failures/invalid responses
                        (default: 5)
  --pytan_user_config PYTAN_USER_CONFIG
                        PyTan User Config file to use for PyTan arguments
                        (defaults to: ~/.pytan_config.json) (default: )
  --force_server_version FORCE_SERVER_VERSION
                        Force PyTan to consider the server version as this,
                        instead of relying on the server version derived from
                        the server info page. (default: )

Create Question from JSON Options:
  -j JSON_FILE, --json JSON_FILE
                        JSON file to use for creating the object (default: )
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Export question id 1 as JSON

  * Get the first question object
  * Save the results to a JSON file

```bash
bin/get_question.py -u Administrator -p 'Tanium2015!' --host 10.0.1.240 --port 443 --loglevel 1 --id 1 --file "/tmp/out.json" --export_format json
```

```
PyTan v2.1.6 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
Found items:  QuestionList, len: 1
Report file '/tmp/out.json' written with 779 bytes
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: file_exist_contents
    * Valid: **True**
    * Messages: File /tmp/out.json exists, content:

```
{
  "_type": "questions", 
  "question": [
    {
      "_type": "question", 
      "action_tracking_flag": 0, 
      "context_group": {
        "_type": "group", 
        "id": 0
      }, 
...trimmed for brevity...
```

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Change name or url_regex in the JSON

  * Add CMDLINE TEST to name or url_regex in the JSON file

```bash
perl -p -i -e 's/^(      "(name|url_regex)": ".*)"/$1 CMDLINE TEST 3074"/gm' /tmp/out.json && cat /tmp/out.json
```

```
{
  "_type": "questions", 
  "question": [
    {
      "_type": "question", 
      "action_tracking_flag": 0, 
      "context_group": {
        "_type": "group", 
        "id": 0
      }, 
      "expiration": "2015-09-14T13:48:06", 
      "expire_seconds": 0, 
      "force_computer_id_flag": 0, 
      "hidden_flag": 0, 
      "id": 1, 
      "management_rights_group": {
        "_type": "group", 
        "id": 0
      }, 
      "query_text": "Get number of machines", 
      "saved_question": {
        "_type": "saved_question", 
        "id": 0
      }, 
      "selects": {
        "_type": "selects", 
        "select": []
      }, 
      "skip_lock_flag": 0, 
      "user": {
        "_type": "user", 
        "id": 1, 
        "name": "Administrator"
      }
    }
  ]
}
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: file_exist
    * Valid: **True**
    * Messages: File /tmp/out.json exists

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


# Create a new question from the modified JSON file

```bash
bin/create_question_from_json.py -u Administrator -p 'Tanium2015!' --host 10.0.1.240 --port 443 --loglevel 1 -j "/tmp/out.json"
```

```
PyTan v2.1.6 Handler for Session to 10.0.1.240:443, Authenticated: True, Platform Version: 6.5.314.4301
Created item: Question, id: 16107, ID: 16107
```

  * Validation Test: exitcode
    * Valid: **True**
    * Messages: Exit Code is 0

  * Validation Test: noerror
    * Valid: **True**
    * Messages: No error texts found in stderr/stdout



[TOC](#user-content-toc)


###### generated by: `build_bin_doc v2.1.0`, date: Fri Oct  2 16:06:22 2015 EDT, Contact info: **Jim Olsen <jim.olsen@tanium.com>**