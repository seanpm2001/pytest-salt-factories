"""
Test the ``salt-ssh`` CLI functionality.
"""
import pathlib


def test_version_info(salt_master, salt_version):
    cli = salt_master.salt_ssh_cli()
    ret = cli.run("--version")
    assert ret.returncode == 0, ret
    assert ret.stdout.strip() == f"{pathlib.Path(cli.script_name).name} {salt_version}"
