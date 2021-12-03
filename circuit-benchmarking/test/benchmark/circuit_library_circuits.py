import numpy as np
from qiskit.circuit.library import *

# Initialization of Circuits to characterise
class CircuitLibraryCircuits():

    # Circuit Instances
    def _repeat(self, circ, repeats):
        if repeats is not None and repeats > 1:
            circ = circ.repeat(repeats).decompose()
        return circ

    # Arithmetic Circuits
    def integer_comparator(self, qubit, repeats):
        if qubit < 2:
            raise ValueError('qubit is too small: {0}'.format(qubit))
        half = int(qubit / 2)
        return self._repeat(IntegerComparator(num_state_qubits=half, value=1), repeats)
    
    def weighted_adder(self, qubit, repeats):
        if qubit > 20:
            raise ValueError('qubit is too big: {0}'.format(qubit))
        return self._repeat(WeightedAdder(num_state_qubits=qubit).decompose(), repeats)
    
    def quadratic_form(self, qubit, repeats):
        if qubit < 4:
            raise ValueError('qubit is too small: {0}'.format(qubit))
        return self._repeat(QuadraticForm(num_result_qubits=(qubit - 3), linear=[1, 1, 1], little_endian=True).decompose(), repeats)

    # Basic Circuits
    def qft(self, qubit, repeats):
        return self._repeat(QFT(qubit), repeats)

    # N-Local Circuits
    def real_amplitudes(self, qubit, repeats):
        return self.transpile(RealAmplitudes(qubit, reps=repeats))

    def real_amplitudes_linear(self, qubit, repeats):
        return self.transpile(RealAmplitudes(qubit, reps=repeats, entanglement='linear'))
    
    def efficient_su2(self, qubit, repeats):
        return self.transpile(EfficientSU2(qubit).decompose())

    def efficient_su2_linear(self, qubit, repeats):
        return self.transpile(EfficientSU2(qubit, reps=repeats, entanglement='linear'))
    
    def excitation_preserving(self, qubit, repeats):
        return self.transpile(ExcitationPreserving(qubit, reps=repeats).decompose())

    def excitation_preserving_linear(self, qubit, repeats):
        return self.transpile(ExcitationPreserving(qubit, reps=repeats, entanglement='linear'))

    # Particular Quantum Circuits
    def fourier_checking(self, qubit, repeats):
        if qubit > 20:
            raise ValueError('qubit is too big: {0}'.format(qubit))
        f = [-1, 1] * (2 ** (qubit - 1))
        g = [1, -1] * (2 ** (qubit - 1))
        return self._repeat(FourierChecking(f, g), repeats)
    
    def graph_state(self, qubit, repeats):
        a = np.reshape([0] * (qubit ** 2), [qubit] * 2)
        for _ in range(qubit):
            while True:
                i = np.random.randint(0, qubit)
                j = np.random.randint(0, qubit)
                if a[i][j] == 0:
                    a[i][j] = 1
                    a[j][i] = 1
                    break
        return self._repeat(GraphState(a), repeats)
    
    def hidden_linear_function(self, qubit, repeats):
        a = np.reshape([0] * (qubit ** 2), [qubit] * 2)
        for _ in range(qubit):
            while True:
                i = np.random.randint(0, qubit)
                j = np.random.randint(0, qubit)
                if a[i][j] == 0:
                    a[i][j] = 1
                    a[j][i] = 1
                    break
        return self._repeat(HiddenLinearFunction(a), repeats)

    def iqp(self, qubit, repeats):
        interactions = np.random.randint(-1024, 1024, (qubit, qubit))
        for i in range(qubit):
            for j in range(i + 1, qubit):
                interactions[j][i] = interactions[i][j]
        return self._repeat(IQP(interactions).decompose(), repeats)

    def quantum_volume(self, qubit, repeats):
        return self._repeat(QuantumVolume(qubit).decompose(), repeats)

    def phase_estimation(self, qubit, repeats):
        if qubit < 5:
            raise ValueError('qubit is too small: {0}'.format(qubit))
        return self._repeat(PhaseEstimation(2, QuantumVolume(qubit - 2).decompose()).decompose(), repeats)

    # Probability Distribution Circuit
    def uniform_distribution(self, qubit, repeats):
        return self._repeat(UniformDistribution(qubit).decompose(), repeats)

    def normal_distribution(self, qubit, repeats):
        mu = 100
        sigma = 12.5
        return self._repeat(NormalDistribution(qubit, mu, sigma), repeats)

    def log_normal_distribution(self, qubit, repeats):
        mu = 100
        return self._repeat(LogNormalDistribution(qubit, mu, sigma=12.5), repeats)