class StateMachine:
    def __init__( self, initialState ):
        self._current = None
        self._enter( initialState, None )

    def _enter( self, stateClass, reason ):
        state = stateClass()
        state.enter( self._current, reason )
        self._current = state

    @property
    def current( self ):
        return self._current
