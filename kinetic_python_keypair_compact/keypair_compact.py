class KeypairCompact:

    @staticmethod
    def from_secret(secret: str):
        try:
            return KeypairCompact.from_string(secret)
        except:
            return KeypairCompact.from_base_58(secret)


    @staticmethod
    def from_string(seed: str):
        pass


    @staticmethod
    def from_base_58(seed: str):
        pass


    @staticmethod
    def get_keypair(secret_key):
        pass
