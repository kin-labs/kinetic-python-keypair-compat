from kinetic_python_keypair_compact.keypair_compact import KeypairCompact

class TestKeypairCompact:

    def test_should_work_with_stellar_seed(self):
        """Test Stellar Seed """
        kp = KeypairCompact()
        kp.get_keypair('SBB3CCFLL5WKQE2ZPRHSULEFL2623BNDYPHTJVEEXJCTOYNBOZHZUFEF')
        assert kp.public_key == 'HeDZgu4ee1PJiU7EB2oBFFphBAcUDk5MXgaDBzmDrTEQ'


    def test_should_work_with_stellar_seed_b58_encoded(self):
        """Test Stellar Seed b58 encoded"""
        kp = KeypairCompact()
        kp.get_keypair('9huFHrW6zfQvHsJXLvzDuQGFRyWL7YJ39vTkib63CDXj')
        assert kp.public_key == 'FrHoAVJXuXtkfHuyzG8uvfRherAK1pRehu9kGkvcgj6r'

