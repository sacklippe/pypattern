"""
State pattern
-------------
Allows an object to alter its behavior when its internal state changes.
The object will appear to change its class.

src: https://refactoring.guru/design-patterns/state/python/example
"""
from __future__ import annotations

from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    _prev_state = None

    def __init__(self, state: State):
        """
        Initialise the initial state.

        Parameters
        ----------
        state : State
        """
        self.transition_to(state)

    @property
    def state(self) -> State:
        """Retreive state."""
        return self._state

    def transition_to(self, state: State) -> None:
        """
        Transit to another state.

        Parameters
        ----------
        state : State
        """
        assert isinstance(state, State), f"{state=}"
        print(f"{type(self).__name__}: Transition to {type(state).__name__}")
        self._prev_state = self._state
        self._state = state
        self._state.context = self

    def request(self) -> None:
        """Request state state handle."""
        self._state.handle()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    _context: Context = None

    @property
    def context(self) -> Context:
        """Return the state's context"""
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        """
        Set the state's context.

        Parameters
        ----------
        context : Context
        """
        assert isinstance(context, Context), f"{context=}"
        self._context = context

    @abstractmethod
    def handle(self) -> None:
        """Execute state logic."""
