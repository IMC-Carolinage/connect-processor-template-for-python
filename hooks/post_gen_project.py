# -*- coding: utf-8 -*-

# This file is part of the Ingram Micro Cloud Blue Connect Report Python Boilerplate.
# Copyright (c) 2019-2020 Ingram Micro. All Rights Reserved.

import os
import shutil
import string
import sys
import pathlib

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_license():
        os.remove('LICENSE')

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

def main():
    if '{{ cookiecutter.license }}' == 'Other, not Open-source':
        remove_license()
    
    if '{{ cookiecutter.Require_subscription_change_usecase }}'.lower() == 'n':
        c_file = os.path.join('connect_processor','app','change.py')
        remove_file(c_file)
        c_file = os.path.join('tests', 'test_change.py')
        remove_file(c_file)

    if '{{ cookiecutter.Require_subscription_cancel_usecase }}'.lower() == 'n':
        c_file = os.path.join('connect_processor', 'app', 'cancel.py')
        remove_file(c_file)

    if '{{ cookiecutter.Require_subscription_suspend_and_resume_usecases }}'.lower() == 'n':
        c_file = os.path.join('connect_processor', 'app', 'suspend.py')
        remove_file(c_file)
        c_file = os.path.join('connect_processor', 'app', 'resume.py')
        remove_file(c_file)

    if '{{ cookiecutter.Require_usage_reporting_for_Pay_as_you_go_usecase }}'.lower() == 'n':
        c_file = os.path.join('connect_processor', 'app', 'report_usage.py')
        remove_file(c_file)
        c_file = os.path.join('tests', 'test_report_usage.py')
        remove_file(c_file)

    if '{{ cookiecutter.Require_dynamic_validation_of_ordering_parameters_for_subscription }}'.lower() == 'n':
        c_file = os.path.join('connect_processor', 'app', 'dynamic_validation.py')
        remove_file(c_file)

    if '{{ cookiecutter.Require_reseller_information_for_provisioning }}'.lower() == 'n':
        c_file = os.path.join('connect_processor', 'app', 'tier_fulfillment.py')
        remove_file(c_file)

    print('Done! Your report project is ready to go!')

if __name__ == '__main__':
    main()
