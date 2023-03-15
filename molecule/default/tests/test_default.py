#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_phpinfo(host):
	cmd = host.run("curl -v -L --fail http://localhost/matomo/")
	print(cmd.stdout)
	assert 'HTTP/1.1 200 OK' in cmd.stderr
	assert "Matomo" in cmd.stdout
