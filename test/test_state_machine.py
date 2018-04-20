from testix.frequentlyused import *
import pytest
from aots import state_machine
import test_states

class TestStateMachine:
    @pytest.fixture
    def states( self ):
        STATES = 'Idle', 'Starting', 'Playing', 'Stopping'
        return [ FakeObject( state ) for state in STATES ]

    def test_machine_starts_with_null_state( self, states ):
        tested = state_machine.StateMachine( states )
        assert tested.current is None
