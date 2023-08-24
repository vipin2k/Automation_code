cd ..
echo %cd%
python -m pytest -s -v --env dev %cd%/TestCases/testsuites/test_sample.py --html=Reports/htmlreports/Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/allurereports
REM python -m pytest -s -v --env dev %cd%/TestCases/testsuites/test_request.py --html=Reports/htmlreports/Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/allurereports
REM python -m pytest -s -v --env dev %cd%/TestCases/testsuites/test_url_06.py --html=Reports/htmlreports/Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/allurereports