from benchmark.simulator_benchmark import SimulatorBenchmarkSuite
from benchmark.output import OutputSimulatorBenchmarkSuite

DEFAULT_APPS = {
    'fourier_checking':1,
    'graph_state':1,
    'hidden_linear_function':1,
    'iqp':1,
    'quantum_volume': 1,
    'phase_estimation':1,
}

DEFAULT_QUBITS = [5]

DEFAULT_RUNTIME = [
    SimulatorBenchmarkSuite.RUNTIME_STATEVECTOR_CPU,
]

DEFAULT_MEASUREMENT_COUNTS = [1, 10, 100, 1000, 10000]

DEFAULT_NOISE_MODELS = [
    SimulatorBenchmarkSuite.NOISE_IDEAL
]


class Sampling(OutputSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measure_counts is None:
            measure_counts = DEFAULT_MEASUREMENT_COUNTS
        if measures is None:
            measures = [SimulatorBenchmarkSuite.MEASUREMENT_SAMPLING]
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if apps is None:
            apps = DEFAULT_APPS
        if qubits is None:
            qubits = DEFAULT_QUBITS

        super().__init__('sampling',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)
        self.__name__ = 'sampling'


class ExpVal(OutputSimulatorBenchmarkSuite):

    def __init__(self,
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = DEFAULT_NOISE_MODELS
        if measure_counts is None:
            measure_counts = DEFAULT_MEASUREMENT_COUNTS
        if measures is None:
            measures = [SimulatorBenchmarkSuite.MEASUREMENT_EXPVAL]
        if runtime_names is None:
            runtime_names = DEFAULT_RUNTIME
        if qubits is None:
            qubits = DEFAULT_QUBITS
        if apps is None:
            apps = DEFAULT_APPS

        super().__init__('expval',
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)
        self.__name__ = 'expval'


if __name__ == "__main__":
    Sampling().run_manual()
    ExpVal().run_manual()
