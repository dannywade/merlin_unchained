# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import yaml
import time
import json
import shutil
import logging
import requests
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from general_functionalities import ParseShowCommandFunction
from datetime import datetime
from merlin.models import Serail2ContractCredentials, Serial2Contract

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect(learn_hostname=True)

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed:
            # Show Version to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = Serail2ContractCredentials.objects.all().values('key')
                    db_user = Serail2ContractCredentials.objects.all().values('client_secret')
                    serial2contract_api_username = db_key[0]['key']
                    serial2contract_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (serial2contract_api_username,serial2contract_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Serial 2 Contract using each serial number and Oauth token




                with steps.start('Calling API',continue_=True) as step:
                    try:
                        serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/SAL210302JA", headers=oauth_headers)
                        # serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % serial, headers=oauth_headers)
                    except Exception as e:
                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                    serial2contract_json = serial2contract_raw.json()

                    serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,
                    
                    
                    
                    ,timestamp=datetime.now().replace(microsecond=0))
                        
                    serial2contract.save()