class StellarKeypair:

    type
    secret_seed
    secret_key
    public_key

    def __init__(self, keys):
        self.type = keys.type
        self.secret_seed = keys.secret_key
        self.secret_key = keys.secret_key
        self.public_key = keys.public_key


    @staticmethod
    def from_secret_keypair(secret: str):
        """
        Creates a new `Keypair` instance from secret. This can either be secret key or secret seed depending
        on underlying public-key signature system. Currently `Keypair` only supports ed25519.
        @param {string} secret secret key (ex. `SDAKFNYEIAORZKKCYRILFQKLLOCNPL5SWJ3YY5NM3ZH6GJSZGXHZEPQS`)
        @returns {StellarKeypair}
        """
        pass


    @staticmethod
    def from_raw_ed_25519_seed(raw_reed):
        """
        Creates a new `Keypair` object from ed25519 secret key seed raw bytes.
        @param {Buffer} rawSeed Raw 32-byte ed25519 secret key seed
        @returns {StellarKeypair}
        """
        pass  


    def raw_public_key():
        """
        Returns raw public key
        @returns {Buffer}
        """
        pass

    def secret() -> str:
        """
        Returns secret key associated with this `Keypair` object
        @returns {string}
        """
        pass
