def verify_checksum(expected: any, actual: any):
    pass


class StrKey:
    """ StrKey is a helper class that allows encoding and decoding strkey. """
    
    @staticmethod
    def encode_ed25519_public_key(data) -> str:
        """ 
        Encodes data to strkey ed25519 public key.
        @param {Buffer} data data to encode
        @returns {string}
        """
        pass
    }

    @staticmethod
    def encode_ed25519_secret_seed(data) -> str:
        """
        Encodes data to strkey ed25519 seed.
        @param {Buffer} data data to encode
        @returns {string}
        """
        pass
    }

    @staticmethod
    def decodeEd25519SecretSeed(data: str) -> str:
        """
        Decodes strkey ed25519 seed to raw data.
        @param {string} data data to decode
        @returns {Buffer}
        """
        pass


def decode_check(versionByteName: str, encoded):
    pass


def encodeCheck(version_byte_name: str, data):
    pass


def calculate_checksum(payload):
    # This code calculates CRC16-XModem checksum of payload
    # and returns it as Buffer in little-endian order.
    pass