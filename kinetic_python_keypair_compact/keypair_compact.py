from io import BufferedReader
from kinetic_python_keypair_compact.str_key import StrKey
from kinetic_python_keypair_compact.stellar_keypair import StellarKeypair
from kinetic_python_keypair_compact.base64 import base_64_to_byte_array
from kinetic_sdk import Keypair

class KeypairCompact:

    @staticmethod
    def from_secret(secret: str) -> StellarKeypair:
        try:
            return KeypairCompact.from_string(secret)
        except:
            return KeypairCompact.from_base_58(secret)


    @staticmethod
    def from_string(seed: str) -> StellarKeypair:
        if seed[0] == 'S' and len(seed == 56:
            return StellarKeypair.from_secret_keypair(seed);

        return StellarKeypair.from_raw_ed_25519_seed(Buffer.from(seed, 'hex'));


    @staticmethod
    def from_base_58(seed: str) -> StellarKeypair:
        const decoded58 = bs58.decode(seed);

        if len(decoded58) == 32:
            return StellarKeypair.from_raw_ed_25519_seed(Buffer.from(decoded58))

        raise Exception('seed is not a valid base58-encoded secret seed')


    @staticmethod
    def get_keypair(secret_key) -> Keypair:
        skp = KeypairCompact.from_secret(secret_key);
        public_key = StrKey.encode_ed25519_public_key(skp.raw_public_key());

        secret_hex = hex_to_32.decode(skp.secret());
        public_hex = hex_to_32.decode(public_key);
        secret_hex_cut = secret_hex.slice(2, -4);
        public_hex_cut = public_hex.slice(2, -4);

        joined = secret_hex_cut + public_hex_cut;
        joined64 = BufferedReader(joined, 'hex').toString('base64');

        base_64_byte_array = base_64_to_byte_array(joined64)

        return Keypair.from_byte_array(base_64_byte_array)
