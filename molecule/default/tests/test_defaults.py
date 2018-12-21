import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
files = [
    '/etc/hosts.allow',
    '/etc/hosts.deny',
]


@pytest.mark.parametrize('file', files)
def test_configuration_file_exists(host, file):
    file = host.file(file)
    assert file.exists


@pytest.mark.parametrize('cmd, expected', [
  ("grep 'sshd: ALL' /etc/hosts.allow", 0),
])
def test_hosts_allow_contains_sshd(host, cmd, expected):
    result = host.run(cmd)
    assert result.rc == expected


@pytest.mark.parametrize('cmd, expected', [
  ("grep 'ALL: ALL' /etc/hosts.allow", 1),
])
def test_hosts_allow_not_contains_all_connections(host, cmd, expected):
    result = host.run(cmd)
    assert result.rc == expected


@pytest.mark.parametrize('cmd, expected', [
  ("grep 'vsftpd: ALL' /etc/hosts.deny", 1),
])
def test_hosts_deny_not_contains_vsftpd(host, cmd, expected):
    result = host.run(cmd)
    assert result.rc == expected


@pytest.mark.parametrize('cmd, expected', [
  ("grep 'ALL: ALL' /etc/hosts.deny", 0),
])
def test_hosts_deny_contains_all_connections(host, cmd, expected):
    result = host.run(cmd)
    assert result.rc == expected
