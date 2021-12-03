
from benchmark.simulator_benchmark import SimulatorBenchmarkSuite
from benchmark.noise import NoiseSimulatorBenchmarkSuite

DEFAULT_APPS = {
    'fourier_checking': 1,
    'graph_state': 1,
    'hidden_linear_function': 1,
    'iqp': 1,
    'quantum_volume': 1,
    'phase_estimation': 1
}

DEFAULT_QUBITS = [12]

DEFAULT_RUNTIME = [
    SimulatorBenchmarkSuite.RUNTIME_STATEVECTOR_CPU,
    SimulatorBenchmarkSuite.RUNTIME_STATEVECTOR_GPU,
]

DEFAULT_MEASUREMENT_METHODS = [
    SimulatorBenchmarkSuite.MEASUREMENT_SAMPLING
]

DEFAULT_MEASUREMENT_COUNTS = [1000]

DEFAULT_NOISE_MODELS = [
    SimulatorBenchmarkSuite.NOISE_DAMPING,
    SimulatorBenchmarkSuite.NOISE_DEPOLARIZING
]


class DampingError(NoiseSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = [SimulatorBenchmarkSuite.NOISE_DAMPING]
        if measure_counts is None:
            measure_counts = DEFAULT_MEASUREMENT_COUNTS
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if apps is None:
            apps = DEFAULT_APPS
        super().__init__('damping_error',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)
        self.__name__ = 'damping_error'


class DepolarizingError(NoiseSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = [SimulatorBenchmarkSuite.NOISE_DEPOLARIZING]
        if apps is None:
            apps = DEFAULT_APPS
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if measures is None:
            measures = DEFAULT_MEASUREMENT_METHODS
        if measure_counts is None:
            measure_counts = DEFAULT_MEASUREMENT_COUNTS
        self.__name__ = 'depolarizing_error'

        super().__init__('depolarizing_error',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)


if __name__ == "__main__":
    DampingError().run_manual()
    DepolarizingError().run_manual()