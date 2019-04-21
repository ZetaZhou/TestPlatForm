from xml.etree import ElementTree as ET
from lxml import etree

from .CommonConfig import *


class TestReport(CommonConfig):
    """description of class"""

    def __init__(self):
        super().__init__()
        self.reportfile = self.result_dir + "\TestResult_" + self.today + ".html"

    # Create init test report file
    def CreateHtmlFile(self):
        if os.path.exists(self.reportfile) == False:
            f = open(self.reportfile, 'w')
            message = """<html>
            <head>    
                <title>Automation Test Result</title>
                <style>
                    table {
			                border-collapse: collapse;
			                padding: 15px;
			                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
		                    }
							.tem{
							  background-color: #4F94CD;
							}
							.tem th{
							  color: white;
							}
		            th{
			          
			            color: #333;
			            border: 1px solid #ddd;
			            padding-bottom: 15px;
			            padding-top: 15px;
		            }
		            tr{
			            border: 1px solid #008000;
			            padding-bottom: 8px;
			            padding-top: 8px;
			            text-align: left;
		            }
                    td{
                        border: 1px solid #008000;
                    } 
                </style>
            </head>
            <body>
                <h1>Automation Test Result</h1>
                <table>
                    <tr class='tem'>
                        <th>CaseId</th>
                        <th>Name</th>
                        <th>ModuleName</th>
                        <th>Owner</th>
                        <th>Result</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>Duration(s)</th>
                        <th>ErrorMessage</th>
                   </tr>
                </table>
            </body>
            </html>
            """
            f.write(message)
            f.close()

    def WriteHTML(self, testcaseinfodict):
        self.CreateHtmlFile()

        testcaseinfo_dict = testcaseinfodict

        f = open(self.reportfile, "r")
        htmlcontent = f.read()
        f.close()

        body = etree.fromstring(htmlcontent.encode('utf-8'))
        table = body.cssselect('table')[0]
        tr = etree.SubElement(table, 'tr')

        for key, value in testcaseinfo_dict.items():
            if key == "ADDR":
                break

            td = etree.SubElement(tr, 'td')
            if key == 'TEST_RESULT' and value != 'PASS':
                td.set('bgcolor', 'red')
                td.set('color', 'white')

            try:
                # td.text = str(value).encode('utf-8')
                td.text = str(value)
            except Exception:
                print(traceback.format_exc())

        f = open(self.reportfile, 'w+')
        f.write(etree.tostring(body).decode('utf-8'))
        f.close()
