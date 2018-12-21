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


@pytest.mark.parametrize('file', files[0])
def test_hosts_allow_contains_sshd(host, file):
    cmd = "grep 'sshd: ALL' " + file
    result = host.run(cmd)
    assert result.rc == 0


@pytest.mark.parametrize('file', files[0])
def test_hosts_allow_not_contains_all_connections(host, file):
    cmd = "grep 'ALL: ALL' " + file
    result = host.run(cmd)
    assert result.rc == 1


@pytest.mark.parametrize('file', files[1])
def test_hosts_deny_not_contains_vsftpd(host, file):
    cmd = "grep 'sshd: ALL' " + file
    result = host.run(cmd)
    assert result.rc == 1


@pytest.mark.parametrize('file', files[1])
def test_hosts_deny_contains_all_connections(host, file):
    cmd = "grep 'ALL: ALL' " + file
    result = host.run(cmd)
    assert result.rc == 2
