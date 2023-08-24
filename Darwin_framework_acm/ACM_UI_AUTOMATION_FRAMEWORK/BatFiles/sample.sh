cd ..
echo %cd%
python3.7 -m pytest -s -v ${PWD}/TestCases/testsuites/test_sample.py --html=Reports/htmlreports/Report.html --self-contained-html --capture=sys --show-capture=log --alluredir=Reports/allurereports