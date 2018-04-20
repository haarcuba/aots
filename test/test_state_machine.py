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

    def test_machine_goes_through_two_states( self ):
        with Scenario() as scenario:
            scenario <<\
                Call( 'Idle' ).returns( FakeObject( 'idle' ) ) <<\
                Call( 'idle.enter', None, None )

            tested = state_machine.StateMachine( FakeObject( 'Idle' ) )
            assert tested.current is FakeObject( 'idle' )

        with Scenario() as scenario:
            scenario <<\
                Call( 'idle.next', FakeObject( 'someEvent' ) ).returns( FakeObject( 'Starting' ) ) <<\
                Call( 'Starting' ).returns( FakeObject( 'starting' ) ) <<\
                Call( 'starting.enter', FakeObject( 'idle' ), FakeObject( 'someEvent' ) )

            tested.event( FakeObject( 'someEvent' ) )
            assert tested.current is FakeObject( 'starting' )

    def test_event_ignored_state_stays_the_same( self ):
        with Scenario() as scenario:
            scenario <<\
                Call( 'Idle' ).returns( FakeObject( 'idle' ) ) <<\
                Call( 'idle.enter', None, None )

            tested = state_machine.StateMachine( FakeObject( 'Idle' ) )
            assert tested.current is FakeObject( 'idle' )

        with Scenario() as scenario:
            scenario <<\
                Call( 'idle.next', FakeObject( 'someEvent' ) ).returns( None )

            tested.event( FakeObject( 'someEvent' ) )
            assert tested.current is FakeObject( 'idle' )
