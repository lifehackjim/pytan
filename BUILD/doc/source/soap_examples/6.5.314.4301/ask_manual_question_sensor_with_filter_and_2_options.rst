
Ask Manual Question Sensor With Filter And 2 Options
==========================================================================================

Ask the question 'Get Operating System containing "Windows" from all machines' and set max_age_seconds to 3600 and value_type to 1 on the Operating System sensor, then wait for result data to be complete, and get result data


Step 1 - Authenticate to the SOAP API via /auth
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/auth
* HTTP Method: GET
* Elapsed Time: 0:00:00.008899
* `Step 1 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_1_request.txt>`_
* `Step 1 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_1_response.txt>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip, deflate", 
      "Connection": "keep-alive", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "password": "VGFuaXVtMjAxNSE=", 
      "username": "QWRtaW5pc3RyYXRvcg=="
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "135", 
      "content-type": "text/plain; charset=us-ascii"
    }


Step 2 - Get the server version via /info.json
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/info.json
* HTTP Method: GET
* Elapsed Time: 0:00:00.014913
* `Step 2 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_2_request.txt>`_
* `Step 2 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_2_response.json>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip, deflate", 
      "Connection": "keep-alive", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "88017", 
      "content-type": "application/json"
    }


Step 3 - Issue a GetObject to get the full object of a sensor for inclusion in a Select for a Question
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.002268
* `Step 3 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_3_request.xml>`_
* `Step 3 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_3_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "568", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 4 - Issue an AddObject to add a Question object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.009065
* `Step 4 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_4_request.xml>`_
* `Step 4 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_4_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "784", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-length": "769", 
      "content-type": "text/xml;charset=UTF-8"
    }


Step 5 - Issue a GetObject on the recently added object in order to get the full object
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.013911
* `Step 5 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_5_request.xml>`_
* `Step 5 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_5_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "494", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 6 - Issue a GetResultInfo for a Question to check the current progress of answers
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.001928
* `Step 6 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_6_request.xml>`_
* `Step 6 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_6_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "498", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 7 - Issue a GetResultInfo for a Question to check the current progress of answers
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.002026
* `Step 7 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_7_request.xml>`_
* `Step 7 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_7_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "498", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 8 - Issue a GetResultInfo for a Question to check the current progress of answers
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.002111
* `Step 8 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_8_request.xml>`_
* `Step 8 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_8_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "498", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


Step 9 - Issue a GetResultData to get answers for a question
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

* URL: https://10.0.1.240:443/soap
* HTTP Method: POST
* Elapsed Time: 0:00:00.001795
* `Step 9 Request Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_9_request.xml>`_
* `Step 9 Response Body <../_static/soap_outputs/ask_manual_question_sensor_with_filter_and_2_options_step_9_response.xml>`_

* Request Headers:

.. code-block:: json
    :linenos:

    
    {
      "Accept": "*/*", 
      "Accept-Encoding": "gzip", 
      "Connection": "keep-alive", 
      "Content-Length": "526", 
      "Content-Type": "text/xml; charset=utf-8", 
      "User-Agent": "python-requests/2.6.0 CPython/2.7.10 Darwin/14.5.0", 
      "session": "1-6993-17fa9da998b1727bf636c12c4388c86cbd275fef1bcd8dd676fb15b62a9a60e410dca9d5d481c6f38eb50ca6e5f5570459b9312dc8c16f8f7f6761b989a4e91e"
    }

* Response Headers:

.. code-block:: json
    :linenos:

    
    {
      "connection": "keep-alive", 
      "content-encoding": "gzip", 
      "content-type": "text/xml;charset=UTF-8", 
      "transfer-encoding": "chunked"
    }


.. rubric:: Footnotes

.. [#] this file automatically created by BUILD/build_api_examples.py