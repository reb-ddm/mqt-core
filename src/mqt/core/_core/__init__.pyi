from collections.abc import Iterable, Iterator, Mapping, MutableMapping, MutableSequence, Sequence
from os import PathLike
from typing import overload

from .._compat.typing import Self
from .operations import Control, Operation, OpType
from .symbolic import Expression, Variable

class Permutation(MutableMapping[int, int]):
    def __getitem__(self: Self, idx: int) -> int: ...
    def __setitem__(self: Self, idx: int, val: int) -> None: ...
    def __delitem__(self: Self, key: int) -> None: ...
    def __iter__(self: Self) -> Iterator[int]: ...
    def __len__(self: Self) -> int: ...
    @overload
    def apply(self: Self, controls: set[Control]) -> set[Control]: ...
    @overload
    def apply(self: Self, targets: list[int]) -> list[int]: ...

class QuantumComputation(MutableSequence[Operation]):
    # --------------------------------------------------------------------------
    #                               Constructors
    # --------------------------------------------------------------------------

    @overload
    def __init__(self: Self) -> None: ...
    @overload
    def __init__(self: Self, nq: int, nc: int = 0) -> None: ...
    @overload
    def __init__(self: Self, filename: str | PathLike[str]) -> None: ...
    @staticmethod
    def from_qasm(qasm: str) -> QuantumComputation: ...

    # --------------------------------------------------------------------------
    #                          General Properties
    # --------------------------------------------------------------------------

    name: str
    global_phase: float

    @property
    def num_qubits(self: Self) -> int: ...
    @property
    def num_ancilla_qubits(self: Self) -> int: ...
    @property
    def num_qubits_without_ancilla_qubits(self: Self) -> int: ...
    @property
    def num_classical_bits(self: Self) -> int: ...
    @property
    def num_ops(self: Self) -> int: ...
    def num_single_qubit_ops(self: Self) -> int: ...
    @property
    def num_total_ops(self: Self) -> int: ...
    def depth(self: Self) -> int: ...
    def invert(self: Self) -> None: ...
    def to_operation(self: Self) -> Operation: ...

    # --------------------------------------------------------------------------
    #                 Mutable Sequence Interface
    # --------------------------------------------------------------------------

    def __len__(self: Self) -> int: ...
    @overload
    def __getitem__(self: Self, idx: int) -> Operation: ...
    @overload
    def __getitem__(self: Self, idx: slice) -> list[Operation]: ...
    @overload
    def __setitem__(self: Self, idx: int, op: Operation) -> None: ...
    @overload
    def __setitem__(self: Self, idx: slice, ops: Iterable[Operation]) -> None: ...
    @overload
    def __delitem__(self: Self, idx: int) -> None: ...
    @overload
    def __delitem__(self: Self, idx: slice) -> None: ...
    def insert(self: Self, idx: int, op: Operation) -> None: ...
    def append(self: Self, op: Operation) -> None: ...
    def reverse(self: Self) -> None: ...
    def clear(self: Self) -> None: ...

    # --------------------------------------------------------------------------
    #                          (Qu)Bit Registers
    # --------------------------------------------------------------------------

    def add_ancillary_register(self: Self, n: int, name: str = "q") -> None: ...
    def add_classical_register(self: Self, n: int, name: str = "c") -> None: ...
    def add_qubit_register(self: Self, n: int, name: str = "anc") -> None: ...
    def unify_quantum_registers(self: Self, name: str = "q") -> None: ...

    # --------------------------------------------------------------------------
    #                  Initial Layout and Output Permutation
    # --------------------------------------------------------------------------

    initial_layout: Permutation
    output_permutation: Permutation

    def initialize_io_mapping(self: Self) -> None: ...

    # --------------------------------------------------------------------------
    #                       Ancilla and Garbage Handling
    # --------------------------------------------------------------------------

    @property
    def ancillary(self: Self) -> list[bool]: ...
    def set_circuit_qubit_ancillary(self: Self, q: int) -> None: ...
    def is_circuit_qubit_ancillary(self: Self, q: int) -> bool: ...
    @property
    def garbage(self: Self) -> list[bool]: ...
    def set_circuit_qubit_garbage(self: Self, q: int) -> None: ...
    def is_circuit_qubit_garbage(self: Self, q: int) -> bool: ...

    # --------------------------------------------------------------------------
    #                        Symbolic Circuit Handling
    # --------------------------------------------------------------------------

    @property
    def variables(self: Self) -> set[Variable]: ...
    def add_variable(self: Self, var: Expression | float) -> None: ...
    def add_variables(self: Self, vars_: Sequence[Expression | float]) -> None: ...
    def is_variable_free(self: Self) -> bool: ...
    def instantiate(self: Self, assignment: Mapping[Variable, float]) -> None: ...

    # --------------------------------------------------------------------------
    #                             Output Handling
    # --------------------------------------------------------------------------

    def qasm2_str(self: Self) -> str: ...
    def qasm2(self: Self, filename: PathLike[str]) -> None: ...
    def qasm3_str(self: Self) -> str: ...
    def qasm3(self: Self, filename: PathLike[str]) -> None: ...

    # --------------------------------------------------------------------------
    #                               Operations
    # --------------------------------------------------------------------------

    def i(self: Self, q: int) -> None: ...
    def ci(self: Self, control: Control | int, target: int) -> None: ...
    def mci(self: Self, controls: set[Control | int], target: int) -> None: ...
    def x(self: Self, q: int) -> None: ...
    def cx(self: Self, control: Control | int, target: int) -> None: ...
    def mcx(self: Self, controls: set[Control | int], target: int) -> None: ...
    def y(self: Self, q: int) -> None: ...
    def cy(self: Self, control: Control | int, target: int) -> None: ...
    def mcy(self: Self, controls: set[Control | int], target: int) -> None: ...
    def z(self: Self, q: int) -> None: ...
    def cz(self: Self, control: Control | int, target: int) -> None: ...
    def mcz(self: Self, controls: set[Control | int], target: int) -> None: ...
    def h(self: Self, q: int) -> None: ...
    def ch(self: Self, control: Control | int, target: int) -> None: ...
    def mch(self: Self, controls: set[Control | int], target: int) -> None: ...
    def s(self: Self, q: int) -> None: ...
    def cs(self: Self, control: Control | int, target: int) -> None: ...
    def mcs(self: Self, controls: set[Control | int], target: int) -> None: ...
    def sdg(self: Self, q: int) -> None: ...
    def csdg(self: Self, control: Control | int, target: int) -> None: ...
    def mcsdg(self: Self, controls: set[Control | int], target: int) -> None: ...
    def t(self: Self, q: int) -> None: ...
    def ct(self: Self, control: Control | int, target: int) -> None: ...
    def mct(self: Self, controls: set[Control | int], target: int) -> None: ...
    def tdg(self: Self, q: int) -> None: ...
    def ctdg(self: Self, control: Control | int, target: int) -> None: ...
    def mctdg(self: Self, controls: set[Control | int], target: int) -> None: ...
    def v(self: Self, q: int) -> None: ...
    def cv(self: Self, control: Control | int, target: int) -> None: ...
    def mcv(self: Self, controls: set[Control | int], target: int) -> None: ...
    def vdg(self: Self, q: int) -> None: ...
    def cvdg(self: Self, control: Control | int, target: int) -> None: ...
    def mcvdg(self: Self, controls: set[Control | int], target: int) -> None: ...
    def sx(self: Self, q: int) -> None: ...
    def csx(self: Self, control: Control | int, target: int) -> None: ...
    def mcsx(self: Self, controls: set[Control | int], target: int) -> None: ...
    def sxdg(self: Self, q: int) -> None: ...
    def csxdg(self: Self, control: Control | int, target: int) -> None: ...
    def mcsxdg(self: Self, controls: set[Control | int], target: int) -> None: ...
    def rx(self: Self, theta: float | Expression, q: int) -> None: ...
    def crx(self: Self, theta: float | Expression, control: Control | int, target: int) -> None: ...
    def mcrx(self: Self, theta: float | Expression, controls: set[Control | int], target: int) -> None: ...
    def ry(self: Self, theta: float | Expression, q: int) -> None: ...
    def cry(self: Self, theta: float | Expression, control: Control | int, target: int) -> None: ...
    def mcry(self: Self, theta: float | Expression, controls: set[Control | int], target: int) -> None: ...
    def rz(self: Self, theta: float | Expression, q: int) -> None: ...
    def crz(self: Self, theta: float | Expression, control: Control | int, target: int) -> None: ...
    def mcrz(self: Self, theta: float | Expression, controls: set[Control | int], target: int) -> None: ...
    def p(self: Self, theta: float | Expression, q: int) -> None: ...
    def cp(self: Self, theta: float | Expression, control: Control | int, target: int) -> None: ...
    def mcp(self: Self, theta: float | Expression, controls: set[Control | int], target: int) -> None: ...
    def u2(self: Self, phi: float | Expression, lambda_: float | Expression, q: int) -> None: ...
    def cu2(
        self: Self, phi: float | Expression, lambda_: float | Expression, control: Control | int, target: int
    ) -> None: ...
    def mcu2(
        self: Self, phi: float | Expression, lambda_: float | Expression, controls: set[Control | int], target: int
    ) -> None: ...
    def u(
        self: Self, theta: float | Expression, phi: float | Expression, lambda_: float | Expression, q: int
    ) -> None: ...
    def cu(
        self: Self,
        theta: float | Expression,
        phi: float | Expression,
        lambda_: float | Expression,
        control: Control | int,
        target: int,
    ) -> None: ...
    def mcu(
        self: Self,
        theta: float | Expression,
        phi: float | Expression,
        lambda_: float | Expression,
        controls: set[Control | int],
        target: int,
    ) -> None: ...
    def swap(self: Self, target1: int, target2: int) -> None: ...
    def cswap(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mcswap(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def dcx(self: Self, target1: int, target2: int) -> None: ...
    def cdcx(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mcdcx(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def ecr(self: Self, target1: int, target2: int) -> None: ...
    def cecr(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mcecr(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def iswap(self: Self, target1: int, target2: int) -> None: ...
    def ciswap(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mciswap(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def iswapdg(self: Self, target1: int, target2: int) -> None: ...
    def ciswapdg(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mciswapdg(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def peres(self: Self, target1: int, target2: int) -> None: ...
    def cperes(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mcperes(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def peresdg(self: Self, target1: int, target2: int) -> None: ...
    def cperesdg(self: Self, control: Control | int, target1: int, target2: int) -> None: ...
    def mcperesdg(self: Self, controls: set[Control | int], target1: int, target2: int) -> None: ...
    def rxx(self: Self, theta: float | Expression, target1: int, target2: int) -> None: ...
    def crxx(self: Self, theta: float | Expression, control: Control | int, target1: int, target2: int) -> None: ...
    def mcrxx(
        self: Self, theta: float | Expression, controls: set[Control | int], target1: int, target2: int
    ) -> None: ...
    def ryy(self: Self, theta: float | Expression, target1: int, target2: int) -> None: ...
    def cryy(self: Self, theta: float | Expression, control: Control | int, target1: int, target2: int) -> None: ...
    def mcryy(
        self: Self, theta: float | Expression, controls: set[Control | int], target1: int, target2: int
    ) -> None: ...
    def rzz(self: Self, theta: float | Expression, target1: int, target2: int) -> None: ...
    def crzz(self: Self, theta: float | Expression, control: Control | int, target1: int, target2: int) -> None: ...
    def mcrzz(
        self: Self, theta: float | Expression, controls: set[Control | int], target1: int, target2: int
    ) -> None: ...
    def rzx(self: Self, theta: float | Expression, target1: int, target2: int) -> None: ...
    def crzx(self: Self, theta: float | Expression, control: Control | int, target1: int, target2: int) -> None: ...
    def mcrzx(
        self: Self, theta: float | Expression, controls: set[Control | int], target1: int, target2: int
    ) -> None: ...
    def xx_minus_yy(
        self: Self, theta: float | Expression, beta: float | Expression, target1: int, target2: int
    ) -> None: ...
    def cxx_minus_yy(
        self: Self,
        theta: float | Expression,
        beta: float | Expression,
        control: Control | int,
        target1: int,
        target2: int,
    ) -> None: ...
    def mcxx_minus_yy(
        self: Self,
        theta: float | Expression,
        beta: float | Expression,
        controls: set[Control | int],
        target1: int,
        target2: int,
    ) -> None: ...
    def xx_plus_yy(
        self: Self, theta: float | Expression, beta: float | Expression, target1: int, target2: int
    ) -> None: ...
    def cxx_plus_yy(
        self: Self,
        theta: float | Expression,
        beta: float | Expression,
        control: Control | int,
        target1: int,
        target2: int,
    ) -> None: ...
    def mcxx_plus_yy(
        self: Self,
        theta: float | Expression,
        beta: float | Expression,
        controls: set[Control | int],
        target1: int,
        target2: int,
    ) -> None: ...
    def gphase(self: Self, theta: float) -> None: ...
    @overload
    def measure(self: Self, qubit: int, cbit: int) -> None: ...
    @overload
    def measure(self: Self, qubit: int, creg_bit: tuple[str, int]) -> None: ...
    @overload
    def measure(self: Self, qubits: Sequence[int], cbits: Sequence[int]) -> None: ...
    def measure_all(self: Self, add_bits: bool = True) -> None: ...
    @overload
    def reset(self: Self, q: int) -> None: ...
    @overload
    def reset(self: Self, qubits: Sequence[int]) -> None: ...
    @overload
    def barrier(self: Self) -> None: ...
    @overload
    def barrier(self: Self, q: int) -> None: ...
    @overload
    def barrier(self: Self, qubits: Sequence[int]) -> None: ...
    @overload
    def classic_controlled(
        self: Self,
        op: OpType,
        target: int,
        creg: tuple[int, int],
        expected_value: int,
        params: Sequence[float],
    ) -> None: ...
    @overload
    def classic_controlled(
        self: Self,
        op: OpType,
        target: int,
        control: Control | int,
        creg: tuple[int, int],
        expected_value: int,
        params: Sequence[float],
    ) -> None: ...
    @overload
    def classic_controlled(
        self: Self,
        op: OpType,
        target: int,
        controls: set[Control | int],
        creg: tuple[int, int],
        expected_value: int,
        params: Sequence[float],
    ) -> None: ...

__all__ = [
    "Permutation",
    "QuantumComputation",
]
