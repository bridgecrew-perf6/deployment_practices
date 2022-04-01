#to install vault in your environment,  check https://phoenixnap.com/kb/how-to-install-vault-ubuntu

from vaultlib import vaultlib


def connection_to_vault_server(self):
    """
    This method is connects with Vault Server and read application configurations
    :return: raise ValueError exception (failure)
    """

    try:
        self.vault_conn = vaultlib.Vault(
            self.get_env_cfg("VAULT_URL"),
            self.get_env_cfg("VAULT_PORT"),
            self.get_env_cfg("VAULT_TOKEN"),
        )
        if self.vault_conn.authenticated():
            self.logger.info(
                f"Successfully connected to Vault Server "
                f"{self.get_env_cfg('VAULT_URL')}:{self.get_env_cfg('VAULT_PORT')}."
            )
        else:
            self.logger.error(
                f"Failed to connect Vault Server "
                f"{self.get_env_cfg('VAULT_URL')}:{self.get_env_cfg('VAULT_PORT')}"
            )
            raise ValueError(
                f"Failed to connect Vault Server "
                f"{self.get_env_cfg('VAULT_URL')}:{self.get_env_cfg('VAULT_PORT')}"
            )

        vault_app_cfg = self.vault_conn.read_secret(
            self.get_env_cfg("VAULT_SECRET_PATH"),
            self.get_env_cfg("VAULT_MOUNT_PATH"),
            key_name=self.get_app_name(),
        )
        self.set_app_cfg(json.loads(vault_app_cfg))

        vault_general_cfg = self.vault_conn.read_secret(
            self.get_env_cfg("VAULT_GENERAL_CONFIG"),
            self.get_env_cfg("VAULT_GENERAL_MOUNT_PATH"),
        )
        self.set_general_cfg(json.loads(vault_general_cfg))
    except Exception as ex:
        self.logger.error(
            f"Exception while reading data from vault {sys.exc_info()[-1].tb_lineno}:{repr(ex)}"
        )
        raise ValueError(
            f"Exception while reading data from vault {sys.exc_info()[-1].tb_lineno}:{repr(ex)}"
        )
