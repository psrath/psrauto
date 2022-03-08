#!/usr/bin/python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import time

class SendReportEmail:

    def __init__(self,subject,to,report_path,report_file_name,log_file):
        self.subject=subject
        self.to=to.split(",")
        self.report_path=report_path
        self.report_file_name=report_file_name
        self.log_file = log_file

    def send_mail(self):
        module_command = "awk '/short test summary info/,/deselected/' "+self.log_file+" | grep -v \"======\" | grep -o -P " \
                                                                                              "'(" \
                         "?<=\.\./).*(" \
                         "?=\ - TC)' | sort -u | awk -F\"/\" '{print $NF}'"

        passed_command = "awk '/short test summary info/,/deselected/' "+self.log_file+" | grep -c \"PASSED\""
        failed_command = "awk '/short test summary info/,/deselected/' "+self.log_file+" | grep -c \"FAIL\""
        skipped_command = "awk '/short test summary info/,/deselected/' "+self.log_file+" | grep -c \"SKIP\""
        duration_command= "grep seconds "+self.log_file+" |  grep -o -P '(?<= in ).*(?=seconds)'"

        p_module = os.popen(module_command)
        module_name = str(p_module.read())
        p_passed = os.popen(passed_command)
        passed_cnt = str(p_passed.read())
        p_failed = os.popen(failed_command)
        failed_cnt = str(p_failed.read())
        p_skipped = os.popen(skipped_command)
        skipped_cnt = str(p_skipped.read())
        p_duration = os.popen(duration_command)
        duration = p_duration.read()
        SUBJECT = self.subject
        msg = MIMEMultipart()
        msg['Subject'] = SUBJECT
        msg['From'] = "abcd@gmail.com"
        msg['To'] = ', '.join(self.to)
        html = """\
        <html>
          <head></head>
          <body>
          <table>
            <tr><td><b>Hi All,</b></td></tr>
            <tr><td>Please Find attached report of ABC Service</td></tr>
            <tr><td><i>Download the report to view in proper format</i></td></tr>
            <tr><td><br></td></tr>
            <tr><td><table style="width: 594px; height: 61px;">
<tbody>
<tr style="height: 21px;">
<td style="width: 593px; text-align: center; height: 21px; background-color: #00ccff;" colspan="5"><strong>Summary</strong></td>
</tr>
<tr style="height: 21px; background-color: #00ffff;">
<td style="width: 224px; text-align: center; height: 21px;"><strong>Module</strong></td>
<td style="width: 70px; text-align: center; height: 21px;"><strong>Passed</strong></td>
<td style="width: 70px; text-align: center; height: 21px;"><strong>Failed</strong></td>
<td style="width: 70px; text-align: center; height: 21px;"><strong>Skipped</strong></td>
<td style="width: 70px; text-align: center; height: 21px;"><strong>Duration</strong></td>
</tr>
<tr style="height: 20px; background-color: #a1ebeb;">
<td style="width: 224px; text-align: center; height: 20px;">"""+module_name+"""</span></td>
<td style="width: 70px; text-align: center; height: 20px;"><h3><span style="color: 
#008000;"><strong>"""+passed_cnt+"""<strong></span></h3></td>
<td style="width: 70px; text-align: center; height: 20px;"><h3><span style="color: 
#ff0000;"><strong>"""+failed_cnt+"""<strong></span></h3></td>
<td style="width: 70px; text-align: center; height: 20px;"><h3><span style="color: 
#ff6600;"><strong>"""+skipped_cnt+"""<strong></span></h3></td>
<td style="width: 70px; text-align: center; height: 20px;">"""+str(time.strftime("%H:%M:%S", time.gmtime(
            int(float(duration)))))+"""</td>
</tr>
</tbody>
</table>
 </td></tr>
            <tr><td><br>
            Thanks,
            <br>
            Purnendu Rath
            </td></tr>
            </table>
          </body>
        </html>
        """
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(self.report_path, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="'+self.report_file_name+'"')
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        msg.attach(part)
        server = smtplib.SMTP('localhost')
        server.sendmail(msg['From'], self.to, msg.as_string())

#send_mail ("ABC-Report","parath@hotmail","/API_Automation/automation/reports/report.html")
