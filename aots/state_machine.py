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

    def event( self, event ):
        nextState = self._current.next( event )
        if nextState is None:
            return
        self._enter( nextState, event )
