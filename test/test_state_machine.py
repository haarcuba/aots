from testix.frequentlyused import *
import pytest
from aots import state_machine

class TestStateMachine:
    def test_machine_starts_with_initial_state( self ):
        with Scenario() as scenario:
            scenario <<\
                Call( 'Idle' ).returns( FakeObject( 'idle' ) ) <<\
                Call( 'idle.enter', None, None )

            tested = state_machine.StateMachine( FakeObject( 'Idle' ) )
            assert tested.current is FakeObject( 'idle' )
