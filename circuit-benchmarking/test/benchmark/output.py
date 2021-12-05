from qiskit.circuit.library import IntegerComparator, WeightedAdder, QuadraticForm

from benchmark.simulator_benchmark import SimulatorBenchmarkSuite


class OutputSimulatorBenchmarkSuite(SimulatorBenchmarkSuite):

    def __init__(self,
                 name='output',
                 apps=None,
                 qubits=None,
                 runtime_names=None,
                 measures=None,
                 measure_counts=None,
                 noise_model_names=None):
        if noise_model_names is None:
            noise_model_names = []
        if measure_counts is None:
            measure_counts = []
        if measures is None:
            measures = []
        if runtime_names is None:
            runtime_names = []
        if qubits is None:
            qubits = []
        if apps is None:
            apps = []

        super().__init__(name,
                         apps,
                         qubits=qubits,
                         runtime_names=runtime_names,
                         measures=measures,
                         measure_counts=measure_counts,
                         noise_model_names=noise_model_names)
'''
    def track_statevector(self, app, measure, measure_count, noise_name, qubit):
        return self._run(self.RUNTIME_STATEVECTOR_CPU, app, measure, measure_count, noise_name, qubit)
'''