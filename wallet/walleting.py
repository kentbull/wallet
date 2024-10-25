class WalletError(Exception):
    """Base class for exceptions in Wallet."""

    pass


class OldKeystoreError(WalletError):
    """Raised when an old keystore is detected."""

    pass
